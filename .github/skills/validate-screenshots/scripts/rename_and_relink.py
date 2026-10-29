#!/usr/bin/env python3
"""Rename a screenshot and rewrite every markdown reference to it.

Validates the new filename against the skill's own rule-2 checks (check_metadata.py)
before touching anything, so this script can never produce a name that
would still fail the naming rule. It never chooses the new name itself —
the caller (the auto-fix phase of validate-screenshots, after applying its own mechanical or
vision-driven suffix logic) always supplies the destination path.

Usage:
    python3 rename_and_relink.py <old-path> <new-path> [--skip-naming-check]

--skip-naming-check bypasses the destination-name validation. It exists
only for the rollback path: the auto-fix phase's rule 2 renames a file's
matching Figma frame in the same pass, and if that Figma-side rename can't
be completed and verified, the skill reverts by calling this script again
with the old and new paths swapped. When the original name failed rule 2's
own check_naming (as opposed to a vision-only suffix-vs-content mismatch),
reverting to it would otherwise be rejected by the same guard that flagged
it in the first place. Never pass this flag for a forward (non-revert)
rename.

Prints a JSON object:
    {
      "old_path": "...", "new_path": "...",
      "renamed": true|false,
      "updated_files": ["docs/foo.md", ...],
      "errors": ["..."]
    }
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

try:
    from check_metadata import check_naming  # type: ignore
    from collect_targets import IMAGE_RE, git_repo_root  # type: ignore
except ImportError as exc:  # pragma: no cover - surfaced to the caller, not raised
    print(json.dumps({
        "old_path": None,
        "new_path": None,
        "renamed": False,
        "updated_files": [],
        "errors": [
            "could not import check_metadata/collect_targets from "
            f"{SCRIPTS_DIR}: {exc}. The validate-screenshots scripts directory "
            "is incomplete; reinstall the skill and retry.",
        ],
    }))
    raise SystemExit(0) from exc


def rewrite_references(repo_root: Path, old_basename: str, new_basename: str) -> tuple[list[str], list[str]]:
    """Rewrite every markdown image reference ending in old_basename.

    Returns (updated_relative_paths, errors).
    """
    try:
        out = subprocess.check_output(
            [
                "git", "-C", str(repo_root),
                "grep", "--files-with-matches", "--null", "--untracked",
                "-e", old_basename, "--",
                "*.md",
            ],
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return [], []
    except OSError as exc:
        return [], [f"git grep failed: {exc}"]

    updated: list[str] = []
    errors: list[str] = []
    for rel in (p for p in out.decode().split("\0") if p):
        md_path = repo_root / rel
        try:
            text = md_path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{rel}: could not read ({exc})")
            continue

        changed = False

        def _replace(match: re.Match[str]) -> str:
            nonlocal changed
            ref = match.group(1)
            if Path(ref).name != old_basename:
                return match.group(0)
            changed = True
            new_ref = ref[: -len(old_basename)] + new_basename
            return match.group(0).replace(ref, new_ref, 1)

        new_text = IMAGE_RE.sub(_replace, text)
        if changed:
            try:
                md_path.write_text(new_text, encoding="utf-8")
                updated.append(rel)
            except OSError as exc:
                errors.append(f"{rel}: could not write ({exc})")

    return updated, errors


def main(argv: list[str]) -> int:
    positional = [a for a in argv[1:] if a != "--skip-naming-check"]
    skip_naming_check = "--skip-naming-check" in argv[1:]
    if len(positional) != 2:
        print(
            "usage: rename_and_relink.py <old-path> <new-path> [--skip-naming-check]",
            file=sys.stderr,
        )
        return 2

    old_path = Path(positional[0]).expanduser().resolve()
    new_path = Path(positional[1]).expanduser().resolve()
    result = {
        "old_path": str(old_path),
        "new_path": str(new_path),
        "renamed": False,
        "updated_files": [],
        "errors": [],
    }

    if not old_path.is_file():
        result["errors"].append(f"source file not found: {old_path}")
        print(json.dumps(result))
        return 0

    if not skip_naming_check:
        naming = check_naming(new_path)
        if naming["verdict"] != "pass":
            result["errors"].append(
                f"destination name would still fail rule 2: {naming['reason']}",
            )
            print(json.dumps(result))
            return 0

    if new_path.exists():
        # On a case-insensitive filesystem (default on macOS/Windows), a pure
        # case change (DataMashup-ODCS.png -> datamashup-odcs.png) makes
        # new_path.exists() true even though it's the same file as old_path,
        # not a real collision. os.path.samefile compares inodes, which is
        # case-agnostic-safe either way.
        same_file = old_path.exists() and os.path.samefile(old_path, new_path)
        if not same_file:
            result["errors"].append(f"destination already exists: {new_path}")
            print(json.dumps(result))
            return 0

    repo_root = git_repo_root(old_path.parent)
    if repo_root is None:
        result["errors"].append(f"not inside a git repository: {old_path.parent}")
        print(json.dumps(result))
        return 0

    try:
        subprocess.run(
            ["git", "-C", str(repo_root), "mv", str(old_path), str(new_path)],
            check=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError:
        # Not tracked by git yet (or some other git-level issue) - fall back
        # to a plain filesystem rename so the fix still lands.
        try:
            old_path.rename(new_path)
        except OSError as exc:
            result["errors"].append(f"rename failed: {exc}")
            print(json.dumps(result))
            return 0
    except OSError as exc:
        result["errors"].append(f"git mv failed: {exc}")
        print(json.dumps(result))
        return 0

    result["renamed"] = True

    updated, rewrite_errors = rewrite_references(repo_root, old_path.name, new_path.name)
    result["updated_files"] = updated
    result["errors"].extend(rewrite_errors)

    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
