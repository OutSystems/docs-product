#!/usr/bin/env python3
"""Regression tests for the baked-in (RGB fallback) shadow detector.

Run directly: python3 test_has_shadow.py

Exercises _baked_feather_length() against synthetic luma profiles, so a
future change to it can be checked without needing real screenshots on
disk. Covers the two failure modes this detector was rewritten for: a
locked global ramp direction that broke on light-theme "valley" profiles
(content lighter than the canvas background), and a flat plateau (a
header bar, a panel background) being miscounted as part of a gradient.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import has_shadow as hs  # noqa: E402


class FakeImage:
    """Minimal stand-in for a PIL image: a flat grid of grayscale rows."""

    def __init__(self, grid: list[list[int]]):
        self._grid = grid
        self.size = (len(grid[0]), len(grid))

    def getpixel(self, xy):
        x, y = xy
        v = self._grid[y][x]
        return (v, v, v, 255)


def top_edge_image(depth_values: list[int], w: int = 60, h: int = 60) -> FakeImage:
    """A FakeImage whose "top" edge slice reads exactly depth_values.

    Every row is filled uniformly so _averaged_lumas' perpendicular
    column sampling reads back the same value, unaffected by averaging.
    """
    grid = []
    n = len(depth_values)
    for y in range(h):
        v = depth_values[y] if y < n else depth_values[-1]
        grid.append([v] * w)
    return FakeImage(grid)


def run(name, fn) -> bool:
    try:
        fn()
        print(f"PASS  {name}")
        return True
    except AssertionError as e:
        print(f"FAIL  {name}: {e}")
        return False


def test_valley_profile_detected():
    # Light-theme capture: 229 background dips to ~181 (the shadow) before
    # jumping to 255 (lighter content) -- exactly the profile that broke
    # the original locked-sign implementation (a2a-call-details-odcs.png).
    depth = [229, 229, 229, 225, 218, 210, 202, 195, 188, 181, 181, 255] + [255] * 28
    img = top_edge_image(depth)
    w, h = img.size
    feather = hs._baked_feather_length(img, "top", w, h)
    assert feather is not None and feather > 0, f"expected a positive feather, got {feather}"


def test_straight_dark_theme_ramp_detected():
    # Straight monotonic ramp: background 40 -> darker content 10.
    depth = [40, 38, 35, 32, 28, 24, 20, 16, 12, 10] + [10] * 30
    img = top_edge_image(depth)
    w, h = img.size
    feather = hs._baked_feather_length(img, "top", w, h)
    assert feather is not None and feather > 0, f"expected a positive feather, got {feather}"


def test_flat_header_plateau_not_counted_as_feather():
    # A hard-edged UI region: white -> a flat gray header block -> white
    # again. No gradient anywhere -- must not be read as one long feather.
    depth = [255, 240, 230] + [230] * 20 + [255] * 17
    img = top_edge_image(depth)
    w, h = img.size
    feather = hs._baked_feather_length(img, "top", w, h)
    assert feather == 0, f"expected 0 (no real shadow), got {feather}"


def test_no_gradient_at_all_returns_zero():
    depth = [255] * 40
    img = top_edge_image(depth)
    w, h = img.size
    feather = hs._baked_feather_length(img, "top", w, h)
    assert feather == 0, f"expected 0, got {feather}"


def test_sharp_hard_edge_rejected():
    # A single-pixel jump straight from background to a very different
    # region -- an anti-aliased UI edge, not a shadow.
    depth = [255, 255, 30] + [30] * 37
    img = top_edge_image(depth)
    w, h = img.size
    feather = hs._baked_feather_length(img, "top", w, h)
    assert feather == 0, f"expected 0 (sharp edge, not a shadow), got {feather}"


TESTS = [
    test_valley_profile_detected,
    test_straight_dark_theme_ramp_detected,
    test_flat_header_plateau_not_counted_as_feather,
    test_no_gradient_at_all_returns_zero,
    test_sharp_hard_edge_rejected,
]


def main() -> int:
    results = [run(t.__name__, t) for t in TESTS]
    passed = sum(results)
    print(f"\n{passed}/{len(results)} passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
