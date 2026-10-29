#!/usr/bin/env python3
"""Generate a swimlane process diagram as SVG from a JSON spec.

Usage: python3 swimlane.py SPEC.json OUTPUT.svg

The spec places every element with explicit coordinates, so the layout
is deterministic and each edge follows the route you define. See
examples/semantic-search-process.json for a complete spec. All colors come
from the approved docs palette, so the SVG passes the validate-svgs skill.
"""
import json
import sys
from html import escape

INK, GREY, LIGHT, RED = "#0A141E", "#686E76", "#F5F6FA", "#F22800"
DIVIDER, RULE, CARD_STROKE = "#979CA2", "#D9D9D9", "#D9D9D9"

LANE_X = 30
SIDES = ("top", "bottom", "left", "right")
TOP_LEVEL_KEYS = ("width", "height", "phases", "lanes", "cards", "edges")
RIGHT_MARGIN = 24  # space to leave on the right of the last card
CHAR_WIDTH = 8.2  # average width in px of one character of 15 px Inter
FIT_SLACK = 8  # px a line can come within of the card edge before it is flagged
MAX_CARD_LINES = 2


def load_spec(spec_path):
    """Read the spec, or exit with a plain message that says what to fix."""
    try:
        with open(spec_path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        sys.exit(f"❌ The spec file {spec_path} doesn't exist. Check the path, "
                 "or copy examples/semantic-search-process.json and edit it.")
    except UnicodeDecodeError:
        sys.exit(f"❌ The spec file {spec_path} isn't UTF-8 text. Save it as UTF-8 and run again.")
    except json.JSONDecodeError as e:
        sys.exit(f"❌ The spec file {spec_path} isn't valid JSON: {e.msg} at line {e.lineno}, "
                 f"column {e.colno}. Fix the syntax and run again.")


def is_point(value):
    return (isinstance(value, list) and len(value) == 2
            and all(isinstance(n, (int, float)) and not isinstance(n, bool) for n in value))


def validate_spec(spec):
    """Return (errors, warnings) as lists of plain sentences.

    An error means the diagram can't be drawn, or would be drawn wrong. A warning
    means it is drawn but probably needs a change, such as text that is too wide.
    """
    errors, warnings = [], []
    if not isinstance(spec, dict):
        return ["The spec must be a JSON object. Start from examples/semantic-search-process.json."], warnings

    missing = [k for k in TOP_LEVEL_KEYS if k not in spec]
    errors += [f'The spec has no "{k}" key. Add it, as in examples/semantic-search-process.json.'
               for k in missing]
    for key in ("phases", "lanes", "cards", "edges"):
        if key in spec and not isinstance(spec[key], list):
            errors.append(f'"{key}" must be a list.')
    for key in ("width", "height"):
        if key in spec and (not isinstance(spec[key], (int, float)) or isinstance(spec[key], bool)):
            errors.append(f'"{key}" must be a number of pixels.')
    if errors:
        return errors, warnings

    def items_with_keys(kind, items, keys):
        valid = []
        for i, item in enumerate(items, 1):
            gone = [k for k in keys if not isinstance(item, dict) or k not in item]
            errors.extend(f'{kind} {i} has no "{k}" key. Add it, as in the example spec.' for k in gone)
            if not gone:
                valid.append(item)
        return valid

    items_with_keys("Phase", spec["phases"], ("number", "title", "x"))
    items_with_keys("Lane", spec["lanes"], ("label", "top", "bottom"))
    items_with_keys("Caption", spec.get("captions", []), ("x", "y", "text"))
    cards = items_with_keys("Card", spec["cards"], ("id", "x", "y", "lines"))
    for x in spec.get("dividers", []):
        if not isinstance(x, (int, float)) or isinstance(x, bool):
            errors.append(f'"dividers" must hold x positions as numbers, but it holds {x!r}.')

    width, height = spec["width"], spec["height"]
    card_w, card_h = spec.get("card_width", 150), spec.get("card_height", 60)
    labels_end = LANE_X + spec.get("lane_label_width", 150)

    seen = set()
    for c in cards:
        name = c["id"]
        if name in seen:
            errors.append(f"The card id '{name}' is used by more than one card. Give each card its own id.")
        seen.add(name)
        lines = c["lines"]
        if not (isinstance(lines, list) and lines and all(isinstance(l, str) for l in lines)):
            errors.append(f'Card \'{name}\': "lines" must be a list of one or two lines of text.')
        else:
            if len(lines) > MAX_CARD_LINES:
                warnings.append(f"Card '{name}' has {len(lines)} lines, and a card holds {MAX_CARD_LINES}. "
                                "Shorten the label, for example to a verb and an object.")
            for line in lines:
                est = len(line) * CHAR_WIDTH
                if est > card_w - FIT_SLACK:
                    warnings.append(f"Card '{name}': the line \"{line}\" is about {est:.0f} px wide and may "
                                    f"not fit the {card_w} px card. Shorten it or split it into two lines.")
        if c["x"] < labels_end:
            errors.append(f"Card '{name}' at x={c['x']} overlaps the lane labels, which end at x={labels_end}. "
                          "Move the card to the right, or reduce lane_label_width.")
        if c["x"] + card_w > width - RIGHT_MARGIN:
            errors.append(f"Card '{name}' ends at x={c['x'] + card_w}, which leaves less than {RIGHT_MARGIN} px "
                          f"before the canvas edge at x={width}. Move the card to the left, or increase width.")
        if c["y"] < 0 or c["y"] + card_h > height:
            errors.append(f"Card '{name}' at y={c['y']} falls outside the canvas height of {height}. "
                          "Move the card, or increase height.")
    for i, a in enumerate(cards):
        for b in cards[i + 1:]:
            if a["id"] != b["id"] and a["x"] < b["x"] + card_w and b["x"] < a["x"] + card_w \
                    and a["y"] < b["y"] + card_h and b["y"] < a["y"] + card_h:
                errors.append(f"Cards '{a['id']}' and '{b['id']}' overlap. Move one of them to its own "
                              "column or sub-row.")

    ids = sorted(seen)
    known = f" The card ids are: {', '.join(ids)}." if 0 < len(ids) <= 12 else ""
    for i, e in enumerate(spec["edges"], 1):
        label = f"Edge {i}"
        if not isinstance(e, dict):
            errors.append(f"{label} must be a JSON object.")
            continue
        if "points" in e:
            if not (isinstance(e["points"], list) and len(e["points"]) >= 2
                    and all(is_point(p) for p in e["points"])):
                errors.append(f'{label}: "points" must be a list of at least two [x, y] pairs.')
            continue
        errors.extend(f'{label} has no "{k}" key. Add it, or give the whole route with "points".'
                      for k in ("from", "from_side", "to", "to_side") if k not in e)
        for end, side in (("from", "from_side"), ("to", "to_side")):
            if end in e and e[end] not in seen:
                errors.append(f"{label}: \"{end}\" is '{e[end]}', but no card has that id. "
                              f"Check the spelling.{known}")
            if side in e and e[side] not in SIDES:
                errors.append(f"{label}: \"{side}\" is '{e[side]}', which isn't a card side. "
                              f"Use one of: {', '.join(SIDES)}.")
        if "via" in e and not (isinstance(e["via"], list) and all(is_point(p) for p in e["via"])):
            errors.append(f'{label}: "via" must be a list of [x, y] pairs.')
    return errors, warnings


def warn(message):
    line = f"⚠️ {message}"
    try:
        print(line, file=sys.stderr)
    except UnicodeEncodeError:  # a console code page that can't print the marker
        print(line.encode("ascii", "replace").decode("ascii"), file=sys.stderr)


def main(spec_path, out_path):
    spec = load_spec(spec_path)
    errors, warnings = validate_spec(spec)
    for message in warnings:
        warn(message)
    if errors:
        sys.exit("\n".join(
            [f"❌ {len(errors)} problem{'s' if len(errors) > 1 else ''} in {spec_path}:"]
            + [f"* {e}" for e in errors] + ["Fix the spec and run again."]))

    width, height = spec["width"], spec["height"]
    card_w = spec.get("card_width", 150)
    card_h = spec.get("card_height", 60)
    font = spec.get("font", "Inter, 'Helvetica Neue', Arial, sans-serif")
    lane_x, lane_w = LANE_X, spec.get("lane_label_width", 150)
    out = []

    def text(x, y, lines, size=15, weight=400, fill=INK, anchor="middle", lh=19):
        y0 = y - (len(lines) - 1) * lh / 2
        spans = "".join(
            f'<tspan x="{x}" y="{y0 + i * lh:.1f}">{escape(l)}</tspan>'
            for i, l in enumerate(lines))
        out.append(
            f'<text font-family="{escape(font)}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" dominant-baseline="central">{spans}</text>')

    cards = {c["id"]: c for c in spec["cards"]}

    def anchor(card_id, side):
        c = cards[card_id]
        x, y = c["x"], c["y"]
        return {
            "top": (x + card_w / 2, y),
            "bottom": (x + card_w / 2, y + card_h),
            "left": (x, y + card_h / 2),
            "right": (x + card_w, y + card_h / 2),
        }[side]

    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
               f'viewBox="0 0 {width} {height}">')
    out.append(
        '<defs><marker id="head" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" '
        f'markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{GREY}"/></marker>'
        '<filter id="shadow" x="-5%" y="-5%" width="110%" height="115%"><feDropShadow dx="0" dy="3" '
        'stdDeviation="5" flood-color="#0A141E" flood-opacity="0.12"/></filter></defs>')

    # Canvas
    out.append(f'<rect x="12" y="12" width="{width - 24}" height="{height - 24}" rx="10" '
               f'fill="#FFFFFF" stroke="{RULE}" filter="url(#shadow)"/>')

    # Phase headers: red numbered badge, then the phase title
    for p in spec["phases"]:
        cx = p["x"] + 14
        out.append(f'<circle cx="{cx}" cy="56" r="14" fill="{RED}"/>')
        text(cx, 56, [str(p["number"])], size=15, weight=700, fill="#FFFFFF")
        text(p["x"] + 38, 56, [p["title"]], size=17, weight=600, anchor="start")

    # Lanes: dark label block on the left, rules between lanes
    lanes = spec["lanes"]
    for lane in lanes:
        top, bottom = lane["top"], lane["bottom"]
        mid = (top + bottom) / 2
        out.append(f'<rect x="{lane_x}" y="{top + 4}" width="{lane_w}" height="{bottom - top - 8}" '
                   f'rx="6" fill="{GREY}"/>')
        cx = lane_x + lane_w / 2
        if lane.get("tool"):
            text(cx, mid - 10, [lane["label"]], size=16, weight=600, fill="#FFFFFF")
            text(cx, mid + 12, [lane["tool"]], size=14, fill="#FFFFFF")
        else:
            text(cx, mid, [lane["label"]], size=16, weight=600, fill="#FFFFFF")
    for upper, lower in zip(lanes, lanes[1:]):
        y = (upper["bottom"] + lower["top"]) / 2
        out.append(f'<line x1="{lane_x}" y1="{y}" x2="{width - 30}" y2="{y}" stroke="{RULE}" stroke-width="1.5"/>')

    # Dashed dividers between phases
    first_top, last_bottom = lanes[0]["top"], lanes[-1]["bottom"]
    for x in spec.get("dividers", []):
        out.append(f'<line x1="{x}" y1="{first_top - 8}" x2="{x}" y2="{last_bottom - 4}" '
                   f'stroke="{DIVIDER}" stroke-width="1.5" stroke-dasharray="6 6"/>')

    # Small grey captions, for example to name a path or a condition
    for c in spec.get("captions", []):
        text(c["x"], c["y"], [c["text"]], size=13, fill=GREY, anchor=c.get("anchor", "start"))

    # Edges before cards, so cards sit on top of line ends
    for e in spec["edges"]:
        if "points" in e:
            pts = [tuple(p) for p in e["points"]]
        else:
            pts = ([anchor(e["from"], e["from_side"])] + [tuple(p) for p in e.get("via", [])]
                   + [anchor(e["to"], e["to_side"])])
        d = " ".join(f"{'M' if i == 0 else 'L'}{x},{y}" for i, (x, y) in enumerate(pts))
        dash = ' stroke-dasharray="5 5"' if e.get("dashed") else ""
        out.append(f'<path d="{d}" fill="none" stroke="{GREY}" stroke-width="1.6" '
                   f'stroke-linejoin="round"{dash} marker-end="url(#head)"/>')

    # Task cards
    for c in spec["cards"]:
        out.append(f'<rect x="{c["x"]}" y="{c["y"]}" width="{card_w}" height="{card_h}" rx="8" '
                   f'fill="{LIGHT}" stroke="{CARD_STROKE}"/>')
        text(c["x"] + card_w / 2, c["y"] + card_h / 2, c["lines"])

    out.append("</svg>")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    # A Windows console or pipe can default to a code page that can't print the ❌ marker.
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="replace")
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 swimlane.py SPEC.json OUTPUT.svg")
    main(sys.argv[1], sys.argv[2])
