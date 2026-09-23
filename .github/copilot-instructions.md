# Documentation instructions (chunked)

This repository’s documentation writing and review guidance is split into smaller, focused files to avoid context overload.

## Source of truth

Use these files as the authoritative documentation style guide:

* `.github/doc-styles/formatting.md`: Markdown conventions, emphasis, UI elements, placeholders, admonitions.
* `.github/doc-styles/tone.md`: voice, language, capitalization, product names.
* `.github/doc-styles/structure.md`: headings, paragraphs, lists, procedures, document types.
* `.github/doc-styles/content.md`: grammar, clarity, and general content-quality rules.
* `.github/doc-styles/markdown.md`: Markdown syntax mechanics (headings, emphasis, lists, tables, links, images).
* `.github/doc-styles/procedure-rules.md`: rules specific to procedure (task-based) topics.
* `.github/doc-styles/process-rules.md`: rules specific to process (multi-task, end-to-end) topics.
* `.github/doc-styles/word-lists.md`: approved product names and terminology.
* `.github/doc-styles/working-with-files.md`: file and folder naming conventions, and table of contents placement.
* `.github/doc-styles/visual-assets.md` (only when working on diagrams or other visual assets): Mermaid diagram rules, color palette, visual audit workflow.

## Claude Code commands

In Claude Code, use these commands to automatically pull in the right chunks:

* `/doc-write`: Writing documentation (applies formatting, tone, and structure).
* `/doc-review`: Reviewing documentation (applies formatting, tone, and structure).

## If you cannot use commands

Include the relevant style files in your prompt (for example, by referencing the files above).
