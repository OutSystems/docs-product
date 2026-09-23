#!/usr/bin/env python3
"""Accumulate one job's cache counters and emit them as a single log line.

The daily usage collector already fetches these job logs and already
parses them per file, so the cheapest place to publish cache numbers is
the log itself. It reads one machine-readable line rather than the
human-facing decision lines, which are prose and would be brittle to
parse:

    <!-- CACHE-METRICS {"skill":"validate-screenshots","candidates":2,...} -->

Counters are accumulated into a JSON file across steps, because the
numbers come from three different places — the pre-checkout gate, the
invocation loop, and the validation record merge — and the gate may end the job
before the other two ever run.

Nothing here can fail a build: every entry point swallows its own errors.
A metric is worth less than the run it would break.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def _load(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def bump(path: Path, counters: dict) -> dict:
    """Add `counters` into the accumulator, summing numbers and dicts."""
    data = _load(path)
    for key, value in counters.items():
        if isinstance(value, dict):
            slot = data.setdefault(key, {})
            if not isinstance(slot, dict):
                slot = {}
            for k, v in value.items():
                slot[k] = slot.get(k, 0) + v
            data[key] = slot
        elif isinstance(value, bool):
            data[key] = value
        elif isinstance(value, (int, float)):
            data[key] = data.get(key, 0) + value
        else:
            data[key] = value
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data), encoding="utf-8")
    except OSError:
        pass
    return data


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True, help="accumulator path")
    ap.add_argument("--set", default="", help="JSON object to merge in")
    ap.add_argument("--emit", action="store_true", help="print the CACHE-METRICS line")
    args = ap.parse_args(argv[1:])

    path = Path(args.file)
    if args.set:
        try:
            bump(path, json.loads(args.set))
        except ValueError:
            pass

    if args.emit:
        data = _load(path)
        if data:
            # Single line, no newlines inside: the collector greps for it.
            print("<!-- CACHE-METRICS " + json.dumps(data, sort_keys=True) + " -->")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except SystemExit:
        raise
    except Exception as exc:  # never fail a build over a metric
        print(f"::warning::cache metrics not recorded: {exc}")
        raise SystemExit(0)
