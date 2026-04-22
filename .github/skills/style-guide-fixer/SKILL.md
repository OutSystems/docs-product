---
name: style-guide-fixer
description: Fix style guide errors reported in the "STYLE GUIDE VALIDATION" PR comment. Reads the latest style guide validation comment and applies fixes for errors it can confidently resolve without changing content meaning, following the documentation style guidelines. Use when asked to fix style guide errors on a file.
---

# Style guide fixer rules

This assistant fixes style guide errors reported in PR validation comments.
This is an automated skill — do not ask for user confirmation at any step.

## Step 1 — read the file and locate errors

### Objective

Read the provided files and find all style guide errors reported for them in the PR comment.

### Instructions

1. Read the provided files in full.
1. Use GitHub tools to retrieve the most recent PR comment on the pull request whose number is specified in the prompt. Look for the latest comment that has the `STYLE GUIDE VALIDATION` header — it contains tables of markdownlint and Vale errors.
    * If no such comment exists, stop and report that no style guide validation comment was found.
1. From the comment, extract all rows from both error tables where:
    * The `File` column matches the path of the current file.
    * The `Severity` column is `error❌`.
    * Ignore all rows with severity `warning⚠️` or `suggestion💡`.
1. If no `error❌` rows are found for this file, stop and report that no fixable errors were found.

### Output

List the errors found for each file, grouped by tool (Markdownlint / Vale), including the line number, rule, and message for each.
Proceed automatically to Step 2 without waiting for confirmation.

## Step 2 — fix the errors

### Objective

Apply fixes to each file for all errors from Step 1 that can be resolved without changing the meaning or intent of the content.

### Fixable errors

Fix any error you can resolve with high confidence — meaning the correct fix is unambiguous and does not change the meaning or intent of the content. There is no fixed allowlist: apply your judgment based on the rule, the error message, and the context.

### Guidance on OutSystems.Headings errors

`OutSystems.Headings` enforces sentence case in headings. The rule allows a list of exceptions for legitimate proper nouns, product names, and acronyms. When you encounter a heading that triggers this rule, apply the following reasoning:

**Fix if the heading uses standard title case on ordinary words.** Convert to sentence case, preserving known proper nouns, product names, and acronyms. For example: `## Configure Your App Settings` → `## Configure your app settings`.

**Skip and flag for human review if the heading is or contains a code identifier** — a camelCase or PascalCase technical name such as `appConfigurations`, `GetCreditScore`, or `WorkflowNewCustomerLoan`. These are not a capitalization problem; the underlying heading needs to be rewritten as human-readable text, which requires understanding the content and is not safe to automate. Do not simply lowercase or reformat a technical identifier — the result would be meaningless. Do not suggest adding it to the Headings.yml exception list. Report the error as requiring human judgment.

**Skip and flag for human review if you are unsure whether a word is a proper noun** that should remain capitalized. Report it with a note that the author should verify.

Summary of decision logic:

* Ordinary title-case words → fix to sentence case.
* Technical identifiers (camelCase, PascalCase, code names) → skip, flag for human rewrite.
* Uncertain proper nouns → skip, flag for human verification.
* Never suggest adding terms to the exceptions file to bypass the rule, unless the term is a legitimate proper noun, product name, or acronym that genuinely requires capitalization.

### Constraints

* Only modify the exact lines identified in the error table.
* Do not rewrite, reword, or restructure content beyond what the specific error requires.
* Do not add, remove, or reorder sections, headings, or paragraphs.
* Do not modify front-matter fields unless an error explicitly targets one.
* Always follow the style guidelines in `.github/doc-styles/formatting.md`, `.github/doc-styles/tone.md`, and `.github/doc-styles/structure.md`.

## Step 3 — report results

### Objective

Summarize what was fixed and what was skipped.

### Instructions

1. List every error that was fixed: line number, rule, and a brief description of what changed.
1. List every error that was skipped: line number, rule, and the reason it was not fixed.
1. Do not ask for confirmation. Report results and stop.

## Global constraints

* This is a fully automated skill — never ask for confirmation.
* Never use git commands.
* Only modify the provided input file. All other files are read-only.
* Never fix errors with severity `warning⚠️` or `suggestion💡`.
* When in doubt about a fix, skip it and include it in the skipped list.
