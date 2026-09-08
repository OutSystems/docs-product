#!/usr/bin/env python3
"""Regression tests for collect_targets.py's dedup env vars.

Run directly: python3 test_collect_targets.py

Exercises resolve_markdown()'s COLLECT_TARGETS_EXCLUDE handling and
resolve_single_png()'s COLLECT_TARGETS_SHARED_WITH handling against a
throwaway git repo (collect_targets.py shells out to `git grep`/`git
rev-parse` to resolve an image's owning article, so a real repo is
needed for the "no shared_with" case).
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import collect_targets as ct  # noqa: E402


def run(name, fn) -> bool:
    try:
        fn()
        print(f"PASS  {name}")
        return True
    except AssertionError as e:
        print(f"FAIL  {name}: {e}")
        return False


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _git(*args: str, cwd: Path) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


class TmpRepo:
    def __enter__(self) -> Path:
        self.root = Path(tempfile.mkdtemp(prefix="collect-targets-test-"))
        _git("init", "-q", cwd=self.root)
        _git("config", "user.email", "test@example.com", cwd=self.root)
        _git("config", "user.name", "Test", cwd=self.root)
        return self.root

    def __exit__(self, *exc) -> None:
        shutil.rmtree(self.root, ignore_errors=True)


def test_resolve_markdown_honors_exclude():
    with TmpRepo() as root:
        img_a = root / "images" / "a-ss.png"
        img_b = root / "images" / "b-ss.png"
        _write(img_a, "a")
        _write(img_b, "b")
        md = root / "article.md"
        _write(md, "![alt](images/a-ss.png)\n![alt](images/b-ss.png)\n")

        entries = ct.resolve_markdown(md)
        assert {e["image_path"] for e in entries} == {str(img_a.resolve()), str(img_b.resolve())}, entries

        entries = ct.resolve_markdown(md, exclude={str(img_a.resolve())})
        assert {e["image_path"] for e in entries} == {str(img_b.resolve())}, entries


def test_resolve_single_png_with_shared_with():
    with TmpRepo() as root:
        img = root / "images" / "shared-ss.png"
        _write(img, "shared")
        article_a = str((root / "article-a.md").resolve())
        article_b = str((root / "article-b.md").resolve())

        entries = ct.resolve_single_png(img, shared_with=[article_a, article_b])
        assert len(entries) == 1, entries
        entry = entries[0]
        assert entry["article_path"] is None, entry
        assert entry["shared_with"] == [article_a, article_b], entry


def test_resolve_single_png_without_shared_with_resolves_owner():
    with TmpRepo() as root:
        img = root / "images" / "owned-ss.png"
        _write(img, "owned")
        md = root / "article.md"
        _write(md, "![alt](images/owned-ss.png)\n")
        _git("add", "-A", cwd=root)
        _git("commit", "-q", "-m", "init", cwd=root)

        entries = ct.resolve_single_png(img)
        assert len(entries) == 1, entries
        entry = entries[0]
        assert entry["article_path"] == str(md.resolve()), entry
        assert "shared_with" not in entry, entry


TESTS = [
    test_resolve_markdown_honors_exclude,
    test_resolve_single_png_with_shared_with,
    test_resolve_single_png_without_shared_with_resolves_owner,
]


def main() -> int:
    results = [run(t.__name__, t) for t in TESTS]
    passed = sum(results)
    print(f"\n{passed}/{len(results)} passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
