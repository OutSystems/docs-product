# Documentation structure rules

Use these rules when writing or reviewing documentation in this repository.

## Put critical information first

* Put the most important information first in a paragraph.
* Do not hide the key point at the end. Readers scan.

## Headings

Follow these hierarchy and formatting rules for headings:

* **Hierarchy**:
    * Use heading levels to show the relationship of ideas.
    * Do not skip levels (for example, do not go from `#` to `###`).
    * Limit headings to three levels (`#`, `##`, `###`) unless a template requires more.
* **Format**:
    * Use sentence case for headings and titles (capitalize the first word).
    * Do not use numbers in headings to indicate sequence.
    * Do not put links in headings.

## Paragraphs

* Break up long paragraphs to improve scannability.
* A paragraph longer than 5–6 sentences often contains too much information.
* Keep each paragraph focused on one idea.

## Lists

Use lists to make content easier to scan.

### Choose the right list type

* **Numbered lists**: Use when sequence matters (steps, phases, priorities).
* **Bulleted lists**: Use for nonsequential options, examples, or sets.
* **Description lists (run-in headings)**: Use **bold** terms followed by descriptions to explain multiple concepts compactly.
* **Bulleted list marker**: Use `*` for unordered list bullets (do not use `-`).

### Introduce lists

* Precede a list with an introductory sentence in most cases.
* End the introductory sentence with:
    * A colon if the list follows immediately.
    * A period if there is intervening material (such as a note paragraph).

## Procedures

Write procedures as step-by-step instructions.

### Procedure title

* Start with an active verb (for example, "Set up OpenTelemetry Collector").
* Avoid gerunds.

### Procedure introduction

Start every procedure with context:

* Explain what the task is and what the user achieves.
* Optionally explain when and why the user performs the task.
* Identify the intended audience when helpful.

### Prerequisites

List prerequisites near the top:

* Tools, permissions, or prior steps.
* Keep prerequisites clear and concise.

### Steps

* Use a lead-in sentence such as "To do this task, follow these steps:".
* Keep to 7–10 steps. If you need more, split into multiple procedures.
* Each step should describe a single action.
* Do not explain concepts inside steps. Link to concepts instead.
* When describing UI actions, include the why, where, and what:
    * **Why** (optional): purpose of the step.
    * **Where**: location or context in the UI.
    * **What**: the action the user takes.

### After the steps

* Add a short summary that recaps outcomes.
* Put optional links in a **Related resources** section at the end.

## High-level process documents

Use process documents for end-to-end guidance that is not step-by-step.

* **Title**: Start with a verb in the gerund form (for example, "Streaming log data").
* **Content**:
    * Focus on _what_ and _why_, not detailed UI steps.
    * Use diagrams when they clarify the flow.
    * Link to detailed procedures in a **Next steps** section.

## Overview documents

Use overview documents for a birds-eye view of a capability.

* **Title**: Use a specific noun or phrase (avoid generic "Introduction" or "Overview").
* **Content**:
    * Describe the capability and intended audience.
    * List the top 3 benefits from the user's point of view.
    * Provide real-world use cases.
    * Optionally describe how it works at a high level (diagram, components, workflow).
    * Optionally list restrictions or limitations.

## Concept documents

Use concept documents to explain background knowledge and principles.

* **Title**: Use a noun (for example, "About business processes").
* **Content**:
    * Define the concept clearly and its scope.
    * Include who/what/where/when/why/how when relevant.
    * Use diagrams if they clarify system fit or relationships.
    * Include common use cases.

## Reference documents

Use reference documents for feature-specific settings and configurations.

* Provide a short introduction, then a table or list.
* Typical table columns: Setting, Description, Considerations (or Default value).

## Troubleshooting articles

Use troubleshooting articles to help users resolve specific errors or issues.

* **Title**: Use the error message or symptom (for example, "ORA-01000: maximum open cursors exceeded").
* **Structure**:
    * Symptoms (what the user sees).
    * Causes (order from easiest to confirm to most complex).
    * Resolution (steps per cause).
