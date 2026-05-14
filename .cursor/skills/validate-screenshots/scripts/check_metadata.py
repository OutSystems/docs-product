#!/usr/bin/env python3
"""Deterministic checks for image metadata.

Covers three rules from the rubric that don't require vision:
    rule 1  — file extension must be .png
    rule 2  — filename must be lowercase letters, digits and hyphens,
              and must end with one of the documented surface suffixes
    rule 10 — pixel width must be <= 1200

Output is a JSON object so the skill can merge this verdict with the
vision-based ones. Every verdict has the shape
    {"verdict": "pass" | "fail" | "warn", "reason": "..."}.

Usage:
    python3 check_metadata.py <path-to-image>
"""
from __future__ import annotations

import json
import re
import struct
import sys
from pathlib import Path

VALID_SUFFIXES = {
    "ss", "odcs", "pl", "lt", "sc", "usr", "fg", "at", "ct", "af",
    "gc", "ams", "ib", "eb", "we", "az", "vs", "ok", "fc", "diag",
    "sa", "is",
}

# Surface suffix for a diagram — screenshots shouldn't use this.
DIAGRAM_SUFFIX = "diag"

STEM_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

MAX_WIDTH = 1200


def check_format(path: Path) -> dict:
    ext = path.suffix.lower().lstrip(".")
    if ext == "png":
        return {"verdict": "pass", "reason": ""}
    return {
        "verdict": "fail",
        "reason": f"extension .{ext} is not allowed; must be .png",
    }


def check_naming(path: Path) -> dict:
    stem = path.stem
    if not STEM_RE.match(stem):
        return {
            "verdict": "fail",
            "reason": (
                "filename must be lowercase letters, digits and hyphens only"
            ),
        }
    parts = stem.split("-")
    if len(parts) < 2:
        return {
            "verdict": "fail",
            "reason": "missing surface suffix (e.g. -ss, -odcs, -pl)",
        }
    last = parts[-1]
    if last not in VALID_SUFFIXES:
        return {
            "verdict": "fail",
            "reason": (
                f"suffix -{last} is not a documented surface suffix; "
                "see rule 2 for the full list"
            ),
        }
    if len(parts) >= 3 and parts[-2] in VALID_SUFFIXES:
        return {
            "verdict": "fail",
            "reason": (
                f"double surface suffix -{parts[-2]}-{last}; keep only one"
            ),
        }
    if last == DIAGRAM_SUFFIX:
        return {
            "verdict": "warn",
            "reason": (
                "-diag is for diagrams; screenshots should use a surface "
                "suffix like -ss or -odcs"
            ),
        }
    return {"verdict": "pass", "reason": ""}


def png_width(path: Path) -> int | None:
    try:
        with path.open("rb") as f:
            header = f.read(24)
    except OSError:
        return None
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">I", header[16:20])[0]


def check_width(path: Path) -> dict:
    width = png_width(path)
    if width is None:
        return {
            "verdict": "skip",
            "reason": "not a PNG; width check skipped",
            "px": None,
        }
    if width > MAX_WIDTH:
        return {
            "verdict": "warn",
            "reason": f"width {width}px exceeds the {MAX_WIDTH}px suggestion",
            "px": width,
        }
    return {"verdict": "pass", "reason": "", "px": width}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: check_metadata.py <path-to-image>", file=sys.stderr)
        return 2
    path = Path(argv[1]).expanduser().resolve()
    if not path.is_file():
        print(json.dumps({"error": f"file not found: {path}"}))
        return 0
    report = {
        "image_path": str(path),
        "format": check_format(path),
        "naming": check_naming(path),
        "width": check_width(path),
    }
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
