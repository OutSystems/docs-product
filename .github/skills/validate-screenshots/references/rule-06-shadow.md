# Rule 6 (shadow) — effect clone

Referenced from `auto-fix-procedure.md` (apply) and `auto-fix-verify.md`
(verify). Read the apply procedure's general backup/re-export preamble in
`auto-fix-procedure.md`
before using this file.

## Apply

1. Resolve the **frame node itself**, not its inner image/rectangle child —
   the TK-shadow effect is a real Figma effect style applied on the frame.
1. Pick a donor: a sibling frame on the same canvas whose detection verdict was
   `shadow: true`. Read its style with a read-only `use_figma` script:
   ```js
   const donor = await figma.getNodeByIdAsync("<donorFrameId>");
   return { effectStyleId: donor.effectStyleId, effects: donor.effects };
   ```
1. Apply it to the broken frame:
   ```js
   const broken = await figma.getNodeByIdAsync("<brokenFrameId>");
   if (donorEffectStyleId) {
     await broken.setEffectStyleIdAsync(donorEffectStyleId);
   } else {
     broken.effects = JSON.parse(JSON.stringify(donorEffects));
   }
   return { mutatedNodeId: broken.id, appliedEffectStyleId: broken.effectStyleId };
   ```
1. If no sibling on this canvas currently passes, fall back to
   `search_design_system({ fileKey, query: "TK-shadow" })` (try a couple of
   query variants — the tool matches a single intent, not an OR of terms).
   If a published style turns up, import it
   (`figma.importStyleByKeyAsync`) and assign it the same way.
1. If neither a donor nor a library style is found, don't synthesize a
   drop-shadow from `has_shadow.py`'s pixel-feather tolerances — those
   describe the rendered *result* of the real effect, not its actual
   parameters, and guessing risks merely fooling the detector rather than
   fixing anything. Flag it as manual-only instead.
1. Re-export via `download_assets(fileKey, nodeId)` — no
   `defaultFormat`/`defaultScale` override (per the re-export rule in
   `auto-fix-procedure.md`) — and overwrite (after backup).

## Verification

**Rule 6 is a deliberate exception to "re-run the same checker the rule uses."**
Testing against a real Figma frame with the actual TK/Shadow effect
(`DROP_SHADOW`, radius 10, offset (5,5), color `#00000040` — confirmed via
`get_metadata` to match the design library exactly) showed that
`has_shadow.py`'s feather-length tolerance was calibrated against PNGs
exported through Figma's own Export UI, and doesn't match what this
skill's own re-export path (`download_assets`) produces for the identical,
correctly-applied effect — the rendered feather comes out shorter and more
symmetric than the calibration expects, so a genuinely correct fix would
still read `shadow: wrong` and get needlessly reverted. Until
`has_shadow.py`'s calibration is regenerated against `download_assets`
output specifically, verify rule 6 by reading the frame's own
`effectStyleId`/`effects` back from Figma instead — that's the property
the fix actually controls, and it isn't sensitive to the rendering
mismatch. `validate-screenshots` itself is unaffected by this — it only
ever reads screenshots that already exist, it never re-exports through
this path.

Pass condition: matches the donor's `effectStyleId` (or the imported
library style's), confirmed structurally — **not** a re-run of
`has_shadow.py`.

**Amendment — the likely real cause, found later.** A subsequent run traced
at least part of this "wrong" reading to the `defaultFormat`/`defaultScale`
override bug described in the re-export rule in `auto-fix-procedure.md`, not purely a
feather-length calibration gap: re-exporting the same frames via
`download_assets(fileKey, nodeId)` with **no** override (letting the node's
own `exportSettings` apply) produced a `shadow: true` verdict from
`has_shadow.py` directly, with an alpha falloff profile matching Figma's own
Export UI output almost exactly. Sample size is small (three frames), so
this isn't proven to eliminate every case the paragraph above describes —
keep verifying rule 6 via `effectStyleId`/`effects` as the safe fallback,
since it's cheap and never wrong — but if `has_shadow.py` keeps reading
`wrong` on a frame this skill re-exported *without* a `defaultFormat`/
`defaultScale` override, that's now a real signal worth investigating
directly (e.g. a genuinely different or missing effect), not something to
dismiss as the known calibration gap by default.
