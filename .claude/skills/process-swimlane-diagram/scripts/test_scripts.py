#!/usr/bin/env python3
"""Regression tests for swimlane.py and render.py.

Run directly: python3 test_scripts.py

swimlane.py is exercised against the shipped example spec and small throwaway
specs. render.py needs a real browser and network access for the font, so only
its browser lookup and SVG size parsing are tested here.
"""
from __future__ import annotations

import contextlib
import io
import json
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXAMPLES = HERE.parent / "examples"
sys.path.insert(0, str(HERE))
import render  # noqa: E402
import swimlane  # noqa: E402

SVG_NS = "{http://www.w3.org/2000/svg}"
EXAMPLE_SPEC = EXAMPLES / "semantic-search-process.json"
MAX_DIAGRAM_WIDTH = 1650  # diagram limit in the validate-svgs skill


def run(name, fn) -> bool:
    try:
        fn()
        print(f"PASS  {name}")
        return True
    except AssertionError as e:
        print(f"FAIL  {name}: {e}")
        return False


def generate(spec: dict) -> tuple[str, ET.Element]:
    """Render a spec to SVG text and its parsed root."""
    with tempfile.TemporaryDirectory() as tmp:
        spec_path, out_path = Path(tmp) / "spec.json", Path(tmp) / "out.svg"
        spec_path.write_text(json.dumps(spec), encoding="utf-8")
        swimlane.main(str(spec_path), str(out_path))
        svg = out_path.read_text(encoding="utf-8")
    return svg, ET.fromstring(svg)


def minimal_spec(**overrides) -> dict:
    spec = {
        "width": 600,
        "height": 300,
        "phases": [{"number": 1, "title": "Phase", "x": 200}],
        "lanes": [{"label": "Role", "top": 60, "bottom": 280}],
        "cards": [
            {"id": "a", "x": 200, "y": 100, "lines": ["First"]},
            {"id": "b", "x": 400, "y": 100, "lines": ["Second"]},
        ],
        "edges": [{"from": "a", "from_side": "right", "to": "b", "to_side": "left"}],
    }
    spec.update(overrides)
    return spec


def test_example_is_well_formed_svg():
    spec = json.loads(EXAMPLE_SPEC.read_text(encoding="utf-8"))
    _, root = generate(spec)
    assert root.tag == f"{SVG_NS}svg", root.tag
    assert root.get("width") == str(spec["width"]), root.get("width")
    assert root.get("height") == str(spec["height"]), root.get("height")


def test_example_has_every_card_edge_and_label():
    spec = json.loads(EXAMPLE_SPEC.read_text(encoding="utf-8"))
    svg, root = generate(spec)
    card_rects = [r for r in root.iter(f"{SVG_NS}rect")
                  if r.get("fill") == swimlane.LIGHT]
    assert len(card_rects) == len(spec["cards"]), len(card_rects)
    paths = list(root.iter(f"{SVG_NS}path"))
    arrows = [p for p in paths if p.get("marker-end")]
    assert len(arrows) == len(spec["edges"]), len(arrows)
    for card in spec["cards"]:
        for line in card["lines"]:
            assert f">{line}</tspan>" in svg, f"missing label {line!r}"
    for phase in spec["phases"]:
        assert f">{phase['title']}</tspan>" in svg, phase["title"]


def test_example_matches_committed_svg():
    spec = json.loads(EXAMPLE_SPEC.read_text(encoding="utf-8"))
    svg, _ = generate(spec)
    committed = (EXAMPLES / "semantic-search-process.svg").read_text(encoding="utf-8")
    assert svg == committed, (
        "examples/semantic-search-process.svg is out of date; "
        "regenerate it with swimlane.py")


def test_example_fits_diagram_width_limit():
    spec = json.loads(EXAMPLE_SPEC.read_text(encoding="utf-8"))
    assert spec["width"] <= MAX_DIAGRAM_WIDTH, spec["width"]
    last_card_right = max(c["x"] for c in spec["cards"]) + spec.get("card_width", 150)
    assert spec["width"] - last_card_right >= 24, "less than 24 px right of the last card"


def test_only_approved_colors():
    spec = json.loads(EXAMPLE_SPEC.read_text(encoding="utf-8"))
    svg, _ = generate(spec)
    allowed = {swimlane.INK, swimlane.GREY, swimlane.LIGHT, swimlane.RED,
               swimlane.DIVIDER, swimlane.RULE, swimlane.CARD_STROKE, "#FFFFFF"}
    used = {c.upper() for c in re.findall(r"#[0-9A-Fa-f]{6}\b", svg)}
    assert used <= {c.upper() for c in allowed}, sorted(used - {c.upper() for c in allowed})


def test_edge_starts_and_ends_on_card_sides():
    # Cards are 150x60 by default: a's right side is (350, 130), b's left is (400, 130).
    svg, root = generate(minimal_spec())
    d = [p.get("d") for p in root.iter(f"{SVG_NS}path") if p.get("marker-end")]
    assert d == ["M350,130.0 L400,130.0"], d


def test_via_points_are_followed_in_order():
    spec = minimal_spec(edges=[{"from": "a", "from_side": "bottom", "via": [[275, 200], [475, 200]],
                                "to": "b", "to_side": "bottom"}])
    _, root = generate(spec)
    d = [p.get("d") for p in root.iter(f"{SVG_NS}path") if p.get("marker-end")][0]
    assert d == "M275.0,160 L275,200 L475,200 L475.0,160", d


def test_points_key_replaces_from_and_to():
    spec = minimal_spec(edges=[{"points": [[10, 10], [10, 50], [90, 50]]}])
    _, root = generate(spec)
    d = [p.get("d") for p in root.iter(f"{SVG_NS}path") if p.get("marker-end")][0]
    assert d == "M10,10 L10,50 L90,50", d


def test_dashed_edge_only_when_requested():
    spec = minimal_spec(edges=[
        {"from": "a", "from_side": "right", "to": "b", "to_side": "left", "dashed": True},
        {"from": "b", "from_side": "left", "to": "a", "to_side": "right"},
    ])
    _, root = generate(spec)
    arrows = [p for p in root.iter(f"{SVG_NS}path") if p.get("marker-end")]
    assert arrows[0].get("stroke-dasharray") == "5 5", arrows[0].attrib
    assert arrows[1].get("stroke-dasharray") is None, arrows[1].attrib


def test_special_characters_are_escaped():
    spec = minimal_spec(cards=[
        {"id": "a", "x": 200, "y": 100, "lines": ["Read <b> & write"]},
        {"id": "b", "x": 400, "y": 100, "lines": ["Second"]},
    ])
    svg, _ = generate(spec)  # ET.fromstring fails if the markup is broken
    assert "Read &lt;b&gt; &amp; write" in svg, svg


def test_lane_tool_is_optional():
    spec = minimal_spec(lanes=[
        {"label": "Developer", "tool": "ODC Studio", "top": 60, "bottom": 160},
        {"label": "Platform", "top": 164, "bottom": 280},
    ])
    svg, _ = generate(spec)
    assert ">Developer</tspan>" in svg and ">ODC Studio</tspan>" in svg
    assert ">Platform</tspan>" in svg


def test_one_dashed_divider_per_entry():
    _, root = generate(minimal_spec(dividers=[350, 550]))
    dividers = [l for l in root.iter(f"{SVG_NS}line") if l.get("stroke-dasharray") == "6 6"]
    assert len(dividers) == 2, len(dividers)


def test_output_uses_lf_line_endings():
    svg, _ = generate(minimal_spec())
    assert "\r" not in svg


def test_svg_size_reads_root_dimensions():
    assert render.svg_size('<svg xmlns="x" width="1372" height="640" viewBox="0 0 1372 640">') == (1372, 640)


def test_svg_size_exits_without_dimensions():
    try:
        render.svg_size('<svg xmlns="x" viewBox="0 0 10 10">')
    except SystemExit as e:
        assert "width and height" in str(e), e
        return
    raise AssertionError("expected SystemExit")


def test_render_reports_missing_browser():
    saved = render.find_browser
    render.find_browser = lambda: None
    try:
        with tempfile.TemporaryDirectory() as tmp:
            svg = Path(tmp) / "in.svg"
            svg.write_text('<svg width="10" height="10"></svg>', encoding="utf-8")
            try:
                render.main(str(svg), str(Path(tmp) / "out.png"))
            except SystemExit as e:
                assert "Chrome, Chromium, or Edge not found" in str(e), e
                return
            raise AssertionError("expected SystemExit")
    finally:
        render.find_browser = saved


def spec_error(spec_or_text) -> str:
    """Run swimlane.main on a spec (dict) or raw file text and return its exit message."""
    text = spec_or_text if isinstance(spec_or_text, str) else json.dumps(spec_or_text)
    with tempfile.TemporaryDirectory() as tmp:
        spec_path = Path(tmp) / "spec.json"
        spec_path.write_text(text, encoding="utf-8")
        try:
            swimlane.main(str(spec_path), str(Path(tmp) / "out.svg"))
        except SystemExit as e:
            return str(e)
    raise AssertionError("expected SystemExit")


def generate_stderr(spec: dict) -> str:
    """Generate a spec that is drawn, and return what it printed to stderr."""
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        generate(spec)
    return err.getvalue()


def assert_in_all(message, *parts):
    for part in parts:
        assert part in message, f"{part!r} not in {message!r}"


def test_spec_unknown_card_id_names_edge_and_card():
    msg = spec_error(minimal_spec(edges=[{"from": "a", "from_side": "right", "to": "zzz", "to_side": "left"}]))
    assert_in_all(msg, "❌ 1 problem in", "Edge 1", "'zzz'", "no card has that id", "The card ids are: a, b.")


def test_spec_misspelled_side_lists_valid_sides():
    msg = spec_error(minimal_spec(edges=[{"from": "a", "from_side": "botom", "to": "b", "to_side": "left"}]))
    assert_in_all(msg, "Edge 1", '"from_side" is \'botom\'', "top, bottom, left, right")


def test_spec_missing_top_level_key_names_it():
    spec = minimal_spec()
    del spec["lanes"]
    assert_in_all(spec_error(spec), 'The spec has no "lanes" key', "Add it")


def test_spec_missing_card_key_names_card_and_key():
    spec = minimal_spec()
    del spec["cards"][1]["id"]
    assert_in_all(spec_error(spec), 'Card 2 has no "id" key')


def test_spec_edge_without_endpoints_asks_for_them_or_points():
    msg = spec_error(minimal_spec(edges=[{"from": "a", "from_side": "right"}]))
    assert_in_all(msg, 'Edge 1 has no "to" key', 'has no "to_side" key', '"points"')


def test_spec_bad_via_and_points_are_reported():
    msg = spec_error(minimal_spec(edges=[
        {"from": "a", "from_side": "right", "via": [[1]], "to": "b", "to_side": "left"},
        {"points": [[1, 2]]},
    ]))
    assert_in_all(msg, '❌ 2 problems in', 'Edge 1: "via" must be', 'Edge 2: "points" must be')


def test_spec_duplicate_card_id_is_reported():
    spec = minimal_spec()
    spec["cards"][1]["id"] = "a"
    assert_in_all(spec_error(spec), "The card id 'a' is used by more than one card")


def test_spec_overlapping_cards_are_reported():
    spec = minimal_spec()
    spec["cards"][1]["x"] = 300
    assert_in_all(spec_error(spec), "Cards 'a' and 'b' overlap")


def test_spec_card_over_lane_labels_is_reported():
    spec = minimal_spec()
    spec["cards"][0]["x"] = 100
    assert_in_all(spec_error(spec), "Card 'a' at x=100 overlaps the lane labels", "end at x=180", "lane_label_width")


def test_spec_card_past_canvas_edge_is_reported():
    spec = minimal_spec()
    spec["cards"][1]["x"] = 500
    assert_in_all(spec_error(spec), "Card 'b' ends at x=650", "less than 24 px", "increase width")


def test_spec_card_below_canvas_is_reported():
    spec = minimal_spec()
    spec["cards"][0]["y"] = 280
    assert_in_all(spec_error(spec), "Card 'a' at y=280 falls outside the canvas height of 300")


def test_spec_lane_label_width_moves_the_overlap_limit():
    # With wider lane labels, a card that fit before now overlaps them.
    msg = spec_error(minimal_spec(lane_label_width=210))
    assert_in_all(msg, "Card 'a' at x=200 overlaps the lane labels", "end at x=240")


def test_spec_invalid_json_gives_line_and_column():
    assert_in_all(spec_error('{"width": 600,\n "height": }'), "isn't valid JSON", "line 2", "Fix the syntax")


def test_spec_missing_file_gives_path_and_next_step():
    try:
        swimlane.main("does-not-exist.json", "out.svg")
    except SystemExit as e:
        assert_in_all(str(e), "does-not-exist.json", "doesn't exist", "examples/semantic-search-process.json")
        return
    raise AssertionError("expected SystemExit")


def test_spec_that_is_not_an_object_is_reported():
    assert_in_all(spec_error("[1, 2]"), "must be a JSON object")


def test_wide_label_warns_without_failing():
    err = generate_stderr(minimal_spec(cards=[
        {"id": "a", "x": 200, "y": 100, "lines": ["Update the authentication flows"]},
        {"id": "b", "x": 400, "y": 100, "lines": ["Second"]},
    ]))
    assert_in_all(err, "⚠️", "Card 'a'", "may not fit the 150 px card", "split it into two lines")


def test_three_line_card_warns():
    err = generate_stderr(minimal_spec(cards=[
        {"id": "a", "x": 200, "y": 100, "lines": ["One", "Two", "Three"]},
        {"id": "b", "x": 400, "y": 100, "lines": ["Second"]},
    ]))
    assert_in_all(err, "Card 'a' has 3 lines", "holds 2")


def test_example_spec_has_no_warnings():
    spec = json.loads(EXAMPLE_SPEC.read_text(encoding="utf-8"))
    assert generate_stderr(spec) == ""


def test_svg_size_rejects_missing_svg_element():
    try:
        render.svg_size("<html></html>")
    except SystemExit as e:
        assert_in_all(str(e), "❌", "no <svg> element", "swimlane.py")
        return
    raise AssertionError("expected SystemExit")


def test_svg_size_rejects_percentage_width():
    try:
        render.svg_size('<svg width="100%" height="50">')
    except SystemExit as e:
        assert_in_all(str(e), '"100%"', "number of pixels", 'width="1372"')
        return
    raise AssertionError("expected SystemExit")


def test_svg_size_rounds_decimals_up_and_accepts_px():
    assert render.svg_size('<svg width="1372.5" height="640px">') == (1373, 640)


def test_svg_size_ignores_stroke_width():
    assert render.svg_size('<svg stroke-width="3" width="10" height="20">') == (10, 20)
    try:
        render.svg_size('<svg stroke-width="3" height="20">')
    except SystemExit as e:
        assert "width and height" in str(e), e
        return
    raise AssertionError("expected SystemExit")


class FakeRun:
    """Stand-in for subprocess.run that records the command and can write the PNG."""

    def __init__(self, returncode=0, stderr="", write_png=True, error=None):
        self.returncode, self.stderr, self.write_png, self.error = returncode, stderr, write_png, error
        self.command = None

    def __call__(self, command, **kwargs):
        self.command = command
        if self.error:
            raise self.error
        if self.write_png:
            for arg in command:
                if arg.startswith("--screenshot="):
                    Path(arg.split("=", 1)[1]).write_bytes(b"png")
        return subprocess.CompletedProcess(command, self.returncode, "", self.stderr)


def render_with(fake, no_sandbox=False):
    """Run render.main with a fake browser and return (exit message or None, fake)."""
    saved_find, saved_run = render.find_browser, render.subprocess.run
    render.find_browser, render.subprocess.run = (lambda: "browser"), fake
    try:
        with tempfile.TemporaryDirectory() as tmp:
            svg = Path(tmp) / "in.svg"
            svg.write_text('<svg width="10" height="10"></svg>', encoding="utf-8")
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    render.main(str(svg), str(Path(tmp) / "out.png"), no_sandbox=no_sandbox)
            except SystemExit as e:
                return str(e), fake
            return None, fake
    finally:
        render.find_browser, render.subprocess.run = saved_find, saved_run


def test_render_browser_failure_shows_output_and_hint():
    msg, _ = render_with(FakeRun(returncode=1, stderr="noise\nGPU process crashed", write_png=False))
    assert_in_all(msg, "❌", "exited with code 1", "Browser output:", "GPU process crashed", "--no-sandbox")


def test_render_reports_missing_png_after_clean_exit():
    msg, _ = render_with(FakeRun(returncode=0, write_png=False))
    assert_in_all(msg, "❌", "didn't write", "The browser printed no output.")


def test_render_timeout_is_explained():
    msg, _ = render_with(FakeRun(error=subprocess.TimeoutExpired("browser", 120)))
    assert_in_all(msg, "❌", "didn't finish within 120 seconds")


def test_render_browser_that_cannot_start_is_explained():
    msg, _ = render_with(FakeRun(error=PermissionError(13, "Permission denied")))
    assert_in_all(msg, "❌", "couldn't start", "Permission denied")


def test_render_no_sandbox_flag_is_passed_only_when_asked():
    msg, fake = render_with(FakeRun())
    assert msg is None and "--no-sandbox" not in fake.command, fake.command
    msg, fake = render_with(FakeRun(), no_sandbox=True)
    assert msg is None and "--no-sandbox" in fake.command, fake.command


def test_render_failure_with_no_sandbox_does_not_repeat_the_hint():
    msg, _ = render_with(FakeRun(returncode=1, stderr="boom", write_png=False), no_sandbox=True)
    assert "boom" in msg and "--no-sandbox" not in msg, msg


def test_render_missing_svg_file_is_explained():
    saved = render.find_browser
    render.find_browser = lambda: "browser"
    try:
        render.main("does-not-exist.svg", "out.png")
    except SystemExit as e:
        assert_in_all(str(e), "does-not-exist.svg", "doesn't exist", "swimlane.py")
        return
    finally:
        render.find_browser = saved
    raise AssertionError("expected SystemExit")


TESTS = [
    test_example_is_well_formed_svg,
    test_example_has_every_card_edge_and_label,
    test_example_matches_committed_svg,
    test_example_fits_diagram_width_limit,
    test_only_approved_colors,
    test_edge_starts_and_ends_on_card_sides,
    test_via_points_are_followed_in_order,
    test_points_key_replaces_from_and_to,
    test_dashed_edge_only_when_requested,
    test_special_characters_are_escaped,
    test_lane_tool_is_optional,
    test_one_dashed_divider_per_entry,
    test_output_uses_lf_line_endings,
    test_svg_size_reads_root_dimensions,
    test_svg_size_exits_without_dimensions,
    test_render_reports_missing_browser,
    test_spec_unknown_card_id_names_edge_and_card,
    test_spec_misspelled_side_lists_valid_sides,
    test_spec_missing_top_level_key_names_it,
    test_spec_missing_card_key_names_card_and_key,
    test_spec_edge_without_endpoints_asks_for_them_or_points,
    test_spec_bad_via_and_points_are_reported,
    test_spec_duplicate_card_id_is_reported,
    test_spec_overlapping_cards_are_reported,
    test_spec_card_over_lane_labels_is_reported,
    test_spec_card_past_canvas_edge_is_reported,
    test_spec_card_below_canvas_is_reported,
    test_spec_lane_label_width_moves_the_overlap_limit,
    test_spec_invalid_json_gives_line_and_column,
    test_spec_missing_file_gives_path_and_next_step,
    test_spec_that_is_not_an_object_is_reported,
    test_wide_label_warns_without_failing,
    test_three_line_card_warns,
    test_example_spec_has_no_warnings,
    test_svg_size_rejects_missing_svg_element,
    test_svg_size_rejects_percentage_width,
    test_svg_size_rounds_decimals_up_and_accepts_px,
    test_svg_size_ignores_stroke_width,
    test_render_browser_failure_shows_output_and_hint,
    test_render_reports_missing_png_after_clean_exit,
    test_render_timeout_is_explained,
    test_render_browser_that_cannot_start_is_explained,
    test_render_no_sandbox_flag_is_passed_only_when_asked,
    test_render_failure_with_no_sandbox_does_not_repeat_the_hint,
    test_render_missing_svg_file_is_explained,
]

if __name__ == "__main__":
    results = [run(t.__name__, t) for t in TESTS]
    sys.exit(0 if all(results) else 1)
