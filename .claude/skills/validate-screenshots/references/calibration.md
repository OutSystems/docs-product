# Calibration (one-off)

`visual-rules-screenshots.md` starts as a placeholder. To populate it:

1. Gather a reference set of approved PNG screenshots from `docs-next`.
1. Run `python3 <skill-dir>/scripts/calibrate.py <path-or-folder> [<path-or-folder> …]`.
   The script walks the paths, prints one image per turn, and expects the
   assistant to describe what it sees and cluster findings into concrete rules.
1. When done, the script writes a draft `visual-rules-screenshots.md`. Review
   and edit it — the skill uses whatever is in that file.
1. Re-run calibration whenever the Figma library changes (new highlight
   component, etc.) so the rubric stays current.

If the calibration output looks thin or inconsistent across runs, switch to
authoring the rules manually — the skill doesn't care how the file was
produced, only that it describes checkable rules.
