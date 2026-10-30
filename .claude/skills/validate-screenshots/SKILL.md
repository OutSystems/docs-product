---
name: validate-screenshots
description: >-
  Validates PNG screenshots in an OutSystems docs article against the team's
  visual rules (highlight components, shadow, naming, cropping, width, PII)
  and automatically fixes the findings that have a safe, verifiable remedy by
  editing the source Figma frame and re-exporting the image. Returns a short
  report: the issues still pending, then what was fixed. Without Figma access
  it only validates.

  Use when a content developer wants to check or fix their screenshots before
  merging, or asks to "review screenshots", "check my screenshots", "validate
  screenshots", "fix my screenshots", "fix the screenshot warnings", "apply the
  shadow", "add the missing highlight" or "fix the highlight color".
allowed-tools: Read,Bash,Edit,AskUserQuestion,mcp__claude_ai_Figma__whoami,mcp__claude_ai_Figma__get_metadata,mcp__claude_ai_Figma__get_design_context,mcp__claude_ai_Figma__get_screenshot,mcp__claude_ai_Figma__download_assets,mcp__claude_ai_Figma__search_design_system,mcp__claude_ai_Figma__use_figma
---

# Validate screenshots

Runs a design-system review on PNG screenshots a content developer added to an
OutSystems docs article, so they can self-check before asking for manual design
review. Where a finding has a safe, verifiable remedy, the skill then fixes it
in the screenshot's source Figma frame, re-exports the image, and reports what
it changed. Anything it can't fix safely stays pending for a human.

## When to use

* Checking or fixing the screenshots in a docs article before it merges,
  locally or in CI.

## When not to use

* Diagrams and SVGs: use `validate-svgs`.
* Judging article text or style.

## Quick reference

| Step | What happens |
|---|---|
| 1 | Collect the images to check, and find byte-identical duplicates |
| 2 | Run the checker scripts, judge every rule, and print one NOTE per rule |
| 3 | Classify the findings; ask once if a user is present, else just proceed |
| 4 | Fix in Figma, re-export, verify; revert whatever fails |
| 5 | Report the pending issues; print what was fixed as its own block |

The rubric lives in `visual-rules-screenshots.md` next to this file — it is
produced by running `scripts/calibrate.py` against a reference set of approved
screenshots. If that file is still a placeholder, stop and tell the user to run
calibration first (see `references/calibration.md`).

## Setup

Read `visual-rules-screenshots.md` from the same directory as this SKILL.md.
If it still contains the placeholder marker (`<!-- NOT CALIBRATED -->`), stop
and print:

> "No screenshot rubric yet. Run `scripts/calibrate.py` once with a set of
> approved screenshots to generate `visual-rules-screenshots.md`, then try
> again."

## Step 1: Resolve targets

Call the target collector with whatever the user passed (default to empty):

```
python3 -B <skill-dir>/scripts/collect_targets.py "$ARGUMENTS"
```

It prints a JSON array to stdout. Each entry has:

* `image_path` — absolute path to the PNG
* `article_path` — the markdown that references it, or `null`
* `shared_with` — only present on a single-image invocation when the
  calling workflow already knows the image is referenced by more than
  one article changed in this same pull request; a list of those
  articles' absolute paths. Mutually exclusive with `article_path` being
  set — see "Choosing the summary title" in Step 5.

If the array is empty, stop with:

> "No screenshots to validate. Pass a markdown file, a PNG path, or run without
> arguments on a branch that has image changes vs. master."

### Duplicate detection

After collecting targets, group entries by their `sha256` field. If two or
more entries share a hash, the files are byte-for-byte identical and only
one copy should exist. Mark every duplicate with a ❌ finding in the final
summary:

> "Byte-identical duplicate of `<other image name>`. Keep one and delete the
> rest."

Empty `sha256` values (file unreadable) are not grouped.

**Run this over every entry, including ones marked `"cached": true`.**
Whether an image duplicates another depends on the whole set, not on that
image's own content, so a cached image can become a duplicate when a new copy
is added and stop being one when the copy is deleted. This grouping is cheap
and needs no vision, so it is never skipped. Note `sha256` is used here and
nowhere else; the cache keys on `blob_sha` instead.

## Step 2: Validate each target

Detection is the same for every rule in the rubric, including the ones the
automatic fixes never touch (rules 8 and 9, for example). Finish it for every
target first. Don't open `references/auto-fix-*.md` or any `rule-*.md` file
until Step 3 or 4 asks for it; the theme table behind rule 9 is in
`visual-rules-screenshots.md`, not in `references/`.

**Cached entries first.** If an entry has `"cached": true`, this exact file
content already passed this rubric on an earlier run. Skip the numbered steps
below for it entirely — no `Read` into vision, no checker scripts — and reuse
its `cached_findings` array verbatim as that image's findings (an empty array
means it passed clean). It still counts toward `N` in Step 5, and toward `M`
when `cached_findings` is non-empty. Do not re-word, re-order, or re-judge a
cached finding: it was produced by this same rubric and must read identically
so the report stays stable across runs.

`cache_reason` and `cache_detail` on each entry say why it was or wasn't
cached; they are for the log, not for the report.

For every entry that is **not** cached:

1. Read the image with the Read tool so it goes into vision.
1. Run the deterministic checkers. They are authoritative for the rules
   they cover — do **not** second-guess them from vision.

   ```
   python3 -B <skill-dir>/scripts/check_metadata.py "<image_path>"
   python3 -B <skill-dir>/scripts/has_shadow.py    "<image_path>"
   python3 -B <skill-dir>/scripts/check_red.py     "<image_path>"
   ```

   * `check_metadata.py` prints JSON covering rule 1 (PNG format), rule 2
     (filename regex + surface suffix, including double-suffix detection),
     and rule 10 (width ≤ 1200 px; a `-diag` diagram is exempt and gets a
     `skip` verdict, which is not a finding). Parse the JSON and use each
     verdict directly.
   * `has_shadow.py` prints one of `shadow: true` / `shadow: wrong` /
     `shadow: false` / `shadow: inconclusive` / `shadow: unknown` for
     rule 6. Map them to severity as follows:
     `true` passes.
     `wrong` is ❌ — output **exactly** this text (do not paraphrase):
     "Shadow doesn't match the TK-shadow effect available in the TK design
     library — apply it from the Effects menu in Figma (rule 6)".
     `false` is ❌ for large-surface captures and ⚠️ otherwise — never
     a clean pass, so the reviewer always sees it and can dismiss when
     it's genuinely a self-bounded close crop. Output **exactly** this
     text (do not paraphrase):
     "Missing TK-shadow effect available in the TK design library — apply
     it from the Effects menu in Figma (rule 6)".
     `inconclusive` is ⚠️ — the alpha channel is present but the
     detector couldn't reach opaque content on the sampled edges (e.g.
     content far from the borders, transparent mid-edges). Output
     **exactly** this text (do not paraphrase):
     "Shadow check inconclusive — designer should verify the TK-shadow
     effect available in the TK design library (Effects menu in Figma)
     is applied (rule 6)". Do not restate it as "missing shadow" — the
     script didn't say that.
     `unknown` means the image has no alpha channel at all (typically a
     JPG saved as `.png`, which rule 1 already fails); don't emit a
     separate shadow finding in that case. Do not suppress a `false`
     verdict based on your own close-crop judgment — surface it as ⚠️
     at minimum. Refer to rule 6 in the rubric for the full definitions.
   * `check_red.py` prints one of `red: ok #RRGGBB` / `red: wrong #RRGGBB
      (token #F22800)` / `red: none` for the color half of rule 3. Map
     it as: `ok` passes; `none` passes (the image has no red highlight,
     so there's nothing to color-check); `wrong` is ⚠️ — phrase as
     "Highlight red is #RRGGBB, not the design-system token #F22800 —
     re-snap from the Figma library", quoting the actual hex from the
     script so the user can confirm. Vision can't reliably distinguish
     similar reds (#F22800 vs #CC2200 vs #BB1F00), so do not second-guess
     the script.
1. Use vision only for the rules the scripts don't cover: rule 2's
   suffix-vs-content mismatch (filename says `-ss` but the image shows
   ODC Studio), rule 3's _placement_ (whether a highlight is present and
    on the right element — the color is scripted; check
   `visual-rules-screenshots.md` rule 3's "Native selection state" case
   first — if the product's own selection highlight already marks the focal
   element but no red rectangle was added, that's a ⚠️ with the quoted
   verdict wording, not a ❌; only fail ❌ when there's neither a red
   rectangle nor a native selection state), rule 4 (numbered callouts),
   rule 5 (arrows), rule 7 (PII), rule 8 (internal environment URLs), rule 9
   (theme: compare the image's light or dark theme with the mandate for its
   suffix in `visual-rules-screenshots.md` rule 9's table; a contradicted
   mandate is ❌, and a suffix missing from the table is ⚠️).

   For `-ss`/`-odcs` files showing an entity or data-model layout (boxes
   connected by lines), check against `visual-rules-screenshots.md` rule 2's
   entity/data-model carve-out before concluding the suffix is wrong. A
   Data-tab capture cropped tight with no toolbar chrome is not by itself a
   sign of a misfiled `-diag` diagram — don't fall back on the genuine-diagram
   checklist below as the only reference point for that judgment.

   For `-ss`/`-odcs` files showing a Studio capture together with a
   third-party app panel (for example a spreadsheet), check
   `visual-rules-screenshots.md` rule 2's mixed-surface composite exception
   before concluding the suffix is wrong. The third-party panel is not a
   surface mismatch.

   For files ending in **`-diag`**: use vision to determine whether the
   content is a genuine diagram or a UI screenshot.

   A genuine diagram has all of the following:

   * No product UI chrome (no IDE toolbars, portal navigation, or browser
     address bar)
   * A conceptual layout: flow chart, sequence diagram, hierarchy tree,
     architecture box, icon grid, or swimlane diagram
   * OutSystems branded orange/red iconography representing concepts
   * Connecting elements: arrows, dashed lines, or swimlanes
   * A white or light-gray background with a rounded-rectangle shadow border
   * Descriptive text labels naming concepts or roles, not UI controls

   Excluded: entity or data-model diagrams captured directly from Service
   Studio's or ODC Studio's Data tab, even when cropped tight with no
   visible toolbar chrome. These are native tool renderings, not
   standalone Figma diagrams — refer to `visual-rules-screenshots.md`
   rule 2's entity/data-model carve-out for the native iconography and
   connector traits that identify them.

   A UI screenshot shows product interface chrome with interactive elements
   (panels, toolbars, dropdowns, form fields, menus) from ODC Studio, ODC
   Portal, Service Studio, or similar tools.

   A Studio capture shown next to a third-party app panel with no
   connecting arrows, highlights or OutSystems-branded iconography is a UI
   screenshot, not a diagram. Rule 2's mixed-surface composite exception
   gives the correct suffix: `-ss` or `-odcs`, from the Studio panel. The
   same layout **with** arrows, highlights or branded iconography is a
   genuine diagram.

   * If the content is a genuine diagram → suffix is correct; no naming
     finding.
   * If the content is a UI screenshot → emit ❌ Rule 2: "Image looks like
     a UI screenshot but uses the `-diag` suffix — rename with the correct
     surface suffix (e.g. `-ss`, `-odcs`)."
1. Collect only failures and warnings — passing rules are not reported.

Keep per-image notes internal until every image is processed. Do not stream
partial reports.

### Gate: write down every verdict before moving on

For each non-cached image, print one working-note line per rule below, in this
exact shape, before anything else is printed. They exist so no rule is skipped;
the calling workflow ignores everything printed before the verdict block.

```
NOTE <image relative path> | rule <N> | <evidence in a few words> | pass|fail
```

* Scripted rules (use the checker's verdict as the evidence): 1 (format), 2
  (filename), 3 (highlight color), 6 (shadow), 10 (width).
* Vision rules: 2 (suffix against content), 3 (placement), 4 (callouts), 5
  (arrows), 7 (PII), 8 (internal URLs), 9 (theme). Write `pass (none present)`
  for a rule that has nothing to judge. For rule 9 the evidence must state the
  image's theme and the mandate for its suffix, for example `dark, suffix -odcs
  mandates light`.

A rule whose verdict is `skip` (rule 10 on a `-diag` diagram) is written as
`pass`, with `exempt diagram` as the evidence; it is never a finding and never
reaches Step 3.
A `fail` becomes a finding in Step 5, worded as this skill's rules say. A rule
that only warns (⚠️, such as width) is a `fail` here too: the last field is
always `pass` or `fail`, never `warning`.
Nothing moves to Step 3 until every non-cached image has all of these lines.

### Extract the Figma link (once per article)

If any entry has a non-null `article_path`, open that markdown file once and
grep its YAML frontmatter for a `figma:` key (the value is a `figma.com` URL).
Remember the value — the report header will surface it so the content
developer can jump straight to Figma to fix things. If the frontmatter has no
`figma:` field, or the value is empty, skip the link entirely (don't print an
empty `Figma:` line).

When multiple articles reference different screenshots (branch-diff mode),
collect the unique Figma URLs per article and emit them grouped under each
article in the header. In the common single-article case, one line is enough.

## Step 3: Decide what to fix

Only when Step 2 is complete. Open `references/auto-fix-scope.md` and classify
every finding of a non-cached entry as AUTO_FIX or FLAG_ONLY (a cached entry is
never fixed: its findings are reused as they are). Warnings (⚠️) are findings
like any other: classify them too, and fix the ones the scope lists. Print one
line per finding, before anything else of this step:

```
FIX DECISION <image relative path> | rule <N> | AUTO_FIX|FLAG_ONLY
```

A run with at least one `fail` NOTE and no FIX DECISION line has skipped this
step. With no AUTO_FIX finding, skip to Step 5 and don't touch Figma.

* **Interactive session** (a user is present): ask once with AskUserQuestion,
  "N findings can be fixed automatically in Figma and the images re-exported.
  Fix them now?", with "Yes, fix them (Recommended)" first and "No, just
  report" second. On "No", go to Step 5 with everything pending.
* **Unattended run** (the caller says to skip questions, or there is no user):
  don't ask; the answer is yes.

## Step 4: Apply the automatic fixes

Skip when Step 3 left nothing to fix or the answer was no. Otherwise follow
`references/auto-fix-procedure.md`, then verify as
`references/auto-fix-verify.md` says. It starts with one `whoami` call: if
Figma is unreachable or rejects the credential, skip this step, keep every
finding pending and note it once in the report, so the run only validates.

A fix that passes verification moves its finding from pending to **fixed**
(what changed, and the checker verdict). A fix that fails is reverted and its
finding stays pending with the reason added. Never commit or push: the changes
stay in the working tree and the calling workflow collects them.

## Step 5: Emit the summary

### Verdict block (always, before anything else)

Print one line recording the outcome for every target in this invocation —
cached and freshly validated alike — before any other Step 3 output, and
before the `<!-- REPORT BEGIN -->` sentinel the calling workflow expects:

```
<!-- VERDICTS {"src/foo/images/a-ss.png":"clean","src/foo/images/b-ss.png":"findings"} -->
```

Keys are repo-relative POSIX paths, values are exactly `clean` or `findings`
(`findings` when that image still has at least one ❌ or ⚠️ pending in this
report, after any automatic fixes; an image whose findings were all fixed is
`clean`, and the verdict describes the image as it is left in the working
tree). One line, valid JSON, no line breaks inside it. HTML comments don't render on
GitHub, so this never shows up in the PR comment.

**Print it even when the whole run is clean** — that is, print it immediately
before `<!-- NO REPORT -->` too. It is what lets the workflow record which
files passed. A missing or malformed block is not fatal: the workflow falls
back to caching only fully-clean invocations, which is safe but coarser.

Never record a duplicate-detection ❌ as that image's own `findings` verdict
unless it also has a non-duplicate finding: duplicates depend on the whole
set, so they must be re-derived every run rather than cached against one file.

### Report

Follow this exact format:

```
## Screenshot review: <TITLE>

Figma: <url from frontmatter — omit this line entirely when no figma key>

Checked N screenshots. M need changes. F fixed automatically.

### <image relative path>
- ❌ <short description of a failure still pending — reference the rule>
- ⚠️ <short description of a warning still pending>

### <next image relative path>
- ❌ <...>

```

The report holds the pending issues, in the per-image format above. What was
fixed does not go in it.

### The fixes block

When F > 0, print this block right after the report (and after its closing
`</details>`):

```
<!-- FIXED BEGIN -->
<details>
<summary>TITLE — F fixed automatically</summary>

- `<image relative path>` — ✅ rule <N> (<name>): <what changed>; <checker> now reports <verdict>.

</details>
<!-- FIXED END -->
```

The calling workflow posts this block as a comment of its own, which later runs
leave alone, so what was fixed stays visible after a later run re-reports only
what is still pending. Never repeat the fixed lines inside the report.

### Choosing the summary title

`TITLE` is also what goes in the wrapping `<summary>` line (see the
calling prompt). Every form of `TITLE` below is a file name with its
extension kept: `input-parameter.md`, never `input-parameter`. For a
markdown-article invocation `TITLE` is the article's file name, and in
branch-diff mode it is "branch changes". For a single-image invocation,
`TITLE` follows the `collect_targets.py` entry:

* `article_path` is set — use that article's file name, `.md` included.
  The image resolves to an owning article even when that article itself
  isn't part of this pull request; the finding still belongs to it.
* `shared_with` is set (`article_path` is `null`) — use the image's file
  name, `.png` included, appended with " (shared image)". The image is
  referenced by more than one article changed in this same pull request,
  so don't attribute it to just one of them.
* Neither is set — use the image's file name, `.png` included, appended
  with " (orphan image)". No article anywhere in the repository
  references it.

Rules:

* `N` counts every target in this invocation, cached ones included; `M` counts
  those with at least one finding **still pending after the automatic fixes**,
  again cached ones included; `F` counts the fixes that were applied and
  verified (leave "F fixed automatically." out when it is 0). A cached image
  is a validated image — never quietly drop it from the totals, or the counts
  will shrink as the cache warms up and the report will look like coverage
  was lost.
* If N > 0, M == 0 and F == 0: replace the body with `All N screenshots pass.`
  and skip the per-image sections entirely. Keep the `Figma:` line in the
  header if it was extracted.
* If M == 0 and F > 0: replace the per-image pending sections with `All N
  screenshots pass after the automatic fixes.` and still print the fixes block,
  so the author can see what changed in Figma.
* A finding whose automatic fix was attempted and reverted stays in the
  pending list, with the reason appended: "— automatic fix reverted: <reason>".
* If Step 4 was skipped because Figma was unavailable, and there were
  AUTO_FIX findings, add one line under the counts: "Automatic fixes skipped:
  Figma was unavailable."
* Severity: `❌` means "must fix before the article ships"; `⚠️` means "a
  designer should eyeball this, but it might be acceptable". Lines in the fixes
  block use ✅ and never ❌ or ⚠️.
* Every fixed line quotes the actual post-fix checker verdict (or
  "(vision-verified)" for rules 4 and 5) — never claim success without it. A
  rule 2 line names the old and new file name and says the Figma frame was
  renamed and the markdown references updated. A rule 7 line says whether the
  cover was word-level or whole-line, and restates that it hides the text in
  the published image only: the original pixels stay in the frame's raw image
  asset in Figma.
* Never echo a sensitive value (rule 7), pending or fixed: say where it is
  and what kind of data it looks like, not the value itself.
* Never list a rule that passed — the point is to be short.
* Don't repeat the rubric text. Quote the rule name only if needed for clarity.

## Common mistakes

* Skipping a vision rule because the scripts passed. Every rule gets a NOTE
  line per image (Step 2), rule 9's evidence included.
* Reading the auto-fix scope as the detection scope. Rules 8 and 9 are always
  detected and reported; they are just never fixed.
* Fixing an entry marked `"cached": true`, or touching Figma on a run with
  nothing to fix.
* Putting ❌ or ⚠️ on a fixed line, or repeating the fixed lines inside the
  report. The fixes block is posted separately so it survives the next run.
* Treating a ⚠️ finding as not worth a fix. Warnings go through Step 3 like
  failures; only the scope file says what is fixed.
* Committing or pushing. The changes stay in the working tree.

## Calibration (one-off)

`visual-rules-screenshots.md` starts as a placeholder and is populated by
`scripts/calibrate.py`; the procedure is in `references/calibration.md`.
