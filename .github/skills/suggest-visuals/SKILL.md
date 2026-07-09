---
name: suggest-visuals
description: >-
  Analyses an existing markdown article and suggests the right visual assets —
  Mermaid diagrams or screenshots — based on coverage-type and audience frontmatter
  fields. Follows OutSystems brand guidelines. Proposes diagram placement with
  rationale and inserts accepted diagrams interactively. Recommends screenshots
  where the coverage type calls for them.

  Use when a content developer wants to audit an article for missing visuals, or
  when asked to "add diagrams", "suggest visuals", "diagram this article", or
  "add visuals to my article". For creating a standalone diagram without an article,
  use /create-diagram instead.

  Trigger phrases: "add diagrams", "diagram this article", "suggest visuals",
  "add visuals to my article".
argument-hint: <path-to-markdown-file>
allowed-tools: Read,Edit,AskUserQuestion
---

# Suggest visuals

Suggest OutSystems-brand-compliant visual assets (Mermaid diagrams or screenshots)
for a markdown article, based on its coverage-type and audience.

## Setup

Before starting, read the two companion files from the same directory as this skill:

* `visual-rules.md` — decision matrix for coverage-type × audience
* `brand-guidelines.md` — OutSystems Mermaid color and style rules

## Workflow

### Step 1: Read the article

Read the file at `$ARGUMENTS`. If no argument is provided, ask the user for the file path.

### Step 2: Parse frontmatter

Extract the following YAML frontmatter fields:

* `coverage-type`: a single value or array (e.g., `understand`, `[understand, apply]`)
* `audience`: a single value or array (e.g., `Architect`, `[Architect, Tech lead]`)

If either field is missing, inform the user and stop. Explain which field is missing
and give an example of valid values from visual-rules.md.

### Step 3: Apply visual rules

Using visual-rules.md, determine which coverage types are diagram-eligible:

* **Diagram-eligible**: `understand`, `evaluate`, `remember`
* **Screenshot-only**: `apply`, `unblock`

**If ALL coverage types are screenshot-only** (`apply` and/or `unblock` only):

* Explain that this article type is best served by screenshots, not diagrams
* Cite the specific reason from visual-rules.md (e.g., "Apply content guides users
  through UI interactions — screenshots of the steps are the right asset here")
* Stop. Do not suggest any diagrams.

**If coverage types are mixed** (e.g., `[understand, apply]`):

* Note which sections call for screenshots (Apply/Unblock portions)
* Continue to analyze only the sections that align with the diagram-eligible types

**If ALL coverage types are diagram-eligible**:

* Continue to Step 4

### Step 4: Analyze article section by section

While reading, note the **line number of the last content line** in each candidate
section — this is the insertion point for the diagram (the line immediately before
the next heading or end of file).

Walk through each H2 and H3 section heading and its content. For each section,
assess whether a diagram would materially aid comprehension:

**Good candidates for a diagram:**

* A section explaining how components relate to each other
* A section describing a multi-step process or workflow
* A section comparing two or more options or trade-offs
* A section describing data flow, API interaction, or authentication sequence
* A section introducing a hierarchy of concepts

**Poor candidates (skip these):**

* Sections that are purely procedural UI steps (these need screenshots)
* Sections with fewer than 3 relationships or steps to show
* Sections that already have a diagram

For each good candidate, pick the Mermaid diagram type from the section content
(process, interaction, hierarchy, topology, data model) using the Diagram Type
Reference in visual-rules.md. Then use the audience row in visual-rules.md to
shape the diagram's complexity and focus — which nodes to show, how abstract or
detailed to make it.

### Step 5: Generate and propose each diagram

For each identified section, present a proposal in this exact format:

---
📍 DIAGRAM SUGGESTION — [Section heading]

**Position:** Below the section text, before the next heading
**Jump to:** [filename:LINE](relative/path/from/workspace/root#LLINE)
**Rationale:** [1–2 sentences: why this diagram, what concept it clarifies, which audience need it serves]
**Diagram type:** [flowchart TD / sequenceDiagram / etc.]

---

Then ask:

> Insert this diagram into the article? Reply **yes**, **no**, or **edit** (describe the change).

* **yes** → insert immediately using the Edit tool: generate a one-sentence intro that
  describes what the diagram shows in context (e.g., "The following diagram shows how
  the authentication service interacts with the identity provider during a login flow."),
  place it on the line immediately before the Mermaid code block, then move to the next
  suggestion
* **no** → skip and move to the next suggestion
* **edit** → apply the requested change to the Mermaid code internally, then show
  **only the revised code block** in the conversation so the user can verify the change,
  and ask again

### Step 6: Final summary

After all suggestions have been processed, print a brief summary:

```
## Summary
- Diagrams inserted: N
- Diagrams skipped: N
- Screenshot recommendations: [list any sections in Apply/Unblock coverage that need
  screenshots, if applicable]
```

## Diagram styling rules

Always follow brand-guidelines.md exactly. Key rules:

* Every diagram starts with the `%%{init}%%` block from brand-guidelines.md
* Apply the correct `classDef` group for every node
* Never use gradients, shading, shadows, or 3D effects
* Sequence diagrams always use `autonumber` and include `"messageFontSize": "14px"` in the init block
* Keep labels concise — node text ≤ 5 words where possible
* **Label casing**: use sentence case for all labels — capitalise the first word only; keep the rest lowercase except acronyms (such as ODC, AI, API) and proper product names (such as Amazon Bedrock, Azure OpenAI).
* Use `<br/>` for line breaks inside node labels — never `\n` (renders literally in most environments)
* **Cross-subgraph edges**: do not add text labels on arrows that cross a subgraph boundary — the label renders on the border and overlaps the container. Describe such relationships in prose instead, or use a single-word label maximum.
* **Mindmaps**: use HTML spans for hierarchical font sizes (root 20px bold, level 1 18px, level 2 16px, level 3+ 14px); set `cScale0`–`cScale4` in the init block for distinct branch colors — do NOT rely on Mermaid auto-coloring.
* **Process node shapes**: use `NodeId(Label):::process` (rounded rectangle) not `NodeId[Label]:::process` (sharp rectangle).
* **Semantic colors**: `:::start`/`:::stop` are only for workflow entry/exit points; `:::error` is only for failure outcome nodes. Use `:::process` for all component/server nodes regardless of state — show unavailability with dashed arrows (`-.->`) and a descriptive label.
* **No empty node labels**: verify every node has non-empty text before inserting.
* **Nested subgraphs for containment**: when a concept requires a containment hierarchy (e.g. Environment → Zone → Servers), **keep the nested subgraphs** — do not flatten or restructure them. Fix title visibility with two rules: (1) declare a sibling node _before_ the inner subgraph, and (2) add `direction TB` inside every nested subgraph. Without `direction TB`, Mermaid places the sibling node and the inner subgraph side-by-side horizontally even in a `flowchart TB` diagram, making both titles hard to read. See the nested subgraph section in brand-guidelines.md for the full code pattern.
* **Sequence diagram autonumber circles**: add `"labelBoxBkgColor": "#F22800"` and `"labelTextColor": "#FFFFFF"` to themeVariables — numbered circles render in OutSystems red with white text.
* **Sequence diagram notes**: add `"noteBkgColor": "#F5F6FA"`, `"noteBorderColor": "#686E76"`, and `"noteTextColor": "#0A141E"` to themeVariables — overrides Mermaid's default yellow `Note over` boxes with the OutSystems light-grey1 palette.
* **Sequence diagram `themeCSS` fallback**: include the `themeCSS` block from brand-guidelines.md's sequence recipe alongside the theme variables. Some renderers (including VS Code's Markdown preview) ignore `labelBoxBkgColor`/`noteBkgColor`; the CSS overrides win where the variables don't.
