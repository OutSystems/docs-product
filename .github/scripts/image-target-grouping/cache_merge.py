#!/usr/bin/env python3
"""Fold this run's verdicts into the validation record and prune what has gone stale.

Runs once at the end of a skill's job. The restored validation record is whatever the
prefix restore-key found — this PR's previous push, or the promoted
default-branch baseline — and the delta is what this run proved. New entries
win; everything else is carried forward so the validation record accumulates across
pushes instead of resetting each time.

Pruning is by `validated_at` age only. Entries for files that no longer exist
are deliberately kept: the validation record is keyed on content, so a file that comes
back unchanged (a revert, a cherry-pick, a branch that re-adds it) should hit
rather than re-validate.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cache_metrics  # noqa: E402
from lib import RECORD_SCHEMA, load_validation_record  # noqa: E402


def prune(entries: dict, max_age_days: int | None, now: datetime) -> tuple[dict, int]:
    if not max_age_days:
        return entries, 0
    kept, dropped = {}, 0
    for rel, entry in entries.items():
        when = (entry or {}).get("validated_at")
        try:
            parsed = datetime.fromisoformat(str(when).replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
        except (ValueError, TypeError):
            # No usable timestamp: keep it. cache_decision() already refuses
            # to trust an entry it can't age, so this can't extend a verdict's
            # life, and dropping it would just churn the validation record.
            kept[rel] = entry
            continue
        if (now - parsed).days > max_age_days:
            dropped += 1
        else:
            kept[rel] = entry
    return kept, dropped


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--record", required=True)
    ap.add_argument("--delta", default="")
    ap.add_argument("--skill", default="")
    ap.add_argument("--max-age-days", type=int, default=0)
    ap.add_argument("--metrics", default="", help="counters file for the usage collector")
    args = ap.parse_args(argv[1:])

    existing = load_validation_record(args.record)
    before = len(existing)

    delta = {}
    if args.delta:
        try:
            delta = json.loads(Path(args.delta).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            delta = {}
    if not isinstance(delta, dict):
        delta = {}

    merged = dict(existing)
    merged.update(delta)
    merged, dropped = prune(merged, args.max_age_days or None, datetime.now(timezone.utc))

    out = Path(args.record)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps({"schema": RECORD_SCHEMA, "skill": args.skill, "entries": merged}),
        encoding="utf-8",
    )

    added = len([k for k in delta if k not in existing])
    updated = len(delta) - added
    print(
        f"🗃️ Validation record: {before} entr(ies) restored, {added} added, {updated} refreshed, "
        f"{dropped} pruned as stale — {len(merged)} saved."
    )

    if args.metrics:
        # restored == 0 on a run that should have inherited a baseline is the
        # signal that promotion or the cache scope has quietly broken, so it
        # is worth publishing even though it looks redundant next to saved.
        cache_metrics.bump(Path(args.metrics), {
            "record_restored": before,
            "record_added": added,
            "record_refreshed": updated,
            "record_pruned": dropped,
            "record_entries": len(merged),
        })
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
