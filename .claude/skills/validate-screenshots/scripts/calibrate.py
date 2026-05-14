#!/usr/bin/env python3
"""Driver for the one-off calibration step.

This is not an analysis tool — the LLM does the analysis. The script just walks
the paths the user nominated, collects every PNG, groups them by the OutSystems
source suffix (-ss, -odcs, -pl, -lt, -sc, -usr, -fg, etc.), and prints a JSON
manifest the LLM can work from.

The LLM reads the manifest, reads each image with vision, groups observations
into concrete rules, and writes the draft `visual-rules-screenshots.md` next to
this script's parent SKILL.md.

Usage:
    python3 calibrate.py <path-or-folder> [<path-or-folder> ...]
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

SUFFIX_RE = re.compile(r"-([a-z]{2,4})\.png$")
SUFFIX_LABELS = {
    "ss": "Service Studio",
    "odcs": "ODC Studio",
    "pl": "ODC Portal",
    "lt": "LifeTime",
    "sc": "Service Center",
    "usr": "Users",
    "fg": "Forge",
    "at": "AI Agent Studio",
    "ct": "Consumption Tracker",
    "af": "AgentFlow",
    "gc": "Generative Components",
    "ams": "AI Mentor Studio",
    "ib": "Inbox",
    "eb": "Experience Builder",
    "we": "Workflow Editor",
    "az": "Azure",
    "vs": "Visual Studio",
    "ok": "OK",
    "fc": "Forms Composer",
    "diag": "Diagram",
    "sa": "Solution Architecture",
    "is": "Integration Studio",
}


def walk_pngs(targets: list[Path]) -> list[Path]:
    pngs: list[Path] = []
    seen: set[str] = set()
    for t in targets:
        if t.is_file() and t.suffix.lower() == ".png":
            key = str(t.resolve())
            if key not in seen:
                seen.add(key)
                pngs.append(t.resolve())
        elif t.is_dir():
            for p in t.rglob("*.png"):
                key = str(p.resolve())
                if key not in seen:
                    seen.add(key)
                    pngs.append(p.resolve())
    pngs.sort()
    return pngs


def classify(png: Path) -> tuple[str, str]:
    m = SUFFIX_RE.search(png.name)
    if not m:
        return ("unknown", "Unknown source")
    suffix = m.group(1)
    return (suffix, SUFFIX_LABELS.get(suffix, f"Unknown suffix ({suffix})"))


def build_manifest(pngs: list[Path]) -> dict:
    by_surface: dict[str, list[dict]] = defaultdict(list)
    for p in pngs:
        suffix, label = classify(p)
        by_surface[label].append({
            "path": str(p),
            "filename": p.name,
            "suffix": suffix,
        })
    return {
        "total": len(pngs),
        "surfaces": [
            {"label": label, "count": len(items), "images": items}
            for label, items in sorted(by_surface.items())
        ],
    }


def next_steps_note(out_path: Path) -> str:
    return (
        "Next steps for the LLM:\n"
        "  1. Read each image in the manifest below with the Read tool.\n"
        "  2. Describe what you observe — shadow, cursor, highlight component, "
        "annotation style, cropping, padding, blurring of PII, etc.\n"
        "  3. Cluster the observations into concrete, checkable rules. Each rule "
        "needs a name, a one-line acceptance criterion, and at least one pass "
        "example + one fail example.\n"
        "  4. Write the rubric to:\n"
        f"     {out_path}\n"
        "     Replace the placeholder marker `<!-- NOT CALIBRATED -->` with the "
        "calibrated content. Keep the file format — SKILL.md's validation loop "
        "reads rules from there.\n"
        "  5. Ask the user to review and edit the draft before trusting it.\n"
    )


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(
            "usage: calibrate.py <path-or-folder> [<path-or-folder> ...]",
            file=sys.stderr,
        )
        return 2

    targets = [Path(os.path.expanduser(a)).resolve() for a in argv[1:]]
    missing = [t for t in targets if not t.exists()]
    if missing:
        print(
            "Paths not found: " + ", ".join(str(m) for m in missing),
            file=sys.stderr,
        )
        return 2

    pngs = walk_pngs(targets)
    if not pngs:
        print("No .png files found under the given paths.", file=sys.stderr)
        return 1

    skill_dir = Path(__file__).resolve().parent.parent
    out_path = skill_dir / "visual-rules-screenshots.md"
    manifest = build_manifest(pngs)

    print(next_steps_note(out_path))
    print("Manifest:")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
