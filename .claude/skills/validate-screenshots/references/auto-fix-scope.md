# Auto-fix scope and classification

Read this only at Step 3 of `SKILL.md`, after detection has finished, when there are findings to classify. The auto-fix
phase applies the fixes below to the screenshot's **source Figma frame and
re-exports it**, never by patching the local raster PNG, so anything it fixes
is indistinguishable from a designer applying the same component or effect by
hand in Figma.

**Scope.** This file decides what gets *fixed*, never what gets *detected*.
Detection already covered every rule in the rubric, including rules 8 and 9
and the ones listed below as never fixed, and those findings stay in the
report exactly as detection produced them. Only the findings in the table
below are ever fixed, without confirming each fix (an interactive session is
asked once, up front, whether to run the fix phase at all) and always
re-verified before being reported as fixed. Everything else is never fixed
automatically and stays pending: every ⚠️ not listed here, rules 8 and 9
entirely, rule 3's alignment check, rule 6's close-crop case, rule 4's
sequencing/placement, and any rule 7 finding that doesn't clear rule 7's own
flat-background condition below.

**Rule 7's fix has a real limit — state it every time, not just once at the
top.** Covering PII with a matching-color rectangle in the Figma frame only
hides it in the *composited export*. The screenshot's original pixels stay
embedded in the frame as a raw image asset — `download_assets`'s `rawImages`
output still returns them after the fix, independent of whatever shapes sit
on top. Treat this fix as reducing exposure in the *published* documentation;
it is never a substitute for a synthetic recapture, and it doesn't scrub the
Figma source file.


| Rule | Condition | Fix |
|---|---|---|
| 1 — format | `check_metadata.py` → `format.verdict == "fail"` | Re-export the matching Figma frame as PNG |
| 2 — naming | `check_metadata.py` → `naming.verdict == "fail"`, or vision confirms a suffix-vs-content mismatch | Rename the file, update every markdown reference, and rename the matching Figma frame to match — all three or none |
| 3 — highlight, missing | Vision judges the image documents a click/select step, `check_red.py` → `red: none`, vision confirms no highlight shape exists at all | Place a highlight component instance at the resolved location |
| 3 — highlight, wrong color | `check_red.py` → `red: wrong ...` | Recolor the existing rectangle's stroke to `#F22800` |
| 4 — callout, wrong color | Vision spots a numbered callout filled with a non-token red | Recolor the circle's fill to `#F22800` (never touch sequence or placement) |
| 5 — arrow, wrong color | Vision spots a drag/connection arrow in a non-token color | Recolor the line's stroke (and arrowhead fill, if separate) to `#F22800` |
| 6 — shadow | `has_shadow.py` → `wrong` (always in scope), or → `false` on a large-surface capture (vision judges crop size) | Apply the TK-shadow effect, copied from a passing sibling frame or the design-system library |
| 7 — PII | Vision confirms the text is real (non-synthetic) PII, AND `redact_pii_region.py plan` or `plan-word-range` reports `safe: true` for every occurrence of it in the image | Cover each occurrence with a same-color rectangle in the Figma frame — by default just the PII word(s), whole line only when nothing else is worth keeping or the automatic fallback says so — then re-export; see the caveat above |
| 10 — width | `check_metadata.py` → `width.verdict == "warn"` (> 1200px; never for a `-diag` diagram, whose verdict is `skip`) | Resize the source frame (and its full-bleed background child, plus any qualifying overlay children) to 1180px wide, uniformly scaled, then re-export — or, when there's no enclosing frame at all, resize a matching bare shape sitting directly on the canvas instead |

## Classify each finding

For every finding from the detection step, decide AUTO_FIX or FLAG_ONLY using
the scope table above. Nothing else is ever auto-fixed.

* **AUTO_FIX**: rule 1 (❌ format); rule 2 (❌ naming); rule 3 ❌ (highlight
  fully missing) and rule 3 ⚠️ (highlight present but wrong color); rule 4
  (⚠️, wrong-color callout fill only — never a sequencing/placement issue);
  rule 5 (⚠️, wrong-color arrow); rule 6 (`shadow: wrong` always, `shadow:
  false` only on a large-surface capture); rule 7 (❌, but only when
  `redact_pii_region.py plan` or `plan-word-range` reports `safe: true` for
  every occurrence of the PII in the image — see the rule 7 procedure
  below; `plan-word-range`'s own automatic whole-line fallback still counts
  as `safe: true`, so it never demotes a finding to FLAG_ONLY on its own);
  rule 10 (⚠️, width > 1200px, never on a `-diag` diagram).
* **FLAG_ONLY**: rule 3's grid-alignment ⚠️; rule 4's sequencing/placement
  (a color-correct callout with a numbering gap or wrong corner stays
  untouched — see the reasoning below); rule 6's `false` on a close crop, or
  `inconclusive`; rule 7 whenever vision isn't confident the
  text is real PII rather than synthetic placeholder data, or when the
  script reports `safe: false` for any occurrence (a non-flat background,
  ambiguous bounds even after retrying, or no resolvable Figma frame); rule
  8 (internal URLs); rule 9 (theme mismatch); byte-identical duplicates.

  Rule 4 sequencing is deliberately excluded even though the skill fixes
  rule 4's color: recoloring one shape is a single property mutation with a
  real scripted verifier (`check_red.py`); renumbering has no scripted
  checker at all, so both detecting and "verifying" a renumber would be
  self-graded vision with nothing independent to catch a confidently wrong
  fix, and it can touch every callout in the image. That's too large a blast
  radius to auto-apply without a check that can actually fail it.

