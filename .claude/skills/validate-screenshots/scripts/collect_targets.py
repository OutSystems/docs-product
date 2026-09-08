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

Two env vars let the calling workflow avoid validating the same image
twice when it fans out one invocation per changed file (see
.github/scripts/image-target-grouping/plan_targets.py):

* COLLECT_TARGETS_EXCLUDE — comma-separated absolute image paths to skip
  when resolving a markdown file's references (that image is already
  covered by its own standalone invocation this run).
* COLLECT_TARGETS_SHARED_WITH — comma-separated absolute article paths.
  When set on a single-image invocation, skip the whole-repo owner
  lookup and instead report the image as shared by those articles (the
  "article_path" field is null; a "shared_with" field lists the owners).
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

LIB_DIR = Path(".github") / "scripts" / "image-target-grouping"


def _find_lib_dir() -> Path:
    """Locate the shared owner-resolution module.

    This file sits at `ai-skills/<skill>/scripts/` in tk-cicd but at
    `.github/skills/<skill>/scripts/` and `.claude/skills/<skill>/scripts/`
    once synced into a consumer repo, so the repo root is a different number
    of levels up in each layout. Walk up until the directory turns up instead
    of counting parents.
    """
    for parent in Path(__file__).resolve().parents:
        candidate = parent / LIB_DIR
        if (candidate / "lib.py").is_file():
            return candidate
    raise SystemExit(f"error: cannot find {LIB_DIR}/lib.py in any parent of {__file__}")


sys.path.insert(0, str(_find_lib_dir()))
from lib import extract_image_refs, file_sha256, find_article_for_image, git_repo_root  # noqa: E402

IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+\.png)(?:\s+\"[^\"]*\")?\)")


def _env_path_list(name: str) -> list[str]:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return []
    return [p.strip() for p in raw.split(",") if p.strip()]


def resolve_markdown(md_path: Path, exclude: set[str] | None = None) -> list[dict]:
    exclude = exclude or set()
    entries: list[dict] = []
    for img in extract_image_refs(md_path, IMAGE_RE):
        key = str(img)
        if key in exclude:
            continue
        entries.append({
            "image_path": key,
            "article_path": str(md_path.resolve()),
            "sha256": file_sha256(img),
        })
    return entries


def resolve_single_png(png_path: Path, shared_with: list[str] | None = None) -> list[dict]:
    png_path = png_path.resolve()
    if shared_with:
        return [{
            "image_path": str(png_path),
            "article_path": None,
            "shared_with": shared_with,
            "sha256": file_sha256(png_path),
        }]
    repo_root = git_repo_root(png_path.parent) or png_path.parent
    article = find_article_for_image(IMAGE_RE, png_path, repo_root)
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
        article = find_article_for_image(IMAGE_RE, img, repo_root)
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
            exclude = {str(Path(p).resolve()) for p in _env_path_list("COLLECT_TARGETS_EXCLUDE")}
            entries = resolve_markdown(path, exclude=exclude)
        elif path.suffix.lower() == ".png":
            shared_with = _env_path_list("COLLECT_TARGETS_SHARED_WITH")
            entries = resolve_single_png(path, shared_with=shared_with)
        else:
            entries = []
    print(json.dumps(entries, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
