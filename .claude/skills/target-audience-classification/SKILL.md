---
name: target-audience-classification
description: Identify key target audiences for a given content piece based on the actual content of the piece, not just the topic. This is used to inform content design and ensure the right audiences are addressed.
---

# Target audience classification rules

This assistant must follow a step-by-step flow to classify and identify the target audiences for a given content piece.
After each step, the user must explicitly confirm before proceeding to the next step.
Do not move forward without confirmation.

## Step 1 — collect current list of target audiences

### Objective

Gather the complete list of available target audiences from the `metadata.yaml` file.
This is the taxonomy used to classify content pieces, and is the only valid source of target audiences for this skill.
Do not read target audiences from the front-matter of the content piece.

### Instructions

1. Analyze the @metadata.yaml file, and extract the values from the `audience` field.
    * List each target audience identified
    * Proceed to the next step without user confirmation, as this is just an information collection step.
1. Stop immediately if any of the following occurs:
    * Unable to find the file
    * The `audience` field is missing
    * Duplicated values exist in the `audience` list

### Output requirements

* Present a clear, structured summary of the target audiences identified.

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

Then evaluate **every target audience** from the list obtained in Step 1 against the following scoring rubric:

| Score | Criteria |
| ------- | ---------- |
| 90–100% | The target audience directly and explicitly matches a primary topic, task, or audience covered in the content. Removing this target audience would misrepresent the content. |
| 75–89% | The target audience matches a secondary topic or supporting concept present in the content, but is not the main focus. |
| 50–74% | The target audience is tangentially related — the concept is mentioned or implied, but the content does not teach or address it directly. |
| 0–49% | The target audience is not present or not meaningfully addressed in the content. |

### Output

Present to the user:

* The full evaluation table with every target audience from Step 1, its score, and a one-line justification based on the content
* A final recommended list of target audiences, sorted by relevance score (highest first), limited to target audiences that scored above 85%
* All target audiences suggested must be part of the list obtained in Step 1

After presenting the results, proceed automatically to Step 3.

## Step 3 - Sibling validation

### Objective

Use sibling files — files that share the same identifier but target a different platform — to validate target audiences and improve consistency across platform variants.

### Instructions

1. Read the front-matter of the current file and determine which identifier key is present: `kp-guid` or `guid`. Use whichever is present.
    * If neither is present, skip this entire step and proceed to the confirmation below.
1. Search the repository for other Markdown or YAML files that contain the same key and value, and are not the current file. Exclude any file where the `locale` field is present in the front-matter and does not start with `en`.
    * If no sibling files are found, skip the remaining instructions in this step and proceed to the confirmation below.
1. For each target audience in the current file's recommended list:
    * If the target audience scored 90% or above, keep it regardless of whether it appears in sibling files.
    * If the target audience scored below 90%, check whether it appears in the `audience` field of any sibling file. If it does not appear in any sibling file, remove it from the recommended list.

### Output

* State which identifier key was used and how many sibling files were found, or that none were found.
* For each removed target audience, explain why: low score (below 90%) and absent from all sibling files.
* Present the final, validated recommended target audience list.

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

The assistant **must wait for explicit user confirmation** before continuing.

## Step 4 — Update content piece

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
