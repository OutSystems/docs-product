#!/usr/bin/env python3
"""Record what one skill invocation successfully validated.

Called once per invocation, after the `copilot` call returns, with that
invocation's own stdout. Decides — deterministically, without asking the
model anything it isn't already printing — which files may be skipped next
time, and appends them to a delta the job merges into the validation record at the end.

Two sources of truth, in order:

1. `<!-- VERDICTS {"path": "clean"|"findings"} -->`, printed by the skill.
   Gives per-file granularity, so one bad image in an article doesn't cost
   the other nineteen their cache entries. Findings are stored so the next
   run can re-emit them verbatim instead of re-deriving them.
2. `<!-- NO REPORT -->`, the sentinel the workflow already parses. If the
   verdict block is missing or unparseable, an invocation that printed this
   had nothing to flag, so every file it touched is provably clean. Coarser
   — an article with one finding caches nothing — but it depends on no new
   model behaviour at all, so it is the safe floor.

Anything else writes nothing. A non-zero exit writes nothing. Not writing
costs a re-validation; writing something wrong costs a silently skipped
defect, so every ambiguous case resolves to "write nothing".
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import git_blob_sha1, repo_relpath  # noqa: E402

VERDICTS_RE = re.compile(r"<!--\s*VERDICTS\s*(\{.*?\})\s*-->", re.DOTALL)
NO_REPORT_RE = re.compile(r"^[ \t]*<!--[ \t]*NO REPORT[ \t]*-->[ \t]*$", re.MULTILINE)
_BEGIN_RE = re.compile(r"^[ \t]*<!--[ \t]*REPORT BEGIN[ \t]*-->[ \t]*$")
_OPEN_RE = re.compile(r"^[ \t]*<details>[ \t]*$")
_CLOSE_RE = re.compile(r"^[ \t]*</details>[ \t]*$")


def extract_fragment(text: str) -> str | None:
    """This invocation's rendered <details> block, or None if it printed no report.

    Deliberately the same arming rules the workflow's awk uses: start on a
    line that is only the REPORT BEGIN sentinel, capture from the next
    bare <details> to its matching close. The CLI echoes a truncated
    preview of a shell call before running it, so anchoring to whole lines
    is what stops the preview being mistaken for the real report.

    Storing the fragment is what lets a later run with an unchanged
    dependency closure republish the report without invoking the model at
    all — the findings are already known, so paying for an LLM call to
    retype them is pure waste.
    """
    armed = False
    capturing = False
    out: list[str] = []
    for line in text.splitlines():
        if not capturing and _BEGIN_RE.match(line):
            armed = True
            continue
        if armed and _OPEN_RE.match(line):
            capturing = True
            armed = False
        if capturing:
            out.append(line)
            if _CLOSE_RE.match(line):
                capturing = False
    return "\n".join(out) if out else None


def parse_verdicts(text: str) -> dict | None:
    """The last VERDICTS block in the output, or None if there isn't a usable one.

    The last one wins: the CLI echoes a truncated preview of a shell call
    before running it, so an earlier partial copy of the line can appear in
    the transcript ahead of the real thing.
    """
    matches = VERDICTS_RE.findall(text)
    for raw in reversed(matches):
        try:
            data = json.loads(raw)
        except ValueError:
            continue
        if isinstance(data, dict) and all(
            isinstance(k, str) and v in ("clean", "findings") for k, v in data.items()
        ):
            return data
    return None


def findings_for(text: str, rel: str) -> list[str]:
    """The `- ❌ …` / `- ⚠️ …` bullets under that file's `### <path>` heading.

    Matched on the heading's trailing path segment because the report writes
    paths relative to the article while the validation record keys on repo-relative
    ones.
    """
    name = rel.split("/")[-1]
    out: list[str] = []
    capturing = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("###"):
            capturing = stripped.rstrip().endswith(name)
            continue
        if capturing:
            if stripped.startswith("- "):
                out.append(stripped[2:].strip())
            elif stripped.startswith("#") or stripped.startswith("</details>"):
                capturing = False
    return out


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True, help="this invocation's stdout")
    ap.add_argument("--target", required=True, help="the file handed to the skill")
    ap.add_argument("--manifest", default="", help="paths the collector resolved")
    ap.add_argument("--delta", required=True, help="JSON file to append entries to")
    ap.add_argument("--skill-version", required=True)
    ap.add_argument("--run-id", default="")
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--exit-code", type=int, default=0)
    ap.add_argument(
        "--success-is-clean", action="store_true",
        help="For skills with no report at all (structured-merge, diff-patch, "
             "commit mode): completing on this content IS the verdict, so a "
             "clean exit is enough. The partial-report hazard cannot apply "
             "where there is no report to truncate.",
    )
    args = ap.parse_args(argv[1:])

    if args.exit_code != 0:
        print(f"  🚫 Not caching {args.target}: the skill exited {args.exit_code}.")
        return 0

    try:
        text = Path(args.output).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        print(f"  🚫 Not caching {args.target}: its output could not be read.")
        return 0

    root = Path(args.repo_root).resolve()

    # What this invocation covered: the target, plus whatever the collector
    # resolved from it (an article's images).
    covered: dict[str, str | None] = {}
    if args.manifest:
        try:
            covered.update(json.loads(Path(args.manifest).read_text(encoding="utf-8")))
        except (OSError, ValueError):
            pass
    target_rel = repo_relpath(Path(args.target), root)
    covered.setdefault(target_rel, git_blob_sha1(Path(args.target)))

    verdicts = parse_verdicts(text)
    if verdicts is not None:
        source = "verdict block"
        resolved = {rel: verdicts.get(rel, "clean") for rel in covered}
        # A file the block never mentions was not assessed this run, so don't
        # claim it passed.
        unmentioned = [r for r in covered if r not in verdicts and r != target_rel]
        for rel in unmentioned:
            resolved.pop(rel, None)
    elif NO_REPORT_RE.search(text):
        source = "NO REPORT sentinel"
        resolved = {rel: "clean" for rel in covered}
    elif args.success_is_clean:
        source = "clean exit (no-report skill)"
        resolved = {rel: "clean" for rel in covered}
    else:
        print(
            f"  🚫 Not caching {args.target}: no verdict block and no "
            f"NO REPORT sentinel, so what passed is unknown."
        )
        return 0

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entries: dict[str, dict] = {}
    deps = {r: h for r, h in covered.items() if r != target_rel and h}

    # Only the target carries the rendered report, because the report is
    # produced per invocation and an invocation is per target. "" means the
    # invocation deliberately produced no report (the clean case) — distinct
    # from the key being absent, which means we never learned either way and
    # so must not replay.
    fragment = extract_fragment(text)
    if fragment is None and NO_REPORT_RE.search(text):
        fragment = ""

    for rel, verdict in resolved.items():
        blob = covered.get(rel)
        if not blob:
            # Couldn't hash it, so we could never match it again anyway.
            continue
        entry = {
            "hash": blob,
            "skill_version": args.skill_version,
            "validated_at": now,
            "run_id": args.run_id,
            "verdict": verdict,
            "findings": findings_for(text, rel) if verdict == "findings" else [],
            "deps": deps if rel == target_rel else {},
        }
        if rel == target_rel and fragment is not None:
            entry["report_fragment"] = fragment
        entries[rel] = entry

    try:
        existing = json.loads(Path(args.delta).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        existing = {}
    existing.update(entries)
    Path(args.delta).write_text(json.dumps(existing), encoding="utf-8")

    clean = sum(1 for e in entries.values() if e["verdict"] == "clean")
    flagged = len(entries) - clean
    print(
        f"  💾 Cached {len(entries)} entr(ies) for {args.target} "
        f"via the {source} ({clean} clean, {flagged} with findings)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
