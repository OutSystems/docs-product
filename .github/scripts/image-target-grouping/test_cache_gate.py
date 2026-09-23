#!/usr/bin/env python3
"""Regression tests for the pre-checkout cache gate.

Run directly: python3 test_cache_gate.py

The gate decides whether a whole job can be skipped without cloning the repo,
so the cases that matter are the ones where skipping would be wrong: a
referenced image changed while its article did not, a dep whose hash could
not be resolved, a skill version bump.
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cache_gate as cg  # noqa: E402


def run(name, fn) -> bool:
    try:
        fn()
        print(f"PASS  {name}")
        return True
    except AssertionError as e:
        print(f"FAIL  {name}: {e}")
        return False


SEM = "9f2a1c4d"


def _record(tmp: Path, entries: dict) -> str:
    path = tmp / "validation-record.json"
    path.write_text(
        json.dumps({"schema": 1, "skill": "validate-screenshots", "entries": entries}),
        encoding="utf-8",
    )
    return str(path)


def _blobs(tmp: Path, mapping: dict) -> str:
    path = tmp / "blobs.json"
    path.write_text(json.dumps(mapping), encoding="utf-8")
    return str(path)


def _changed(tmp: Path, files: list[str]) -> str:
    path = tmp / "changed.txt"
    path.write_text("\n".join(files) + "\n", encoding="utf-8")
    return str(path)


def _invoke(tmp: Path, *, changed, record, blobs, glob="*.md,*.png", ignore=".github"):
    """Run the gate and return its parsed $GITHUB_OUTPUT."""
    out = tmp / "gh_output"
    out.write_text("", encoding="utf-8")
    summary = tmp / "gh_summary"
    prev = dict(os.environ)
    os.environ["GITHUB_OUTPUT"] = str(out)
    os.environ["GITHUB_STEP_SUMMARY"] = str(summary)
    try:
        cg.main([
            "cache_gate.py",
            "--changed-files", _changed(tmp, changed),
            "--glob", glob,
            "--ignore-paths", ignore,
            "--record", _record(tmp, record),
            "--skill-version", SEM,
            "--max-age-days", "30",
            "--blob-shas", _blobs(tmp, blobs),
            "--skill", "validate-screenshots",
        ])
    finally:
        os.environ.clear()
        os.environ.update(prev)

    text = out.read_text(encoding="utf-8")
    skip = "skip=true" in text
    body = text.split("candidates<<CACHEGATE_EOF\n", 1)[1].split("CACHEGATE_EOF")[0]
    return skip, [c for c in body.splitlines() if c.strip()], summary


def test_all_cached_skips_before_checkout() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        skip, survivors, summary = _invoke(
            tmp,
            changed=["src/art.md"],
            record={"src/art.md": {
                "hash": "AAA", "skill_version": SEM, "validated_at": "2026-09-20T10:00:00Z",
                "run_id": "1", "verdict": "clean", "findings": [],
                "deps": {"src/images/x-ss.png": "XXX"},
            }},
            blobs={"src/art.md": "AAA", "src/images/x-ss.png": "XXX"},
        )
        assert skip is True, "unchanged article with unchanged deps must skip"
        assert survivors == [], survivors
        # A skipped job has no other output, so the summary must not be empty.
        assert "cache decisions" in summary.read_text().lower(), "summary missing"
        assert "skipped before checkout" in summary.read_text(), "skip not explained"


def test_referenced_image_changed_blocks_the_skip() -> None:
    """The motivating case, inverted: article untouched, image edited."""
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        skip, survivors, _ = _invoke(
            tmp,
            changed=["src/art.md"],
            record={"src/art.md": {
                "hash": "AAA", "skill_version": SEM, "validated_at": "2026-09-20T10:00:00Z",
                "run_id": "1", "verdict": "clean", "findings": [],
                "deps": {"src/images/x-ss.png": "XXX"},
            }},
            blobs={"src/art.md": "AAA", "src/images/x-ss.png": "CHANGED"},
        )
        assert skip is False, "a changed referenced image must force a run"
        assert survivors == ["src/art.md"], survivors


def test_unresolvable_dep_blocks_the_skip() -> None:
    """If we can't prove a dep is unchanged, we must not skip."""
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        skip, survivors, _ = _invoke(
            tmp,
            changed=["src/art.md"],
            record={"src/art.md": {
                "hash": "AAA", "skill_version": SEM, "validated_at": "2026-09-20T10:00:00Z",
                "run_id": "1", "verdict": "clean", "findings": [],
                "deps": {"src/images/x-ss.png": "XXX"},
            }},
            blobs={"src/art.md": "AAA"},  # dep hash absent (e.g. truncated tree)
        )
        assert skip is False, "an unresolvable dep must be treated as changed"
        assert survivors == ["src/art.md"], survivors


def test_changed_file_and_skill_bump_block_the_skip() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        entry = {"src/art.md": {
            "hash": "AAA", "skill_version": SEM, "validated_at": "2026-09-20T10:00:00Z",
            "run_id": "1", "verdict": "clean", "findings": [], "deps": {},
        }}

        skip, survivors, _ = _invoke(
            tmp, changed=["src/art.md"], record=entry, blobs={"src/art.md": "NEW"},
        )
        assert skip is False and survivors == ["src/art.md"], "edited file must run"

        stale_skill = {"src/art.md": dict(entry["src/art.md"], skill_version="OLDSKILL")}
        skip, survivors, _ = _invoke(
            tmp, changed=["src/art.md"], record=stale_skill, blobs={"src/art.md": "AAA"},
        )
        assert skip is False and survivors == ["src/art.md"], "skill bump must run"


def test_cached_findings_still_run_so_the_check_can_fail() -> None:
    """A skipped job is not a failing job — a known ❌ must not slip through.

    A required check that is skipped does not block a merge, so a file whose
    cached verdict has findings must keep the job running even though nothing
    changed. The skill re-emits the stored findings rather than re-deriving
    them, so the report stays complete and fail-on-error-marker still bites.
    """
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        base = {"hash": "AAA", "skill_version": SEM,
                "validated_at": "2026-09-20T10:00:00Z", "run_id": "1"}

        # The changed file itself carries findings.
        skip, survivors, _ = _invoke(
            tmp, changed=["src/art.md"],
            record={"src/art.md": dict(base, verdict="findings",
                                       findings=["❌ no shadow"], deps={})},
            blobs={"src/art.md": "AAA"},
        )
        assert skip is False, "cached findings must not skip the job"
        assert survivors == ["src/art.md"], survivors

        # The article is clean but an image it references is not.
        skip, survivors, _ = _invoke(
            tmp, changed=["src/art.md"],
            record={
                "src/art.md": dict(base, verdict="clean", findings=[],
                                   deps={"src/images/x-ss.png": "XXX"}),
                "src/images/x-ss.png": {"hash": "XXX", "skill_version": SEM,
                                        "verdict": "findings",
                                        "findings": ["❌ no shadow"],
                                        "validated_at": "2026-09-20T10:00:00Z",
                                        "run_id": "1", "deps": {}},
            },
            blobs={"src/art.md": "AAA", "src/images/x-ss.png": "XXX"},
        )
        assert skip is False, "a flagged dependency must not skip the job"
        assert survivors == ["src/art.md"], survivors

        # Control: all clean, so skipping is correct.
        skip, _, _ = _invoke(
            tmp, changed=["src/art.md"],
            record={
                "src/art.md": dict(base, verdict="clean", findings=[],
                                   deps={"src/images/x-ss.png": "XXX"}),
                "src/images/x-ss.png": {"hash": "XXX", "skill_version": SEM,
                                        "verdict": "clean", "findings": [],
                                        "validated_at": "2026-09-20T10:00:00Z",
                                        "run_id": "1", "deps": {}},
            },
            blobs={"src/art.md": "AAA", "src/images/x-ss.png": "XXX"},
        )
        assert skip is True, "an all-clean closure must still skip"


def test_partial_hit_narrows_to_survivors() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        skip, survivors, _ = _invoke(
            tmp,
            changed=["src/a.md", "src/b.md", "src/c.md"],
            record={
                "src/a.md": {"hash": "A", "skill_version": SEM, "deps": {},
                             "validated_at": "2026-09-20T10:00:00Z", "run_id": "1"},
                "src/b.md": {"hash": "B", "skill_version": SEM, "deps": {},
                             "validated_at": "2026-09-20T10:00:00Z", "run_id": "1"},
            },
            blobs={"src/a.md": "A", "src/b.md": "CHANGED", "src/c.md": "C"},
        )
        assert skip is False, skip
        assert survivors == ["src/b.md", "src/c.md"], survivors


def test_select_candidates_matches_workflow_filters() -> None:
    changed = [
        "src/art.md", "src/images/x-ss.png", "src/notes.txt",
        ".github/workflows/run.yml", "translated/pt/art.md",
    ]
    got = cg.select_candidates(changed, "*.md,*.png", ".github,translated")
    assert got == ["src/art.md", "src/images/x-ss.png"], got

    # No glob means no glob-narrowing, matching the workflow's own behaviour.
    assert cg.select_candidates(["a.md", "b.txt"], "", "") == ["a.md", "b.txt"]


def test_no_candidates_is_not_reported_as_a_cache_skip() -> None:
    """An empty run must not masquerade as a spectacularly effective cache."""
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        skip, survivors, _ = _invoke(
            tmp, changed=["src/notes.txt"], record={}, blobs={},
        )
        assert skip is False, "nothing to do is not a cache skip"
        assert survivors == [], survivors


TESTS = [
    test_all_cached_skips_before_checkout,
    test_referenced_image_changed_blocks_the_skip,
    test_unresolvable_dep_blocks_the_skip,
    test_changed_file_and_skill_bump_block_the_skip,
    test_cached_findings_still_run_so_the_check_can_fail,
    test_partial_hit_narrows_to_survivors,
    test_select_candidates_matches_workflow_filters,
    test_no_candidates_is_not_reported_as_a_cache_skip,
]


def main() -> int:
    results = [run(t.__name__, t) for t in TESTS]
    passed = sum(results)
    print(f"\n{passed}/{len(results)} passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
