#!/usr/bin/env python3
"""Render an SVG to a PNG at 2x with headless Chrome, using the Inter font.

Usage: python3 render.py [--no-sandbox] INPUT.svg OUTPUT.png

Works on macOS, Windows, and Linux. It looks for Google Chrome, Chromium, or
Microsoft Edge. The page loads Inter from Google Fonts, so rendering needs a
network connection. Without it, the browser falls back to Helvetica Neue or
Arial.

Add --no-sandbox when you run as root, in a container, or in CI on Linux, where
Chrome refuses to start with its sandbox on.
"""
import argparse
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    r"%ProgramFiles%\Google\Chrome\Application\chrome.exe",
    r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe",
    r"%LocalAppData%\Google\Chrome\Application\chrome.exe",
    r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe",
    r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe",
]
COMMANDS = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome", "msedge"]

BROWSER_TIMEOUT_SECONDS = 120
BROWSER_OUTPUT_LINES = 10

PAGE = """<!doctype html><html><head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=block" rel="stylesheet">
<style>html,body{{margin:0;background:#fff}}</style></head><body>
{svg}
</body></html>
"""


def find_browser():
    for candidate in CANDIDATES:
        path = os.path.expandvars(candidate)
        if os.path.isfile(path):
            return path
    for command in COMMANDS:
        path = shutil.which(command)
        if path:
            return path
    return None


def pixel_value(root, name):
    """Return the root attribute `name` in pixels, rounded up, or exit with a plain message."""
    match = re.search(rf'(?<![\w-]){name}="([^"]*)"', root)
    if not match:
        sys.exit("❌ The SVG root element has no width and height attributes. "
                 "Generate the SVG with swimlane.py, which sets both, and run again.")
    value = match.group(1).strip()
    number = re.fullmatch(r"(\d+(?:\.\d+)?)(?:px)?", value)
    if not number:
        sys.exit(f'❌ The SVG {name} is "{value}", which render.py can\'t use as a window size. '
                 f'Set {name} to a number of pixels, for example {name}="1372", and run again.')
    return math.ceil(float(number.group(1)))


def svg_size(svg):
    root = re.search(r"<svg\b[^>]*>", svg)
    if not root:
        sys.exit("❌ The input file has no <svg> element. "
                 "Check that you passed the SVG that swimlane.py wrote, and run again.")
    return pixel_value(root.group(0), "width"), pixel_value(root.group(0), "height")


def browser_output(result):
    """Return the last lines the browser printed, to show with a failure."""
    lines = [l for l in (result.stderr or "").splitlines() if l.strip()]
    return "\n".join(lines[-BROWSER_OUTPUT_LINES:])


def main(svg_path, png_path, no_sandbox=False):
    browser = find_browser()
    if not browser:
        sys.exit("❌ Chrome, Chromium, or Edge not found. Install one of them and run again.")

    try:
        svg = Path(svg_path).read_text(encoding="utf-8")
    except FileNotFoundError:
        sys.exit(f"❌ The SVG file {svg_path} doesn't exist. Check the path, or run swimlane.py first.")
    width, height = svg_size(svg)
    png = Path(png_path).resolve()

    command = [browser, "--headless=new", "--disable-gpu", "--hide-scrollbars",
               "--force-device-scale-factor=2", f"--window-size={width},{height}",
               "--virtual-time-budget=6000", f"--screenshot={png}"]
    if no_sandbox:
        command.append("--no-sandbox")

    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "page.html"
        page.write_text(PAGE.format(svg=svg), encoding="utf-8")
        try:
            result = subprocess.run(
                command + [page.as_uri()], capture_output=True, text=True,
                encoding="utf-8", errors="replace", timeout=BROWSER_TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            sys.exit(f"❌ The browser didn't finish within {BROWSER_TIMEOUT_SECONDS} seconds. "
                     "Close other Chrome windows that use the same profile, check the network "
                     "connection for the font, and run again.")
        except OSError as e:
            sys.exit(f"❌ The browser at {browser} couldn't start ({e.strerror or e}). "
                     "Reinstall Chrome, Chromium, or Edge, and run again.")

    if result.returncode != 0 or not png.is_file():
        detail = browser_output(result)
        hint = "If you run as root, in a container, or in CI on Linux, run again with --no-sandbox."
        sys.exit("\n".join(filter(None, [
            f"❌ The browser exited with code {result.returncode} and didn't write {png_path}.",
            f"Browser output:\n{detail}" if detail else "The browser printed no output.",
            "" if no_sandbox else hint,
        ])))
    print(f"Wrote {png_path}")


if __name__ == "__main__":
    # A Windows console or pipe can default to a code page that can't print the ❌ marker.
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Render an SVG to a 2x PNG with headless Chrome.")
    parser.add_argument("svg", metavar="INPUT.svg")
    parser.add_argument("png", metavar="OUTPUT.png")
    parser.add_argument("--no-sandbox", action="store_true",
                        help="Start the browser without its sandbox (root, containers, CI on Linux).")
    args = parser.parse_args()
    main(args.svg, args.png, no_sandbox=args.no_sandbox)
