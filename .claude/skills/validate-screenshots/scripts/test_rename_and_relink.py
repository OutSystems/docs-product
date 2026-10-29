#!/usr/bin/env python3
"""Tests for rename_and_relink.py.

Run directly: python3 test_rename_and_relink.py

Each case builds a throwaway git repository, because the script renames with
`git mv` and finds references with `git grep`. Pins down what the auto-fix
phase relies on for rule 2: the file is renamed and its rename is staged, every
markdown reference follows, an invalid destination name or a collision changes
nothing, and the script imports its sibling checkers from its own directory
(it once resolved them through a sibling skill's path, which broke the moment
the two skills were merged).
"""
from __future__ import annotations

import io
import json
import subprocess
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rename_and_relink as rr  # noqa: E402


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True)


def make_repo(tmp: Path) -> Path:
    repo = tmp / "repo"
    (repo / "src" / "images").mkdir(parents=True)
    git(tmp, "init", "-q", "repo")
    git(repo, "config", "user.email", "t@t")
    git(repo, "config", "user.name", "t")
    Image.new("RGBA", (200, 100), (240, 240, 240, 255)).save(repo / "src/images/portal-page-ss.png")
    (repo / "src/a.md").write_text("---\nguid: g\n---\n![x](images/portal-page-ss.png)\n")
    (repo / "src/b.md").write_text("![y](images/portal-page-ss.png) and ![z](images/other-ss.png)\n")
    Image.new("RGBA", (50, 50)).save(repo / "src/images/other-ss.png")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "base")
    return repo


def call(*argv: str) -> dict:
    buf = io.StringIO()
    with redirect_stdout(buf):
        rr.main(["rename_and_relink.py", *argv])
    return json.loads(buf.getvalue())


def run(name, fn) -> bool:
    with tempfile.TemporaryDirectory() as d:
        try:
            fn(make_repo(Path(d)))
            print(f"PASS  {name}")
            return True
        except AssertionError as e:
            print(f"FAIL  {name}: {e}")
            return False


def test_imports_resolve_from_its_own_directory(repo):
    assert rr.SCRIPTS_DIR == Path(rr.__file__).resolve().parent, rr.SCRIPTS_DIR
    assert (rr.SCRIPTS_DIR / "check_metadata.py").is_file(), "check_metadata.py must sit next to the script"


def test_rename_moves_file_stages_it_and_rewrites_every_reference(repo):
    old = repo / "src/images/portal-page-ss.png"
    new = repo / "src/images/portal-page-pl.png"
    res = call(str(old), str(new))
    assert res["renamed"] is True and not res["errors"], res
    assert new.is_file() and not old.exists(), "file was not moved"
    assert sorted(res["updated_files"]) == ["src/a.md", "src/b.md"], res
    assert "portal-page-pl.png" in (repo / "src/a.md").read_text()
    assert "portal-page-ss.png" not in (repo / "src/b.md").read_text()
    assert "other-ss.png" in (repo / "src/b.md").read_text(), "unrelated references must stay"
    staged = git(repo, "diff", "--cached", "--name-status", "-M").splitlines()
    assert any(line.startswith("R") and "portal-page-ss.png" in line and "portal-page-pl.png" in line for line in staged), staged


def test_invalid_destination_name_changes_nothing(repo):
    old = repo / "src/images/portal-page-ss.png"
    res = call(str(old), str(repo / "src/images/portal-page.png"))
    assert res["renamed"] is False, res
    assert any("rule 2" in e for e in res["errors"]), res
    assert old.is_file(), "source must be untouched"
    assert "portal-page-ss.png" in (repo / "src/a.md").read_text()


def test_existing_destination_is_not_overwritten(repo):
    old = repo / "src/images/portal-page-ss.png"
    res = call(str(old), str(repo / "src/images/other-ss.png"))
    assert res["renamed"] is False, res
    assert any("already exists" in e for e in res["errors"]), res
    assert old.is_file()


def test_missing_source_is_reported(repo):
    res = call(str(repo / "src/images/nope-ss.png"), str(repo / "src/images/nope-pl.png"))
    assert res["renamed"] is False and any("not found" in e for e in res["errors"]), res


TESTS = [
    test_imports_resolve_from_its_own_directory,
    test_rename_moves_file_stages_it_and_rewrites_every_reference,
    test_invalid_destination_name_changes_nothing,
    test_existing_destination_is_not_overwritten,
    test_missing_source_is_reported,
]


def main() -> int:
    results = [run(t.__name__, t) for t in TESTS]
    print(f"\n{sum(results)}/{len(results)} passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
