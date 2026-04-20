---
name: summary-writer
description: Generate a short SEO summary (under 160 characters) for a given content piece and add it to the front-matter of the provided .md or .yaml file.
---

# Summary writer rules

This assistant must follow a step-by-step flow to generate and apply an SEO summary for a given content piece.
After each step, the user must explicitly confirm before proceeding to the next step.
Do not move forward without confirmation.

## Step 1 — read the content piece

### Objective

Understand the content of the provided file so you can generate an accurate summary.

### Instructions

1. Read the provided file.
    * If the file is a `.yaml` file and contains a `subtitles` field, also read the file referenced by that field (a JSON file with the transcript or subtitles). Use this as the primary source for understanding the content. The JSON file is read-only — do not modify it.
    * If the file is a `.md` file, read the full content between the front-matter delimiters and the body text.
    * Note whether a `summary` field already exists in the front-matter.
    * Proceed to the next step without user confirmation, as this is just an information collection step.
1. Follow links to directly referenced files (one hop only) to gather additional context.
    * Identify all files explicitly referenced in the content or front-matter (for example, linked Markdown files, included fragments, or referenced resources).
    * Read each reachable linked file for context. Do not follow links found inside those files.
    * All linked files are read-only — do not modify them.
    * Use the context gathered from linked files only to inform the summary for the current file. Do not summarize the linked files themselves.
1. Stop immediately if any of the following occurs:
    * The file cannot be found or read.
    * The file has no identifiable front-matter or content.
    * The file is `metadata.yaml` — this file is read-only and must never be modified by this skill.

### Output requirements

* Present a brief summary confirming which file was read, which linked files were read for context, and whether a `summary` field already exists.

## Step 2 — evaluate existing summary

### Objective

Determine whether the existing `summary` value needs to be replaced. The default is to keep the existing summary. Only proceed to regeneration if there is a clear, specific reason the existing summary is wrong or misleading — not because a better one could theoretically be written.

### Instructions

1. If no `summary` field was found in Step 1, skip this step and proceed directly to Step 3.
1. If a `summary` field exists, check whether any of the following failure conditions are true:
    * It describes something the content does not actually cover.
    * The main topic or technology is wrong or absent (for example, the summary mentions O11 but the content is about ODC).
    * It is so generic that it could apply word-for-word to a completely different content piece in this repository.
1. If none of the failure conditions are true, the existing summary is sufficient.
    * Inform the user that the existing summary is still valid and no update is needed.
    * Present the existing summary text.
    * **Stop the skill here** — do not proceed to Step 3.
1. If at least one failure condition is true, proceed to Step 3 without user confirmation.
    * Briefly state which specific failure condition was triggered and why.
    * Do not proceed on the grounds that the summary could be improved or better worded — only on a clear failure.

### Output requirements

* Present the existing summary and — if proceeding — the specific failure condition that was triggered.

## Step 3 — generate summary

### Objective

Write a short, accurate SEO summary for the content piece.

### Instructions

1. Identify the primary keyword or key phrase for this content piece — the specific term a user would type into a search engine to find it. This is typically the most specific combination of product name, feature, and action (for example, "ODC SQL query", "OutSystems aggregate filter", "PWA distribution ODC").
1. Identify the search intent this content satisfies:
    * **How-to / procedural** — the user wants to accomplish a specific task. Use action-oriented language that mirrors the task (for example, "Set up...", "Build...", "Configure...").
    * **Conceptual / understand** — the user wants to understand a topic. Signal what concept is explained and why it matters.
    * **Reference** — the user wants a quick lookup. Signal what information is covered.
1. Write the summary following these SEO rules:
    * **Begin with the primary keyword or key phrase** — the summary must open with the primary keyword or key phrase. Do not start with a verb or filler word. Search engines bold matching terms in results, and users scan left-to-right; terms in the first 60–70 characters have the most impact.
    * **Be specific** — name the exact technology, product, feature, or concept (for example, "ODC", "OutSystems 11", "SQL node", "aggregate"). Also name at least one specific sub-topic, principle, or concept actually covered in the content — not just the general subject area. Generic language that applies to any page has no SEO value.
    * **Match the search intent** in the phrasing — procedural content should sound actionable; conceptual content should signal insight.
    * **Signal the value** the reader gets (the skill, knowledge, or outcome) without filler phrases such as "Learn how to", "Discover", "Find out", "Understand", "Leverage", or "In this video".
    * **Keep it unique** — the summary must not be reusable across other pages; if it could describe a different content piece in this repo, rewrite it to be more specific.
    * **Use active voice, present tense, and second person** ("you") where natural.
    * **Avoid modal verbs** (can, may, should, etc.) when avoidable.
    * **Do not include the title verbatim** — rephrase to add context the title alone does not provide.
    * **Stay under 150 characters** to avoid truncation in search results (160 is the absolute maximum; target 150 for safety). Count the characters before proposing.
    * Use a single sentence only.
    * **Name the platform using the canonical format**:
        * For O11 content: "OutSystems 11 (O11)"
        * For ODC content: "OutSystems Developer Cloud (ODC)"
        * For content covering both: "OutSystems platform"
    * **Avoid** the following:
        * Phrases like "this guide," "this document," "guide on," or "instructions for"
        * "Click here" or similar call-to-action anchors
        * Keyword stuffing — each keyword must appear naturally and only as many times as needed
1. Before presenting the summary to the user, verify it passes all of the following criteria:
    * Does it start with the primary keyword or key phrase (not a verb or filler word)?
    * Does it accurately reflect the main topic and scope of the content?
    * Does it mention the specific technology, feature, or concept the content covers?
    * Does it name at least one specific sub-topic, principle, or concept from the content — not just the general subject?
    * Does it avoid describing something the content does not actually cover?
    * Could it apply to a different content piece in this repository? If yes, rewrite it to be more specific.
    * If the summary fails any criterion, revise it and re-check before proceeding. Do not present a summary to the user that fails any of these checks.
1. If a `summary` already existed, compare the generated summary to the existing one before presenting anything to the user.
    * The summaries are **semantically equivalent** if a user searching for this content would be equally served by either — same primary keyword, same search intent, same core topic. Wording differences, minor rephrasing, and stylistic improvements do not make them meaningfully different.
    * When in doubt, treat the summaries as equivalent and keep the existing one.
    * If they are semantically equivalent, keep the existing summary and **stop the skill here** without prompting the user. Inform the user that the existing summary remains accurate and no update is needed.
    * Only proceed to present a new proposal if the generated summary corrects a clear failure identified in Step 2 and cannot be considered equivalent to the existing one by any reasonable interpretation.

### Output

Present to the user:

* The proposed summary text.
* Its exact character count.
* The primary keyword identified and where it appears in the summary.
* The search intent category used (how-to, conceptual, or reference).
* If a `summary` already exists, show the current value alongside the proposed replacement.

### Confirmation

After presenting the proposed summary, explicitly ask for confirmation.

Prompt the user using buttons (instead of freeform input), using the `vscode_askQuestions` tool with the following pattern:

```json
{
    "header": "Confirm action",
    "question": "Do you want to use this summary?",
    "options": [
        { "label": "Yes" },
        { "label": "No, let me provide feedback" }
    ],
    "allowFreeformInput": false
}
```

* If the user selects **Yes**, proceed to Step 4.
* If the user selects **No, let me provide feedback**, ask the user for their feedback, incorporate it, and re-present the revised summary for confirmation. Repeat until the user approves.

The assistant **must wait for explicit user confirmation** before continuing.

## Step 4 — update the front-matter

### Objective

Add or update the `summary` field in the front-matter of the provided file.

### Instructions

#### For `.yaml` files

The entire file is a front-matter block (no `---` delimiters). Update or add the `summary` field as a top-level key.

* If `summary` already exists, replace its value in place.
* If `summary` does not exist, add it as the first key in the file, before all other keys.

#### For `.md` files

The front-matter is the YAML block delimited by `---` at the start of the file.

* If `summary` already exists within the front-matter block, replace its value in place.
* If `summary` does not exist, add it as the first key after the opening `---` delimiter.

### Constraints

* Only the input file provided by the user may be modified — no other file.
* Only modify the `summary` field — do not add, remove, or reorder any other line in the file.
* Do not touch the `---` delimiters in `.md` files.
* The value must be a plain scalar string. If the summary contains a colon (`:`) or other special YAML characters, wrap the value in double quotes.

### Post-write validation

After writing the file, read it back and perform the following checks in order:

1. Locate the `summary` line in the file.
1. Check whether the written value matches the approved summary exactly.
1. Check for YAML special characters that require quoting — specifically, a colon followed by a space (`:`) anywhere in an unquoted value. Common triggers include colons after product names such as "OutSystems Developer Cloud (ODC): ...".
1. If the value is unquoted and contains any such character, the front-matter is invalid. Rewrite only the `summary` line, wrapping the entire value in double quotes, then re-read the file to confirm the fix was applied correctly.
1. After applying the quoting fix, re-validate that the corrected summary still satisfies all Step 3 rules: character count under 160, no forbidden phrases, correct platform name, and no YAML special characters left unquoted. If it fails any check, treat this as a new generation failure and restart from Step 3.
1. If the value matches the approved summary and no unquoted special characters are present, validation passes — inform the user the file was updated successfully.

## Global constraints

* **Only the input file provided by the user may be modified.** All other files read during this skill — linked files, subtitles JSON, or any other referenced file — are strictly read-only. Do not write to, create, or delete any file other than the input file.
* **`metadata.yaml` is permanently read-only** and must never be modified by this skill, even if explicitly provided as the input file.
* **Prefer stability over perfection.** The goal of this skill is to ensure a good summary exists — not to produce the ideal summary on every run. An existing summary that is accurate and specific is always preferred over a replacement that is merely better worded. When in doubt at any step, keep the existing summary.
* Never skip steps.
* Never assume approval — always use buttons to confirm with the user.
* Always reference the current step explicitly.
* Ask clarifying questions if required inputs are missing.

## Front-matter boundaries in Markdown files

The front-matter is the YAML block at the beginning of the file and is delimited by:

```markdown
---
(front-matter content)
---

# Heading

(content)
```

The first `---` marks the start of the front-matter.
The second `---` marks the end of the front-matter.

These two delimiter lines **must never be removed, modified, moved, or duplicated**.
