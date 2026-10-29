# Rule 10 (oversized width) — resize the source frame or bare shape, then re-export

Referenced from `auto-fix-procedure.md`. Read the apply procedure's general
backup/re-export preamble in `auto-fix-procedure.md` before using this file — it covers the
`defaultFormat`/`defaultScale` gotcha every rule here depends on.

## Resolve which procedure applies

1. If the frame map resolved an unambiguous **frame** for this image's stem, follow
   the Frame procedure below.
1. If the frame map found **no** frame match at all, don't jump straight to
   flagging it — re-check the same canvas the frame map already read (from its one
   `get_metadata` call) for exactly one **other** child whose name matches
   this stem the same way the frame map matches frames (exact, falling back to a
   case/hyphen-insensitive substring match) — a bare shape (a rectangle or
   similar) sitting directly on the canvas, with no enclosing frame at all.
   Some real screenshots are built this way instead of inside a frame. If
   exactly one such match exists, follow the Bare shape procedure below —
   **for rule 10 only**. Every other rule still requires an actual frame:
   if this same image also has a non-width finding, that other finding
   stays FLAG_ONLY regardless of this fallback resolving the width one.
1. Anything else — zero matches even after this fallback, or more than one
   same-stem bare shape on the canvas — don't guess, flag it: "no matching
   Figma frame or shape named `<stem>` found; needs a manual resize and
   re-export."

## Frame procedure

1. Read the matched frame's current `width` and `height` from the frame map's
   metadata (both are already present on the resolved frame node — no
   extra Figma call needed).
1. The target width is a fixed **1180px**, not a ratio or percentage of the
   current width. Reason: `download_assets` bakes in rule 6's TK-shadow
   effect as a fixed-pixel bleed on top of whatever the frame's own width
   is — the effect's asymmetric feather adds left 5px + right 15px = 20px
   onto width, confirmed empirically (a 1566px-wide frame exported at the
   default scale came out 1586px, exactly +20). Sizing the frame itself to
   1180px means the exported result lands at 1180 + 20 = 1200px. Never
   recompute this target from the exported/measured width, and never turn
   it into a percentage-of-current-width formula — the bleed is a fixed
   pixel offset baked into the effect style, not a percentage of frame
   size.
1. Compute the target height proportionally from the frame's own current
   width/height — never from the previously-exported/measured width, which
   already includes the 20px bleed and isn't the right basis for the
   frame's own aspect ratio:
   `target_height = round(1180 * frame_height / frame_width)`.
1. Confirm the frame's structure before resizing anything. Read-only
   `use_figma` script — reads every child's type, rotation, and fill kind,
   not just its bounding box:
   ```js
   const frame = await figma.getNodeByIdAsync("<frameId>");
   const children = frame.children;
   return {
     frameId: frame.id,
     frameWidth: frame.width,
     frameHeight: frame.height,
     children: children.map(c => ({
       id: c.id,
       name: c.name,
       type: c.type,
       x: c.x,
       y: c.y,
       width: c.width,
       height: c.height,
       rotation: c.rotation,
       hasImageFill: Array.isArray(c.fills) && c.fills.some(f => f && f.type === "IMAGE"),
     })),
   };
   ```
   Classify the returned children:
   * **Background candidate**: a child with `x === 0`, `y === 0`,
     `width === frame.width`, `height === frame.height`, `rotation === 0`
     (allow a `0.01°` epsilon for float noise), and `hasImageFill === true`.
     There must be **exactly one** such child. If there are zero or more
     than one, don't guess — flag: "frame `<frame-name>` has no
     unambiguous full-bleed image-fill background child; needs a manual
     resize."
   * **Overlay candidates**: every remaining child — typically a Highlight
     instance from rule 3, or a small patch/callout rectangle. Each must
     satisfy **all** of:
       * `type` is `"INSTANCE"` or `"RECTANGLE"` — an explicit allow-list,
         not a blocklist. A `TEXT` node, a nested `FRAME`/`COMPONENT`, a
         `VECTOR`, `GROUP`, `ELLIPSE`, or `LINE` never qualifies,
         regardless of size or position.
       * `rotation` is `0` (same epsilon as above).
       * Fully contained in the frame:
         `x >= 0 && y >= 0 && (x + width) <= frame.width && (y + height) <= frame.height`.
     If **any** overlay fails **any** of these, don't resize anything on
     this frame — flag it, naming the specific offending child and the
     guard it failed, e.g. "frame `<frame-name>` has a child
     `<child-name>` (TEXT) that isn't an Instance/Rectangle overlay; needs
     a manual resize" or "...child `<child-name>` (RECTANGLE) is rotated
     12°..." or "...child `<child-name>` (INSTANCE) extends outside the
     frame bounds...".
   * As a defensive backstop against a structure this pattern was never
     meant to handle, cap it at **8 total children** (background +
     overlays combined) — a frame with more is flagged rather than
     attempted, regardless of whether every individual child would
     otherwise pass.
   * If the background candidate and every overlay candidate pass, proceed
     to the mutation step below with the full set of
     `{backgroundChildId, overlayChildIds: [...]}` (`overlayChildIds` may
     be empty — a bare background-only frame is just the trivial case of
     the same algorithm).
1. If the pattern matches, resize the frame and every child (background
   plus overlays) in one atomic mutation script. Use `.resizeWithoutConstraints()`
   everywhere — on the frame itself too, not just its children. Never
   `.resize()`: it cascades to children per each child's own `constraints`
   property (MIN/MAX/CENTER/STRETCH/SCALE), which can't be assumed safe for
   an arbitrary overlay — `resizeWithoutConstraints()` bypasses that
   cascade entirely, so nothing moves except what this script explicitly
   sets. Never `.rescale()` either (rescale would also shrink the
   TK-shadow effect's stroke weight/radius/offset, which must stay at its
   original absolute px values for the frame-size-independent bleed this
   fix relies on to hold — the same reasoning applies to an overlay
   Highlight instance's own stroke weight, which the rubric requires to
   stay a fixed ~2–3px regardless of the highlighted element's size).
   Frame, background, and every overlay are resized in one atomic script
   because they must all move in lockstep — a partial mutation (background
   resized but an overlay left behind) would be visibly *more* broken than
   doing nothing, since the overlay would now be misaligned against the
   resized background rather than merely oversized:
   ```js
   const frame = await figma.getNodeByIdAsync("<frameId>");
   const targetWidth = 1180;
   const targetHeight = <targetHeight>; // from the proportional formula above
   const factor = targetWidth / frame.width;

   const backgroundId = "<backgroundChildId>";
   const overlayIds = [/* zero or more overlay child IDs */];

   frame.resizeWithoutConstraints(targetWidth, targetHeight);

   const background = await figma.getNodeByIdAsync(backgroundId);
   background.resizeWithoutConstraints(targetWidth, targetHeight);
   background.x = 0;
   background.y = 0;

   const overlays = [];
   for (const overlayId of overlayIds) {
     const overlay = await figma.getNodeByIdAsync(overlayId);
     const preStrokeWeight = typeof overlay.strokeWeight === "number" ? overlay.strokeWeight : null;

     const newWidth = Math.round(overlay.width * factor);
     const newHeight = Math.round(overlay.height * factor);
     const newX = Math.round(overlay.x * factor);
     const newY = Math.round(overlay.y * factor);

     overlay.resizeWithoutConstraints(newWidth, newHeight);
     overlay.x = newX;
     overlay.y = newY;

     // strokeWeight is an absolute-px value that only .rescale()-style ops
     // multiply — resizeWithoutConstraints() shouldn't touch it, but this
     // is unverified for INSTANCE nodes specifically. Force it back if it
     // drifted; if the property throws on write, let the script fail —
     // verification treats that as a normal revert-and-flag, never a silent
     // partial fix.
     if (preStrokeWeight !== null && overlay.strokeWeight !== preStrokeWeight) {
       overlay.strokeWeight = preStrokeWeight;
     }

     overlays.push({
       id: overlay.id, x: overlay.x, y: overlay.y,
       width: overlay.width, height: overlay.height,
       strokeWeight: typeof overlay.strokeWeight === "number" ? overlay.strokeWeight : null,
     });
   }

   return {
     mutatedNodeIds: [frame.id, background.id, ...overlayIds],
     frameWidth: frame.width,
     frameHeight: frame.height,
     background: { id: background.id, x: background.x, y: background.y, width: background.width, height: background.height },
     overlays,
   };
   ```
   Known limitation: the `strokeWeight` check/restore above only looks at
   the **instance root** — if a real Highlight component's stroke actually
   lives on an internal child node instead, this silently no-ops (reads
   `undefined`, skips the correction) rather than catching drift. Accepted
   for now, same spirit as the Rule 6 `has_shadow.py` calibration note in
   `references/rule-06-shadow.md` — flag it as a follow-up if it turns out
   to matter in practice. Independently rounding each overlay's scaled
   `x`/`y`/`width`/`height` can also introduce ±1px drift relative to the
   background on frames with several overlays — cosmetic, within the
   rubric's own "~2–3 px stroke" tolerance, not worth engineering around.
1. `download_assets(fileKey, nodeId)` — **no** `defaultFormat`/
   `defaultScale` override (per the re-export rule in
   `auto-fix-procedure.md`); the
   frame is already the right size and already carries its own PNG export
   setting, so the node-configured default is exactly what's wanted.
   Download the result and overwrite the local file (after the backup).
1. If `check_metadata.py` still reports `width.verdict == "warn"` after
   this (rounding, or a bleed that turns out not to be perfectly constant
   across frames), don't recompute a new target width and re-export again
   — the "never retry the same fix blindly after an error" rule applies
   here too. Treat it as a verification failure: revert the frame's, background's,
   and every overlay's `width`/`height`/`x`/`y`/`strokeWeight` back to what
   was recorded before this resize (same `resizeWithoutConstraints()` +
   explicit `x`/`y`/`strokeWeight` assignment approach as the forward
   mutation, run node-by-node in reverse), restore the backed-up PNG, and
   leave the finding pending with "— automatic fix reverted:
   <the still-failing verdict>" appended.
1. If no matching frame exists for a rule 10 finding, don't guess — flag
   it: "no matching Figma frame named `<stem>` found; needs a manual
   resize and re-export."

## Bare shape procedure

A bare shape has no children by construction (a `RECTANGLE` node can't
nest anything in Figma's model), so there's no background/overlay
classification to do here — the shape itself is the whole image.

1. Check for anything else sharing this shape's space before touching it.
   Read-only `use_figma` script:
   ```js
   const shape = await figma.getNodeByIdAsync("<shapeId>");
   const canvas = shape.parent;
   const overlapping = canvas.children.filter(c => {
     if (c.id === shape.id) return false;
     const noOverlapX = c.x + c.width <= shape.x || shape.x + shape.width <= c.x;
     const noOverlapY = c.y + c.height <= shape.y || shape.y + shape.height <= c.y;
     return !(noOverlapX || noOverlapY);
   });
   return {
     shapeId: shape.id, x: shape.x, y: shape.y,
     width: shape.width, height: shape.height,
     overlappingIds: overlapping.map(c => c.id),
   };
   ```
   If `overlappingIds` is non-empty, don't resize — flag: "shares canvas
   space with `<N>` other node(s) (`<ids>`); needs a manual resize." A
   highlight or patch meant to sit on top of a bare shape has to live as a
   *sibling* on the canvas, not a child (this node type can't have one) —
   and this skill has no way to safely reposition/rescale a sibling in
   lockstep with the shape the way the Frame procedure does for real
   overlay children, so don't attempt it.
1. If nothing overlaps, compute the target the same way as the Frame
   procedure: width **1180px**, height proportional
   (`round(1180 * shape_height / shape_width)`). Unlike a frame, this
   width does **not** reliably predict the final exported pixel width —
   whether an effect bleeds beyond a bare shape's own bounds during export
   depends entirely on whether *this specific node* happens to carry one.
   Checked directly against real docs screenshots at their *current* (not
   post-resize) size: some bare shapes export at exactly their own size
   (no bleed at all), others export with the same +20px-in-both-dimensions
   bleed a frame's TK-shadow produces (`radius 10, offset (5,5)`) — so the
   effect, when present, is applied to this node type directly, not just
   to frames. That comparison was never run *after* a resize on a real
   node (this skill never mutates production Figma files to prove a
   point), so treat "1180 in, ~1180 or ~1200 out" as a reasonable
   assumption carried over from the pre-resize evidence, not a confirmed
   post-resize measurement. 1180 is a safe starting target either way — it
   lands at exactly 1180px with no bleed, or near 1200px with the
   frame-style bleed, and both pass the `≤ 1200px` check — but never
   document or assume a guaranteed final width the way the Frame
   procedure's "+20 → 1200" reasoning does. Verification (or
   reverting) is what actually confirms it, not this math.
1. Resize the shape directly — a single mutation, nothing else to
   coordinate:
   ```js
   const shape = await figma.getNodeByIdAsync("<shapeId>");
   shape.resizeWithoutConstraints(1180, <targetHeight>); // from the formula above
   return { mutatedNodeId: shape.id, width: shape.width, height: shape.height };
   ```
1. `download_assets(fileKey, nodeId)` — **no** `defaultFormat`/
   `defaultScale` override (per the re-export rule in
   `auto-fix-procedure.md`).
   Download the result and overwrite the local file (after the backup).
1. If `check_metadata.py` still reports `width.verdict == "warn"` after
   this, don't recompute and retry — same "never retry the same fix
   blindly after an error" rule as the Frame procedure. This is the
   expected outcome for the cases where this node's export bleed can't be
   predicted in advance (see above) — landing here isn't a bug, it's the
   designed fallback for genuine uncertainty. Revert: resize the shape
   back to its recorded original `width`/`height`, restore the backed-up
   PNG, and leave the finding pending with "— automatic fix reverted:
   <the still-failing verdict>" appended.
