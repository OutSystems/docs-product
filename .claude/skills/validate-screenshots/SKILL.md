---
name: validate-screenshots
description: >-
  Validates PNG screenshots in an OutSystems docs article against the team's
  visual rules (highlight components, shadow, cursor, naming, cropping).
  Returns a short issues-only summary so the content developer knows whether
  the images are ready for design review.

  Use when a content developer wants to check their screenshots before merging,
  or asks to "review screenshots", "check my screenshots", "validate
  screenshots", "screenshot review".

  Trigger phrases: "validate screenshots", "review screenshots", "check my
  screenshots", "are these screenshots good", "screenshot review".
allowed-tools: Read,Bash,Edit,AskUserQuestion
metadata:
  exclude-repos:
    - OutSystems/training-internal
---

# Validate screenshots

Runs a design-system review on PNG screenshots a content developer added to an
OutSystems docs article, so they can self-check before asking for manual design
review.

The rubric lives in `visual-rules-screenshots.md` next to this file — it is
produced by running `scripts/calibrate.py` against a reference set of approved
screenshots. If that file is still a placeholder, stop and tell the user to run
calibration first (see the Calibration section below).

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
python3 <skill-dir>/scripts/collect_targets.py "$ARGUMENTS"
```

It prints a JSON array to stdout. Each entry has:

* `image_path` — absolute path to the PNG
* `article_path` — the markdown that references it, or `null`

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

## Step 2: Validate each target

For each entry in the list:

1. Read the image with the Read tool so it goes into vision.
1. Run the deterministic checkers. They are authoritative for the rules
   they cover — do **not** second-guess them from vision.

   ```
   python3 <skill-dir>/scripts/check_metadata.py "<image_path>"
   python3 <skill-dir>/scripts/has_shadow.py    "<image_path>"
   python3 <skill-dir>/scripts/check_red.py     "<image_path>"
   ```

   * `check_metadata.py` prints JSON covering rule 1 (PNG format), rule 2
     (filename regex + surface suffix, including double-suffix detection),
     and rule 10 (width ≤ 1200 px). Parse the JSON and use each verdict
     directly.
   * `has_shadow.py` prints one of `shadow: true` / `shadow: wrong` /
     `shadow: false` / `shadow: unknown` for rule 6. Map them to severity
     as follows: `true` passes; `wrong` is ❌ (phrase as "Shadow doesn't
     match the design-system token — …" so the user knows there is a
     shadow but it's the wrong one); `false` is ❌ for large-surface
     captures and ⚠️ otherwise — never a clean pass, so the reviewer
     always sees it and can dismiss when it's genuinely a self-bounded
     close crop. Phrase every `false` finding as "Missing design-system
     shadow — …" so the user immediately understands the shadow is
     absent (don't lead with "no design-system frame" or other paraphrases
     that bury what's wrong). `unknown` means the image has no alpha
     (typically a JPG, which rule 1 already fails). Do not suppress a
     `false` verdict based on your own close-crop judgment — surface it
     as ⚠️ at minimum. Refer to rule 6 in the rubric for the full
     definitions.
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
    on the right element — the color is scripted), rule 4 (numbered
   callouts), rule 5 (arrows), rule 7 (cursor), rule 8 (PII), rule 9
   (internal environment URLs).
1. Collect only failures and warnings — passing rules are not reported.

Keep per-image notes internal until every image is processed. Do not stream
partial reports.

## Step 3: Emit the summary

Follow this exact format:

```
## Screenshot review: <article filename or "branch changes">

Checked N screenshots. M need changes.

### <image relative path>
- ❌ <short description of the failure — reference the rule>
- ⚠️ <short description of a warning>

### <next image relative path>
- ❌ <...>
```

Rules:

* If N > 0 and M == 0: replace the body with `All N screenshots pass.` and skip
  the per-image sections entirely.
* Severity: `❌` means "must fix before the article ships"; `⚠️` means "a
  designer should eyeball this, but it might be acceptable".
* Never list a rule that passed — the point is to be short.
* Don't repeat the rubric text. Quote the rule name only if needed for clarity.

## Calibration (one-off)

`visual-rules-screenshots.md` starts as a placeholder. To populate it:

1. Gather a reference set of approved PNG screenshots from `docs-next`.
1. Run `python3 <skill-dir>/scripts/calibrate.py <path-or-folder> [<path-or-folder> …]`.
   The script walks the paths, prints one image per turn, and expects the
   assistant to describe what it sees and cluster findings into concrete rules.
1. When done, the script writes a draft `visual-rules-screenshots.md`. Review
   and edit it — the skill uses whatever is in that file.
1. Re-run calibration whenever the Figma library changes (new highlight
   component, new cursor asset, etc.) so the rubric stays current.

If the calibration output looks thin or inconsistent across runs, switch to
authoring the rules manually — the skill doesn't care how the file was
produced, only that it describes checkable rules.
