#!/usr/bin/env python3
"""Decide, before any checkout, whether a skill has anything left to validate.

The expensive part of an AI-skill job is fixed setup — the sparse clone, the
Copilot CLI install, pip — not the model call. A filter that runs after the
checkout therefore recovers only a fraction of a fully-cached run, which is
why this gate exists above it and answers entirely from the GitHub API.

It re-derives the candidate set from the workflow's own inputs (the changed
files, the glob filter, ignore-paths) and compares each candidate's blob SHA,
plus the dependency closure recorded for it last time, against the restored
validation record. Every candidate surviving as a cache hit means the whole job can be
skipped without cloning anything.

The front-matter filter that runs after the checkout can only ever *shrink*
the candidate set, so "every candidate is cached" safely implies "every real
target is cached".

Outputs to $GITHUB_OUTPUT:
    skip=true|false
    candidates=<newline-separated survivors, for the post-checkout path>

Deliberately conservative: anything it cannot prove — a path with no known
blob SHA, an unparseable validation record, a dep it could not resolve — is treated as
"not cached", so the job runs. A missed skip costs time; a wrong skip costs
correctness.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path, PurePosixPath

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cache_metrics  # noqa: E402
from lib import (  # noqa: E402
    cache_decision,
    format_decision_line,
    load_validation_record,
    summary_table,
)


def select_candidates(changed: list[str], glob: str, ignore_paths: str) -> list[str]:
    """The same narrowing the workflow applies, minus the front-matter filter.

    Kept in step with the `Filter files by glob pattern` and `ignore-paths`
    steps in ai-copilot-skill.yml — if those change, this must too, or the
    gate could skip a job that still had work to do.
    """
    out = list(changed)
    patterns = [p.strip() for p in glob.split(",") if p.strip()]
    if patterns:
        out = [f for f in out if any(PurePosixPath(f).match(p) for p in patterns)]
    ignores = [p.strip() for p in ignore_paths.split(",") if p.strip()]
    if ignores:
        out = [f for f in out if not any(ig in f for ig in ignores)]
    return out


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--changed-files", required=True, help="newline-separated list")
    ap.add_argument("--glob", default="")
    ap.add_argument("--ignore-paths", default="")
    ap.add_argument("--record", default="")
    ap.add_argument("--skill-version", default="")
    ap.add_argument("--max-age-days", type=int, default=0)
    ap.add_argument("--blob-shas", required=True, help="JSON {path: blob sha}")
    ap.add_argument("--skill", default="skill")
    args = ap.parse_args(argv[1:])

    changed = [
        line.strip()
        for line in Path(args.changed_files).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    candidates = select_candidates(changed, args.glob, args.ignore_paths)

    try:
        blobs = json.loads(Path(args.blob_shas).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        blobs = {}

    entries = load_validation_record(args.record or None)
    record_present = bool(args.record) and bool(entries)
    skill_version = args.skill_version or None
    max_age = args.max_age_days or None

    print(f"Candidates after glob + ignore-paths: {len(candidates)}")
    if not candidates:
        # Nothing to do at all. Not a cache skip — say so plainly, so an empty
        # run is never mistaken for a suspiciously effective cache.
        _emit(skip=False, candidates=[])
        print("ℹ️ No candidate files for this skill; leaving the existing filters to no-op.")
        return 0

    rows: list[tuple[str, dict]] = []
    survivors: list[str] = []
    for rel in candidates:
        decision = cache_decision(
            entries, rel, blobs.get(rel),
            skill_version=skill_version, max_age_days=max_age,
            record_present=record_present,
        )
        # A hit on the file itself is not enough for an enumerating skill: the
        # article may be untouched while an image it references changed. Only
        # the dependency closure recorded last time can rule that out, and a
        # dep whose hash we could not resolve counts against the hit.
        if decision["cached"]:
            stale_dep = _first_stale_dep(decision["entry"], blobs)
            if stale_dep:
                dep, was, now = stale_dep
                decision = {
                    "cached": False,
                    "reason": "content-changed",
                    "detail": f"a file it references changed: {dep} "
                              f"({_short(was)} -> {_short(now)})",
                    "entry": decision["entry"],
                }
        if decision["cached"]:
            # Same hazard one level down: an article can be clean while an
            # image it references is not. The report covers both, so the job
            # has to run if either carries findings.
            flagged_dep = _dep_with_findings(decision["entry"], entries)
            if flagged_dep:
                decision = {
                    "cached": False,
                    "reason": "hit",
                    "detail": f"unchanged, but a file it references has cached "
                              f"findings ({flagged_dep}) — re-running to report them",
                    "entry": decision["entry"],
                }
        if decision["cached"] and _has_findings(decision["entry"]):
            # Cached, but the cached verdict is a finding. Skipping the job
            # would leave the check "skipped" rather than failing, and a
            # required check that is skipped does not block a merge — so a
            # known ❌ could be merged. Keep it as a survivor: the job runs,
            # the skill re-emits the stored findings without re-deriving
            # them, the sticky comment stays complete, and
            # fail-on-error-marker still fails. The expensive per-image work
            # is still skipped inside the skill; only the job-level shortcut
            # is given up.
            decision = {
                "cached": False,
                "reason": "hit",
                "detail": "unchanged, but its last verdict had findings — "
                          "re-running so they are reported again",
                "entry": decision["entry"],
            }
        rows.append((rel, decision))
        if not decision["cached"]:
            survivors.append(rel)

    width = max(len(rel) for rel, _ in rows)
    print("::group::Cache decisions")
    for rel, decision in rows:
        print(format_decision_line(rel, decision, width))
    print("::endgroup::")

    skip = not survivors
    _write_summary(args.skill, rows, skip)
    _emit(skip=skip, candidates=survivors)
    _record_metrics(args, rows, skip)

    if skip:
        print(f"✅ All {len(rows)} candidate(s) already validated — skipping before checkout.")
    else:
        print(f"▶️ {len(survivors)} of {len(rows)} candidate(s) need validation.")
    return 0


def _record_metrics(args, rows, skip: bool) -> None:
    """Counters for the daily collector, plus the line itself when we stop here.

    A gate that skips ends the job, so nothing downstream would ever get
    the chance to publish — the line has to go out from here in that case.
    """
    metrics_file = os.environ.get("AI_SKILL_CACHE_METRICS")
    if not metrics_file:
        return
    reasons: dict[str, int] = {}
    for _, d in rows:
        reasons[d.get("reason", "unknown")] = reasons.get(d.get("reason", "unknown"), 0) + 1
    hits = sum(1 for _, d in rows if d.get("cached"))
    cache_metrics.bump(Path(metrics_file), {
        "skill": args.skill,
        "skill_version": args.skill_version,
        "candidates": len(rows),
        "gate_hits": hits,
        "reasons": reasons,
        "job_skipped": skip,
    })
    if skip:
        cache_metrics.main(["cache_metrics.py", "--file", metrics_file, "--emit"])


def _has_findings(entry) -> bool:
    """True when this entry's cached verdict was anything but a clean pass."""
    entry = entry or {}
    return entry.get("verdict") == "findings" or bool(entry.get("findings"))


def _dep_with_findings(entry, entries: dict) -> str | None:
    deps = (entry or {}).get("deps") or {}
    if not isinstance(deps, dict):
        return None
    for dep in deps:
        if _has_findings(entries.get(dep)):
            return dep
    return None


def _first_stale_dep(entry, blobs) -> tuple[str, object, object] | None:
    deps = (entry or {}).get("deps") or {}
    if not isinstance(deps, dict):
        return None
    for dep, recorded in deps.items():
        current = blobs.get(dep)
        if current is None or current != recorded:
            return dep, recorded, current
    return None


def _short(sha) -> str:
    return str(sha)[:8] if sha else "unknown"


def _write_summary(skill: str, rows, skip: bool) -> None:
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not path:
        return
    # Written even when the job is about to be skipped: that job produces no
    # other output at all, so without this a skip is an empty run page.
    note = (
        "\nWhole job skipped before checkout — nothing left to validate.\n"
        if skip else ""
    )
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(summary_table(skill, rows) + note)
    except OSError:
        pass


def _emit(*, skip: bool, candidates: list[str]) -> None:
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"skip={'true' if skip else 'false'}\n")
        f.write("candidates<<CACHEGATE_EOF\n")
        for c in candidates:
            f.write(c + "\n")
        f.write("CACHEGATE_EOF\n")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
