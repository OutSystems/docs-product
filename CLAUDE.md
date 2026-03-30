# Claude Code guidance

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

This `CLAUDE.md` is shared across multiple documentation repositories in this workspace. Repo-specific details (content roots, frontmatter schema, build toolchain, and workflow names) can vary. When unsure, check the repo’s source-of-truth configuration files (for example, `.github/`, `toc.yml`, and `config.yml`) and follow existing patterns in nearby content.

## Repository overview

These repositories are OutSystems documentation-first codebases. Most changes are Markdown content, images, and configuration for building, validating, and publishing documentation. Some repositories also include scripts and tooling that support those workflows.

## Repository structure

Look for the files and folders that define content roots, navigation, and validations. Common patterns include:

* `README.md` — Project-specific instructions (if present)
* `toc.yml` — Table of contents / navigation (if present)
* `config.yml` (or equivalent) — Build configuration such as input/output folders (if present)
* `src/` (or equivalent) — Markdown source content (if present)
* `src/shared/` (or equivalent) — Reusable content fragments included into other docs (if present)
* `images/` subfolders — Screenshots and diagrams referenced by pages (if present)
* `.github/workflows/` — CI validations and build steps
* `.github/doc-styles/` and `.github/copilot-instructions.md` — Writing and formatting rules
* `styles/` — Vale linting styles (if present)
* `scripts/` — Custom lint rules or helpers (if present)

## Frontmatter format

Many Markdown pages start with YAML frontmatter. The exact required fields and allowed values are enforced by CI and can vary by repository.

Treat the schema as authoritative (commonly `.github/workflows/frontmatter.json`, if present) and copy frontmatter from a similar page in the same repo/section.

When editing or creating pages:

* Copy frontmatter from a similar page.
* Don’t invent enum values—reuse values already used in the repo or listed in the schema.
* If the frontmatter contains a unique identifier (for example, `guid`), leave the new value empty when creating a new page and don’t reuse an existing one.

## Style guide (source of truth)

When writing or reviewing docs, follow the rules in:

* `.github/doc-styles/formatting.md` — Markdown conventions, emphasis, UI elements, placeholders, admonitions
* `.github/doc-styles/tone.md` — Voice, language, capitalization, product names
* `.github/doc-styles/structure.md` — Headings, paragraphs, lists, procedures, document types
* `.github/doc-styles/visual-assets.md` — Mermaid diagram rules, color palette, visual audit workflow (only when working on diagrams or visual assets)

Key rules:

* Always add an introductory sentence between a heading and a list.
* Use `*` for bullet lists (not `-`), indent nested lists by 4 spaces
* Ordered lists: prefix every item with `1.`
* ATX-style headings (`#`), sentence case, no skipping levels
* Bold for UI elements and property names; `inline code` for user-typed values
* Do not use italic for emphasis (bold only); underscore `_` is the configured emphasis marker
* Use "refer to" (not "see") for cross-references
* American English, present tense, active voice, contractions allowed
* Avoid modal verbs (can, may, should, etc.) when possible
* Use second person ("you") to address the reader.
* Avoid filler politeness ("please", "sorry") and time-based words ("new", "now", "currently")
* Use serial comma in lists of three or more items
* File/folder names: lowercase, hyphens only (no spaces or underscores)
* Image names include a source suffix: `-ss` (Service Studio), `-odcs` (ODC Studio), `-pl` (ODC Portal), `-lt` (LifeTime), `-sc` (Service Center), `-usr` (Users), `-fg` (Forge)
* Placeholders:
    * Uppercase with underscore delimiters, wrapped in backticks only: `PLACEHOLDER_NAME`
    * For a single placeholder, use: "Replace `PLACEHOLDER_NAME` with ..."
    * For two or more placeholders, follow the command with a list introduced by "Replace the following:", listed in order of appearance
    * Inside code fences, formatting (bold/italic) cannot be applied
    * Don't use possessive adjectives (MY_, YOUR_) in placeholders
    * Don't use x or xx as placeholders unless it's a standard convention (e.g. HTTP status codes)
    * Explain each placeholder the first time you use it
* No hard line breaks mid-paragraph — use soft-wrap at 80 columns

Callouts use HTML divs with blank lines inside:

```html
<div class="warning" markdown="1">

Warning text here.

</div>
```

Use `class="info"` for informational callouts.

Product names: follow capitalization and naming in `.github/doc-styles/tone.md`.

## Linting

### Vale (prose linting)

Configuration is typically in `.vale.ini` (if present). Run locally with:

```
vale src/path/to/file.md
```

### Markdownlint

Configuration is typically in `.markdownlint.json` (if present). Custom rules may live in `scripts/` (if present). Key settings:

* `ul-style`: asterisk
* `ul-indent`: 4 spaces
* `ol-prefix`: "one" (all items use `1.`)
* `emphasis-style`: underscore
* `no-inline-html`: disabled (inline HTML is allowed for div, br, table elements and nested strong/b/a/sup/code within td/th)
* `line-length`: disabled
* `no-duplicate-heading`: siblings only

Rules that cause CI failure may be listed in `markdownlint_fail.json` (if present).

## CI workflows

Validations run on PRs via `.github/workflows/`. Workflow names and checks vary by repository, but commonly include:

* `validations.yml` — Shared docs validation (markdownlint, vale, etc.)
* `validate-frontmatter.yml` — Frontmatter schema validation against `.github/workflows/frontmatter.json`
* `validate-toc.yml` — TOC structure validation
* `build.yml` — Documentation build
* `visual-assets-validate.yml` / `visual-assets-pr.yml` — Image/diagram validation

## Editor settings

* Indent with 4 spaces (configured in `.editorconfig`)
* UTF-8 encoding
* Insert final newline
* Soft-wrap at 80 columns (no hard line breaks in paragraphs)
