---
name: coverage-type-classification
description: Identify the coverage types for a given content piece based on Bloom's taxonomy. This is used to inform content design and ensure proper coverage measurement.
---

# Coverage type classification

This assistant must follow a step-by-step flow to classify the coverage types for a given content piece.
After each step, the user must explicitly confirm before proceeding to the next step.
Do not move forward without confirmation.

## Coverage type definitions

The five coverage types map to Bloom's taxonomy cognitive processes:

| Coverage Type | Primary Goal | Typical Content Types |
| --- | --- | --- |
| `remember` | Aid in recall of key terms, concepts, or component relationships. | Reference |
| `understand` | Explain a concept, an architecture, or the theory behind a feature. | Conceptual |
| `apply` | Demonstrate how to perform a task or outline the necessary steps to take. | Process, Procedure, Tutorial, Demo, Exercise |
| `evaluate` | Help the user compare options, understand trade-offs, or judge suitability. | Best practice |
| `unblock` | Show the user what went wrong, where to look, or what a solution looks like. | Troubleshooting, Error/warning docs |

## Step 1 — read the content piece

### Objective

Understand the content of the provided file so you can classify it accurately.

### Instructions

1. Read the provided file.
    * If the file is a `.yaml` file and contains a `subtitles` field, also read the file referenced by that field (a JSON file with the transcript or subtitles). Use this as the primary source for understanding the content. The JSON file is read-only — do not modify it.
    * If the file is a `.md` file, read the full content between the front-matter delimiters and the body text.
    * Note whether a `coverage-type` field already exists in the front-matter, and if so, its current values.
    * Note the `audience` field from the front-matter if present — audience can influence which coverage types apply.
    * Proceed to the next step without user confirmation, as this is just an information collection step.
1. Follow links to directly referenced files (one hop only) to gather additional context.
    * Identify all files explicitly referenced in the content or front-matter (for example, linked Markdown files, included fragments, or referenced resources).
    * Read each reachable linked file for context. Do not follow links found inside those files.
    * All linked files are read-only — do not modify them.
1. Stop immediately if any of the following occurs:
    * The file cannot be found or read.
    * The file has no identifiable front-matter or content.
    * The file is `metadata.yaml` — this file is read-only and must never be modified by this skill.

### Output requirements

* Present a brief summary confirming which file was read, which linked files were read for context, and whether a `coverage-type` field already exists.

## Step 2 — classification

### Objective

Identify all coverage types that apply to the provided file based on its content and purpose.

### Instructions

Before scoring, write a brief summary (2–3 sentences) of what the content piece is about and what cognitive goal it serves for the reader.
Use this summary as the anchor for all scoring decisions below.

If an `audience` value was found in Step 1, use it as a guide to validate that the scores are sound. The audience does not restrict which coverage types are valid, but it should inform your confidence in each score. Use the following as a reference:

* `apply` and `unblock` are most common for Test Engineers, UI Designers, and Business Analysts.
* `understand` and `evaluate` are most common for Architects, Tech Leads, and Full-Stack Developers.
* `remember` applies broadly to all developer audiences.
* `apply` and `unblock` also apply to Mobile, Frontend, and Backend Developers for hands-on content.

If the audience strongly points away from a coverage type you are about to include, treat that as a signal to re-examine the justification — not as a rule to exclude it outright.

Then evaluate **every coverage type** from the definitions above against the following scoring rubric:

| Score | Criteria |
| ------- | ---------- |
| 90–100% | The content directly and primarily serves this cognitive goal. Removing this coverage type would misrepresent the content's purpose. |
| 85–89% | The content partially serves this cognitive goal as a meaningful secondary purpose. |
| 75–84% | The coverage type is present as a minor secondary element — not substantial enough to classify the content. |
| 50–74% | The coverage type is tangentially related — the content touches on this goal but it is not a primary or secondary purpose. |
| 0–49% | The coverage type does not apply to this content. |

### Output

Present to the user:

* The content summary written above
* The full evaluation table with every coverage type, its score, and a one-line justification based on the content
* A final recommended list of coverage types, limited to those that scored above 85%
* Include a maximum of 3 coverage types — if more than 3 exceed the threshold, keep only the 3 with the highest scores
* Sort the final list by Bloom's taxonomy progression: `remember`, `understand`, `apply`, `evaluate`, `unblock`
* All recommended coverage types must come from the five defined types: `remember`, `understand`, `apply`, `evaluate`, `unblock`

If a `coverage-type` field already existed in the file, compare the recommended list against the existing values:

* The lists are equivalent if they contain the same coverage types, regardless of order. Differences in ordering alone are not a reason to update.
* If the lists are equivalent, inform the user that the existing classification is still valid and no update is needed. **Stop the skill here** — do not proceed to Step 3.
* Only proceed to Step 3 if the recommended list differs meaningfully from the existing values (different types, additions, or removals).

After presenting the results, proceed automatically to Step 3.

## Step 3 — sibling validation

### Objective

Use sibling files — files that share the same identifier but target a different platform — to validate coverage types and improve consistency across platform variants.

### Instructions

1. Read the front-matter of the current file and determine which identifier key is present: `kp-guid` or `guid`. Use whichever is present.
    * If neither is present, skip this entire step and proceed to the confirmation below.
1. Search the repository for other Markdown or YAML files that contain the same key and value, and are not the current file. Exclude any file where the `locale` field is present in the front-matter and does not start with `en`.
    * If no sibling files are found, skip the remaining instructions in this step and proceed to the confirmation below.
1. For each coverage type in the current file's recommended list:
    * If the coverage type scored 90% or above, keep it regardless of whether it appears in sibling files.
    * If the coverage type scored below 90%, check whether it appears in the `coverage-type` field of any sibling file. If it does not appear in any sibling file, remove it from the recommended list.

### Output

* State which identifier key was used and how many sibling files were found, or that none were found.
* For each removed coverage type, explain why: low score (below 90%) and absent from all sibling files.
* Present the final, validated recommended coverage type list.

### Confirmation

After presenting the results, explicitly ask for a confirmation.

Prompt the user for confirmation using buttons (instead of freeform input), use the `vscode_askQuestions` tool with the following pattern:

```json
{
    "header": "Confirm action",
    "question": "Do you want to proceed?",
    "options": [
        { "label": "Yes" },
        { "label": "No" }
    ],
    "allowFreeformInput": false
}
```

This shows Yes/No buttons for user selection.

* If the user selects **Yes**, proceed to Step 4.
* If the user selects **No**, ask the user for their feedback, incorporate it into the recommended list, and re-present for confirmation. Repeat until the user approves.

The assistant **must wait for explicit user confirmation** before continuing.

## Step 4 — update content piece

### Objective

Update the `coverage-type` field in the front-matter of the provided file.

### Instructions

Before writing, construct the new file content by taking the exact original file content read in Step 1 and only replacing the `coverage-type` block. Do not regenerate or rewrite the file from memory.

#### For `.yaml` files

The entire file is a front-matter block (no `---` delimiters). Update or add the `coverage-type` field as a top-level key.

* If `coverage-type` already exists, replace its values in place, keeping the key at its current position.
* If `coverage-type` does not exist, insert it using the following order of preference: after the `audience` field if present, otherwise before the `tags` field if present, otherwise at the end of the file.

#### For `.md` files

The front-matter is the YAML block delimited by `---` at the start of the file.

* If `coverage-type` already exists within the front-matter block, replace its values in place, keeping the key at its current position.
* If `coverage-type` does not exist, insert it using the following order of preference: after the `audience` field if present, otherwise before the `tags` field if present, otherwise on the last line before the closing `---` delimiter.

### Constraints

* Only the input file provided by the user may be modified — no other file.
* Only modify the `coverage-type` field — do not add, remove, or reorder any other line in the file.
* Write the coverage types as a YAML sequence (list), one item per line, even if there is only one value.
* Do not touch the `---` delimiters in `.md` files.

### Post-write validation

After writing the file, re-read it and perform the following checks in order:

1. Locate the `coverage-type` field in the file.
1. Verify its values match the approved list exactly — same types, no additions or omissions.
1. Verify the values are written as a YAML sequence, one item per line.
1. Verify that every other line in the file is identical to the original — no other field was added, removed, or modified.
1. If any check fails, rewrite only the `coverage-type` field to correct it, then re-read the file and repeat all checks.
1. Once all checks pass, inform the user the file was updated successfully.

## Global constraints

* Never skip steps
* Never assume approval, always use buttons to confirm with the user
* Always reference the current step explicitly
* Ask clarifying questions if required inputs are missing

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
