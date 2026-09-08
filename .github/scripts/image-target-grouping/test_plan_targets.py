#!/usr/bin/env python3
"""Regression tests for plan_targets.py's asset classification.

Run directly: python3 test_plan_targets.py

Builds a throwaway git repo with two articles and three PNGs covering
the three asset-classification outcomes (single PR-changed owner,
shared by two PR-changed owners, zero PR-changed owners) and asserts on
plan_targets.main()'s stdout.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from io import StringIO
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import plan_targets as pt  # noqa: E402


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
        self.root = Path(tempfile.mkdtemp(prefix="plan-targets-test-"))
        _git("init", "-q", cwd=self.root)
        _git("config", "user.email", "test@example.com", cwd=self.root)
        _git("config", "user.name", "Test", cwd=self.root)
        return self.root

    def __exit__(self, *exc) -> None:
        shutil.rmtree(self.root, ignore_errors=True)


def _run_plan(root: Path, lines: list[str]) -> dict:
    old_cwd = Path.cwd()
    old_stdin, old_stdout = sys.stdin, sys.stdout
    try:
        import os
        os.chdir(root)
        sys.stdin = StringIO("\n".join(lines) + "\n")
        sys.stdout = StringIO()
        pt.main(["plan_targets.py", "--extensions", "png,jpg,jpeg,gif,webp,bmp"])
        return json.loads(sys.stdout.getvalue())
    finally:
        import os
        os.chdir(old_cwd)
        sys.stdin, sys.stdout = old_stdin, old_stdout


def test_classification_cases():
    with TmpRepo() as root:
        _write(root / "images" / "shared-ss.png", "shared")
        _write(root / "images" / "only-a-ss.png", "only-a")
        _write(root / "images" / "orphan-ss.png", "orphan")
        _write(
            root / "article-a.md",
            "![alt](images/shared-ss.png)\n![alt](images/only-a-ss.png)\n",
        )
        _write(root / "article-b.md", "![alt](images/shared-ss.png)\n")

        result = _run_plan(
            root,
            [
                "article-a.md",
                "article-b.md",
                "images/shared-ss.png",
                "images/only-a-ss.png",
                "images/orphan-ss.png",
            ],
        )

        assert result["final_targets"] == [
            "article-a.md",
            "article-b.md",
            "images/shared-ss.png",
            "images/orphan-ss.png",
        ], result["final_targets"]

        article_a_abs = str((root / "article-a.md").resolve())
        article_b_abs = str((root / "article-b.md").resolve())
        shared_abs = str((root / "images" / "shared-ss.png").resolve())

        assert result["shared_map"] == {shared_abs: [article_a_abs, article_b_abs]}, result["shared_map"]
        assert set(result["exclude_map"].keys()) == {article_a_abs, article_b_abs}, result["exclude_map"]
        assert result["exclude_map"][article_a_abs] == [shared_abs]
        assert result["exclude_map"][article_b_abs] == [shared_abs]


TESTS = [test_classification_cases]


def main() -> int:
    results = [run(t.__name__, t) for t in TESTS]
    passed = sum(results)
    print(f"\n{passed}/{len(results)} passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
