# Auto-fix procedure

Read this once, when the classification leaves at least one AUTO_FIX finding
and the run is allowed to fix (see `SKILL.md` Step 4). The per-rule mutation,
the re-export call and every rule-specific edge case live in the
`rule-*.md` files listed in the table near the end.

## Figma tools and availability

* Figma tools are named here by their bare tool name (`whoami`,
  `get_metadata`, `use_figma`, ...). Your client prefixes them: Claude Code
  as `mcp__<server>__<tool>`, Copilot CLI as `<server>-<tool>` (for a server
  called `figma`: `figma-use_figma`). Use whichever form your client lists.
  If the server lists `create_session`, call it once per Figma file key and
  pass the returned `sessionId` on every later call to that file.
* Call `whoami` once, only now, never for a run with nothing to fix. If it
  errors, don't abort the run: skip the whole auto-fix phase, keep every
  finding as pending in the report, and add one line saying the automatic
  fixes were skipped because Figma was unavailable. Say it once, up front,
  rather than discovering it after N failed per-image attempts. Rules 2 and 7
  are Figma-dependent too (rule 2 renames the matching Figma frame, rule 7
  draws into it), so without Figma they stay pending like the rest.

## Resolve the Figma frame map (once per article)

Skip entirely for an article with zero AUTO_FIX findings.

1. Grep the article's frontmatter for a `figma:` key (same pattern
   `validate-screenshots` uses to show its "Figma:" link). If missing or
   empty, every AUTO_FIX finding that needs Figma for this article's
   images becomes FLAG_ONLY instead — note this once at the article level.
   This now includes rule 2: without a resolvable Figma frame there's no
   way to keep the file and frame names in sync, so the naming issue is
   flagged for manual work rather than partially renamed. Same for rule 7:
   without a frame to draw the cover rectangle into, redaction can't
   happen, so it's flagged instead.
1. Parse it: `python3 -B <skill-dir>/scripts/parse_figma_url.py "<url>"` →
   `{"file_key": ..., "node_id": ...}`.
1. Call `get_metadata(fileKey, nodeId)` **once** per
   article. The common case is a `canvas` node listing every sibling
   `frame` as a direct child — if instead the frontmatter pointed straight
   at one `frame`, call `get_metadata(fileKey)` with no `nodeId` to find the
   containing page, then re-call `get_metadata` on that page.
1. Build a map from each target image's filename stem (no extension) to the
   Figma frame whose `name` matches exactly, falling back to a
   case/hyphen-insensitive substring match. If a stem matches zero or more
   than one frame, don't guess — every AUTO_FIX finding on that image
   becomes FLAG_ONLY (see the classification in `auto-fix-scope.md`), **except rule 10, which has its
   own fallback for a clean zero-frame-match case — see
   `references/rule-10-width.md`.**
1. For rule 6, also remember which frame(s) had a local image reporting
   `shadow: true` during detection — these are shadow donors for other frames on
   the same canvas.


## Apply the fixes

Before the first `use_figma` call this session, load the `/figma-use` skill
(or its MCP fallback `skill://figma/figma-use/SKILL.md`) and follow its
rules for every call after: pass `skillNames`, keep each script small and
incremental, always `return` the affected node IDs, never blindly retry
after an error. If neither can be loaded (for example in an unattended run
whose client has no such skill), carry on with those same rules as written
here; don't treat the missing skill as a reason to skip the fix.

For every fix: back up the current local PNG to the harness scratchpad
(never inside the repo) before overwriting it, and record whatever Figma
property is about to be mutated (a stroke/fill color, an `effectStyleId`,
a node's `width`/`height` before a resize) so a failed verification (Step
6) can be undone. For rule 10 specifically, this means recording
`width`/`height`/`x`/`y`/`strokeWeight` for the frame **and every child
about to be touched** — background and overlays alike — not just one.

**The local PNG can be stale relative to Figma.** A frame's checked-in PNG
may have been exported before a designer already fixed the underlying
Figma frame, or before its PNG export settings were even configured — so
the detection step's checkers and vision are judging a *snapshot*, not necessarily the
frame's current state. Recoloring or reapplying an existing property
(rules 3 wrong-color, 4, 5, 6) is harmless even when it turns out to
already be correct — the mutation is idempotent. But *creating* a new node
(rule 3 missing-highlight's instance, rule 7's redaction rectangle) is not:
duplicating something that's already there is a real, visible mistake, not
a no-op. Before either of those two fixes, call
`get_screenshot` on the target frame for a live
render and look for what you're about to add, rather than trusting the
local raster image alone to conclude it's missing.

**Re-export correctly — never pass `defaultFormat`/`defaultScale` to
`download_assets` as a reflex.** Every frame this skill touches already
carries its own `exportSettings` (`{format: "PNG", contentsOnly: true,
constraint: {type: "SCALE", value: 1}}`), and `contentsOnly: true` is what
makes Figma render the frame in isolation — with the TK-shadow's bleed (it
extends past the frame's own bounds, since `clipsContent` is `false`)
composited against true transparency. Passing `defaultFormat` or
`defaultScale` explicitly **overrides the node's own configured export
settings entirely** (this is documented behavior of the tool, not a bug in
it) and Figma falls back to compositing that bleed against the **page's
own canvas background color** instead of transparency. The result is flat
opaque pixels where the shadow should fade to nothing — invisible while
inspecting the frame in Figma itself (the canvas color is irrelevant
there), but a clearly visible halo once the PNG is placed on a white docs
page. This is a real visual regression, not a `has_shadow.py` calibration
quirk — see the amendment to the rule 6 verification note in `auto-fix-verify.md`.

Before **any** `download_assets` call in this skill:
1. Check the frame's `exportSettings` (a plain property read via
   `use_figma`; cheap to fold into whatever other read-only check that
   rule's fix already does).
1. If an entry with `format: "PNG"` already exists, call
   `download_assets(fileKey, nodeId)` with **no** `defaultFormat` and
   **no** `defaultScale` — let the node's own settings drive the export.
   This is the normal case for every rule below.
1. If no PNG entry exists yet, set one first via `use_figma`
   (`frame.exportSettings = [{ format: "PNG", contentsOnly: true,
   constraint: { type: "SCALE", value: 1 } }]`), confirm the write, *then*
   call `download_assets` with no override. Never reach for `defaultFormat`
   as a shortcut past fixing the node's own setting — that shortcut is
   exactly what bakes in the canvas background.

**`download_assets` returns a short-lived URL, not a file.** Fetch it with
`curl -f -L -o <path> '<url>'`, as the tool's own output instructs, and treat
the URL like a secret (don't echo it into the report). Don't swap in another
HTTP client with its default settings: the host answers those with an HTTP 202
challenge page instead of the image. A 202, an HTML body, or a file that
`file` doesn't report as PNG is a failed download, not an export, so go on to
the verification revert rather than installing it. If `curl` itself is denied (an
unattended run that wasn't allowed to reach the host), say so in the report as
the cause; don't retry through another client.

Once the Figma frame map is resolved, open the matching reference file
below for the rule being fixed — it has the exact node mutation, the
re-export call, and every rule-specific edge case. Nothing here duplicates
what's in them; the preamble above (backup, re-export gotcha) applies to
all of them.

| Rule | Reference |
|---|---|
| 1 — format | `references/rule-01-format.md` |
| 10 — width | `references/rule-10-width.md` |
| 2 — naming | `references/rule-02-naming.md` |
| 6 — shadow | `references/rule-06-shadow.md` |
| 3 — missing highlight | `references/rule-03-missing-highlight.md` |
| 3 wrong-color, 4, 5 — recolor | `references/rule-03-04-05-recolor.md` |
| 7 — PII | `references/rule-07-pii.md` |

