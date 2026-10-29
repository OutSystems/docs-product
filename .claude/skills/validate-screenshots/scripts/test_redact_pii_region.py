#!/usr/bin/env python3
"""Regression tests for redact_pii_region.py.

Run directly: python3 test_redact_pii_region.py

Builds tiny synthetic PNGs (flat background + solid "glyph" blocks) so the
plan/plan-word-range/verify logic can be checked without needing a real
screenshot on disk. This script gates whether real PII leaks into published
docs, so its branches are worth pinning down explicitly:
  - a flat background yields a safe, padded cover box
  - a background that isn't dominated by one color is refused
  - content touching the search window's edge is refused (the window might
    not contain the whole text run)
  - word-range segmentation finds the right gap and covers only the target
    word(s)
  - a word-count mismatch falls back to covering the whole run automatically
  - verify() actually flags leftover foreground pixels as a fail
"""
from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
import redact_pii_region as rpr  # noqa: E402

BG = (240, 240, 240)


def run(name, fn) -> bool:
    try:
        fn()
        print(f"PASS  {name}")
        return True
    except AssertionError as e:
        print(f"FAIL  {name}: {e}")
        return False


class TmpImages:
    """Scratch directory for synthetic PNGs, cleaned up on exit."""

    def __enter__(self) -> "TmpImages":
        self.root = Path(tempfile.mkdtemp(prefix="redact-pii-test-"))
        return self

    def __exit__(self, *exc) -> None:
        shutil.rmtree(self.root, ignore_errors=True)

    def make(self, name: str, w: int, h: int, blocks: list[tuple[int, int, int, int, tuple[int, int, int]]]) -> str:
        img = Image.new("RGB", (w, h), BG)
        draw = ImageDraw.Draw(img)
        for x0, y0, x1, y1, color in blocks:
            draw.rectangle([x0, y0, x1, y1], fill=color)
        path = self.root / name
        img.save(path)
        return str(path)


def test_plan_flat_background_returns_safe_padded_cover_box():
    with TmpImages() as tmp:
        path = tmp.make("flat.png", 60, 30, [(20, 10, 39, 19, (0, 0, 0))])
        result = rpr.plan(path, 0, 0, 60, 30, tol=10, pad=4, bg_fraction=0.5)
        assert result["safe"] is True, result
        assert result["color_rgb"] == [240, 240, 240], result
        assert result["cover_box"] == {"x": 16, "y": 6, "w": 28, "h": 18}, result
        assert result["text_bbox"] == {"x": 20, "y": 10, "w": 20, "h": 10}, result


def test_plan_non_flat_background_is_unsafe():
    with TmpImages() as tmp:
        # Three ~equal stripes, each < the 0.5 bg_fraction threshold, and far
        # enough apart in value that they don't merge under tol=10.
        path = tmp.make("stripes.png", 60, 30, [
            (0, 0, 19, 29, (0, 0, 0)),
            (20, 0, 39, 29, (128, 128, 128)),
            (40, 0, 59, 29, (255, 255, 255)),
        ])
        result = rpr.plan(path, 0, 0, 60, 30, tol=10, pad=4, bg_fraction=0.5)
        assert result["safe"] is False, result
        assert "no single color dominates" in result["reason"], result


def test_plan_content_touching_window_edge_is_unsafe():
    with TmpImages() as tmp:
        # A column of "content" flush against the window's left edge (x=0).
        path = tmp.make("edge.png", 60, 30, [(0, 0, 5, 29, (0, 0, 0))])
        result = rpr.plan(path, 0, 0, 60, 30, tol=10, pad=4, bg_fraction=0.5)
        assert result["safe"] is False, result
        assert "touches the search window edge" in result["reason"], result


def test_verify_pass_and_fail():
    with TmpImages() as tmp:
        clean = tmp.make("clean.png", 20, 20, [])
        result = rpr.verify(clean, 0, 0, 20, 20, *BG, tol=10)
        assert result == {"verdict": "pass"}, result

        dirty = tmp.make("dirty.png", 20, 20, [(8, 8, 9, 9, (0, 0, 0))])
        result = rpr.verify(dirty, 0, 0, 20, 20, *BG, tol=10)
        assert result["verdict"] == "fail", result
        assert "pixel(s)" in result["reason"], result


def _three_word_line(tmp: TmpImages) -> str:
    """80x20 image with three 8px-wide "words" at x=10-17, 22-29, 34-41,
    separated by 4px background gaps at x=18-21 and x=30-33."""
    return tmp.make("line.png", 80, 20, [
        (10, 8, 17, 13, (0, 0, 0)),
        (22, 8, 29, 13, (0, 0, 0)),
        (34, 8, 41, 13, (0, 0, 0)),
    ])


def test_plan_word_range_covers_only_the_target_word():
    with TmpImages() as tmp:
        path = _three_word_line(tmp)
        # total_words=3, redact just the middle word (index 1).
        result = rpr.plan_word_range(
            path, 0, 0, 80, 20,
            total_words=3, pii_start_word=1, pii_end_word=1,
            tol=10, pad=4, bg_fraction=0.5, lum_thresh=18,
        )
        assert result["safe"] is True, result
        assert result["scope"] == "word_range", result
        assert result["detected_words"] == 3, result
        assert result["cover_box"] == {"x": 21, "y": 4, "w": 10, "h": 14}, result


def test_plan_word_range_falls_back_to_whole_line_on_count_mismatch():
    with TmpImages() as tmp:
        path = _three_word_line(tmp)
        # Claiming 5 words when only 3 are actually there -- must fall back
        # automatically rather than guess a gap, and must never report unsafe.
        result = rpr.plan_word_range(
            path, 0, 0, 80, 20,
            total_words=5, pii_start_word=3, pii_end_word=4,
            tol=10, pad=4, bg_fraction=0.5, lum_thresh=18,
        )
        assert result["safe"] is True, result
        assert result["scope"] == "whole_line", result
        assert result["detected_words"] == 3, result
        assert result["fallback_reason"] == "word count mismatch", result


TESTS = [
    test_plan_flat_background_returns_safe_padded_cover_box,
    test_plan_non_flat_background_is_unsafe,
    test_plan_content_touching_window_edge_is_unsafe,
    test_verify_pass_and_fail,
    test_plan_word_range_covers_only_the_target_word,
    test_plan_word_range_falls_back_to_whole_line_on_count_mismatch,
]


def main() -> int:
    results = [run(t.__name__, t) for t in TESTS]
    passed = sum(results)
    print(f"\n{passed}/{len(results)} passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
