# Verify, revert and handle failures

In this file FLAG_ONLY means "leave the finding pending in the report": the
reason given in the table is appended to that pending line. A fix that passes
verification moves its finding to the fixes block (see `SKILL.md`, Step 5).

## Verify, or revert and flag

Immediately after every fix, re-run exactly the checker that rule uses — a
fix is never reported as done without a passing re-check:

| Rule | Re-run | Pass condition |
|---|---|---|
| 1 | `check_metadata.py` | `format.verdict == "pass"` |
| 2 | local `rename_and_relink.py` result + the `use_figma` return value from the apply step | local `renamed == true`, no errors, AND the Figma frame's returned `name` equals the new stem exactly |
| 3 (either case) | `check_red.py` | `red: ok #F22800` |
| 4, 5 | fresh vision read against the rubric's rule 4/5 criteria | no scripted checker exists — mark the report line "(vision-verified)"; when in doubt, treat as failed |
| 6 | read back the frame's `effectStyleId`/`effects` via `use_figma` | matches the donor's `effectStyleId` (or the imported library style's), confirmed structurally — **not** a re-run of `has_shadow.py` |
| 7 | `redact_pii_region.py verify`, for every occurrence — on the search window for a `plan`/whole-line result, on the returned `cover_box` for a `word_range` result (see the rule 7 procedure's verification note — the two modes are not interchangeable here) | `verdict == "pass"` for every occurrence — one failing occurrence fails the image |
| 10 | `check_metadata.py` | `width.verdict == "pass"` |

**Rule 6 is a deliberate exception to "re-run the same checker the rule uses"**
— it's verified by reading the frame's `effectStyleId`/`effects` back from
Figma instead of re-running `has_shadow.py`. See
`references/rule-06-shadow.md`'s Verification section for why, including an
amendment on the likely root cause found after the exception was written.

**Rule 7's `verify` pass confirms the export is clean, nothing more** — it
says nothing about the frame's underlying raw image asset. See
`references/rule-07-pii.md`'s Verification section, and repeat that caveat
in the report line for every rule 7 fix, not only once (see the report format in `SKILL.md`).

**Rule 2's revert works differently from the raster-mutation rules** —
there's no PNG backup to restore, since the "fix" is a rename, not a pixel
edit. See `references/rule-02-naming.md`'s Revert section for the exact
command.

* **Pass** → discard the backup, record the image as **Fixed**, quoting the
  actual post-fix verdict.
* **Fail** (any other verdict, a thrown error, or a timeout) → restore the
  backed-up PNG over the local file; attempt a best-effort Figma-side undo
  (restore the recorded stroke/fill color, `effectStyleId`, or node
  `width`/`height`, or `instance.remove()`/`rectangle.remove()` for a newly
  created highlight or PII cover) inside a try/catch, and note in the
  report whether that undo itself succeeded. The finding stays pending,
  with "— automatic fix reverted: <failing verdict>" appended. Never retry
  the same fix blindly after an error — if the cause isn't obviously
  fixable (e.g. a resize that still doesn't clear the width check), revert
  and move on. For rule 7 specifically, a fail on *any* occurrence means
  removing *every* cover rectangle created for that image, not just the one
  that failed — a half-covered set of occurrences is worse than none, since
  it looks fixed at a glance.
* **Never commit or push.** `rename_and_relink.py`'s `git mv` stages the
  rename in git's index, which is expected: the calling workflow stages every
  tracked change itself and collects the result as one patch. Every other
  change is a plain working-tree edit.

## Failure and ambiguity handling

| Situation | Handling |
|---|---|
| Multiple Figma frames share the target name | FLAG_ONLY for every AUTO_FIX finding on that image: "multiple Figma frames named `<name>` found (node IDs: …) — confirm the correct one and fix manually." |
| No frame matches the image at all | FLAG_ONLY: "no matching Figma frame found for this screenshot." |
| Article has no `figma:` key, or it's empty | All Figma-dependent findings for that article's images → FLAG_ONLY, noted once at the article level. This includes rule 2 — without a frame to rename, the naming issue is flagged rather than partially fixed — and rule 7, since there's no frame to draw a cover rectangle into. |
| Rule 2 rename but `article_path` was `null` | Still rename (file + Figma frame), but flag: "renamed the file and Figma frame but found no markdown reference to update — confirm nothing else points at the old filename." |
| Rule 2 destination filename collides with an existing file | Don't rename; flag the collision. |
| Rule 2's Figma frame rename succeeds locally but the Figma-side rename or its verification fails | Roll back per `references/rule-02-naming.md`'s Revert section; the finding stays pending with the Figma error or the name mismatch appended. |
| Ambiguous vision judgment (rubric's own documented edge cases, e.g. a `-sa` file matching neither checklist) | Don't rename or place anything; flag the specific ambiguity. |
| `use_figma` call throws | Per the `/figma-use` skill's rule: don't retry blindly. Restore the local backup (rule 2: roll back via `rename_and_relink.py` in reverse), attempt the best-effort Figma undo, keep the finding pending with the raw error appended. |
| Figma MCP unavailable (`whoami` failed at the start of the apply step) | Skip the whole Figma-dependent pipeline up front — don't fail per-image N times. Report it once under the counts; every finding stays pending, rule 2 and rule 7 included, since neither the Figma-side rename nor the redaction rectangle can be attempted. |
| Same image referenced by multiple articles with different `figma:` links | Try each article's link in turn until one resolves a matching frame. |
| Rule 7: vision isn't confident the text is real PII vs. synthetic placeholder data | Don't guess either way — leave it pending as detection reported it. |
| Rule 7: `redact_pii_region.py plan` or `plan-word-range` still reports `safe: false` after a handful of genuinely different windows | FLAG_ONLY: quote the last reason verbatim (it's already scrubbed of the actual PII value) — "background behind this PII isn't flat enough to auto-redact" or similar — and point to a manual redaction or a recapture. Note that `plan-word-range` reaching an actual `safe: false` should be rare — a bad word segmentation already falls back to `plan`'s own whole-line behavior automatically, so this row is mostly `plan`'s failure modes (or the same window failing both a word-range attempt and its own whole-line fallback). |
| Rule 7: the same PII string has multiple occurrences and only some pass planning/`verify` | Treat the whole image as FLAG_ONLY for rule 7 rather than partially redacting it — a partial cover is a worse outcome than none, since it reads as fixed. |

**Say why a finding stayed pending, for real blockers only.** Whenever the
apply step hits a filename collision (rule 2), an ambiguous or missing Figma
frame match, rule 7's `safe: false` after a handful of genuinely different
windows, rule 10's containment/overlap guard failing (frame
background/overlay classification, or the bare-shape fallback's
sibling-overlap check), or any reverted fix, append the exact blocking reason
to that finding's pending line, as "— not fixed automatically: <reason>". Don't
add a reason for the permanent, by-design exclusions (rule 3 alignment, rule 4
sequencing, rule 6 close-crop or inconclusive, rule 8, rule 9) or for a plain
missing/empty `figma:` key: those are settled scope decisions, not blockers.
Keep any PII-related line free of the actual sensitive value, same as the rest
of the report. Nothing is written to a file: the skill also runs unattended,
where nothing persists between runs.
