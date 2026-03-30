# Claude Caude guidance

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository overview

This is the **OutSystems Developer Cloud (ODC)** documentation repository. It contains Markdown source files published to <https://success.outsystems.com/documentation/outsystems-developer-cloud/>. This is a docs-only repo — no application code, no package manager, no build scripts to run locally. Markdown is converted to HTML via Python Markdown with extensions (extra, meta, toc, blankline, markdown-include).

## Repository structure

* `src/eap/` — Main documentation content, organized by topic area (building-apps, deploying-apps, security, etc.). Each topic folder contains `.md` files and an `images/` subfolder for screenshots and diagrams.
* `src/error/` — Error documentation
* `src/shared/` — Shared/reusable content fragments (included into other docs via markdown-include syntax)
* `toc.yml` — Table of contents defining site navigation hierarchy. Uses `href` paths relative to `src/`. Structured with `# Comment` section headers, `- href:` entries, and nested `- topics:` arrays.
* `config.yml` — Build configuration (input: `src/`, output: `build/`)
* `styles/` — Vale linting styles (OutSystems, Microsoft, proselint, alex)
* `.github/doc-styles/` — Authoritative style guide files (formatting.md, tone.md, structure.md, visual-assets.md)
* `scripts/` — Custom markdownlint rules (MD025 with pagebreaks, MD033 nested inline HTML)

## Frontmatter format

Every `.md` file uses YAML frontmatter validated by CI against `.github/workflows/frontmatter.json`.

Required fields: `summary`, `locale` (always `en-us`), `app_type` (e.g. `mobile apps, reactive web apps`), `guid` (UUID), `platform-version` (always `odc`), `figma` (Figma URL or empty/null).

Optional fields with enum values:

* `coverage-type`: remember, understand, apply, evaluate, unblock, none
* `content-type`: conceptual, procedure, process, error or warning, troubleshooting, reference, tutorial, best practice, vulnerability, release notes, none
* `audience`: mobile developers, frontend developers, backend developers, full stack developers, team lead, team manager, test engineers, architects, platform administrators, tech leads, infrastructure managers, ui designers, business analysts, data engineers, project managers, product owners, none
* `outsystems-tools`, `topic`, `tags`: free-form arrays/strings

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

Product names (exact capitalization): OutSystems, Service Studio, ODC Studio, ODC Portal, LifeTime, Service Center, AI Mentor Studio, Forge, Integration Studio.

## Linting

### Vale (prose linting)

Configuration: `.vale.ini` with `BasedOnStyles = Vale, OutSystems, alex`. Rules from Microsoft and proselint are also enabled selectively. Run locally with:

```
vale src/path/to/file.md
```

### Markdownlint

Configuration: `.markdownlint.json`. Custom rules in `scripts/`. Key settings:

* `ul-style`: asterisk
* `ul-indent`: 4 spaces
* `ol-prefix`: "one" (all items use `1.`)
* `emphasis-style`: underscore
* `no-inline-html`: disabled (inline HTML is allowed for div, br, table elements and nested strong/b/a/sup/code within td/th)
* `line-length`: disabled
* `no-duplicate-heading`: siblings only

Rules that cause CI failure are listed in `markdownlint_fail.json`.

## CI workflows

Validations run on PRs via shared workflows in `OutSystems/tk-cicd`. Key workflows:

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
