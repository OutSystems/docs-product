#!/usr/bin/env python3
"""Tests for the width rule in check_metadata.py.

Run directly: python3 test_check_metadata.py
"""
from __future__ import annotations

import struct
import sys
import tempfile
import zlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_metadata as cm  # noqa: E402


def _png(path: Path, width: int, height: int = 2) -> Path:
    def chunk(kind: bytes, data: bytes) -> bytes:
        body = kind + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body))

    raw = b"".join(b"\x00" + b"\x00\x00\x00" * width for _ in range(height))
    path.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw))
        + chunk(b"IEND", b"")
    )
    return path


def run(name, fn) -> bool:
    try:
        fn()
        print(f"PASS  {name}")
        return True
    except AssertionError as e:
        print(f"FAIL  {name}: {e}")
        return False


def _width(name: str, px: int) -> dict:
    with tempfile.TemporaryDirectory() as d:
        return cm.check_width(_png(Path(d) / name, px))


def test_wide_screenshot_warns() -> None:
    got = _width("sharing-console-pl.png", 1300)
    assert got["verdict"] == "warn" and got["px"] == 1300, got


def test_screenshot_at_the_limit_passes() -> None:
    assert _width("sharing-console-pl.png", 1200)["verdict"] == "pass"


def test_wide_diagram_is_exempt() -> None:
    got = _width("sh-network-reqs-diag.png", 1865)
    assert got["verdict"] == "skip" and got["px"] == 1865, got


def test_name_merely_containing_diag_is_not_exempt() -> None:
    assert _width("diag-console-pl.png", 1300)["verdict"] == "warn"


TESTS = [
    test_wide_screenshot_warns,
    test_screenshot_at_the_limit_passes,
    test_wide_diagram_is_exempt,
    test_name_merely_containing_diag_is_not_exempt,
]


def main() -> int:
    results = [run(t.__name__, t) for t in TESTS]
    print(f"\n{sum(results)}/{len(results)} passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
