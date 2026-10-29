---
name: process-swimlane-diagram
description: >-
  Creates a swimlane process diagram as SVG and PNG, with roles as horizontal
  lanes, phases as numbered columns, and task cards connected by orthogonal
  arrows that don't cross. Follows the OutSystems documentation visual style.

  Use when a process has at least two roles or tools that hand work to each
  other across at least two phases, for example an end-to-end setup that an
  administrator, a developer, and a platform service each take part in. Also
  use when a content developer asks to "draw a process diagram", "make a
  swimlane", "show who does what in each phase", or "create a process overview
  image", or when a Mermaid flowchart can't show roles and phases together.
  For a flow with a single role or no phases, use /create-diagram instead.
allowed-tools: Read,Write,Edit,Bash(python3:*),Bash(python:*)
---

# Process swimlane diagram

This skill produces a process diagram that shows who performs each task, in which tool, and in which phase. The output is an editable SVG for a designer and a 2x PNG for documentation. The layout is deterministic: a JSON spec places every lane, card, and arrow, and a script renders it.

## When to use this skill

Use this skill when a process involves more than one role or tool and the reader needs to see the handoffs between them. Mermaid flowcharts show the flow but can't align role lanes with phase columns, because the Mermaid layout engine places groups and nested groups on its own.

A process fits this skill when all of the following are true:

* Two or more roles, tools, or systems perform tasks, and the work passes between them.
* The process has two or more phases, stages, or steps that a reader needs to tell apart.
* The reader benefits from seeing who does what, for example in a multi-task process page that follows `process-rules.md`.

## When not to use this skill

* The process has a single role or no phases. Use `/create-diagram` instead.
* The diagram must stay as editable Mermaid text in the page. Use `/create-diagram` instead.
* The diagram shows a message exchange between systems with no phases. Use a sequence diagram instead.

## Visual design

The diagram follows the style of the OutSystems documentation diagrams. Every color comes from the approved palette in the `validate-svgs` skill. The following list describes each element:

* **Canvas**: White, with rounded corners, a light border, and a soft drop shadow.
* **Phases**: Columns, each with a red `#F22800` numbered badge and a bold title at the top. Dashed grey vertical lines separate the phases.
* **Lanes**: Horizontal rows, one per role. A dark grey `#686E76` block on the left names the role in bold and the tool below it, for example "Developer" and "ODC Studio". Thin light rules separate the lanes.
* **Task cards**: Light grey `#F5F6FA` rounded rectangles with a verb-first label of up to five words, for example "Publish the app".
* **Arrows**: Grey `#686E76` orthogonal lines with a filled arrowhead. Dashed arrows can show a dependency that isn't a direct handoff.
* **Captions**: Small grey text that names a path or a condition, for example "Knowledge base" or "After indexing finishes".

Write labels in sentence case, and capitalize only the first word, acronyms, and product names.

## Workflow

Follow these steps to create a diagram.

1. Collect the process from the source material: the phases, the roles and their tools, the tasks of each role in each phase, and the handoffs between tasks. Verify each task against the product documentation or the design, rather than inferring it.
1. Order the lanes so that every handoff goes between adjacent lanes. A shared service lane, such as the platform, usually goes in the middle, between the two human roles that hand work to it.
1. Sketch the grid. Give each phase enough columns for its longest chain of tasks. When two tasks in one lane need the same column, split the lane into sub-rows.
1. Write the JSON spec in the scratchpad or a temporary folder, not in the content repo. Start from `examples/semantic-search-process.json` and replace the phases, lanes, cards, captions, and edges.
1. Route each edge with `via` points so that it doesn't cross a card or another edge. Leave a gap of at least 20 px between a vertical edge and a phase divider, so the edge doesn't read as part of the divider.
1. Generate the SVG and render the PNG. Run both commands from this skill's folder, or use the full path to each script:

    ```sh
    python3 scripts/swimlane.py spec.json diagram-diag.svg
    python3 scripts/render.py diagram-diag.svg diagram-diag.png
    ```

    On Windows, use `python` instead of `python3` if `python3` isn't available.

    `swimlane.py` checks the spec before it draws. For each problem it prints a line that names the edge or card and says what to change, and it draws nothing until you fix them all. It also prints warnings for labels that are probably too wide for the card. If `render.py` fails, it prints the browser's last output. On Linux, as root, or in a container, add `--no-sandbox` to the `render.py` command.

1. Open the PNG and check it. Confirm that no edge crosses a card or another edge, that each label fits its card, and that each title is fully visible. Adjust the spec and render again until the image is clean.
1. Save the SVG, and the PNG if the page needs it, in the `images` folder next to the article. End the file name with `-diag`, for example `semantic-search-process-diag.svg`, and use lowercase letters and hyphens only.
1. Write alt text that describes the flow phase by phase, naming the role and the tasks in each phase.
1. Run the `validate-svgs` skill on the SVG before opening the pull request.

## Spec format

The spec is a JSON object. All coordinates are in pixels at 1x, measured from the top left of the canvas. The following table describes each key.

| Key | Description |
| --- | --- |
| `width`, `height` | The canvas size. Keep `width` at 1650 or less, which is the diagram limit in `validate-svgs`. Leave 24 px or more on the right of the last card. |
| `card_width`, `card_height` | The size of every task card. The defaults are 150 and 60. |
| `lane_label_width` | The width of the dark role blocks on the left. The default is 150. Raise it for a long role or tool name. The blocks start at x=30, so no card can start left of `30 + lane_label_width`. |
| `font` | The CSS font stack for all text. The default is Inter with Helvetica Neue, Arial, and sans-serif as fallbacks. |
| `phases` | A list of `{number, title, x}`. `x` is the left edge of the phase header. Align it with the first card of the phase. |
| `dividers` | A list of x positions for the dashed lines between phases. |
| `lanes` | A list of `{label, tool, top, bottom}`, from top to bottom. `tool` is optional. Leave about 4 px between one lane's `bottom` and the next lane's `top`. |
| `captions` | A list of `{x, y, text, anchor}`. `anchor` is `start` by default, or `middle`. |
| `cards` | A list of `{id, x, y, lines}`. `lines` holds one or two lines of label text. |
| `edges` | A list of `{from, from_side, to, to_side, via, dashed}`. Sides are `top`, `bottom`, `left`, or `right`. `via` lists the corner points of the route. Use `points` instead to give the full route. |

## Layout rules

The following rules prevent the most common layout problems:

* Keep a column grid inside each phase, with about 36 px between cards, so arrows have room for their arrowheads.
* Place a card under or over the card that hands work to it, so the handoff edge is a straight vertical line.
* Route a long edge through an empty sub-row or an empty column, never along a lane rule or a divider.
* When several edges join one card, bring them to a shared vertical line just before the card, then enter the card once.
* Label alternative paths with a caption above the first card of each path, instead of with a decision diamond.

The following examples show the rules in practice:

* ✅ A card directly under the card that hands work to it, joined by a straight vertical edge.
* ❌ The same handoff drawn as a long edge with several bends because the receiving card sits far to one side.
* ✅ A long edge routed through an empty sub-row, with at least 20 px between it and any divider.
* ❌ A long edge that runs along a lane rule or a phase divider, so it reads as part of the line.
* ✅ Three edges that meet at one vertical line and then enter the card once.
* ❌ Three edges that each enter the same card side at a different point.
* ✅ A caption such as "After indexing finishes" above the first card of a path.
* ❌ A decision diamond to show which path applies.

## Layout limits

The script places every element where the spec says and doesn't arrange anything. The following limits apply:

* **Fixed card size:** Every card has the same width and height, and the text doesn't wrap. A card holds one or two lines of about 17 characters each at the default width. Write the line breaks yourself, and widen `card_width` for longer labels.
* **Lane label width:** The role blocks are 150 px wide unless you set `lane_label_width`. A long role name needs a wider block, and the cards then start further right.
* **Text fit:** `swimlane.py` estimates the width of each line and warns about lines that probably don't fit. The estimate is approximate, so always check the PNG.
* **Checked for you:** The script stops with a message when two cards overlap, when a card sits over the lane labels, when a card leaves less than 24 px before the right edge or falls outside the canvas, and when an edge names a card or a side that doesn't exist.
* **Not checked:** The script doesn't check whether an edge crosses a card or another edge, or whether a `via` route runs along a divider. Check these in the PNG.

## Requirements

The scripts need Python 3 and Google Chrome, Chromium, or Microsoft Edge, on macOS, Windows, or Linux. The render script loads the Inter font from Google Fonts, so rendering needs a network connection. Without it, the browser falls back to Helvetica Neue or Arial.

## Hand off to a designer

The SVG keeps all text as live text in the Inter font, so a designer can open it in Figma or Illustrator and adjust it. The diagram has no icons. A designer can add them.
