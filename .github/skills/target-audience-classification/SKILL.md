---
name: target-audience-classification
description: Identify key target audiences for a given content piece based on the actual content of the piece, not just the topic. This is used to inform content design and ensure the right audiences are addressed.
---

# Target audience classification rules

This assistant must follow a step-by-step flow to classify and identify the target audiences for a given content piece.
After each step, the user must explicitly confirm before proceeding to the next step.
Do not move forward without confirmation.

## Step 1 — collect taxonomy and current audience

### Objective

Two pieces of information are needed before classifying:

* The full taxonomy of available target audiences, sourced from `metadata.yaml`. This is the only valid source for which audiences exist.
* The file's current `audience` values (if any), read from its front-matter. These are used in Step 2 as a prior, not as part of the taxonomy.

The taxonomy and the prior must come from different sources. Never use the file's front-matter as the taxonomy.

### Instructions

1. Analyze the @metadata.yaml file, and extract the values from the `audience` field.
    * List each target audience identified — this is the taxonomy.
    * Proceed to the next step without user confirmation, as this is just an information collection step.
1. Read the provided file's front-matter and note the current `audience` values, if any.
    * These are used as a prior in Step 2 — they reflect a previous classification of this content.
    * If the field is missing or empty, that's a cold start.
1. Stop immediately if any of the following occurs:
    * Unable to find the `metadata.yaml` file
    * The `audience` field is missing from `metadata.yaml`
    * Duplicated values exist in the `metadata.yaml` `audience` list

### Output requirements

* Present a clear, structured summary of the taxonomy from `metadata.yaml`.
* List the file's current `audience` values explicitly — these will be used as a prior in Step 2 — or state that the file has no existing `audience` field (cold start).

## Step 2 — classification

### Objective

Identify all relevant target audiences for the provided file.
Be thorough and comprehensive in the analysis of the content, and identify all relevant target audiences that apply to the content piece.

### Instructions

Analyze the content piece file, and identify the target audiences.
For YAML files, look for the related files, namely the one mentioned in the `subtitles` field, that points to a JSON file.
This JSON file is only meant to help with the classification, and should not be modified.

Before scoring, write a brief internal summary (2–3 sentences) of what the content piece is about and who it is for.
Use this summary as the anchor for all scoring decisions below.

If the file's front-matter has existing `audience` values (recorded in Step 1), treat those values as a prior judgment about this content. They reflect a previous classification — by an earlier run or a human edit — and should anchor your scoring. When evaluating each target audience:

* For audiences in the existing list: lean toward confirming them. Assume the prior still holds unless your independent reading strongly disagrees or the content has materially diverged.
* For audiences not in the existing list: apply the rubric as written, with no prior bias.

In each justification, label the relationship to the prior: "agrees with prior", "partially agrees with prior", "disagrees with prior", or "no prior" when the audience was not in the existing list. This makes it visible to the reader when a score is being lifted by the prior versus standing on its own.

Then evaluate **every target audience** from the taxonomy obtained in Step 1 using the following scoring rubric:

| Score | Criteria |
| ------- | ---------- |
| 90–100% | The target audience directly and explicitly matches a primary topic, task, or audience covered in the content. Removing this target audience would misrepresent the content. |
| 75–89% | The target audience matches a secondary topic or supporting concept present in the content, but is not the main focus. |
| 50–74% | The target audience is tangentially related — the concept is mentioned or implied, but the content does not teach or address it directly. |
| 0–49% | The target audience is not present or not meaningfully addressed in the content. |

For each target audience scored at 70% or above, ground the score in evidence from the content. Cite 1–3 verbatim passages — one short sentence or phrase each — that support the score. When direct quotes are sparse (short content, transcripts, code-heavy pages), structural observations are valid evidence: "the content covers REST API endpoints under an Architects section", "the page is a step-by-step deployment guide aimed at platform administrators". For scores below 70%, evidence is not required; a brief statement of why is enough.

This evidence anchors the score to specific content, which reduces run-to-run variance, and creates an audit trail a reviewer can verify.

### Output

Present to the user:

* The content summary written above
* For each target audience in the taxonomy, an evaluation block containing:
    * The target audience name and its score
    * The relationship to the prior: "agrees with prior", "partially agrees with prior", "disagrees with prior", or "no prior"
    * Evidence — for scores 70% or above, 1–3 verbatim quotes from the content (or structural observations when quotes are sparse); for scores below 70%, a brief statement of why
* A final recommended list of target audiences, built using the rules below
* Sort the final list by relevance score, highest first
* All recommended target audiences must be part of the taxonomy obtained in Step 1

#### Building the recommended list

The rules depend on whether the file already has existing `audience` values. This asymmetry, called hysteresis, prevents borderline scores from causing the classification to flip across runs.

If the file does **not** have existing `audience` values (cold start):

* Include every target audience that scored 85% or above.

If the file **has** existing `audience` values (update with hysteresis):

* Keep an existing target audience in the list if it scores 70% or above.
* Add a target audience that is not in the existing list only if it scores 90% or above.
* Target audiences not in the existing list with scores between 70% and 89% are **not** added — this dead zone is intentional and absorbs run-to-run score variance.

If existing `audience` values were found in the file, compare the recommended list against them:

* The lists are equivalent if they contain the same audiences, regardless of order. Differences in ordering alone are not a reason to update.
* If the lists are equivalent, inform the user that the existing classification is still valid and no update is needed. **Stop the skill here** — do not proceed to Step 3.
* Only proceed to Step 3 if the recommended list differs meaningfully from the existing values (different audiences, additions, or removals).

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

* If the user selects **Yes**, proceed to Step 3.
* If the user selects **No**, ask the user for their feedback, incorporate it into the recommended list, and re-present for confirmation. Repeat until the user approves.

The assistant **must wait for explicit user confirmation** before continuing.

## Step 3 — update content piece

### Objective

Identify where the front-matter section of the content piece is located in the provided file.
Update the front-matter content, and the front-matter content only.
If the `audience` key already exists in the front-matter, update its child values.
If the `audience` key does not exist in the front-matter, add it with the list of target audiences obtained in the previous step.
Only add target audiences that were identified above the threshold.
Sort the tags alphabetically before writing them to the file.
Do not delete any line from the file, with the exception of values from  the `audience` key if needed.

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
