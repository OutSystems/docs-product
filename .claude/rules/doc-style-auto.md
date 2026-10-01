# Documentation style: always apply

Apply the documentation style guide whenever you create, edit, rewrite, summarize, or review a Markdown content page. This holds however the request is phrased ("fix this paragraph", "add a section", "update the steps") and whether or not the user ran `/doc-write` or `/doc-review`.

Small edits are covered too. A one-sentence or one-heading change is where style drifts most often, so don't skip the steps below because the change looks trivial.

## What counts as content

* Content pages and reusable fragments, wherever they live (`src/`, `src/shared/`, `online-training/`, `journeys/`, `boot-camps/`, `master-classes/`, and similar content roots).
* Not content, so this rule doesn't apply: `README.md`, `CONTRIBUTING.md`, `CLAUDE.md`, files under `.claude/` and `.github/`, scripts, tooling folders such as `tools/` and `scripts/`, and `translated/` content, which is generated automatically from the English version (edit the English source instead). If you are unsure, treat the file as content.

## Before your first edit in the task

Read the style files from `.github/doc-styles/` that apply. Don't work from memory. Read each file once per conversation.

| When | Read |
|---|---|
| Always | `formatting.md`, `tone.md`, `word-lists.md` `content.md` |
| Creating a page, adding a section, or rewriting more than a few sentences | also `structure.md`, `content.md`, `markdown.md` |
| The page has numbered steps (procedure) | also `procedure-rules.md` |
| The page covers a multi-task, end-to-end flow (process) | also `process-rules.md` |
| Creating, renaming, or moving files or images, or touching `toc.yml` | also `working-with-files.md` |
| Diagrams or other visual assets | also `visual-assets.md` |
| Reviewing | all of the above |

## After your edits

1. Check the changed text against the key rules in `CLAUDE.md`.
2. If `vale` or `markdownlint` is available, run it on the changed files and fix what it reports.
3. In your final reply, name the style files you applied. If you skipped any that the table above requires, say so and why.
