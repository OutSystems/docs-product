#!/usr/bin/env python3
"""Regression tests for republishing a cached report without the model.

Run directly: python3 test_cache_replay.py

Replay publishes a PR comment that gates a merge, so the cases that matter
are the ones where it must refuse: a changed image behind an unchanged
article, an entry from an older skill version, an entry that predates
fragment storage.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cache_replay as cr  # noqa: E402
from cache_write import extract_fragment  # noqa: E402
from lib import git_blob_sha1  # noqa: E402

SEM = "9f2a1c4d"
FRAGMENT = "<details>\n<summary>art.md — 1 of 2 need changes</summary>\n\n### images/b-ss.png\n- ❌ Missing TK-shadow effect (rule 6)\n\n</details>"


def run(name, fn) -> bool:
    try:
        fn()
        print(f"PASS  {name}")
        return True
    except AssertionError as e:
        print(f"FAIL  {name}: {e}")
        return False


def _repo(tmp: Path):
    (tmp / "src" / "images").mkdir(parents=True, exist_ok=True)
    art = tmp / "src" / "art.md"
    art.write_text("# Art\n", encoding="utf-8")
    imgs = {}
    for name, body in (("a-ss.png", "AAA"), ("b-ss.png", "BBB")):
        p = tmp / "src" / "images" / name
        p.write_text(body, encoding="utf-8")
        imgs[f"src/images/{name}"] = git_blob_sha1(p)
    return art, imgs


def _record(tmp: Path, art: Path, imgs: dict, **over) -> str:
    entry = {
        "hash": git_blob_sha1(art), "skill_version": SEM,
        "validated_at": "2026-09-20T10:00:00Z", "run_id": "1",
        "verdict": "findings", "findings": ["❌ Missing TK-shadow effect (rule 6)"],
        "deps": dict(imgs), "report_fragment": FRAGMENT,
    }
    entry.update(over)
    path = tmp / "validation-record.json"
    path.write_text(json.dumps({"schema": 1, "skill": "validate-screenshots",
                                "entries": {"src/art.md": entry}}), encoding="utf-8")
    return str(path)


def _replay(tmp: Path, art: Path, record: str, sem=SEM):
    out = tmp / "out.txt"
    rc = cr.main(["cache_replay.py", "--target", str(art), "--record", record,
                  "--skill-version", sem, "--repo-root", str(tmp), "--out", str(out)])
    return rc, (out.read_text(encoding="utf-8") if out.exists() else "")


def test_replays_when_everything_is_unchanged() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, imgs = _repo(tmp)
        rc, out = _replay(tmp, art, _record(tmp, art, imgs))
        assert rc == 0, "an unchanged closure must replay"
        # Must reproduce exactly what the skill would have printed, so the
        # workflow's existing awk capture still finds it.
        assert "<!-- REPORT BEGIN -->" in out, out
        assert FRAGMENT in out, out
        assert extract_fragment(out) == FRAGMENT, "round-trips through the awk equivalent"


def test_log_counts_findings_from_the_report_not_the_article(capsys=None) -> None:
    """The article's own findings list is empty; the report's is not.

    Counting the wrong one printed "republishing 0 finding(s)" while
    republishing fourteen, which is exactly the line someone reads to decide
    whether the cache is lying to them.
    """
    import io
    from contextlib import redirect_stdout
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, imgs = _repo(tmp)
        # Article clean, findings live on the images — the real shape.
        record = _record(tmp, art, imgs, verdict="clean", findings=[])
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc, _ = _replay(tmp, art, record)
        out = buf.getvalue()
        assert rc == 0, out
        assert "1 blocking" in out, out
        assert "0 warning" in out, out
        assert "0 blocking" not in out, "must not report the article's empty list"


def test_clean_target_replays_the_no_report_sentinel() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, imgs = _repo(tmp)
        record = _record(tmp, art, imgs, verdict="clean", findings=[], report_fragment="")
        rc, out = _replay(tmp, art, record)
        assert rc == 0, "a clean target must replay too"
        assert out.strip() == "<!-- NO REPORT -->", out
        # That sentinel is what deletes a stale sticky comment, so it must be
        # reproduced rather than silently omitted.


def test_changed_dependency_refuses_to_replay() -> None:
    """The article is untouched but one of its images is not."""
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, imgs = _repo(tmp)
        record = _record(tmp, art, imgs)
        (tmp / "src" / "images" / "b-ss.png").write_text("CHANGED", encoding="utf-8")
        rc, _ = _replay(tmp, art, record)
        assert rc == 1, "a changed image must force a real run"


def test_missing_dependency_refuses_to_replay() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, imgs = _repo(tmp)
        record = _record(tmp, art, imgs)
        (tmp / "src" / "images" / "b-ss.png").unlink()
        rc, _ = _replay(tmp, art, record)
        assert rc == 1, "an unreadable image must force a real run"


def test_changed_article_refuses_to_replay() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, imgs = _repo(tmp)
        record = _record(tmp, art, imgs)
        art.write_text("# Art\n\nNew prose.\n", encoding="utf-8")
        rc, _ = _replay(tmp, art, record)
        assert rc == 1, "a changed article must force a real run"


def test_skill_version_change_refuses_to_replay() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, imgs = _repo(tmp)
        rc, _ = _replay(tmp, art, _record(tmp, art, imgs), sem="DIFFERENT")
        assert rc == 1, "a rubric or model change must force a real run"


def test_entry_without_a_fragment_refuses_to_replay() -> None:
    """Written before fragments existed: we know the verdict, not the wording."""
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, imgs = _repo(tmp)
        entry_path = _record(tmp, art, imgs)
        data = json.loads(Path(entry_path).read_text())
        del data["entries"]["src/art.md"]["report_fragment"]
        Path(entry_path).write_text(json.dumps(data))
        rc, _ = _replay(tmp, art, entry_path)
        assert rc == 1, "no stored report means no replay"


def test_no_record_refuses_to_replay() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        art, _ = _repo(tmp)
        rc, _ = _replay(tmp, art, str(tmp / "absent.json"))
        assert rc == 1, "no validation record means no replay"


def test_extract_fragment_ignores_the_cli_preview() -> None:
    """The CLI echoes a truncated preview of a shell call before running it."""
    text = (
        "  │ <!-- REPORT BEGIN -->\n"
        "  │ <details>\n"
        "  └ 12 lines…\n"
        "<!-- REPORT BEGIN -->\n"
        "<details>\n"
        "real report\n"
        "</details>\n"
    )
    got = extract_fragment(text)
    assert got == "<details>\nreal report\n</details>", got
    assert extract_fragment("nothing here") is None, "no report means None"


TESTS = [
    test_replays_when_everything_is_unchanged,
    test_log_counts_findings_from_the_report_not_the_article,
    test_clean_target_replays_the_no_report_sentinel,
    test_changed_dependency_refuses_to_replay,
    test_missing_dependency_refuses_to_replay,
    test_changed_article_refuses_to_replay,
    test_skill_version_change_refuses_to_replay,
    test_entry_without_a_fragment_refuses_to_replay,
    test_no_record_refuses_to_replay,
    test_extract_fragment_ignores_the_cli_preview,
]


def main() -> int:
    results = [run(t.__name__, t) for t in TESTS]
    print(f"\n{sum(results)}/{len(results)} passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
