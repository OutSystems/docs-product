# Rule 1 (format) — re-export

Referenced from `auto-fix-procedure.md`. Read the apply procedure's general
backup/re-export preamble in `auto-fix-procedure.md` before using this file — it covers the
`defaultFormat`/`defaultScale` gotcha every rule here depends on.

1. Confirm the frame's `exportSettings` already include a `format: "PNG"`
   entry (per the re-export rule in
   `auto-fix-procedure.md`) — fix it via `use_figma`
   first if not, then call `download_assets(fileKey, nodeId)` for the frame
   the frame map resolved for this image, with **no** `defaultFormat`/`defaultScale`
   override. A pure format fix never changes the frame's size, only its
   export format, and the node's own setting already produces PNG at 1x —
   there's nothing to override. Download the result and overwrite the
   local file (after the backup).
1. If rule 1 also means the extension itself must change (e.g. the source
   was `.jpg`), call `rename_and_relink.py` with the corrected `.png` path
   so the rename and every markdown reference update happen in one step.
1. If no matching frame exists for a rule 1 finding, don't guess — flag it:
   "no matching Figma frame named `<stem>` found; needs a manual
   re-export."
