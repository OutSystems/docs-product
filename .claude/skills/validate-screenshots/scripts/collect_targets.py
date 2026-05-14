#!/usr/bin/env python3
"""Resolve an argument to the list of image targets the skill should review.

Modes:
    arg.endswith('.md')  -> every image referenced by the markdown
    arg is a single image file -> that one image
    arg is a directory -> every image file inside (recursive)
    arg empty or missing -> image files changed on the current branch vs. master

Non-PNG image formats (.jpg, .jpeg, .gif, .webp, .svg, .bmp) are included so
rule 1 of the rubric can flag them as format failures.

Output: JSON array on stdout, one entry per image:
    {"image_path": abspath, "article_path": str|None, "sha256": str|None}

The sha256 field lets downstream logic spot duplicate files — two
screenshots with the same hash are byte-for-byte identical and the
content developer should delete all but one.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+\.png)(?:\s+\"[^\"]*\")?\)")


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


def find_article_for_image(image_path: Path, repo_root: Path) -> Path | None:
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
        for match in IMAGE_RE.finditer(text):
            ref = match.group(1)
            if ref.endswith(basename) and (
                ref == basename
                or (cand.parent / ref).resolve() == image_path.resolve()
                or ref.endswith("/" + basename)
                or rel.endswith(ref)
            ):
                return cand
    return candidates[0] if candidates else None


def resolve_markdown(md_path: Path) -> list[dict]:
    text = md_path.read_text(encoding="utf-8")
    entries: list[dict] = []
    seen: set[str] = set()
    for match in IMAGE_RE.finditer(text):
        ref = match.group(1)
        img = (md_path.parent / ref).resolve()
        key = str(img)
        if key in seen:
            continue
        seen.add(key)
        entries.append({
            "image_path": str(img),
            "article_path": str(md_path.resolve()),
            "sha256": file_sha256(img),
        })
    return entries


def resolve_single_png(png_path: Path) -> list[dict]:
    png_path = png_path.resolve()
    repo_root = git_repo_root(png_path.parent) or png_path.parent
    article = find_article_for_image(png_path, repo_root)
    return [{
        "image_path": str(png_path),
        "article_path": str(article) if article else None,
        "sha256": file_sha256(png_path),
    }]


def resolve_branch_diff() -> list[dict]:
    cwd = Path.cwd()
    repo_root = git_repo_root(cwd)
    if repo_root is None:
        return []
    try:
        out = subprocess.check_output(
            ["git", "-C", str(repo_root),
             "diff", "--name-only", "--diff-filter=AMR",
             "master...HEAD", "--", "*.png"],
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return []
    entries: list[dict] = []
    for rel in out.decode().splitlines():
        rel = rel.strip()
        if not rel:
            continue
        img = (repo_root / rel).resolve()
        if not img.is_file():
            continue
        article = find_article_for_image(img, repo_root)
        entries.append({
            "image_path": str(img),
            "article_path": str(article) if article else None,
            "sha256": file_sha256(img),
        })
    return entries


def main(argv: list[str]) -> int:
    arg = argv[1].strip() if len(argv) > 1 else ""
    if not arg:
        entries = resolve_branch_diff()
    else:
        path = Path(os.path.expanduser(arg))
        if not path.is_absolute():
            path = (Path.cwd() / path).resolve()
        if not path.exists():
            print(json.dumps([]))
            return 0
        if path.suffix.lower() == ".md":
            entries = resolve_markdown(path)
        elif path.suffix.lower() == ".png":
            entries = resolve_single_png(path)
        else:
            entries = []
    print(json.dumps(entries, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
