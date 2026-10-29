#!/usr/bin/env python3
"""Parse a `figma:` frontmatter URL into a fileKey/nodeId pair.

Articles carry a value like:
    https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=9332-117
or the legacy path form:
    https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=9332-117

The `node-id` query parameter always uses `-` where every Figma MCP tool
expects `:` (`9332-117` -> `9332:117`); some URLs instead use the
URL-encoded `%3A`, and node ids for nested nodes contain no more than one
separator, so a simple last-hyphen-or-percent split is sufficient.

Usage:
    python3 parse_figma_url.py "<figma-url>"

Prints a JSON object:
    {"file_key": "...", "node_id": "9332:117"}                (success)
    {"file_key": "...", "node_id": null}                       (no node-id)
    {"error": "..."}                                            (empty/invalid input)
"""
from __future__ import annotations

import json
import re
import sys
from urllib.parse import urlparse, parse_qs

FILE_KEY_RE = re.compile(r"/(?:design|file)/([^/]+)/")


def parse_figma_url(url: str) -> dict:
    url = url.strip()
    if not url:
        return {"error": "empty figma: value"}

    match = FILE_KEY_RE.search(url)
    if not match:
        return {"error": f"could not find a /design/ or /file/ file key in: {url}"}
    file_key = match.group(1)

    parsed = urlparse(url)
    node_ids = parse_qs(parsed.query).get("node-id")
    if not node_ids:
        return {"file_key": file_key, "node_id": None}

    raw = node_ids[0]
    node_id = raw.replace("%3A", ":").replace("%3a", ":")
    if ":" not in node_id:
        # "9332-117" -> "9332:117". Only the first hyphen separates the two
        # numeric parts; anything after would be a second, deeper node id
        # rarely (if ever) seen in frontmatter, so no attempt is made to
        # handle more than one substitution.
        node_id = node_id.replace("-", ":", 1)

    return {"file_key": file_key, "node_id": node_id}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: parse_figma_url.py <figma-url>", file=sys.stderr)
        return 2
    print(json.dumps(parse_figma_url(argv[1])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
