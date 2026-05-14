#!/usr/bin/env python3
"""Detect whether a PNG has the OutSystems design-system drop shadow.

The shadow is exported as partially-transparent alpha pixels feathered
outside the opaque content. Asymmetric offsets (from the design token):
    top = 5 px, left = 5 px, right = 15 px, bottom = 15 px.

Detection runs in two stages:

1. Alpha feather (canonical export):
   Walk inward from each edge mid-point. The slice should be
   fully-transparent padding (alpha == 0), then a band of partially-
   transparent pixels (the shadow), terminating at the first opaque
   content pixel (alpha >= OPAQUE_THRESHOLD).

2. Baked-in feather (RGB fallback for flat exports):
   Some screenshots are exported without alpha — the shadow is
   rasterised into the pixel data as a luminance gradient between
   the bright article background and the content. When stage 1 finds
   nothing, walk the same edge slice in RGB and count pixels that sit
   between the edge background luma and the inner content luma.

Either stage produces a feather length per edge, which is compared
against the asymmetric design token to decide whether the shadow is
correct (true), present-but-wrong (wrong), or absent (false).

Using mid-edges rather than corners avoids false positives from
rounded-corner content exported without a shadow — those only have
transparent *corners*, mid-edges still touch opaque content.

Usage:
    python3 has_shadow.py <path-to-png>

Prints one of:
    shadow: true      (feather present and matches the OS token, in either
                       the alpha channel or the RGB pixels)
    shadow: wrong     (feather present but profile doesn't match — e.g.
                       symmetric shadow, too narrow, too wide)
    shadow: false     (no feather detected on any edge — content runs
                       straight to the border, or only a hard 1-px border)
    shadow: unknown   (decoding failed)

Exit codes: 0 on success (any verdict), 2 on usage error.
"""
from __future__ import annotations

import struct
import subprocess
import sys
import tempfile
from pathlib import Path

# A content pixel whose alpha is below this is considered partially-
# transparent (inside the shadow band).
OPAQUE_THRESHOLD = 250

# How far inward (in pixels) to walk from each edge while measuring the
# feather. Must be larger than the widest expected feather plus reasonable
# transparent padding around the shadow.
SAMPLE_DEPTH = 40

# Expected feather length per edge (in pixels), as a (min, max) range.
# Tolerances allow for rounding when Figma rasterises the shadow and
# slight differences in how exporters handle sub-pixel coverage.
EXPECTED_FEATHER = {
    "top":    (2, 9),
    "left":   (2, 9),
    "bottom": (10, 22),
    "right":  (10, 22),
}

# Baked-in (RGB) detector tuning. The edge mid-point is sampled and a
# *smooth, monotonic* luminance ramp toward inner-content luminance is
# treated as a shadow gradient. Sharp step transitions (e.g. anti-aliased
# UI edges between two flat regions) are rejected.
BAKED_DELTA_THRESHOLD = 8       # min |edge_luma − inner_luma| to call it a gradient
BAKED_PADDING_TOLERANCE = 3     # pixels within this of edge_luma still count as bg
BAKED_INSIDE_TOLERANCE = 5      # pixels within this of inner_luma count as content
BAKED_MAX_STEP = 20             # max luma delta between adjacent feather pixels
BAKED_MIN_FEATHER = 2           # feathers shorter than this are treated as noise


def _load_rgba_via_pillow(path: Path):
    from PIL import Image  # type: ignore
    img = Image.open(path)
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    return img, img.size


def _load_rgba_via_sips(path: Path):
    """Convert PNG to BMP via `sips`, then parse the BMP.

    BMP's header is simple and its pixel data is uncompressed — far easier
    than a full PNG decoder. Both 32-bit (BGRA) and 24-bit (BGR) BMPs are
    accepted; 24-bit pixels are returned with alpha 255 so callers can
    treat the image as RGBA uniformly.
    """
    with tempfile.NamedTemporaryFile(suffix=".bmp", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        subprocess.check_output(
            ["sips", "-s", "format", "bmp", str(path),
             "--out", str(tmp_path)],
            stderr=subprocess.DEVNULL,
        )
        data = tmp_path.read_bytes()
    finally:
        tmp_path.unlink(missing_ok=True)

    if data[:2] != b"BM":
        return None, (0, 0)
    pixel_offset = struct.unpack_from("<I", data, 10)[0]
    width = struct.unpack_from("<i", data, 18)[0]
    height_raw = struct.unpack_from("<i", data, 22)[0]
    bpp = struct.unpack_from("<H", data, 28)[0]
    if bpp not in (24, 32):
        return None, (width, abs(height_raw))

    height = abs(height_raw)
    top_down = height_raw < 0
    bytes_per_pixel = bpp // 8
    row_size = ((width * bytes_per_pixel) + 3) & ~3  # 4-byte aligned

    if bpp == 32:
        def at(x: int, y: int) -> tuple[int, int, int, int]:
            row_index = y if top_down else (height - 1 - y)
            off = pixel_offset + row_index * row_size + x * 4
            b, g, r, a = data[off:off + 4]
            return r, g, b, a
    else:
        def at(x: int, y: int) -> tuple[int, int, int, int]:
            row_index = y if top_down else (height - 1 - y)
            off = pixel_offset + row_index * row_size + x * 3
            b, g, r = data[off:off + 3]
            return r, g, b, 255

    class _Img:
        size = (width, height)
        def getpixel(self, xy): return at(*xy)
    return _Img(), (width, height)


def load_rgba(path: Path):
    try:
        return _load_rgba_via_pillow(path)
    except ImportError:
        pass
    return _load_rgba_via_sips(path)


def _alpha_at(img, x, y) -> int | None:
    try:
        pixel = img.getpixel((x, y))
    except Exception:
        return None
    if len(pixel) < 4:
        return None
    return pixel[3]


def _rgb_at(img, x, y) -> tuple[int, int, int] | None:
    try:
        pixel = img.getpixel((x, y))
    except Exception:
        return None
    if len(pixel) < 3:
        return None
    return pixel[0], pixel[1], pixel[2]


def _luma(r: int, g: int, b: int) -> int:
    """Rec. 601 luminance approximation (0..255)."""
    return (r * 299 + g * 587 + b * 114) // 1000


def _edge_slice(edge: str, w: int, h: int) -> list[tuple[int, int]]:
    """Coordinates from the mid-point of an edge inward, up to SAMPLE_DEPTH."""
    cx, cy = w // 2, h // 2
    if edge == "top":
        depth = min(SAMPLE_DEPTH, h)
        return [(cx, y) for y in range(depth)]
    if edge == "bottom":
        depth = min(SAMPLE_DEPTH, h)
        return [(cx, h - 1 - y) for y in range(depth)]
    if edge == "left":
        depth = min(SAMPLE_DEPTH, w)
        return [(x, cy) for x in range(depth)]
    depth = min(SAMPLE_DEPTH, w)
    return [(w - 1 - x, cy) for x in range(depth)]


def _feather_length(img, edge: str, w: int, h: int) -> int | None:
    """Walk the edge slice inward and count partially-transparent pixels.

    Returns the number of pixels with 0 < alpha < OPAQUE_THRESHOLD between
    optional fully-transparent padding and the first opaque content pixel.
    Returns 0 when content meets the edge with no feathering.
    Returns None when the slice never reaches opaque content (malformed).
    """
    state = "padding"
    feather = 0
    for (x, y) in _edge_slice(edge, w, h):
        a = _alpha_at(img, x, y)
        if a is None:
            return None
        if state == "padding":
            if a == 0:
                continue
            if a >= OPAQUE_THRESHOLD:
                return 0
            state = "feather"
            feather = 1
            continue
        # state == "feather"
        if a >= OPAQUE_THRESHOLD:
            return feather
        if a == 0:
            return None
        feather += 1
    return None


def _baked_feather_length(img, edge: str, w: int, h: int) -> int | None:
    """Measure a baked-in shadow gradient at an edge using RGB luminance.

    Walks SAMPLE_DEPTH pixels inward from the edge mid-point and counts
    pixels that form a *smooth, monotonic* gradient between the edge
    background luma (lumas[0]) and an inner-content luma sampled deep
    inside the slice. A real soft drop shadow rasterised into pixels
    produces small per-pixel luma steps (≤ BAKED_MAX_STEP) all moving
    toward the content luma. Sharp transitions (a single big jump from
    background to a different region) are anti-aliased UI edges, not
    shadows — those are rejected and the function returns 0.

    Returns 0 for: no gradient (edge ≈ inside), step transitions, or
    feathers shorter than BAKED_MIN_FEATHER. Returns None if the slice
    is too short or pixels can't be read.
    """
    coords = _edge_slice(edge, w, h)
    if len(coords) < 5:
        return None

    lumas: list[int] = []
    for (x, y) in coords:
        pixel = _rgb_at(img, x, y)
        if pixel is None:
            return None
        lumas.append(_luma(*pixel))

    edge_luma = lumas[0]
    inside_start = max(0, len(lumas) - 5)
    inside_window = sorted(lumas[inside_start:])
    inside_luma = inside_window[len(inside_window) // 2]

    if abs(edge_luma - inside_luma) < BAKED_DELTA_THRESHOLD:
        return 0

    sign = 1 if inside_luma > edge_luma else -1
    state = "padding"
    feather = 0
    prev = edge_luma
    for l in lumas:
        if state == "padding":
            if abs(l - edge_luma) < BAKED_PADDING_TOLERANCE:
                continue
            if abs(l - edge_luma) > BAKED_MAX_STEP:
                return 0
            if abs(l - inside_luma) < BAKED_INSIDE_TOLERANCE:
                return 0
            state = "feather"
            feather = 1
            prev = l
            continue
        # state == "feather"
        if abs(l - inside_luma) < BAKED_INSIDE_TOLERANCE:
            break
        progress = (l - prev) * sign
        if progress < -BAKED_PADDING_TOLERANCE:
            break
        if abs(l - prev) > BAKED_MAX_STEP:
            break
        feather += 1
        prev = l
    return feather if feather >= BAKED_MIN_FEATHER else 0


def has_shadow(path: Path) -> str:
    img, (w, h) = load_rgba(path)
    if img is None or w == 0 or h == 0:
        return "unknown"

    alpha_feathers: dict[str, int] = {}
    for edge in EXPECTED_FEATHER:
        f = _feather_length(img, edge, w, h)
        if f is None:
            return "unknown"
        alpha_feathers[edge] = f

    if any(f > 0 for f in alpha_feathers.values()):
        feathers = alpha_feathers
    else:
        baked_feathers: dict[str, int] = {}
        for edge in EXPECTED_FEATHER:
            f = _baked_feather_length(img, edge, w, h)
            if f is None:
                return "unknown"
            baked_feathers[edge] = f
        if all(f == 0 for f in baked_feathers.values()):
            return "false"
        feathers = baked_feathers

    in_range = all(
        EXPECTED_FEATHER[edge][0] <= feathers[edge] <= EXPECTED_FEATHER[edge][1]
        for edge in feathers
    )
    return "true" if in_range else "wrong"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: has_shadow.py <path-to-png>", file=sys.stderr)
        return 2
    path = Path(argv[1]).expanduser().resolve()
    if not path.is_file():
        print(f"shadow: unknown  # file not found: {path}", file=sys.stdout)
        return 0
    verdict = has_shadow(path)
    print(f"shadow: {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
