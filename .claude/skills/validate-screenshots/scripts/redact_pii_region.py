#!/usr/bin/env python3
"""Plan and verify a rule 7 (PII) redaction cover.

The auto-fix phase never guesses where to draw a PII cover rectangle from
vision's rough read alone — vision supplies a generous search window and a
judgment call ("is this real PII, not synthetic placeholder data?"); this
script owns the pixel-level geometry so the actual cover box is derived,
not eyeballed.

Three modes:

  plan <image> <x> <y> <w> <h> [--tol N] [--pad N] [--bg-fraction F]
    Given a search window in the image's own pixel coordinates (generous
    enough to contain the whole text run plus a visible margin of
    surrounding background on all sides), returns either:
      {"safe": true, "cover_box": {...}, "text_bbox": {...},
       "color_rgb": [r,g,b], "color_hex": "#RRGGBB"}
    or
      {"safe": false, "reason": "..."}
    Never returns a cover box unless the padding margin around the
    detected text is *also* confirmed uniform background — that's what
    makes it safe to paint over without clipping something else or
    leaving a visible seam. Covers the WHOLE text run in the window — use
    this when the PII is the only thing in the window, or when the run
    can't be reliably word-segmented (see plan-word-range's fallback).

  plan-word-range <image> <x> <y> <w> <h> <total_words> <pii_start_word> <pii_end_word> [--tol N] [--pad N] [--bg-fraction F] [--lum-thresh N]
    Same window semantics as `plan`, but covers only a word-range within
    the line instead of the whole run — e.g. redact just "Isabel Martins"
    out of "Revision 62 Published at 4:16 PM by Isabel Martins" while
    leaving "...by" fully legible. The caller supplies the line's total
    whitespace-split word count and the 0-indexed inclusive word range that
    is the PII (e.g. total_words=9, pii_start_word=7, pii_end_word=8 for
    the two-word name at the end). The script finds the actual word
    boundaries itself via a per-column "ink density" profile (see
    Algorithm below) — it never trusts a caller-supplied pixel x for the
    split, only a caller-supplied *word count*, because the whole point is
    to stop guessing pixel coordinates by eye. Returns the same shape as
    `plan`, plus `"scope"`: `"word_range"` when the narrow box was used, or
    `"whole_line"` when the detected word count didn't match
    `total_words` and it silently fell back to covering the entire run
    (still automatic, just less surgical for that one occurrence — see
    Algorithm below for exactly when this happens). Never returns
    `"safe": false` for a reason a human would need to resolve by eye;
    the fallback exists precisely so this mode never needs one.

  verify <image> <x> <y> <w> <h> <r> <g> <b> [--tol N]
    Re-scans the SAME window (not just the cover box that was drawn) after
    the fix and confirms every pixel in it matches the target background
    color. Scanning the whole original window, not only the rectangle that
    was drawn, is what catches a fragment of text that leaked just outside
    the cover.

Algorithm (plan):
  1. Build a color histogram over the whole window and take the most common
     color as the background — NOT the window's four corners. A rounded
     badge/pill's corners are frequently cut by the shape's own corner
     radius, landing on whatever sits behind it rather than the badge fill,
     so corner-sampling is fooled by exactly the rounded shapes this rule
     needs to handle. The dominant color is robust to that: as long as most
     of the window is one flat fill (the normal case for a tight, well-
     chosen window), it wins the histogram regardless of where in the
     window a rounded corner happens to land. If no color clears
     `--bg-fraction` of the window, the window doesn't have one dominant
     background — abort rather than guess which color is "the" background.
  2. Find the tight bounding box of every pixel in the window that differs
     from that background color.
  3. If the bounding box touches the window edge (within a small margin),
     the window was too tight to prove the whole text run was seen — abort
     rather than cover a partial run.
  4. Pad the bounding box by `--pad` pixels. If the four margin strips
     between the tight bounding box and the padded box aren't themselves
     uniform background, something else (an icon, a border, adjacent text,
     or the shape's own corner radius curving away) is close enough that a
     rectangular cover would clip it or leave a visible seam — abort.
  5. Otherwise return the padded box as the cover, and the dominant color as
     the fill.

Algorithm (plan-word-range's word segmentation):
  RGB-tolerance column scanning (what `plan` uses to find the *whole*
  run) is too noisy to find gaps *between* words in small anti-aliased or
  sub-pixel-rendered text: a word space often still has a stray fringe
  pixel or two whose per-channel RGB distance from the background clears
  a tolerance of 10, even though no actual glyph is there. Word-internal
  gaps need a different signal:
  1. Convert every pixel to luminance only (0.299R + 0.587G + 0.114B) and
     ignore chrominance entirely — sub-pixel/ClearType-style fringing
     shifts hue at a word gap far more than it shifts brightness, so hue
     is noise here and luminance is signal.
  2. For each column in the whole run's bounding box (found the same way
     `plan` finds it), count pixels whose luminance differs from the
     background's by at least `--lum-thresh` (default 18). A column with
     zero such pixels has no glyph ink in it at all.
  3. Collect maximal runs of zero-count columns as gap candidates. In
     practice every real inter-word space in a text run shows up as one
     of these runs, and — critically — so does every *inter-letter* gap
     within a word, which is why the next step matters.
  4. Count the gap runs: `detected_words = len(gap_runs) + 1`. If this
     doesn't equal the caller's `total_words`, the pixel-level word
     segmentation didn't land on a 1:1 mapping with the real text (a
     ligature, an unusually tight kerning pair, a font whose particular
     rendering merges two words) — silently fall back to covering the
     *whole* run (`"scope": "whole_line"`) rather than picking a gap by
     guesswork. This is the automatic safety valve: it always produces a
     safe, if occasionally less surgical, redaction, and it never asks a
     human to eyeball anything.
  5. When the count matches, gap `i` (0-indexed) sits between word `i` and
     word `i+1`. The cover box's left edge is the *rightmost* column of gap
     `pii_start_word - 1` (or the run's own left edge, padded, if
     `pii_start_word == 0`), and its right edge is one past the *leftmost*
     column of gap `pii_end_word` (or the run's own right edge, padded, if
     `pii_end_word == total_words - 1`) — i.e. the tightest box that still
     starts/ends inside the confirmed-clean gap, not the gap's midpoint.
     No extra `--pad` is added on a gap-derived side: the gap itself,
     already proven ink-free across the full text height, is the buffer.
     Padding is only added on a side that falls back to the run's own
     bbox edge (`pii_start_word == 0` or `pii_end_word == total_words -
     1`), where the margin-uniformity check is the same as `plan`'s;
     a gap-derived side skips that RGB-tolerance re-check entirely, since
     it would just rediscover the same sub-pixel fringing that made RGB
     tolerance unreliable for word segmentation in the first place.

Important limitation, by design: this only ever operates on the exported
PNG's pixels. A passing `verify` means the composited export is clean; it
says nothing about the Figma frame's underlying raw image asset, which
still contains the original pixels (`download_assets`'s `rawImages` output
returns them independently of whatever shapes are drawn on top). Treat a
rule 7 fix as reducing exposure in the *published* documentation, never as
scrubbing the source file — see references/auto-fix-scope.md's scope note.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image

DEFAULT_TOLERANCE = 10
DEFAULT_PADDING = 4
DEFAULT_BG_FRACTION = 0.5  # the dominant color must cover at least this share of the window
DEFAULT_LUM_THRESHOLD = 18  # per-pixel luminance distance to count as "ink" for word segmentation
EDGE_TOUCH_MARGIN = 2  # content this close to the window edge means the window was too tight


def _load_rgb(path: str):
    img = Image.open(path).convert("RGB")
    return img, img.size


def _close(c1, c2, tol: int) -> bool:
    return all(abs(a - b) <= tol for a, b in zip(c1, c2))


def _dominant_color(px, x0: int, y0: int, x1: int, y1: int, bg_fraction: float, tol: int):
    """Cluster window pixels by near-equality and return the largest cluster's
    representative color, if it covers at least `bg_fraction` of the window."""
    total = (x1 - x0) * (y1 - y0)
    if total <= 0:
        return None

    counts: dict[tuple[int, int, int], int] = {}
    for y in range(y0, y1):
        for x in range(x0, x1):
            counts[px[x, y]] = counts.get(px[x, y], 0) + 1

    # Merge near-duplicate colors (anti-aliasing noise) onto the most frequent
    # exact color within tolerance, largest bucket first.
    ordered = sorted(counts.items(), key=lambda kv: -kv[1])
    merged: list[tuple[tuple[int, int, int], int]] = []
    for color, count in ordered:
        for i, (mcolor, mcount) in enumerate(merged):
            if _close(color, mcolor, tol):
                merged[i] = (mcolor, mcount + count)
                break
        else:
            merged.append((color, count))

    merged.sort(key=lambda kv: -kv[1])
    best_color, best_count = merged[0]
    if best_count / total < bg_fraction:
        return None
    return best_color


def _content_bbox(px, x0: int, y0: int, x1: int, y1: int, bg, tol: int):
    """Tight bounding box of pixels differing from bg within [x0,x1) x [y0,y1)."""
    minx = miny = maxx = maxy = None
    for y in range(y0, y1):
        for x in range(x0, x1):
            if not _close(px[x, y], bg, tol):
                if minx is None or x < minx:
                    minx = x
                if maxx is None or x > maxx:
                    maxx = x
                if miny is None or y < miny:
                    miny = y
                if maxy is None or y > maxy:
                    maxy = y
    if minx is None:
        return None
    return (minx, miny, maxx, maxy)


def _strip_uniform(px, sx0: int, sy0: int, sx1: int, sy1: int, bg, tol: int) -> bool:
    for y in range(sy0, sy1):
        for x in range(sx0, sx1):
            if not _close(px[x, y], bg, tol):
                return False
    return True


def _margins_ok(px, cx0: int, cy0: int, cx1: int, cy1: int, bx0: int, by0: int, bx1: int, by1: int, bg, tol: int) -> bool:
    """True if the four strips between the padded box (cx0..cx1, cy0..cy1)
    and the inner content box (bx0..bx1, by0..by1) are all uniform background —
    i.e. padding it doesn't clip or abut anything else."""
    return (
        _strip_uniform(px, cx0, cy0, cx1, by0, bg, tol)  # top
        and _strip_uniform(px, cx0, by1 + 1, cx1, cy1, bg, tol)  # bottom
        and _strip_uniform(px, cx0, by0, bx0, by1 + 1, bg, tol)  # left
        and _strip_uniform(px, bx1 + 1, by0, cx1, by1 + 1, bg, tol)  # right
    )


def _luminance(c) -> float:
    r, g, b = c
    return 0.299 * r + 0.587 * g + 0.114 * b


def _word_gaps(px, bx0: int, by0: int, bx1: int, by1: int, bg, lum_thresh: int):
    """Maximal runs of columns with zero 'ink' pixels, using a luminance-only
    distance from bg. Ignoring chrominance is what makes this robust to
    sub-pixel/ClearType-style fringing at word gaps, which RGB-tolerance
    scanning (see _content_bbox) treats as false ink."""
    bg_lum = _luminance(bg)
    ink_cols = []
    for x in range(bx0, bx1 + 1):
        hot = any(abs(_luminance(px[x, y]) - bg_lum) >= lum_thresh for y in range(by0, by1 + 1))
        ink_cols.append(not hot)  # True = gap column

    gaps = []
    run_start = None
    for i, is_gap in enumerate(ink_cols):
        x = bx0 + i
        if is_gap and run_start is None:
            run_start = x
        elif not is_gap and run_start is not None:
            gaps.append((run_start, x - 1))
            run_start = None
    if run_start is not None:
        gaps.append((run_start, bx0 + len(ink_cols) - 1))

    # bx0/bx1 are RGB-tolerance edges (from _content_bbox); this scan uses a
    # different (luminance-only) metric, so the two can disagree right at
    # the boundary columns. A genuine word-internal gap is strictly inside
    # the run, never touching either outer edge — drop any that do.
    return [g for g in gaps if g[0] > bx0 and g[1] < bx1]


def plan(image_path: str, x: int, y: int, w: int, h: int, tol: int, pad: int, bg_fraction: float) -> dict:
    img, (W, H) = _load_rgb(image_path)
    px = img.load()
    x0, y0, x1, y1 = x, y, min(x + w, W), min(y + h, H)

    if x1 - x0 < 2 * pad + 1 or y1 - y0 < 2 * pad + 1:
        return {"safe": False, "reason": "search window is too small to hold a padded cover box"}

    bg = _dominant_color(px, x0, y0, x1, y1, bg_fraction, tol)
    if bg is None:
        return {
            "safe": False,
            "reason": "no single color dominates the window; background isn't flat enough to auto-redact",
        }

    bbox = _content_bbox(px, x0, y0, x1, y1, bg, tol)
    if bbox is None:
        return {"safe": False, "reason": "no non-background content found in the supplied window; nothing to redact"}

    bx0, by0, bx1, by1 = bbox
    if (
        bx0 <= x0 + EDGE_TOUCH_MARGIN
        or bx1 >= x1 - 1 - EDGE_TOUCH_MARGIN
        or by0 <= y0 + EDGE_TOUCH_MARGIN
        or by1 >= y1 - 1 - EDGE_TOUCH_MARGIN
    ):
        return {
            "safe": False,
            "reason": "detected content touches the search window edge; widen the window so the full text run is visible and retry",
        }

    cx0, cy0, cx1, cy1 = bx0 - pad, by0 - pad, bx1 + 1 + pad, by1 + 1 + pad
    if cx0 < x0 or cy0 < y0 or cx1 > x1 or cy1 > y1:
        return {"safe": False, "reason": "padded cover box would extend outside the supplied search window"}

    if not _margins_ok(px, cx0, cy0, cx1, cy1, bx0, by0, bx1, by1, bg, tol):
        return {
            "safe": False,
            "reason": "padding margin around the detected text isn't uniform background; something else may be nearby",
        }

    r, g, b = bg
    return {
        "safe": True,
        "cover_box": {"x": cx0, "y": cy0, "w": cx1 - cx0, "h": cy1 - cy0},
        "text_bbox": {"x": bx0, "y": by0, "w": bx1 - bx0 + 1, "h": by1 - by0 + 1},
        "color_rgb": [r, g, b],
        "color_hex": f"#{r:02X}{g:02X}{b:02X}",
    }


def plan_word_range(
    image_path: str,
    x: int,
    y: int,
    w: int,
    h: int,
    total_words: int,
    pii_start_word: int,
    pii_end_word: int,
    tol: int,
    pad: int,
    bg_fraction: float,
    lum_thresh: int,
) -> dict:
    img, (W, H) = _load_rgb(image_path)
    px = img.load()
    x0, y0, x1, y1 = x, y, min(x + w, W), min(y + h, H)

    if x1 - x0 < 2 * pad + 1 or y1 - y0 < 2 * pad + 1:
        return {"safe": False, "reason": "search window is too small to hold a padded cover box"}
    if not (0 <= pii_start_word <= pii_end_word < total_words):
        return {"safe": False, "reason": "pii_start_word/pii_end_word out of range for total_words"}

    bg = _dominant_color(px, x0, y0, x1, y1, bg_fraction, tol)
    if bg is None:
        return {
            "safe": False,
            "reason": "no single color dominates the window; background isn't flat enough to auto-redact",
        }

    bbox = _content_bbox(px, x0, y0, x1, y1, bg, tol)
    if bbox is None:
        return {"safe": False, "reason": "no non-background content found in the supplied window; nothing to redact"}

    bx0, by0, bx1, by1 = bbox
    if (
        bx0 <= x0 + EDGE_TOUCH_MARGIN
        or bx1 >= x1 - 1 - EDGE_TOUCH_MARGIN
        or by0 <= y0 + EDGE_TOUCH_MARGIN
        or by1 >= y1 - 1 - EDGE_TOUCH_MARGIN
    ):
        return {
            "safe": False,
            "reason": "detected content touches the search window edge; widen the window so the full text run is visible and retry",
        }

    r, g, b = bg
    color_rgb = [r, g, b]
    color_hex = f"#{r:02X}{g:02X}{b:02X}"

    def whole_line_result(extra: dict) -> dict | None:
        """The same-safety-guarantees whole-run cover `plan` would produce.
        None if even this can't be done safely (caller falls through to a
        hard failure in that case — see below)."""
        cx0, cy0, cx1, cy1 = bx0 - pad, by0 - pad, bx1 + 1 + pad, by1 + 1 + pad
        if cx0 < x0 or cy0 < y0 or cx1 > x1 or cy1 > y1:
            return None
        if not _margins_ok(px, cx0, cy0, cx1, cy1, bx0, by0, bx1, by1, bg, tol):
            return None
        return {
            "safe": True,
            "scope": "whole_line",
            "cover_box": {"x": cx0, "y": cy0, "w": cx1 - cx0, "h": cy1 - cy0},
            "text_bbox": {"x": bx0, "y": by0, "w": bx1 - bx0 + 1, "h": by1 - by0 + 1},
            "color_rgb": color_rgb,
            "color_hex": color_hex,
            **extra,
        }

    gaps = _word_gaps(px, bx0, by0, bx1, by1, bg, lum_thresh)
    detected_words = len(gaps) + 1

    # Word segmentation didn't land 1:1 with the real text (a ligature, a
    # tight kerning pair, a font that merges two words) — cover the whole
    # run instead of guessing a gap. Still fully automatic, just less
    # surgical for this one occurrence.
    if detected_words != total_words:
        result = whole_line_result({"detected_words": detected_words, "fallback_reason": "word count mismatch"})
        if result is not None:
            return result
        return {
            "safe": False,
            "reason": f"word count mismatch (detected {detected_words}, expected {total_words}) and the whole-line fallback isn't safe either",
        }

    # Inner (gap-derived) boundaries get no extra padding — the gap itself,
    # confirmed ink-free by _word_gaps across the full text height, already
    # is the buffer. Outer (bbox-edge) boundaries get the normal padding,
    # same as the whole-line case, since beyond them is unknown territory.
    if pii_start_word == 0:
        cx0, left_is_gap = bx0 - pad, False
    else:
        cx0, left_is_gap = gaps[pii_start_word - 1][1], True  # gap's rightmost clean column
    if pii_end_word == total_words - 1:
        cx1, right_is_gap = bx1 + 1 + pad, False
    else:
        cx1, right_is_gap = gaps[pii_end_word][0] + 1, True  # gap's leftmost clean column
    cy0, cy1 = by0 - pad, by1 + 1 + pad

    word_range_ok = cx0 >= x0 and cy0 >= y0 and cx1 <= x1 and cy1 <= y1
    if word_range_ok:
        top_ok = _strip_uniform(px, cx0, cy0, cx1, by0, bg, tol)
        bottom_ok = _strip_uniform(px, cx0, by1 + 1, cx1, cy1, bg, tol)
        # A gap-derived side was already proven ink-free by _word_gaps over
        # the same y-range — re-checking it with the stricter RGB-tolerance
        # metric would just rediscover the sub-pixel fringing that made RGB
        # tolerance unreliable for word segmentation in the first place.
        left_ok = True if left_is_gap else _strip_uniform(px, cx0, by0, bx0, by1 + 1, bg, tol)
        right_ok = True if right_is_gap else _strip_uniform(px, bx1 + 1, by0, cx1, by1 + 1, bg, tol)
        word_range_ok = top_ok and bottom_ok and left_ok and right_ok

    left, right = cx0, cx1 - 1  # for the text_bbox report below
    if not word_range_ok:
        # The narrow box itself isn't safe (e.g. padding would abut the
        # kept-visible text) — fall back to the whole run rather than
        # surfacing something a human would need to resolve.
        result = whole_line_result({"detected_words": detected_words, "fallback_reason": "word-range box wasn't safe"})
        if result is not None:
            return result
        return {"safe": False, "reason": "word-range cover box isn't safe and the whole-line fallback isn't either"}

    return {
        "safe": True,
        "scope": "word_range",
        "detected_words": detected_words,
        "cover_box": {"x": cx0, "y": cy0, "w": cx1 - cx0, "h": cy1 - cy0},
        "text_bbox": {"x": left, "y": by0, "w": right - left + 1, "h": by1 - by0 + 1},
        "color_rgb": color_rgb,
        "color_hex": color_hex,
    }


def verify(image_path: str, x: int, y: int, w: int, h: int, r: int, g: int, b: int, tol: int) -> dict:
    img, (W, H) = _load_rgb(image_path)
    px = img.load()
    x0, y0, x1, y1 = x, y, min(x + w, W), min(y + h, H)
    bg = (r, g, b)
    bad = 0
    for yy in range(y0, y1):
        for xx in range(x0, x1):
            if not _close(px[xx, yy], bg, tol):
                bad += 1
    if bad == 0:
        return {"verdict": "pass"}
    return {"verdict": "fail", "reason": f"{bad} pixel(s) in the window still differ from the target background color"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="mode", required=True)

    p_plan = sub.add_parser("plan")
    p_plan.add_argument("image")
    p_plan.add_argument("x", type=int)
    p_plan.add_argument("y", type=int)
    p_plan.add_argument("w", type=int)
    p_plan.add_argument("h", type=int)
    p_plan.add_argument("--tol", type=int, default=DEFAULT_TOLERANCE)
    p_plan.add_argument("--pad", type=int, default=DEFAULT_PADDING)
    p_plan.add_argument("--bg-fraction", type=float, default=DEFAULT_BG_FRACTION, dest="bg_fraction")

    p_word = sub.add_parser("plan-word-range")
    p_word.add_argument("image")
    p_word.add_argument("x", type=int)
    p_word.add_argument("y", type=int)
    p_word.add_argument("w", type=int)
    p_word.add_argument("h", type=int)
    p_word.add_argument("total_words", type=int)
    p_word.add_argument("pii_start_word", type=int)
    p_word.add_argument("pii_end_word", type=int)
    p_word.add_argument("--tol", type=int, default=DEFAULT_TOLERANCE)
    p_word.add_argument("--pad", type=int, default=DEFAULT_PADDING)
    p_word.add_argument("--bg-fraction", type=float, default=DEFAULT_BG_FRACTION, dest="bg_fraction")
    p_word.add_argument("--lum-thresh", type=int, default=DEFAULT_LUM_THRESHOLD, dest="lum_thresh")

    p_verify = sub.add_parser("verify")
    p_verify.add_argument("image")
    p_verify.add_argument("x", type=int)
    p_verify.add_argument("y", type=int)
    p_verify.add_argument("w", type=int)
    p_verify.add_argument("h", type=int)
    p_verify.add_argument("r", type=int)
    p_verify.add_argument("g", type=int)
    p_verify.add_argument("b", type=int)
    p_verify.add_argument("--tol", type=int, default=DEFAULT_TOLERANCE)

    args = parser.parse_args()

    if not Path(args.image).is_file():
        print(json.dumps({"safe": False, "verdict": "fail", "reason": f"no such file: {args.image}"}))
        sys.exit(1)

    if args.mode == "plan":
        print(json.dumps(plan(args.image, args.x, args.y, args.w, args.h, args.tol, args.pad, args.bg_fraction)))
    elif args.mode == "plan-word-range":
        print(json.dumps(plan_word_range(
            args.image, args.x, args.y, args.w, args.h,
            args.total_words, args.pii_start_word, args.pii_end_word,
            args.tol, args.pad, args.bg_fraction, args.lum_thresh,
        )))
    else:
        print(json.dumps(verify(args.image, args.x, args.y, args.w, args.h, args.r, args.g, args.b, args.tol)))


if __name__ == "__main__":
    main()
