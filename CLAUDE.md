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

### Punctuation

Do not use em dashes (`—`) or en dashes (`–`) in prose. Em dashes break reading rhythm, render inconsistently, fragment under localization, and read as an LLM stylistic tic. Replace per use case:

* Parenthetical aside: use commas if the aside belongs in the sentence; split into a new sentence if it deserves its own space; delete if it does not earn the space.
* Appositive defining a noun: use commas.
* End-of-sentence amplification: new sentence.
* List preamble: colon.
* Range or span: "to" or a hyphen.
* Compound modifier: hyphen.
* Definition: choose the appropriate form based on context (refer to the definition options below).

For definitions, choose one of the following forms instead of an em dash:

* **Section**: use when the definition is substantial and likely to be referenced directly from another document.
* **Definition list**: use when you have multiple terms to define and they are grouped together, introduced by a lead-in sentence. Ensure your Markdown renderer supports definition list syntax before using it.
* **Colon** (`**Term**: definition`): use when you have only one term to define, or when the definition is very short (one or two words).
* **Sentence**: use when the term is already embedded in surrounding prose, or when definitions are interspersed with other content. Integrate the definition naturally rather than breaking the flow.

Avoid parentheses for hedged content. If the parenthetical matters, integrate it into the sentence; if it does not, remove it. Keep parentheses only for functional uses: acronym expansions on first mention (for example, "Progressive Web App (PWA)"), and Markdown link syntax `[text](url)`.

If a sentence resists rewriting without an em dash or a parenthetical hedge, the sentence is too long. Split it.

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

## Training-internal overrides

The following rules override the shared guidance above for this repository only.

### No HTML div callouts

Do not use `<div class="info">` or `<div class="warning">` callout blocks. The `attach-pdf` build tool used in this repo does not support HTML elements and fails with an "Unsupported HTML element found in attach-pdf" error.

Use inline bold prefixes instead:

* For informational notes: `**Note:** Your note text here.`
* For bad-practice warnings: `**Bad practice:** Your warning text here.`
* For key distinctions: `**Key distinction:** Your explanation here.`

## Shared files

This `CLAUDE.md` and all skills (Claude Code slash commands) are authored and
maintained in the `docs-validation` repository and synced to all other
documentation repositories. Always edit them in the 'docs-validation`. If unsure where to make the edit, ask the user.
