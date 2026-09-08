#!/usr/bin/env python3
"""Shared owner-resolution helpers for image target collectors.

Used by validate-screenshots/scripts/collect_targets.py,
validate-svgs/scripts/collect_targets.py, and
.github/scripts/image-target-grouping/plan_targets.py, so screenshot and
SVG handling stay in lockstep instead of drifting apart.
"""
from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path


def file_sha256(path: Path) -> str | None:
    try:
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except OSError:
        return None


def git_repo_root(start: Path) -> Path | None:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(start), "rev-parse", "--show-toplevel"],
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return Path(out.decode().strip())


def extract_image_refs(md_path: Path, image_re) -> list[Path]:
    """Every image `md_path` references via `image_re`, resolved and deduped."""
    text = md_path.read_text(encoding="utf-8")
    seen: set[str] = set()
    refs: list[Path] = []
    for match in image_re.finditer(text):
        ref = match.group(1)
        img = (md_path.parent / ref).resolve()
        key = str(img)
        if key in seen:
            continue
        seen.add(key)
        refs.append(img)
    return refs


def find_article_for_image(image_re, image_path: Path, repo_root: Path) -> Path | None:
    """The first markdown file anywhere in the repo that references image_path."""
    try:
        rel = image_path.relative_to(repo_root).as_posix()
    except ValueError:
        rel = image_path.name
    basename = image_path.name

    try:
        out = subprocess.check_output(
            [
                "git", "-C", str(repo_root),
                "grep", "--files-with-matches", "--null",
                "-e", basename, "--",
                "*.md",
            ],
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    candidates = [repo_root / p for p in out.decode().split("\0") if p]
    for cand in candidates:
        text = cand.read_text(encoding="utf-8", errors="ignore")
        for match in image_re.finditer(text):
            ref = match.group(1)
            if ref.endswith(basename) and (
                ref == basename
                or (cand.parent / ref).resolve() == image_path.resolve()
                or ref.endswith("/" + basename)
                or rel.endswith(ref)
            ):
                return cand
    return candidates[0] if candidates else None
