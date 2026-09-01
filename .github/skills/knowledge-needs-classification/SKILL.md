---
name: knowledge-needs-classification
description: >
  Use this skill whenever a user wants to propose knowledge needs for an
  existing piece of content — an article or documentation page — given by
  the path to a local markdown file, and map that content against the
  team's knowledge-needs.yaml register. Trigger when the user asks what
  knowledge needs a document covers, wants Claude to tag or index an
  article against the knowledge need register, provides a path to a
  markdown file and asks "what knowledge needs does this cover" or
  "propose knowledge needs for this page", or wants to add coverage
  entries derived from reading actual content rather than a submitted list
  of questions. For validating a list or table of questions the user
  already wrote, use the knowledge-need-validator skill instead — this
  skill's job starts from a file, not a list.
allowed-tools: Bash(gh api repos/OutSystems/tk-cicd/contents/knowledge-needs.yaml:*),Bash(gh repo view:*),Bash(git branch --show-current:*),Bash(gh api repos/OutSystems/tk-cicd --jq '.default_branch':*),Bash(gh api repos/OutSystems/tk-cicd/git/ref/heads/:*),Bash(gh api repos/OutSystems/tk-cicd/git/matching-refs/heads/add-knowledge-needs:*),Bash(gh api repos/OutSystems/tk-cicd/commits/add-knowledge-needs:*),Bash(gh pr list --repo OutSystems/tk-cicd --head add-knowledge-needs:*),Bash(diff:*)
---

# Knowledge needs content classification

## Purpose

Read an existing piece of content, identify the knowledge needs (coverage
questions) it actually answers, check them against the team's
`knowledge-needs.yaml` register, and — once the user approves — add any
genuinely new ones to the register at a sensible placement.

**Input:** the path to a local markdown file — e.g. `src/some-section/some-
article.md` — pointing to an actual markdown source file on disk.

This skill does not accept a submitted list of questions to validate — for
that, use the `knowledge-need-validator` skill instead. This skill always
starts by reading real content.

## Not yet implemented (by explicit request)

One piece of the original design is deliberately **out of scope for this
version** — don't attempt it, and say so plainly if the user asks:

- **Above/below hierarchy check.** Checking sibling markdown files in parent
  or child folders (by file path, delimited by `/`) for knowledge needs
  already assigned there, to avoid re-proposing something a parent or child
  page already covers.

If asked to do this, explain it's planned but not built yet, rather than
attempting a partial or improvised version.

This skill does update the input file's own frontmatter, but only the
`topic` field, and only at the very end — see Step 9.

## Step 1 — Read the content

1. Read the markdown file at the given path directly from disk.
2. If the path doesn't exist or can't be read, stop and ask the user to
   provide the correct path — don't guess at a different path or proceed
   without the content.
3. Read the whole piece before drafting anything — don't propose knowledge
   needs section-by-section without having seen the full document first,
   since later sections can change how earlier ones should be scoped.
4. Note whether a `topic` field already exists in the file's frontmatter,
   and if so, its current values — this is used as a prior in Step 9.

## Step 2 — Fetch the register

**Source of truth:** `knowledge-needs.yaml` at the root of the current
repository.

**Register schema:** a nested taxonomy — category → topic → subtopic, each
with `name` and `id`, and an optional `description`:

```yaml
knowledge-needs:
- name: <category name>
  guid: <uuid>
  topics:
  - name: <topic name>
    id: <slug>
    description: <optional>
    subtopics:
    - name: <subtopic name>
      id: <slug>
      description: <optional>
```

**How to fetch it:**

1. Read `knowledge-needs.yaml` from the root of the current repository.
2. If the file doesn't exist at the repo root, stop and tell the user the
   register couldn't be found, and ask whether to proceed without the
   register check or point to a different location for it. **Never silently
   skip this** — proceed only if the user says to.
3. Parse the file content as YAML and flatten every topic and subtopic into
   one comparable register entry each: identifier (subtopic `id`, or topic
   `id` if no subtopic), comparable text (`description` if present,
   otherwise `name`), and path (category → topic → subtopic) for display.

## Step 3 — Verify the local register is in sync with tk-cicd

The local copy read in Step 2 is a synced duplicate, not the source of
truth — before using it for matching, confirm it hasn't drifted from the
canonical copy.

1. Try fetching `knowledge-needs.yaml` from the `OutSystems/tk-cicd` GitHub
   repository into a scratch file (e.g. in the session's scratchpad
   directory), by running:
   `gh api repos/OutSystems/tk-cicd/contents/knowledge-needs.yaml --jq '.content' | base64 -d > <scratch-path>/tk-cicd-knowledge-needs.yaml`
   (use exactly this command shape — it's the one pre-approved in this
   skill's `allowed-tools`, so it runs without a permission prompt).
2. **If the command fails** (`OutSystems/tk-cicd` isn't reachable —
   missing credentials, no cross-repo access, network issue, etc.): tell
   the user plainly that `tk-cicd` couldn't be reached and the local copy
   will be used instead, then ask, via `AskUserQuestion`, whether to
   proceed on that basis. If the user declines, stop here. If they
   proceed, note for Step 8 that `tk-cicd` was unreachable this run, and
   continue to Step 4 with the local copy as loaded.
3. **If it succeeds**, compare it against the local copy read in Step 2
   with `diff <local-path> <scratch-path>/tk-cicd-knowledge-needs.yaml`.
   - **No output** → they match; proceed with the local copy already
     loaded.
   - **They differ** → stop and ask the user, via `AskUserQuestion`, how to
     proceed:
     - **Sync tk-cicd to local** — overwrite the local copy with the
       canonical `tk-cicd` content, then use that synced version for the
       rest of this skill.
     - **Use local version** — keep working with the local copy as-is,
       even though it differs from `tk-cicd`.
4. Never silently proceed past an unreachable `tk-cicd` or a local/`tk-cicd`
   mismatch without asking first.

## Step 4 — Chunk the content into meaningful sections

Break the document into chunks worth mapping to a knowledge need — a
**meaningful chunk** is a section of at least ~4–5 lines or ~500 characters
that is actually about something (not navigation, boilerplate, or a related-
links list).

**Ignore incidental mentions.** If a chunk references something in passing —
e.g. it mentions "Server Actions" once while explaining a different core
subject — that mention does not get its own knowledge need. Only chunks
where a concept, task, or setting is the *actual subject* of that section
count as candidates.

## Step 5 — Match each chunk against the register first

For every meaningful chunk, check whether an existing register entry already
covers it (same comparison logic as knowledge-need-validator: same user
intent + accomplishment + condition, or a strict subset, counts as a match).

- **Existing entry fits** → reuse it. Don't propose a new knowledge need for
  that chunk — record it as `REUSE` with the matched entry's path and id.
  **Always show the matched entry's existing `description`** in the
  proposal table so the user can judge the match. If the matched entry has
  no `description` (most existing entries don't), say so explicitly — e.g.
  "(no description on file)" — rather than leaving that cell blank or
  omitting it, since a blank cell looks like a missing value rather than a
  deliberate absence.
- **No suitable existing entry** → draft a new knowledge need for that chunk:
  a compact **name** (target 3 words, hard cap 25 characters — extend past 3
  words only when needed to stay unambiguous) and a **description** (the
  full long-form knowledge need, in `[Wants to] + [accomplish what] +
  [condition]` form) that a second reader can rely on for scope. Every new
  knowledge need must have a description — never leave it out.
- Run every new candidate through the same five validation rules used in
  knowledge-need-validator (user-framed, single content unit, specific
  enough, goal-oriented, condition present or justified) before including it
  — don't propose a candidate that would itself fail validation.

## Step 6 — Cap the total by article length

Regardless of how many meaningful chunks or new candidates step 4–5
produced, cap the **total number of knowledge needs proposed for this piece
of content** (reuse + new combined):

- **Longer articles** (roughly 500+ words of body content, excluding nav,
  headers, and boilerplate): **at most 3**.
- **Shorter articles** (under ~500 words): **at most 1–2**.
- This is a hard ceiling, not a target. If more candidates survive step 5
  than the cap allows, consolidate related ones into a single broader (but
  still single-content-unit) knowledge need where possible, and otherwise
  keep the highest-value candidates — the ones most central to what the
  article is actually about — dropping peripheral ones. Say briefly what was
  dropped or merged so the user can override it.

## Step 7 — Decide placement for new entries

For every `NEW` candidate (not `REUSE`):

1. Check whether an existing category and topic already fit conceptually —
   reuse them. Only propose a brand-new category if nothing in the existing
   taxonomy (the categories, topics, and subtopics already in
   `knowledge-needs.yaml`) reasonably covers it.
2. If an existing topic fits but the specific question isn't covered yet, add
   it as a new subtopic under that topic.
3. Generate the `id`: lowercase, hyphen-separated, derived from the name,
   unique across the entire flattened register — check for collisions before
   finalizing.
4. Preserve the file's existing formatting conventions (2-space indents, key
   order: `name`, `id`, `description`, `subtopics`).
5. Quote `name` and `description` values safely instead of always writing
   them as a plain (unquoted) YAML scalar. Use a plain scalar only when the
   value contains none of: a colon followed by whitespace (`: `), a
   leading/trailing quote or YAML indicator character (`"`, `'`, `-`, `#`,
   `&`, `*`, `!`, `|`, `>`, `%`, `@`, `` ` ``, `[`, `]`, `{`, `}`, `,`), or
   trailing whitespace. If any of these appear anywhere in the value, wrap
   the whole value in single quotes and double any literal single quotes
   inside it (`it's` → `it''s`). This matters most for descriptions that
   quote a literal error message or UI text containing a colon (for example
   `Parameter name: key`). An unquoted `: ` inside a plain scalar is
   invalid YAML and breaks every tool that later parses the file, including
   the `metadata-refresh.yml` sync workflow's PR-body generation.

## Step 8 — Review gate: Add / Edit / Scrap and redo

Present the full proposed set (reuse + new) as one table:

```
## Proposed knowledge needs for [content title/file path]

| # | Status | Name | Description | Placement / matched entry |
|---|--------|------|--------------|-----------------------------|
| 1 | NEW   | Configure LLM judge | How do I configure an LLM as a judge...? | [Category] > [Topic] (new subtopic) |
| 2 | REUSE | Reset password      | *(existing entry's own description, or "no description on file" if it has none)* | [Category] > [Topic] > [Subtopic] (id: reset-password) |
```

Then call the `AskUserQuestion` tool with one question ("What should happen
with this proposed set?") offering exactly these three options, in this
order, so the user picks one instead of typing a reply:

- **Add** — add all NEW items to the register at the placements shown; REUSE
  items are left as-is (not added again)
- **Edit** — tell Claude which item #(s) to change (name, description, or
  placement)
- **Scrap and redo** — discard this proposal; Claude will re-read the
  content and produce a different set

Never write to the register before the user responds through this gate. If
the user answers with free text instead of picking one of the tool's
options (e.g. "Other" with their own wording), interpret it the same way as
the matching option above.

**Handling each response:**

- **Add** — finalize: if Step 3 already found `OutSystems/tk-cicd`
  unreachable this run, skip straight to the unreachable handling below.
  Otherwise, fetch the current `knowledge-needs.yaml` from the
  `OutSystems/tk-cicd` GitHub repository — the canonical source — using the
  same `gh api repos/OutSystems/tk-cicd/contents/knowledge-needs.yaml`
  command as Step 3.
  Whichever copy you insert into below, validate it immediately after
  inserting and before saving, committing, or pushing it: parse the file
  with a YAML parser (for example
  `python3 -c "import yaml; yaml.safe_load(open('<path>'))"`) and confirm it
  succeeds. If it fails, the most likely cause is a `name` or `description`
  value that needed the quoting rule from Step 7 — fix it and re-validate
  before continuing. Never save, commit, or push a `knowledge-needs.yaml`
  that fails to parse.
  - **`tk-cicd` unreachable** — insert each approved `NEW` item at its
    placement directly into the **local** `knowledge-needs.yaml` (the file
    read in Step 2, at the repo root) instead, and save it. Tell the user
    plainly that `tk-cicd` couldn't be reached, so no pull request was
    opened there — the local copy now holds the approved additions
    instead. Skip the "open a pull request?" question below and go
    straight to Step 9.
  - **`tk-cicd` reachable** — never write to the local duplicate in the
    current repo; it's a synced copy, not the source of truth. Insert each
    `NEW` item at its approved placement into the `tk-cicd` copy, then ask,
    via `AskUserQuestion`, whether to open a pull request in
    `OutSystems/tk-cicd` with this change:
    - **Yes** — the branch name is
      `add-knowledge-needs/<current-repo-name>/<current-repo-branch-name>`. Get
      `<current-repo-name>` from the **remote** repository, not the local
      folder name — a worktree's folder often doesn't match the repo name —
      by running `gh repo view --json name --jq '.name'`. Get
      `<current-repo-branch-name>` from the current git branch (e.g.
      `git branch --show-current`). Example:
      `add-knowledge-needs/success-docs/tk-12345-add-section`.
      1. Get the default branch of `OutSystems/tk-cicd`:
         `gh api repos/OutSystems/tk-cicd --jq '.default_branch'` — don't
         assume it's `main`.
      2. Check whether the branch already exists:
         `gh api repos/OutSystems/tk-cicd/git/matching-refs/heads/<branch-name> --jq '.[].ref'`.
         Also check for an existing PR on it:
         `gh pr list --repo OutSystems/tk-cicd --head <branch-name> --state all --json number,title,state,url`.
      3. **Doesn't exist** → get the default branch's tip commit SHA
         (`gh api repos/OutSystems/tk-cicd/git/ref/heads/<default-branch> --jq '.object.sha'`),
         create the branch from it
         (`gh api repos/OutSystems/tk-cicd/git/refs -f ref="refs/heads/<branch-name>" -f sha="<sha>"`),
         commit the updated `knowledge-needs.yaml` to it, push, and open a PR
         with `gh pr create` describing what was added and why.
      4. **Already exists** → show the user the branch's latest commit
         (`gh api repos/OutSystems/tk-cicd/commits/<branch-name> --jq '{sha: .sha, message: .commit.message, author: .commit.author.name, date: .commit.author.date}'`)
         and any existing PR found above, then stop and ask, via
         `AskUserQuestion`, how to proceed:
         - **Override changes** — reset the branch to the default branch's
           tip and reapply only this change (force-push), discarding
           whatever was on it before.
         - **Combine changes** — check out the existing branch as-is, apply
           this change on top of what's already there, and push, keeping
           any prior work on the branch.
    - **No** — present the updated file content to the user as a deliverable
      instead, and state plainly that no PR was opened.
- **Edit** — apply only the specified change(s), then re-display the updated
  table for another Add / Edit / Scrap-and-redo round. Loop until the user
  Adds.
- **Scrap and redo** — discard the whole proposal. If the user gave a reason,
  apply it. If not, ask one brief question about what to change (different
  chunking, different scope, a different reading of the content) before
  re-reading and producing a genuinely different set — don't just resend the
  same list.

## Step 9 — Update the input file's frontmatter

Once Add has fully completed (regardless of whether a PR was opened or
declined), update the input markdown file's own frontmatter. This is
separate from, and happens after, everything above.

1. Check the frontmatter of the file read in Step 1 for a `topic` field.
   This is the prior for the hysteresis in step 3 below — its existing
   value if present, or an empty set if the field is missing. A missing
   field means there's no prior to keep, not a reason to skip the update:
   this skill is frequently run specifically to populate `topic` on files
   that don't have it yet, so it must be able to create the field, not
   just edit an existing one.
2. Compute this run's raw topic id set: the `id` of every knowledge need
   identified for this file — REUSE and NEW combined. Use each entry's own
   identifier, same as the flattening in Step 2: a subtopic's `id` when
   the knowledge need is a subtopic-level entry, or the topic's `id` only
   when it has no subtopics.
3. Apply hysteresis against the prior before finalizing the list — the
   same asymmetric keep-vs-add logic the `coverage-type-classification`
   skill uses for its `coverage-type` field, so a borderline run doesn't
   flip the field back and forth:
   - **Keep** every prior id unless this run found positive evidence the
     content no longer covers it (for example, the section that justified
     it was removed or rewritten). Don't drop a prior id just because this
     run's chunking didn't happen to revisit it. (Vacuous when the field
     was missing — there's nothing to keep.)
   - **Add** an id not already in the prior only when this run backs it
     with a solid `REUSE` match or a `NEW` candidate that passed full
     validation (Step 5) — the same bar Step 5 already applies, so no
     extra threshold is needed here.
   - Deduplicate the resulting set and sort it alphabetically.
4. Compare the resulting list to the prior as sets, ignoring order.
   - **Equivalent** → the frontmatter is already correct — either it
     already held exactly this set, or the field was missing and this run
     found nothing to add. Skip the write (don't create an empty `topic`
     field) and tell the user no update was needed.
   - **Different** → write the resulting list to the `topic` field in the
     file read in Step 1, creating the field if it didn't already exist,
     at the same local path, preserving the rest of the frontmatter and
     content unchanged.

The `topic` field must always be written as a YAML list, one item per line,
even when it holds a single value:

```yaml
topic:
  - reset-password
```

Never write `topic` as a single line with comma-separated values (for
example `topic: reset-password, configure-llm-judge`).

## Tone guidance

- Don't over-tag. A short, focused article legitimately may only need one
  knowledge need — resist the urge to invent more just to fill the cap.
- Always show why a chunk was matched to an existing entry or judged new,
  not just the verdict.
