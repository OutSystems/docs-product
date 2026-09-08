#!/usr/bin/env python3
"""Plan which files in a PR's filtered file list get their own skill
invocation, so an image referenced by an article changed in the same PR
is validated once (inside that article's invocation) instead of twice.

Reads a newline-separated list of already-filtered changed files (the
same list that would otherwise feed the per-file Copilot loop directly)
from stdin. Every file is either a markdown article or one of the asset
extensions passed via --extensions; anything else is passed through
untouched.

For every asset, counts how many of the *changed* articles in this same
list actually reference it:

    0 owners  -> keep the asset as its own target (its owning article, if
                 any, is resolved later by collect_targets.py against the
                 whole repo; if none exists anywhere, it's a true orphan).
    1 owner   -> drop the asset; the owning article's own invocation
                 already validates it via resolve_markdown().
    2+ owners -> keep the asset as its own target (so it's validated once,
                 not once per owning article), and record it in the
                 exclude map for every one of those owning articles so
                 their own invocations skip it.

Prints a single JSON object to stdout:
    {
      "final_targets": [...],           # same relative paths as the input, filtered
      "exclude_map": {article_abspath: [asset_abspath, ...]},
      "shared_map": {asset_abspath: [article_abspath, ...]}
    }
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import extract_image_refs, git_repo_root  # noqa: E402


def build_image_re(extensions: list[str]) -> re.Pattern:
    alternation = "|".join(re.escape(ext) for ext in extensions)
    return re.compile(r"!\[[^\]]*\]\(([^)\s]+\.(?:" + alternation + r"))(?:\s+\"[^\"]*\")?\)")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extensions", required=True, help="Comma-separated asset extensions, e.g. 'png,jpg,jpeg,gif,webp,bmp'")
    args = parser.parse_args(argv[1:])

    extensions = {e.strip().lower().lstrip(".") for e in args.extensions.split(",") if e.strip()}
    image_re = build_image_re(sorted(extensions))

    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    repo_root = git_repo_root(Path.cwd()) or Path.cwd()

    articles = [line for line in lines if line.lower().endswith(".md")]
    articles_set = set(articles)
    assets_set = {
        line for line in lines
        if line not in articles_set and Path(line).suffix.lower().lstrip(".") in extensions
    }

    owners_by_asset: dict[str, list[str]] = {}
    for article in articles:
        article_abs = str((repo_root / article).resolve())
        article_path = Path(article_abs)
        if not article_path.is_file():
            continue
        for img in extract_image_refs(article_path, image_re):
            owners_by_asset.setdefault(str(img), []).append(article_abs)

    final_targets: list[str] = []
    exclude_map: dict[str, list[str]] = {}
    shared_map: dict[str, list[str]] = {}

    for line in lines:
        if line in articles_set or line not in assets_set:
            final_targets.append(line)
            continue

        asset_abs = str((repo_root / line).resolve())
        owners = owners_by_asset.get(asset_abs, [])
        if len(owners) == 1:
            continue

        final_targets.append(line)
        if len(owners) >= 2:
            shared_map[asset_abs] = owners
            for owner in owners:
                exclude_map.setdefault(owner, []).append(asset_abs)

    json.dump(
        {"final_targets": final_targets, "exclude_map": exclude_map, "shared_map": shared_map},
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
