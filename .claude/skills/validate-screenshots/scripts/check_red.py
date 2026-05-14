#!/usr/bin/env python3
"""Verify that the dominant red rectangle highlight in a screenshot matches
the OutSystems design-system token #F22800.

The Figma library highlight component renders as a thin, axis-aligned
rectangle outline in #F22800. Custom-drawn rectangles or older variants use
different reds (e.g. #CC2200, #BB1F00) — those need to be re-snapped from
the library.

Native red UI that the captured product happens to render — Service Studio's
MERGE button, the OutSystems logo, red error text in TrueChange, the active
tab underline in Service Center, pink conflict-row backgrounds — must NOT
trigger this check. The signature that distinguishes a Figma rectangle from
native red is geometry: a Figma highlight has BOTH a long thin horizontal
edge AND a long thin vertical edge (it's a closed rectangle), whereas
native red is filled (button, logo), text glyphs, or a single horizontal
underline (Service Center active tabs).

Algorithm:
  1. Build a binary "saturated red" map (R high, G/B near zero — the stroke
     core, not the anti-aliased edges).
  2. Find horizontal thin runs: rows with a maximal red run ≥MIN_RUN long
     where ≥THINNESS_RATIO of the run has no red at the row PERPENDICULAR
     pixels above OR below. This rejects filled regions.
  3. Same for vertical thin runs.
  4. Take colours that appear in BOTH the horizontal-run set AND the
     vertical-run set — those come from a closed rectangle outline. A tab
     underline only contributes horizontal pixels, so it's filtered out.
  5. Compare the dominant common colour against the token within a small
     per-channel tolerance.

Diagonal strokes (Figma red arrows) are out of scope — vision still catches
a wrong-coloured arrow. Very small Figma rectangles (<MIN_RUN px on a side)
are also missed; the trade-off is no false positives on native UI red,
which was the user-reported pain.

Verdicts (printed to stdout):
  red: ok #RRGGBB              — dominant rectangle stroke matches the token
  red: wrong #RRGGBB (token …)  — dominant rectangle stroke is a different colour
  red: none                     — no closed-rectangle red highlight detected
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from has_shadow import load_rgba  # type: ignore

TOKEN = (242, 40, 0)            # #F22800
TOLERANCE = 10                  # per-channel match window
MIN_RUN_LENGTH = 20             # shorter runs are likely text glyphs
PERPENDICULAR_OFFSET = 3        # rows/cols away to test thinness
THINNESS_RATIO = 0.7            # ≥70% of the run must be thin to qualify
MIN_STROKE_PIXELS = 50          # below this combined total, treat as no highlight


def _build_red_map(img, w: int, h: int) -> bytearray:
    """Mark every pixel that is saturated red and opaque."""
    red = bytearray(w * h)
    for y in range(h):
        row = y * w
        for x in range(w):
            r, g, b, a = img.getpixel((x, y))
            if a > 200 and r > 150 and g < 50 and b < 30:
                red[row + x] = 1
    return red


def _scan_axis(
    red: bytearray,
    w: int,
    h: int,
    horizontal: bool,
    img,
) -> Counter:
    """Find long thin runs of red along one axis and return their colour counts."""
    sink: Counter[tuple[int, int, int]] = Counter()
    outer_max = h if horizontal else w
    inner_max = w if horizontal else h

    for outer in range(outer_max):
        run_start = -1
        for inner in range(inner_max + 1):
            is_red = inner < inner_max and red[
                outer * w + inner if horizontal else inner * w + outer
            ]
            if is_red:
                if run_start < 0:
                    run_start = inner
            elif run_start >= 0:
                _emit_if_thin(
                    red, w, h, horizontal, outer, run_start, inner - 1, img, sink,
                )
                run_start = -1
    return sink


def _emit_if_thin(
    red: bytearray,
    w: int,
    h: int,
    horizontal: bool,
    outer: int,
    start: int,
    end: int,
    img,
    sink: Counter,
) -> None:
    length = end - start + 1
    if length < MIN_RUN_LENGTH:
        return

    thin = 0
    for inner in range(start, end + 1):
        if horizontal:
            y, x = outer, inner
            above = (y - PERPENDICULAR_OFFSET) >= 0 and red[
                (y - PERPENDICULAR_OFFSET) * w + x
            ]
            below = (y + PERPENDICULAR_OFFSET) < h and red[
                (y + PERPENDICULAR_OFFSET) * w + x
            ]
            isolated = not above and not below
        else:
            x, y = outer, inner
            left = (x - PERPENDICULAR_OFFSET) >= 0 and red[
                y * w + (x - PERPENDICULAR_OFFSET)
            ]
            right = (x + PERPENDICULAR_OFFSET) < w and red[
                y * w + (x + PERPENDICULAR_OFFSET)
            ]
            isolated = not left and not right
        if isolated:
            thin += 1

    if thin / length < THINNESS_RATIO:
        return

    for inner in range(start, end + 1):
        x, y = (inner, outer) if horizontal else (outer, inner)
        r, g, b, _ = img.getpixel((x, y))
        sink[(r, g, b)] += 1


def dominant_red(path: Path) -> tuple[int, int, int] | None:
    img, (w, h) = load_rgba(path)
    red = _build_red_map(img, w, h)

    h_colors = _scan_axis(red, w, h, True, img)
    v_colors = _scan_axis(red, w, h, False, img)

    # A closed rectangle contributes to BOTH axes. Native red underlines or
    # logos contribute to only one. Take the intersection.
    common: Counter[tuple[int, int, int]] = Counter()
    for color, hcount in h_colors.items():
        if color in v_colors:
            common[color] = hcount + v_colors[color]

    if sum(common.values()) < MIN_STROKE_PIXELS:
        return None
    return common.most_common(1)[0][0]


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: check_red.py <image.png>", file=sys.stderr)
        sys.exit(2)

    dom = dominant_red(Path(sys.argv[1]))
    if dom is None:
        print("red: none")
        return

    r, g, b = dom
    diff = max(abs(r - TOKEN[0]), abs(g - TOKEN[1]), abs(b - TOKEN[2]))
    hex_ = f"#{r:02X}{g:02X}{b:02X}"
    if diff <= TOLERANCE:
        print(f"red: ok {hex_}")
    else:
        print(f"red: wrong {hex_} (token #F22800)")


if __name__ == "__main__":
    main()
