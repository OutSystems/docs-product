#!/usr/bin/env python3
"""Regression tests for the cache write path.

Run directly: python3 test_cache_write.py

The write path decides what may be skipped in future, so the cases that
matter are the ones where recording something would hide a defect: a failed
run, a report with no verdict block, a file the verdict block never
mentions.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cache_write as cw  # noqa: E402

SEM = "9f2a1c4d"


def run(name, fn) -> bool:
    try:
        fn()
        print(f"PASS  {name}")
        return True
    except AssertionError as e:
        print(f"FAIL  {name}: {e}")
        return False


def _setup(tmp: Path, output: str, images=("a-ss.png", "b-ss.png")):
    """A repo-ish tree with an article and its images, plus an output capture."""
    (tmp / "src" / "images").mkdir(parents=True, exist_ok=True)
    art = tmp / "src" / "art.md"
    art.write_text("# Art\n", encoding="utf-8")
    manifest = {}
    for i, name in enumerate(images):
        p = tmp / "src" / "images" / name
        p.write_text(f"content-{i}", encoding="utf-8")
        from lib import git_blob_sha1
        manifest[f"src/images/{name}"] = git_blob_sha1(p)
    mpath = tmp / "manifest.json"
    mpath.write_text(json.dumps(manifest), encoding="utf-8")
    opath = tmp / "out.txt"
    opath.write_text(output, encoding="utf-8")
    return art, mpath, opath


_DELTA_SEQ = [0]


def _invoke(tmp, art, mpath, opath, exit_code=0, success_is_clean=False) -> dict:
    # A fresh delta per call: the real job appends every invocation into one
    # file, but a test that shared it would read back the previous case's
    # entries and assert on the wrong thing.
    _DELTA_SEQ[0] += 1
    delta = tmp / f"delta-{_DELTA_SEQ[0]}.json"
    cw.main([
        "cache_write.py",
        "--output", str(opath), "--target", str(art), "--manifest", str(mpath),
        "--delta", str(delta), "--skill-version", SEM, "--run-id", "42",
        "--repo-root", str(tmp), "--exit-code", str(exit_code),
    ] + (["--success-is-clean"] if success_is_clean else []))
    if not delta.exists():
        return {}
    return json.loads(delta.read_text(encoding="utf-8"))


def test_verdict_block_gives_per_file_granularity() -> None:
    out = """
<!-- VERDICTS {"src/images/a-ss.png":"clean","src/images/b-ss.png":"findings","src/art.md":"clean"} -->
<!-- REPORT BEGIN -->
<details>
## Screenshot review: art.md

### images/b-ss.png
- ❌ Missing TK-shadow effect available in the TK design library (rule 6)
- ⚠️ Highlight red is #CC2200, not the token #F22800
</details>
"""
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, mpath, opath = _setup(tmp, out)
        entries = _invoke(tmp, art, mpath, opath)

        assert set(entries) == {"src/art.md", "src/images/a-ss.png", "src/images/b-ss.png"}, entries
        assert entries["src/images/a-ss.png"]["verdict"] == "clean", "a passed"
        b = entries["src/images/b-ss.png"]
        assert b["verdict"] == "findings", b
        assert len(b["findings"]) == 2, b["findings"]
        assert "TK-shadow" in b["findings"][0], b["findings"]
        # Findings must be stored so the next run re-emits rather than re-derives.
        assert entries["src/images/a-ss.png"]["findings"] == [], "clean files carry none"
        assert all(e["skill_version"] == SEM for e in entries.values()), "skill_version stamped"

        # The target records the closure, so the gate can check it pre-checkout.
        assert set(entries["src/art.md"]["deps"]) == {
            "src/images/a-ss.png", "src/images/b-ss.png"
        }, entries["src/art.md"]["deps"]
        assert entries["src/images/a-ss.png"]["deps"] == {}, "images carry no closure"


def test_no_report_sentinel_is_the_fallback() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, mpath, opath = _setup(tmp, "some chatter\n<!-- NO REPORT -->\n")
        entries = _invoke(tmp, art, mpath, opath)
        assert set(entries) == {"src/art.md", "src/images/a-ss.png", "src/images/b-ss.png"}, entries
        assert all(e["verdict"] == "clean" for e in entries.values()), entries


def test_report_without_verdict_block_caches_nothing() -> None:
    """The dangerous case: findings exist but we can't attribute them."""
    out = """<!-- REPORT BEGIN -->
<details>
### images/b-ss.png
- ❌ Missing TK-shadow effect (rule 6)
</details>
"""
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, mpath, opath = _setup(tmp, out)
        assert _invoke(tmp, art, mpath, opath) == {}, "must not cache an unattributed report"


def test_failed_invocation_caches_nothing() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, mpath, opath = _setup(tmp, "<!-- NO REPORT -->\n")
        assert _invoke(tmp, art, mpath, opath, exit_code=1) == {}, "a failed run must not cache"


def test_unmentioned_file_is_not_claimed_as_passing() -> None:
    """A file the block omits was not assessed — don't record it as clean."""
    out = '<!-- VERDICTS {"src/images/a-ss.png":"clean","src/art.md":"clean"} -->\n'
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, mpath, opath = _setup(tmp, out)
        entries = _invoke(tmp, art, mpath, opath)
        assert "src/images/b-ss.png" not in entries, "unmentioned file must not be cached"
        assert "src/images/a-ss.png" in entries, entries


def test_last_verdict_block_wins_over_cli_preview() -> None:
    """The CLI echoes a truncated preview of a shell call before running it."""
    out = (
        '  │ <!-- VERDICTS {"src/images/a-ss.png":"findings"} -->\n'
        '  └ 12 lines…\n'
        '<!-- VERDICTS {"src/images/a-ss.png":"clean","src/art.md":"clean"} -->\n'
    )
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, mpath, opath = _setup(tmp, out)
        entries = _invoke(tmp, art, mpath, opath)
        assert entries["src/images/a-ss.png"]["verdict"] == "clean", entries


def test_malformed_verdict_block_falls_back_not_crashes() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        # Broken JSON, but the sentinel is present: fall back to it.
        art, mpath, opath = _setup(tmp, "<!-- VERDICTS {oops -->\n<!-- NO REPORT -->\n")
        entries = _invoke(tmp, art, mpath, opath)
        assert entries and all(e["verdict"] == "clean" for e in entries.values()), entries

        # Broken JSON and no sentinel: cache nothing.
        art2, m2, o2 = _setup(tmp, "<!-- VERDICTS {oops -->\n")
        assert _invoke(tmp, art2, m2, o2) == {}, "no usable signal must cache nothing"

        # Wrong value vocabulary is not a verdict block either.
        art3, m3, o3 = _setup(tmp, '<!-- VERDICTS {"src/art.md":"maybe"} -->\n')
        assert _invoke(tmp, art3, m3, o3) == {}, "unknown verdict values are unusable"


def test_fragment_captured_regardless_of_sentinel_order() -> None:
    """REPORT BEGIN is not a precondition for capturing the <details> block.

    The prompt asks the model to print REPORT BEGIN "immediately before the
    Step 3 summary heading" while also wrapping "the entire report" in
    <details>...</details>. The model resolves that ambiguity either way —
    sometimes REPORT BEGIN lands before <details>, sometimes just inside it,
    after <summary>. Both must still produce a stored report_fragment: a
    fragment silently dropped on one order means a later unchanged run has
    a cached verdict but nothing to replay, and (via the same anchor logic
    in the workflow's awk) a cold run's blocking findings go unreported.
    """
    sentinel_before = """
<!-- VERDICTS {"src/images/b-ss.png":"findings","src/art.md":"clean"} -->
<!-- REPORT BEGIN -->
<details>
<summary>art.md — 1 of 1 need changes</summary>

## Screenshot review: art.md

### images/b-ss.png
- ❌ Missing TK-shadow effect (rule 6)
</details>
"""
    sentinel_inside = """
<!-- VERDICTS {"src/images/b-ss.png":"findings","src/art.md":"clean"} -->
<details>
<summary>art.md — 1 of 1 need changes</summary>

<!-- REPORT BEGIN -->
## Screenshot review: art.md

### images/b-ss.png
- ❌ Missing TK-shadow effect (rule 6)
</details>
"""
    for label, out in [("before", sentinel_before), ("inside", sentinel_inside)]:
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            art, mpath, opath = _setup(tmp, out)
            entries = _invoke(tmp, art, mpath, opath)
            fragment = entries.get("src/art.md", {}).get("report_fragment")
            assert fragment, f"sentinel {label} <details>: no fragment stored, {entries}"
            assert fragment.startswith("<details>"), (label, fragment)
            assert fragment.endswith("</details>"), (label, fragment)
            assert "TK-shadow" in fragment, (label, fragment)
            # The sentinel line itself is a strip marker, not report content.
            assert "REPORT BEGIN" not in fragment, (label, fragment)


def test_fragment_ignores_cli_preview_of_details() -> None:
    """A previewed '  │ <details>' line must not be mistaken for the real tag."""
    out = (
        '  │ <details>\n'
        '  └ 12 lines…\n'
        '<!-- VERDICTS {"src/images/b-ss.png":"findings","src/art.md":"clean"} -->\n'
        '<details>\n'
        '<summary>art.md — 1 of 1 need changes</summary>\n'
        '\n'
        '<!-- REPORT BEGIN -->\n'
        '## Screenshot review: art.md\n'
        '\n'
        '### images/b-ss.png\n'
        '- ❌ Missing TK-shadow effect (rule 6)\n'
        '</details>\n'
    )
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, mpath, opath = _setup(tmp, out)
        entries = _invoke(tmp, art, mpath, opath)
        fragment = entries.get("src/art.md", {}).get("report_fragment")
        assert fragment, entries
        assert fragment.count("<details>") == 1, fragment
        assert not fragment.startswith("  │"), fragment


def test_no_report_skills_cache_on_a_clean_exit() -> None:
    """Tags, Summary, Alt Text and friends emit no sentinels at all."""
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, mpath, opath = _setup(tmp, "reclassified the article, wrote front matter\n")

        # Without the flag this output is unusable, and nothing is cached.
        assert _invoke(tmp, art, mpath, opath) == {}, "report skills need a signal"

        entries = _invoke(tmp, art, mpath, opath, success_is_clean=True)
        assert entries.get("src/art.md", {}).get("verdict") == "clean", entries

        # Still nothing on failure, flag or no flag.
        assert _invoke(
            tmp, art, mpath, opath, exit_code=2, success_is_clean=True
        ) == {}, "a failed no-report run must not cache"


TESTS = [
    test_verdict_block_gives_per_file_granularity,
    test_fragment_captured_regardless_of_sentinel_order,
    test_fragment_ignores_cli_preview_of_details,
    test_no_report_skills_cache_on_a_clean_exit,
    test_no_report_sentinel_is_the_fallback,
    test_report_without_verdict_block_caches_nothing,
    test_failed_invocation_caches_nothing,
    test_unmentioned_file_is_not_claimed_as_passing,
    test_last_verdict_block_wins_over_cli_preview,
    test_malformed_verdict_block_falls_back_not_crashes,
]


def main() -> int:
    results = [run(t.__name__, t) for t in TESTS]
    passed = sum(results)
    print(f"\n{passed}/{len(results)} passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
