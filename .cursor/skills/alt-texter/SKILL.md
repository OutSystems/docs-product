---
name: alt-texter
description: "Review the images in a single Markdown file, flagging missing or placeholder alt text and stale titles, and proposing accurate alt text and a matching short title drawn from surrounding context (headings, body text, procedure steps), only opening the image itself as a last resort when that context is too thin. Skips Marp slide decks entirely (front-matter contains marp: true), since there's no accessibility payoff to reviewing them. Updates existing alt text and titles only when they are missing, a placeholder, stale, or demonstrably wrong, never for stylistic rewording."
---

# Alt text review rules

This assistant must follow a step-by-step flow to review and, where needed, update the alt text and title of images in a single Markdown file.
Use Step 1 and Step 2 as information-collection and proposal steps. Only Step 3 requires explicit user confirmation before Step 4.
Do not move forward without confirmation.

Good alt text gives someone who can't see the image the same information a sighted reader gets from it. This skill drafts that description from the surrounding Markdown content first: the text around an image is usually enough to describe it, and opening the image is unnecessary cost. Opening the image itself is a last resort, used only when the surrounding text genuinely isn't enough (see Step 2).

This skill only reviews general documents: standard `![alt text](path)` or `![alt text](path "Title")` syntax, where both the alt text and the optional title are real, human-readable descriptions that get rendered (and are accessible to screen readers) wherever the page is published.

It does **not** review Marp slide decks (front-matter contains `marp: true`): there's no accessibility payoff to reviewing them. Detect this up front and stop before doing any per-image work.

## Step 1 — read the file and collect every image

### Objective

Read the target file, confirm it's in scope, and build a complete inventory of its images.

### Instructions

1. Identify the target file from the user's input. If no file path was provided, ask for one.
1. Stop immediately if any of the following occurs:
    * The file cannot be found or read.
    * The file path is inside the `translated/` folder — this skill never touches translated content.
    * The front-matter contains `marp: true`. Say this is a Marp slide deck out of scope for this skill, and stop without reading the rest of the file for images.
    * The file contains no Markdown images (`![...](...)`).
1. Read the full file.
1. For each image, extract:
    * The alt bracket content (the text between `![` and `]`).
    * The path.
    * The optional title, if the image uses `![alt](path "Title")` or `![alt](path 'Title')` syntax.
1. Classify each image's alt bracket content:
    * **Missing** — the bracket is empty (`![]`), whitespace-only, or is a placeholder value with no real description. Treat the following as placeholders (case-insensitive, exact match after trimming): `alt text`, `image`, `screenshot`, `todo`, `placeholder`, `tbd`. Also treat bracket content as missing if it consists solely of digits, punctuation, or a single character, as these carry no descriptive value. Editors commonly insert `alt text` by default, and it is left unedited far more often than not — always treat it as missing.
    * **Existing** — anything else. This is real alt text.

### Output requirements

* State the file path read.
* Present a table of every image: its path/filename, its raw alt bracket content, its title (or "none"), and its classification (missing / existing).

Proceed to Step 2 without user confirmation, since Step 1 is an information-collection step.

## Step 2 — gather context and draft proposals

### Objective

For every image classified as **missing**, and for every **existing** image whose alt text or title needs replacing (see the stability rules below), draft accurate alt text and a matching title, preferring the surrounding Markdown over opening the image.

### Instructions

1. For each image needing a proposal, gather context from:
    * The nearest preceding heading.
    * The paragraph or procedure step the image is embedded in (these documents are frequently step-by-step exercises, so the numbered step text immediately surrounding the image is usually the most specific context available).
    * The image's file name, when it is descriptive (for example `architecture-design-process.svg` hints at the subject).
1. Draft a concise, specific alt text following these rules:
    * Describe the image's content or function, not its appearance, unless the appearance itself is the point.
    * Never start with the generic "image of" or "picture of" — assistive technology already announces it's an image, so that wrapper is redundant noise. "Screenshot of", "Diagram of", or "Icon representing" are fine, and encouraged, when the image type itself is useful information (for example, telling the reader it's a real product capture rather than an illustration).
    * Don't restate text that already appears verbatim next to the image (a caption or heading); the alt text should add information, not repeat it.
    * Keep it a plain sentence or fragment, no marketing language, no trailing period required.
1. If the surrounding text provides no subject-specific noun or action that identifies what the image depicts, do not guess from text alone. For example, if the only nearby text is a generic heading like "Overview" and the filename is non-descriptive, open the image with the Read tool as a last resort and describe what it actually shows, then draft the alt text from that. Reserve this for images that would otherwise go unlabeled — it costs more than text-based context, so don't use it when the surrounding Markdown already gives a clear answer.

#### Stability rule for existing alt text

The default is to keep existing alt text as-is. Only propose a replacement for an **existing** image if one of the following failure conditions is true:

* The description is factually wrong for what the surrounding context says the image is (for example, it describes a different feature or product area).
* It's a placeholder that classification missed (generic filler with no specific content, such as "picture" or "diagram" alone).
* It's truncated, garbled, or contains leftover authoring artifacts (for example unresolved template text).

Do not propose a replacement just because a better-worded description is possible. If none of the failure conditions apply, keep the existing text and do not include that image in the alt text proposal list.

#### Title handling

A title is a short, Title Case restatement of the alt text naming the concrete subject of the image (the specific screen, dialog, button, or concept), not a truncation or a verbatim copy. Keep it short, typically 2-6 words. Capitalize each major word; keep small connector words (a, an, the, of, in, on, for, and) lowercase unless first or last. For example, alt text "Screenshot of the Service Studio environment menu with the 'Open Files...' option highlighted." pairs with the title "Service Studio Open Files Option".

Use this decision table for title handling.

| Alt text action | Title exists? | Title action |
| --- | --- | --- |
| Added or replaced | Yes or No | Draft new title |
| Kept as-is | Yes | Check staleness; replace if stale, mismatched, or generic |
| Kept as-is | No | Leave without title |

### Output requirements

Present a table with one row per image that needs action (missing images, existing images that failed the alt text stability rule, and existing images with a stale title). For each row:

* Image path/filename and the heading/section it belongs to.
* Current alt bracket content (or "none" if missing) and current title (or "none").
* Proposed new alt bracket content and proposed title (mark "unchanged" if only one of the two is being touched).
* The specific reason: missing, the stability failure condition, or "title no longer matches alt text".
* Whether the proposal was drafted from text context or required opening the image (last resort).

State the total count: images proposed (text-based vs. image-based) and images kept as-is.

If there is at least one proposal, after presenting the table, proceed to Step 3 for confirmation. If there are zero proposals (everything was kept as-is), say so and stop; there is nothing to confirm.

## Step 3 — confirmation

After presenting the results, explicitly ask for confirmation.

Prompt the user for confirmation using buttons (instead of freeform input), use the `vscode_askQuestions` tool with the following pattern:

```json
{
    "header": "Confirm action",
    "question": "Do you want to apply these alt text and title updates?",
    "options": [
        { "label": "Yes" },
        { "label": "No, let me provide feedback" }
    ],
    "allowFreeformInput": false
}
```

* If the user selects **Yes**, proceed to Step 4.
* If the user selects **No, let me provide feedback**, ask for feedback, incorporate it, and re-present the revised proposals for confirmation. Repeat until the user approves.

The assistant **must wait for explicit user confirmation** before continuing.

## Step 4 — update the file

### Objective

Apply only the approved alt text and title changes to the file, using an edit tool. This is not a summary or a preview — actually write the changes to disk before reporting completion.

### Instructions

1. Immediately after the user confirms, edit the file. Do not stop after Step 3's confirmation to restate the plan or wait for a separate "go ahead" — the "Yes" answer is the go-ahead.
1. For each approved image, replace the content between `![` and `]` with the approved bracket content.
1. For each approved title change:
    * If a title already exists in parentheses, replace only the quoted string, keeping its existing quote style (single or double).
    * If no title exists and one is being added, append it after the path inside the parentheses using double quotes and a single leading space, matching this repository's convention: `(path "Title")`.
1. Do not touch images that were kept as-is with no title change.
1. Do not modify anything else in the file: no other line, no image path, no surrounding text, no front-matter.

### Post-write validation

If the edit tool returns an error or the post-write read-back reveals a mismatch, stop immediately, report the specific failure to the user, and do not retry without explicit user instruction.
After writing the file, read it back and confirm each approved image's bracket content and title match exactly what was approved, and that no unrelated line changed. Inform the user the file was updated successfully, restating the count of images changed.

## Global constraints

* Skip Marp slide decks entirely (front-matter contains `marp: true`) — stop at Step 1 without classifying images, gathering context, or drafting proposals.
* Prefer drafting alt text from surrounding Markdown context. Only open an image directly as a last resort, when that context is too thin to support a confident, specific description.
* Only the input file provided by the user may be modified.
* This skill only operates on one file per invocation — never scan a folder or the whole repository.
* Never operate on files under `translated/`.
* Never backfill a title onto an image whose alt text isn't otherwise being added or fixed in this same run.
* Prefer stability over perfection: an existing description that is accurate is always preferred over one that is merely better worded.
* Never skip steps.
* Never assume approval — always use buttons to confirm with the user.
* Always reference the current step explicitly.
* Ask clarifying questions if required inputs are missing.

## Markdown files front-matter boundaries

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
