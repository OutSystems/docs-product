# Rule 7 (PII) — cover with a matching-background rectangle

Referenced from `auto-fix-procedure.md` (apply) and `auto-fix-verify.md`
(verify). Read the apply procedure's general backup/re-export preamble in
`auto-fix-procedure.md`
before using this file.

This is the one AUTO_FIX rule whose "fixed" doesn't mean "gone from the
file" — re-read the scope note at the top of `auto-fix-scope.md` before using it.
Vision's job here is judgment (is this real PII, or synthetic placeholder
data?) and rough localization; `scripts/redact_pii_region.py` owns the
pixel-level geometry so the actual cover box is derived, never eyeballed.

## Apply

1. Apply `<skill-dir>/visual-rules-screenshots.md`'s rule 7 criteria to
   decide whether the text is genuinely someone's real name, email, phone
   number, or ID — not a placeholder like `Sample_Employee` or
   `john.watson@company.com`. If it's ambiguous, don't proceed — flag it,
   same as validate-screenshots would.
1. List every occurrence of that PII in the image. The same string often
   appears more than once — a truncated copy inside a badge, a full copy
   elsewhere, a mirrored copy in a side-by-side comparison view — and each
   occurrence needs its own window, cover box, and verification; missing
   one leaves a real leak next to a "fixed" one.
1. For each occurrence, give a generous rectangular search window in the
   **exported PNG's own pixel coordinates** (not frame-local — the script
   only ever sees the raster): wide/tall enough to contain the whole text
   run plus a few pixels of surrounding background on all four sides.
1. **Default to covering only the PII itself, not the whole text run.**
   When the PII sits inside a longer line that also carries non-sensitive
   context worth keeping legible — "Revision 62 Published at 4:16 PM by
   `Isabel Martins`", "Created by: `dave@x.com`" — redact only the
   backticked span. Cover the *whole* recognized run only when there's
   nothing else in it worth keeping (a table cell that is only ever an
   email address, say). Which mode to use is a judgment call for vision to
   make from what the line actually says, same as the real-vs-synthetic
   call in step 1 — but which *pixels* end up in the box is never a
   judgment call; a script decides that either way, per the two modes
   below.
   * **Whole run** — nothing to preserve alongside the PII:
     ```
     python3 -B <skill-dir>/scripts/redact_pii_region.py plan "<image_path>" <x> <y> <w> <h>
     ```
     Finds the window's dominant color (not just its four corners — a
     rounded badge's own corner radius routinely cuts the corners down to
     whatever sits behind it, so corner-sampling gets fooled by exactly
     the shapes this rule needs to handle), finds the tight bounding box
     of everything that isn't that color, and — only if a small padding
     margin around that bounding box is *also* uniformly the same color —
     returns `{"safe": true, "cover_box": {...}, "color_rgb": [...],
     "color_hex": "..."}`. Otherwise `{"safe": false, "reason": "..."}`,
     and none of the reasons are worth pushing past by loosening `--tol`:
     * *no single color dominates the window* — the background isn't flat
       (a gradient, a texture, or the window straddles two different
       fills)
     * *no non-background content found* — the window missed the text
     * *detected content touches the search window edge* — the window
       wasn't proven to contain the whole text run; widen it and retry
     * *padding margin isn't uniform background* — something else (an
       icon, a border, adjacent text) sits close enough that a
       rectangular cover would clip it or leave a visible seam
     In practice, the two most common causes of the last two verdicts are
     a thin 1px divider/border line running through the window (nudge the
     window to fall entirely on one side of it, or shrink it so the line
     never enters the scan) and a rounded shape's corner antialiasing
     (trim the window a pixel or two short of where the curve begins).
     Both are geometry problems, not tolerance problems — solve them by
     moving or resizing the window, never by raising
     `--tol`/`--bg-fraction` to paper over real content. Retry with an
     adjusted window as many times as it takes to understand the geometry
     (this is a read-only planning call, not the blind-retry-after-an-
     error case `/figma-use` Rule 14 warns about, since nothing has been
     written to Figma yet) — but if it's still `safe: false` after a
     handful of genuinely different windows, stop and flag it rather than
     force a fit.
   * **Word range** — context worth keeping surrounds the PII:
     ```
     python3 -B <skill-dir>/scripts/redact_pii_region.py plan-word-range "<image_path>" <x> <y> <w> <h> <total_words> <pii_start_word> <pii_end_word>
     ```
     `total_words` is the line's whitespace-split word count as vision
     read it; `pii_start_word`/`pii_end_word` are the 0-indexed inclusive
     range of the PII within that split (e.g. `9 7 8` for the two-word
     name ending a nine-word line). **Never pass a pixel x for the split
     — only a word count.** The script finds the real word boundaries
     itself from a luminance-only "ink density" profile, which is
     deliberately a different (more forgiving) signal than the RGB-
     tolerance scan `plan` uses for the outer edges: at small or sub-pixel-
     rendered text, a word *space* routinely still shows a stray
     colour-fringed pixel that clears an RGB tolerance of 10 even though
     no glyph is really there, which is exactly what made finding these
     splits by eye necessary before this mode existed. Luminance-only
     scanning isn't fooled by that fringing.

     This call is **always safe to use automatically and never needs a
     human to eyeball anything**: if the detected word count doesn't
     match `total_words` — the common failure mode is punctuation-heavy
     PII like an email address, whose `@`/`.`/`+` characters routinely
     create extra apparent breaks a plain word-count can't predict — it
     *silently falls back* to covering the whole run (`"scope":
     "whole_line"` in the response, with `fallback_reason` saying why),
     the same safe result `plan` would have given. A response with
     `"scope": "word_range"` means the narrow box was used; report which
     one happened either way (see the report format in `SKILL.md`) — a whole-line fallback is a
     fine, still-fully-automatic outcome, just a less surgical one for
     that specific occurrence, and is never itself a reason to flag
     anything for manual work.
1. Convert `cover_box` from exported-pixel coordinates to frame-local
   coordinates before writing anything to Figma — subtract the same bleed
   offset rule 10 documents (left 5px, top 5px): `frame_x = export_x - 5`,
   `frame_y = export_y - 5`. Width and height are unaffected by the bleed.
1. Create one plain `RECTANGLE` node per occurrence — no stroke, solid fill
   at `color_rgb` (divide each channel by 255) — inside the resolved frame.
   Batch every occurrence for the same image into one `use_figma` script,
   since they all land in the same frame and should appear together:
   ```js
   const frame = await figma.getNodeByIdAsync("<frameId>");
   const covers = [
     { x: X1, y: Y1, w: W1, h: H1, color: { r: R1/255, g: G1/255, b: B1/255 } },
     // ...one entry per occurrence, already converted to frame-local coordinates
   ];
   const createdIds = [];
   for (const c of covers) {
     const rect = figma.createRectangle();
     rect.name = "PII redaction";
     rect.fills = [{ type: "SOLID", color: c.color }];
     rect.strokes = [];
     frame.appendChild(rect);
     rect.resize(c.w, c.h);
     rect.x = c.x; rect.y = c.y;
     createdIds.push(rect.id);
   }
   return { frameId: frame.id, createdIds };
   ```
1. Re-export via `download_assets(fileKey, nodeId)` — no
   `defaultFormat`/`defaultScale` override (per the re-export rule in
   `auto-fix-procedure.md`) — and overwrite the local file (after the backup, as usual).

## Verification

Re-runs the same script's `verify` mode — the window it checks depends on
which planning mode produced the cover, and using the wrong one either
misses a real leak or fails a genuinely correct fix:

* **Whole run** (`plan`): verify the **same search window** that was
  passed to `plan`, not just the cover box that was drawn:
  ```
  python3 -B <skill-dir>/scripts/redact_pii_region.py verify "<image_path>" <x> <y> <w> <h> <r> <g> <b>
  ```
  Scanning the whole original window, not just the rectangle, is what
  catches a fragment that leaked just outside the cover instead of letting
  it pass by construction — the window only ever contained the PII, so
  every pixel in it should be background after the fix.
* **Word range** (`plan-word-range`): verify the **`cover_box` the response
  returned**, not the (much larger) search window passed in — the search
  window was deliberately sized to see the *whole* line so the word
  segmentation would work, and most of it is supposed to still show the
  kept-visible context text after the fix. Checking the full search window
  here doesn't add safety, it just fails a correct fix (the parts of the
  window outside `cover_box` were never meant to turn into background):
  ```
  python3 -B <skill-dir>/scripts/redact_pii_region.py verify "<image_path>" <cover_box.x> <cover_box.y> <cover_box.w> <cover_box.h> <r> <g> <b>
  ```
  This is still a meaningful check, not a rubber stamp: `plan-word-range`
  already proved every side of `cover_box` — the padded outer edges via the
  same RGB-tolerance margin check `plan` uses, the gap-derived inner
  edge(s) via the luminance scan that found the gap in the first place —
  was ink-free *before* the fix, so nothing outside the box could have
  legitimately leaked from a correctly-drawn rectangle; re-verifying the
  box's own interior confirms the fill itself landed correctly (right
  color, right position, nothing left unpainted inside it).
* When `plan-word-range` fell back to `"scope": "whole_line"`, verify it
  the same way as a plain `plan` result (the full search window) — the
  fallback *is* a whole-run cover, geometrically and safety-wise, just
  produced by the other function.

Pass condition either way: `verdict == "pass"` for **every** occurrence in
the image — one leaked occurrence fails the whole image's rule 7 fix.

**Rule 7's `verify` pass confirms the export is clean, nothing more.** A
`"pass"` verdict means the text is gone from the composited PNG the docs
site serves. It says nothing about the frame's underlying raw image asset,
which still holds the original pixels — repeat that caveat in the report
line for every rule 7 fix, not only once (see the report format in `SKILL.md`).

For rule 7 specifically, a fail on *any* occurrence means removing *every*
cover rectangle created for that image, not just the one that failed — a
half-covered set of occurrences is worse than none, since it looks fixed at
a glance.
