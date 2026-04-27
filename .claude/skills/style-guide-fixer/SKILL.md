---
name: style-guide-fixer
description: Fix style guide errors on a file. Runs vale and markdownlint locally to find errors. Falls back to the PR comment marked with the sticky marker "STYLE GUIDE VALIDATION" only when the prompt explicitly instructs it. Use when asked to fix style guide errors on a file.
---

# Style guide fixer rules

This assistant fixes style guide errors on documentation files.
This is an automated skill — do not ask for user confirmation at any step.

## Step 1 — read the file and locate errors

### Objective

Read the provided files and collect all style guide errors for them.

### Instructions

1. Collect errors using the following priority order:

    **Primary — run local linters** (default, no PR required):
    * Determine which file to fix:
        * If a file path was explicitly passed with the command, use that.
        * Otherwise, use the file currently open in the IDE, available in the conversation context via the `<ide_opened_file>` tag. If no file is open, stop and ask the user to provide a file path.
    * Read the file in full.
    * Collect errors using the following sub-priority:

        **IDE diagnostics** (preferred, if available):
        * After reading the file, check whether `<ide_diagnostics>` data is present in the conversation context for this file.
        * If it is, use those diagnostics as the error source. Treat entries with severity `"Error"` as errors; ignore `"Warning"` and `"Information"` entries.

        **CLI linters** (fallback, when IDE diagnostics are absent):
        * Run `markdownlint` on the file and capture all output.
        * Run `vale` on the file and capture all output.
        * From the markdownlint output, collect only errors for rules listed in `markdownlint_fail.json`. Treat all other markdownlint findings as warnings and ignore them.
        * From the vale output, collect only findings with severity `error`. Ignore `warning` and `suggestion` findings.

    **Fallback — PR comment** (use only when the prompt explicitly says to use the PR comments):
    * Use GitHub tools to retrieve all PR comments on the pull request whose number is specified in the prompt. Find the most recent comment that contains the sticky marker `<!-- Sticky Pull Request CommentSTYLE GUIDE VALIDATION -->`.
    * If no such comment exists, stop and report that no style guide validation comment was found.
    * From the comment, extract all rows from both error tables where the `File` column matches the path of the current file and the `Severity` column is `error❌`. Ignore `warning⚠️` and `suggestion💡` rows.

1. If no errors are found for this file, stop and report that no fixable errors were found.

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
