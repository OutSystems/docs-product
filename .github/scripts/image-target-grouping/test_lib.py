#!/usr/bin/env python3
"""Regression tests for the validation-cache helpers in lib.py.

Run directly: python3 test_lib.py

Covers the three properties the AI-skills file-hash cache depends on:
git_blob_sha1 agreeing with `git hash-object` (so the workflow's
pre-checkout gate and the in-skill collector share a hash space), and
load_validation_record / record_hit failing towards "not cached" on every kind of
bad input rather than towards a stale verdict.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import (  # noqa: E402
    CACHE_REASONS,
    RECORD_SCHEMA,
    cache_decision,
    format_decision_line,
    git_blob_sha1,
    record_hit,
    load_validation_record,
    repo_relpath,
    summary_table,
)


def run(name, fn) -> bool:
    try:
        fn()
        print(f"PASS  {name}")
        return True
    except AssertionError as e:
        print(f"FAIL  {name}: {e}")
        return False


def _record_file(tmp: Path, payload) -> str:
    path = tmp / "validation-record.json"
    path.write_text(
        payload if isinstance(payload, str) else json.dumps(payload),
        encoding="utf-8",
    )
    return str(path)


def test_blob_sha1_matches_git_hash_object() -> None:
    """The whole design rests on this: our hash == the one the API returns."""
    if not shutil.which("git"):
        print("      (skipped: git not on PATH)")
        return
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        cases = {
            "empty.txt": b"",
            "text.md": b"# Title\n\nSome content with a trailing newline.\n",
            "binary.png": bytes(range(256)) * 300,  # >64 KiB, exercises chunking
        }
        for name, content in cases.items():
            path = tmp / name
            path.write_bytes(content)
            expected = subprocess.check_output(
                ["git", "hash-object", str(path)]
            ).decode().strip()
            actual = git_blob_sha1(path)
            assert actual == expected, f"{name}: {actual} != {expected}"


def test_blob_sha1_unreadable_is_none() -> None:
    with tempfile.TemporaryDirectory() as td:
        missing = Path(td) / "nope.png"
        assert git_blob_sha1(missing) is None, "missing file should hash to None"
        assert git_blob_sha1(Path(td)) is None, "a directory should hash to None"


def test_load_validation_record_degrades_to_empty() -> None:
    """Every bad input must mean "nothing cached", never a partial validation record."""
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        good = {"schema": RECORD_SCHEMA, "entries": {"a.md": {"hash": "abc"}}}

        assert load_validation_record(None) == {}, "unset path"
        assert load_validation_record("") == {}, "empty path"
        assert load_validation_record(str(tmp / "absent.json")) == {}, "missing file"
        assert load_validation_record(_record_file(tmp, "{not json")) == {}, "truncated json"
        assert load_validation_record(_record_file(tmp, [1, 2, 3])) == {}, "not an object"
        assert load_validation_record(_record_file(tmp, {"entries": {"a": {}}})) == {}, "no schema"
        assert load_validation_record(
            _record_file(tmp, {"schema": RECORD_SCHEMA + 1, "entries": {"a": {}}})
        ) == {}, "future schema"
        assert load_validation_record(
            _record_file(tmp, {"schema": RECORD_SCHEMA, "entries": "nope"})
        ) == {}, "entries not an object"
        assert load_validation_record(_record_file(tmp, good)) == good["entries"], "valid validation record"


def test_record_hit_only_on_exact_hash() -> None:
    entries = {
        "src/a.md": {"hash": "aaa", "verdict": "clean", "findings": []},
        "src/b.png": {"hash": "bbb", "verdict": "findings", "findings": ["x"]},
        "src/weird.png": "not-a-dict",
    }
    assert record_hit(entries, "src/a.md", "aaa") == entries["src/a.md"], "exact match"
    assert record_hit(entries, "src/a.md", "zzz") is None, "changed hash must miss"
    assert record_hit(entries, "src/absent.md", "aaa") is None, "no entry must miss"
    assert record_hit(entries, "src/a.md", None) is None, "unhashable file must miss"
    assert record_hit(entries, "src/a.md", "") is None, "empty hash must miss"
    assert record_hit(entries, "src/weird.png", "ccc") is None, "malformed entry must miss"

    hit = record_hit(entries, "src/b.png", "bbb")
    assert hit is not None and hit["findings"] == ["x"], "findings must survive a hit"


def test_repo_relpath() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td).resolve()
        inside = root / "src" / "images" / "x-ss.png"
        assert repo_relpath(inside, root) == "src/images/x-ss.png", "inside the repo"

        # Outside the root, the key falls back to an absolute path: it is
        # workspace-specific so it can only ever miss, which beats a bare
        # basename that two different files could share.
        outside = Path(td).parent / "elsewhere-ss.png"
        assert repo_relpath(outside, root) == outside.resolve().as_posix(), "outside"
        assert repo_relpath(inside, None) == inside.resolve().as_posix(), "no root"


def test_cache_decision_reasons() -> None:
    """Every outcome must carry a reason a human can act on in a log."""
    now = datetime(2026, 9, 21, tzinfo=timezone.utc)
    entries = {
        "src/a.md": {
            "hash": "aaa", "verdict": "clean", "findings": [],
            "validated_at": "2026-09-20T10:00:00Z", "run_id": "111",
        },
        "src/b.png": {
            "hash": "bbb", "verdict": "findings", "findings": ["❌ no shadow"],
            "validated_at": "2026-09-20T10:00:00Z", "run_id": "111",
        },
        "src/old.png": {
            "hash": "ccc", "verdict": "clean", "findings": [],
            "validated_at": "2026-01-01T10:00:00Z", "run_id": "001",
        },
    }

    def decide(rel, sha, **kw):
        return cache_decision(entries, rel, sha, now=now, **kw)

    hit = decide("src/a.md", "aaa")
    assert hit["cached"] is True and hit["reason"] == "hit", hit
    assert "111" in hit["detail"] and "2026-09-20" in hit["detail"], hit["detail"]

    findings = decide("src/b.png", "bbb")
    assert findings["cached"] is True, findings
    assert "1 cached finding" in findings["detail"], findings["detail"]
    assert findings["entry"]["findings"] == ["❌ no shadow"], findings

    changed = decide("src/a.md", "zzz")
    assert changed["cached"] is False and changed["reason"] == "content-changed", changed
    assert "aaa" in changed["detail"] and "zzz" in changed["detail"], changed["detail"]

    absent = decide("src/new.md", "aaa")
    assert absent["cached"] is False and absent["reason"] == "never-validated", absent

    unhashable = decide("src/a.md", None)
    assert unhashable["cached"] is False and unhashable["reason"] == "unreadable", unhashable

    stale = decide("src/old.png", "ccc", max_age_days=30)
    assert stale["cached"] is False and stale["reason"] == "expired", stale
    assert "30d max age" in stale["detail"], stale["detail"]

    # Same entry, no max age configured: still a hit.
    assert decide("src/old.png", "ccc")["cached"] is True, "no max age means no expiry"

    cold = decide("src/a.md", "aaa", record_present=False)
    assert cold["cached"] is False and cold["reason"] == "not-cached-yet", cold

    for rel, sha, kw in [
        ("src/a.md", "aaa", {}), ("src/a.md", "zzz", {}), ("src/new.md", "aaa", {}),
        ("src/a.md", None, {}), ("src/old.png", "ccc", {"max_age_days": 30}),
    ]:
        d = decide(rel, sha, **kw)
        assert d["reason"] in CACHE_REASONS, f"unknown reason {d['reason']}"
        assert d["detail"], f"no detail for {d['reason']}"


def test_skill_change_invalidates_and_says_so() -> None:
    """A rubric/checker/model change must re-run everything, with the cause named."""
    entries = {
        "src/a.md": {
            "hash": "aaa", "skill_version": "9f2a1c4d", "verdict": "clean",
            "findings": [], "validated_at": "2026-09-20T10:00:00Z", "run_id": "111",
        },
    }

    same = cache_decision(entries, "src/a.md", "aaa", skill_version="9f2a1c4d")
    assert same["cached"] is True, "unchanged skill must still hit"

    changed = cache_decision(entries, "src/a.md", "aaa", skill_version="4b8e2d77")
    assert changed["cached"] is False, changed
    assert changed["reason"] == "rubric-changed", changed
    # The whole point of storing it per entry: name both versions in the log.
    assert "9f2a1c4d" in changed["detail"], changed["detail"]
    assert "4b8e2d77" in changed["detail"], changed["detail"]

    # A skill change is reported even when the content also changed, so the
    # log makes it obvious the cause is global rather than per-file.
    both = cache_decision(entries, "src/a.md", "zzz", skill_version="4b8e2d77")
    assert both["reason"] == "rubric-changed", both

    # An entry written before skill_version were recorded is not trustworthy.
    legacy = {"src/a.md": {"hash": "aaa", "validated_at": "2026-09-20T10:00:00Z"}}
    d = cache_decision(legacy, "src/a.md", "aaa", skill_version="9f2a1c4d")
    assert d["cached"] is False and d["reason"] == "rubric-changed", d

    # Callers that don't track skill_version (nothing does today, but the
    # signature allows it) must not be forced into a permanent miss.
    assert cache_decision(legacy, "src/a.md", "aaa")["cached"] is True, "opt-out"


def test_cache_decision_survives_bad_timestamps() -> None:
    """A malformed timestamp must not crash the run or fake a skip."""
    entries = {"src/a.md": {"hash": "aaa", "validated_at": "not-a-date"}}
    d = cache_decision(entries, "src/a.md", "aaa", max_age_days=30)
    assert d["cached"] is True and d["reason"] == "hit", d

    entries = {"src/a.md": {"hash": "aaa"}}  # no timestamp at all
    d = cache_decision(entries, "src/a.md", "aaa", max_age_days=30)
    assert d["cached"] is True, d
    assert d["detail"], "a hit with no timestamp still needs a detail line"


def test_log_formatting_distinguishes_skip_from_run() -> None:
    entries = {
        "src/a.md": {
            "hash": "aaa", "verdict": "clean", "findings": [],
            "validated_at": "2026-09-20T10:00:00Z", "run_id": "111",
        },
    }
    hit = cache_decision(entries, "src/a.md", "aaa")
    miss = cache_decision(entries, "src/b.md", "bbb")

    hit_line = format_decision_line("src/a.md", hit)
    miss_line = format_decision_line("src/b.md", miss)
    assert hit_line.startswith("⏭️"), hit_line
    assert miss_line.startswith("▶️"), miss_line
    assert "run 111" in hit_line, hit_line
    assert "never validated" in miss_line, miss_line

    table = summary_table("validate-screenshots", [("src/a.md", hit), ("src/b.md", miss)])
    assert "1 of 2 target(s) skipped (cache), 1 validated" in table, table
    assert "`src/a.md`" in table and "`src/b.md`" in table, table
    assert "2026-09-20T10:00:00Z" in table and "111" in table, table
    # A miss has no entry, so its timestamp/run columns must degrade, not crash.
    assert "| — |" in table, table


TESTS = [
    test_blob_sha1_matches_git_hash_object,
    test_blob_sha1_unreadable_is_none,
    test_load_validation_record_degrades_to_empty,
    test_record_hit_only_on_exact_hash,
    test_repo_relpath,
    test_cache_decision_reasons,
    test_cache_decision_survives_bad_timestamps,
    test_skill_change_invalidates_and_says_so,
    test_log_formatting_distinguishes_skip_from_run,
]


def main() -> int:
    results = [run(t.__name__, t) for t in TESTS]
    passed = sum(results)
    print(f"\n{passed}/{len(results)} passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
