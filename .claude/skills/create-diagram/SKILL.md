---
name: create-diagram
description: >-
  On-demand Mermaid diagram creation from a natural-language description. Follows
  OutSystems brand guidelines. Optionally inserts the result into a markdown article.

  Use when a content developer wants to create a specific diagram without going
  through article analysis. For auditing an article and deciding where diagrams
  are needed, use /suggest-visuals instead.

  Trigger phrases: "create a diagram", "make a diagram", "I want a diagram",
  "new diagram", "create a mermaid diagram", "generate a diagram".
argument-hint: <description of what to diagram>
allowed-tools: Read,Edit,AskUserQuestion
---

# Create diagram

Generate a single OutSystems-brand-compliant Mermaid diagram from a natural-language
description.

## Setup

Before starting, read both companion files from the sibling
`suggest-visuals` skill directory (same parent folder as this SKILL.md):

* `visual-rules.md` — audience → diagram type mapping
* `brand-guidelines.md` — OutSystems Mermaid style rules

## Workflow

### Step 1: Get the description

Use `$ARGUMENTS` as the diagram description. If no argument was provided, ask:
> "What do you want the diagram to show?"

### Step 2: Clarify audience and purpose

Ask the user two questions in a single AskUserQuestion call:

**Question 1 — Audience:**

* Architect
* Business analyst
* Developer
* Front-end developer
* Platform administrator
* Product owner
* Tech lead

**Question 2 — Purpose:**

* Process or workflow
* System / component overview
* Data model
* Concept overview / mental model

### Step 3: Select diagram type

Using visual-rules.md, cross-reference the audience and purpose to select the most
appropriate Mermaid diagram type:

* Process or workflow → `flowchart TD` / `flowchart LR` / `sequenceDiagram`
* System / component overview → `architecture` / `flowchart TB`
* Data model → `erDiagram`
* Concept overview / mental model → `mindmap` / `flowchart TD`

Prefer the type that appears in both the audience row and the purpose column. When
in doubt, prefer `flowchart` for process/system content and `sequenceDiagram` for
multi-actor interactions.

### Step 4: Generate the diagram

Generate brand-compliant Mermaid code following brand-guidelines.md exactly:

* Always include the `%%{init}%%` block
* Apply correct `classDef` groups to every node in flowcharts
* Sequence diagrams always use `autonumber` and include `"messageFontSize": "14px"` in the init block `themeVariables`
* Keep node labels ≤ 5 words; use `<br/>` for line breaks (never `\n`)
* **Label casing**: use sentence case for all labels — capitalise the first word only; keep the rest lowercase except acronyms (such as ODC, AI, API) and proper product names (such as Amazon Bedrock, Azure OpenAI).
* Never use gradients, shading, or 3D effects
* **Cross-subgraph edges**: do not add text labels on arrows that cross a subgraph boundary — the label renders on the border and overlaps the container. Describe such relationships in prose instead, or use a single-word label maximum.
* **Mindmaps**: use HTML spans for hierarchical font sizes (root 20px bold, level 1 18px, level 2 16px, level 3+ 14px); set `cScale0`–`cScale4` in the init block for distinct branch colors — do NOT rely on Mermaid auto-coloring.
* **Process node shapes**: use `NodeId(Label):::process` (rounded rectangle) not `NodeId[Label]:::process` (sharp rectangle).
* **Semantic colors**: `:::start`/`:::stop` are only for workflow entry/exit points; `:::error` is only for failure outcome nodes. Use `:::process` for all component/server nodes regardless of state — show unavailability with dashed arrows (`-.->`) and a descriptive label.
* **No empty node labels**: verify every node has non-empty text before presenting.
* **Nested subgraphs for containment**: when the concept requires a containment hierarchy (e.g. Environment → Zone → Servers), **keep the nested subgraphs** — do not flatten or restructure away the nesting. Fix title visibility with two rules: (1) declare a sibling node _before_ the inner subgraph, and (2) add `direction TB` inside every nested subgraph. Without `direction TB`, Mermaid places the sibling node and the inner subgraph side-by-side horizontally even in a `flowchart TB` diagram. See the nested subgraph section in brand-guidelines.md for the full code pattern.
* **Sequence diagram autonumber circles**: add `"labelBoxBkgColor": "#F22800"` and `"labelTextColor": "#FFFFFF"` to themeVariables — numbered circles render in OutSystems red with white text.
* **Sequence diagram notes**: add `"noteBkgColor": "#F5F6FA"`, `"noteBorderColor": "#686E76"`, and `"noteTextColor": "#0A141E"` to themeVariables — overrides Mermaid's default yellow `Note over` boxes with the OutSystems light-grey1 palette.
* **Sequence diagram `themeCSS` fallback**: include the `themeCSS` block from brand-guidelines.md's sequence recipe alongside the theme variables. Some renderers (including VS Code's Markdown preview) ignore `labelBoxBkgColor`/`noteBkgColor`; the CSS overrides win where the variables don't.
* **Init-block JSON pitfalls**: never put single quotes inside any `%%{init}%%` value (e.g. `'Noto Sans'` for a spaced font name). The directive parser in some renderers — including the OutSystems docs-next production renderer — breaks on embedded single quotes and silently drops the **entire** init block, reverting the diagram to Mermaid defaults (lavender actors, yellow notes, dark autonumber). Use values that contain no spaces or quotes: `"fontFamily": "NotoSans, Helvetica, Arial, sans-serif"`.

### Step 5: Present the diagram

Show the Mermaid code block with:

1. A one-sentence explanation of what the diagram shows
1. The diagram type chosen and why

````text
```mermaid
[Full Mermaid code]
```
````

### Step 6: Offer to insert into an article

Ask:
> "Would you like to insert this into an article? If yes, share the file path and
> the heading it should go under."

If the user provides a file and heading:

* Use Read to confirm the heading exists in the file
* Use Edit to insert a one-sentence intro (describing what the diagram shows in
  context) immediately followed by the Mermaid code block, placed after the
  specified heading

### Step 7: Offer to iterate

Ask:
> "Any changes to the diagram, or are we done?"

If the user requests changes, apply them and return to Step 5. Repeat until the
user confirms they're done.
