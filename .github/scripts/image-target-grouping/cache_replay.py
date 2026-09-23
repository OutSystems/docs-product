#!/usr/bin/env python3
"""Republish a target's stored report instead of asking the model to retype it.

Skipping the per-image vision and checker work still left one model call per
target, purely to reassemble a report whose every finding was already sitting
in the validation record. That call costs wall-clock and Copilot credits to reproduce
known text, and it is the one place a cached verdict could drift from what
was actually cached.

So when a target and its entire dependency closure are unchanged, this
reproduces exactly what the skill would have printed — the stored
`<details>` block behind a REPORT BEGIN sentinel, or the NO REPORT sentinel
for a clean target — and the workflow skips the invocation altogether.

Exit 0 and write the replacement stdout to --out when the target can be
replayed; exit 1 otherwise, which tells the caller to run the skill for real.
Any doubt resolves to exit 1: a needless model call costs time, a wrong
replay would publish a stale report.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import cache_decision, git_blob_sha1, load_validation_record, repo_relpath  # noqa: E402


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", required=True)
    ap.add_argument("--record", required=True)
    ap.add_argument("--skill-version", required=True)
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--max-age-days", type=int, default=0)
    ap.add_argument("--out", required=True, help="file to write the replayed stdout to")
    args = ap.parse_args(argv[1:])

    entries = load_validation_record(args.record)
    if not entries:
        return 1

    root = Path(args.repo_root).resolve()
    target = Path(args.target)
    rel = repo_relpath(target, root)

    decision = cache_decision(
        entries, rel, git_blob_sha1(target),
        skill_version=args.skill_version,
        max_age_days=args.max_age_days or None,
    )
    if not decision["cached"]:
        print(f"  ↻ {rel}: {decision['detail']} — running the skill.")
        return 1

    entry = decision["entry"] or {}
    if "report_fragment" not in entry:
        # Recorded before fragments were stored, so we know the verdict but
        # not how it was presented. Re-run rather than invent a report.
        print(f"  ↻ {rel}: cached but with no stored report — running the skill.")
        return 1

    # The report covers the article's images too, so every one of them has to
    # be unchanged for the stored text to still be true.
    for dep, recorded in (entry.get("deps") or {}).items():
        current = git_blob_sha1(root / dep)
        if current != recorded:
            what = "changed" if current else "could not be read"
            print(f"  ↻ {rel}: {dep} {what} — running the skill.")
            return 1

    fragment = entry["report_fragment"]
    n_deps = len(entry.get("deps") or {})
    if fragment:
        payload = "<!-- REPORT BEGIN -->\n" + fragment + "\n"
        # Counted from the fragment, not from entry["findings"]: a report is
        # about the article's images, so the article's own findings list is
        # usually empty and quoting it read as "republishing 0 findings"
        # while republishing fourteen.
        blocking = sum(1 for ln in fragment.splitlines() if "❌" in ln)
        warnings = sum(1 for ln in fragment.splitlines() if "⚠️" in ln)
        what = f"{blocking} blocking and {warnings} warning finding(s)"
    else:
        payload = "<!-- NO REPORT -->\n"
        what = "no findings"
    Path(args.out).write_text(payload, encoding="utf-8")

    print(
        f"  ⏭️  {rel}: unchanged with {n_deps} unchanged dependencie(s) — "
        f"republishing the cached report ({what}) without calling the model."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
