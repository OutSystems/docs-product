#!/usr/bin/env python3
"""Tests for parse_figma_url.py.

Run directly: python3 test_parse_figma_url.py

The `figma:` frontmatter value is the only way the auto-fix phase finds the
Figma file, so a mis-parsed node id would send every Figma call to the wrong
node (or to none). Covers the design/file URL forms, the two node-id spellings
and the empty/invalid inputs.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from parse_figma_url import parse_figma_url  # noqa: E402

KEY = "6G4tyYswfWPn5uJPDlBpvp"


def run(name, fn) -> bool:
    try:
        fn()
        print(f"PASS  {name}")
        return True
    except AssertionError as e:
        print(f"FAIL  {name}: {e}")
        return False


def test_design_url_with_hyphenated_node_id():
    got = parse_figma_url(f"https://www.figma.com/design/{KEY}/Building-apps?node-id=9332-117")
    assert got == {"file_key": KEY, "node_id": "9332:117"}, got


def test_legacy_file_url():
    got = parse_figma_url(f"https://www.figma.com/file/{KEY}/Building-apps?node-id=9332-117")
    assert got == {"file_key": KEY, "node_id": "9332:117"}, got


def test_url_encoded_colon_node_id():
    got = parse_figma_url(f"https://www.figma.com/design/{KEY}/x?node-id=9332%3A117")
    assert got["node_id"] == "9332:117", got


def test_extra_query_parameters_are_ignored():
    got = parse_figma_url(f"https://www.figma.com/design/{KEY}/x?m=auto&node-id=10901-98&t=abc")
    assert got == {"file_key": KEY, "node_id": "10901:98"}, got


def test_no_node_id_returns_null_node():
    got = parse_figma_url(f"https://www.figma.com/design/{KEY}/Building-apps")
    assert got == {"file_key": KEY, "node_id": None}, got


def test_empty_value_is_an_error():
    assert "error" in parse_figma_url("   "), "empty value must be reported"


def test_non_figma_url_is_an_error():
    assert "error" in parse_figma_url("https://example.com/not-figma"), "no file key must be reported"


TESTS = [
    test_design_url_with_hyphenated_node_id,
    test_legacy_file_url,
    test_url_encoded_colon_node_id,
    test_extra_query_parameters_are_ignored,
    test_no_node_id_returns_null_node,
    test_empty_value_is_an_error,
    test_non_figma_url_is_an_error,
]


def main() -> int:
    results = [run(t.__name__, t) for t in TESTS]
    print(f"\n{sum(results)}/{len(results)} passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
