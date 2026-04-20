---
name: tags-classification
description: Identify key tags for a given content piece based on the actual content of the piece, not just the topic. This is used to inform content design and ensure the right audiences are addressed.
---

# Tags classification rules

This assistant must follow a step-by-step flow to classify and identify the tags for a given content piece.
After each step, the user must explicitly confirm before proceeding to the next step.
Do not move forward without confirmation.

## Step 1 — collect current list of tags

### Objective

Gather the complete list of available tags from the `metadata.yaml` file.
This is the taxonomy used to classify content pieces, and is the only valid source of tags for this skill.
Do not read tags from the front-matter of the content piece.

### Instructions

1. Analyze the @metadata.yaml file, and extract the values from the `tags` field.
    * List each tag identified
    * Proceed to the next step without user confirmation, as this is just an information collection step.
1. Stop immediately if any of the following occurs:
    * Unable to find the file
    * The `tags` field is missing
    * Duplicated values exist in the `tags` list

### Output requirements

* Present a clear, structured summary of the tags identified.

## Step 2 — classification

### Objective

Identify all relevant tags for the provided file.
Be thorough and comprehensive in the analysis of the content, and identify all relevant tags that apply to the content piece.

### Instructions

Analyze the content piece file, and identify the tags.
For YAML files, look for the related files, namely the one mentioned in the `subtitles` field, that points to a JSON file.
This JSON file is only meant to help with the classification, and should not be modified.

Before scoring, write a brief internal summary (2–3 sentences) of what the content piece is about and who it is for.
Use this summary as the anchor for all scoring decisions below.

Then evaluate **every tag** from the list obtained in Step 1 against the following scoring rubric:

| Score | Criteria |
| ------- | ---------- |
| 90–100% | The tag directly and explicitly matches a primary topic, task, or audience covered in the content. Removing this tag would misrepresent the content. |
| 75–89% | The tag matches a secondary topic or supporting concept present in the content, but is not the main focus. |
| 50–74% | The tag is tangentially related — the concept is mentioned or implied, but the content does not teach or address it directly. |
| 0–49% | The tag is not present or not meaningfully addressed in the content. |

### Output

Present to the user:

* The full evaluation table with every tag from Step 1, its score, and a one-line justification based on the content
* A final recommended list of tags, sorted by relevance score (highest first), limited to tags that scored above 85%
* Include a maximum of 7 tags — if more than 7 tags exceed the threshold, keep only the 7 with the highest scores
* All tags suggested must be part of the list obtained in Step 1

After presenting the results, proceed automatically to Step 3.

## Step 3 — sibling validation

### Objective

Use sibling files — files that share the same identifier but target a different platform — to validate tags and improve consistency across platform variants.

### Instructions

1. Read the front-matter of the current file and determine which identifier key is present: `kp-guid` or `guid`. Use whichever is present.
    * If neither is present, skip this entire step and proceed to the confirmation below.
1. Search the repository for other Markdown or YAML files that contain the same key and value, and are not the current file. Exclude any file where the `locale` field is present in the front-matter and does not start with `en`.
    * If no sibling files are found, skip the remaining instructions in this step and proceed to the confirmation below.
1. For each tag in the current file's recommended list:
    * If the tag scored 90% or above, keep it regardless of whether it appears in sibling files.
    * If the tag scored below 90%, check whether it appears in the `tags` field of any sibling file. If it does not appear in any sibling file, remove it from the recommended list.

### Output

* State which identifier key was used and how many sibling files were found, or that none were found.
* For each removed tag, explain why: low score (below 90%) and absent from all sibling files.
* Present the final, validated recommended tag list.

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
If the `tags` key already exists in the front-matter, update its child values.
If the `tags` key does not exist in the front-matter, add it with the list of tags obtained in the previous step.
Only add tags that were identified above the threshold, up to a maximum of 7 tags.
Sort the tags alphabetically before writing them to the file.
Do not delete any line from the file, with the exception of values from  the `tags` key if needed.

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
