# Rule 2 (naming) — rename + relink + Figma frame rename

Referenced from `auto-fix-procedure.md` (apply) and `auto-fix-verify.md`
(verify/revert). Read the apply procedure's general backup/re-export preamble
in `auto-fix-procedure.md` before using this file.

## Apply

All three happen together, or none of them do. A finding that reached this
step already has an unambiguous Figma frame resolved for its *old* stem in
the frame map — if the frame map couldn't resolve one (no `figma:` key, no match, or
ambiguous match), this finding was already downgraded to FLAG_ONLY and
never reaches the apply step at all. Don't rename the local file for a rule 2
finding without a resolved frame.

1. Choose the corrected filename:
   * Character-set-only violation (uppercase, spaces, stray punctuation)
     with an otherwise-valid suffix — mechanical normalization
     (lowercase, collapse invalid characters to `-`); no vision needed.
   * Missing or undocumented suffix, or a suffix-vs-content mismatch — pick
     the suffix vision judges to match what's actually shown, applying
     `visual-rules-screenshots.md`'s `-diag` (genuine diagram vs. UI
     screenshot) and `-sa` (genuine Sample app) checklists verbatim.
   * Double suffix — keep whichever of the two matches the content and
     drop the other.
   * If vision lands on the rubric's own documented ambiguous case (e.g. a
     `-sa` file matching neither the diagram nor Sample-app traits), don't
     rename — flag it.
1. ```
   python3 -B <skill-dir>/scripts/rename_and_relink.py "<old_path>" "<new_path>"
   ```
   It re-validates the new name against `check_metadata.py`'s own rules
   before renaming, so it can never produce a name that still fails rule 2.
   It reports a collision or a missing repo root as an error rather than
   guessing around it — treat either as a fix failure (see `auto-fix-verify.md`). Nothing on
   the Figma side has been touched yet, so a failure here needs no
   rollback beyond what the script itself already refused to do.
1. On success, rename the Figma frame the frame map resolved for `<old_path>`'s
   stem, and confirm from the same return value — no separate read-back
   call, mirroring rule 6's pattern:
   ```js
   const frame = await figma.getNodeByIdAsync("<frameId>");
   frame.name = "<newStem>";
   return { mutatedNodeId: frame.id, name: frame.name };
   ```
   Pass condition: the returned `name` equals `<newStem>` exactly.
1. If the `use_figma` call throws, or the returned name doesn't match, roll
   back the local side — see the Revert section below. Never leave the
   file/markdown renamed while the Figma frame still carries the old name,
   or vice versa.

## Revert (verification failure path)

Rule 2's revert works differently from the raster-mutation rules. There's
no PNG backup to restore — the "fix" is a rename, not a pixel edit — so
reverting means running the rename in reverse:
```
python3 -B <skill-dir>/scripts/rename_and_relink.py "<new_path>" "<old_path>" --skip-naming-check
```
This undoes both the file and the markdown reference in one call (the
script's rewrite logic is symmetric). `--skip-naming-check` is required
here: when rule 2 fired because the *original* name failed
`check_metadata.py`'s own naming check (not just a vision-only suffix
mismatch), reverting to that name would otherwise be rejected by the same
guard that flagged it in the first place. Then, best-effort, also attempt
to rename the Figma frame back to its original name if it had already been
changed before verification failed (wrap in try/catch; note in the report
whether that undo itself succeeded).
