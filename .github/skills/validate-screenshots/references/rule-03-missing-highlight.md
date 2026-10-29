# Rule 3, missing highlight — placement without a confirm step

Referenced from `auto-fix-procedure.md`. Read the apply procedure's general
backup/re-export preamble in `auto-fix-procedure.md` before using this file.

1. Find the article's step text naming the control to click or select, near
   this image's reference.
1. Cross-reference the frame's structure (`get_design_context`/
   `get_metadata`) for a node whose name or text matches that control, and
   independently confirm via vision on the raster image that the same
   control is visible at roughly that location. That raster image is the
   *local* file, which can be stale — it may predate a designer already
   placing the highlight directly in Figma, or predate the frame's PNG
   export settings being configured at all. Before concluding "no highlight
   exists" from the local image alone, call
   `get_screenshot` on the resolved frame for a live
   render and check it too: instantiating a duplicate on top of one that's
   already there is a real, visible mistake, not a harmless no-op like
   re-applying an already-correct color (rule 3 wrong-color) would be.
1. If the text-based match and the vision-based read disagree, or nothing
   matches at all, don't guess a location — flag it instead of placing a
   highlight in the wrong spot.
1. Otherwise, find the highlight component. Search the literal, most likely
   component name on its own (e.g. `"Highlight"`) rather than a descriptive
   phrase — `search_design_system` ranks by name match, so adding words like
   `"rectangle"` or the library name actually dilutes the match and buries
   the real component under unrelated results (`Highlighter`, `ic_highlight`,
   icon-library noise, etc. from other teams' libraries). A bare `"Highlight"`
   query surfaces it as a top result even alongside that noise. When more
   than one library has a same-named component, prefer whichever
   `libraryName` matches the library that owns the TK-shadow effect already
   confirmed elsewhere on this canvas (rule 6) — that's the design system
   this file actually draws from, not a same-named component in an unrelated
   library. If nothing plausible turns up after that, only then conclude no
   highlight component exists. Instantiate the match at the resolved
   bounding box:
   ```js
   const main = await figma.importComponentByKeyAsync("<componentKey>");
   const instance = main.createInstance();
   (await figma.getNodeByIdAsync("<frameId>")).appendChild(instance);
   instance.x = X; instance.y = Y;
   instance.resize(W, H);
   return { newNodeId: instance.id, x: instance.x, y: instance.y, width: instance.width, height: instance.height };
   ```
1. Re-export via `download_assets(fileKey, nodeId)` — no
   `defaultFormat`/`defaultScale` override (per the re-export rule in
   `auto-fix-procedure.md`) — and overwrite (after backup).
