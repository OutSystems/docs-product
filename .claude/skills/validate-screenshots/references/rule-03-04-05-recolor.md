# Rule 3 wrong-color, rule 4, rule 5 — recolor in place

Referenced from `auto-fix-procedure.md`. Read the apply procedure's general
backup/re-export preamble in `auto-fix-procedure.md` before using this file.

The shape already exists; mutate its color property directly instead of
cloning a new node. Identify the exact node from `check_red.py`'s reported
wrong hex (rule 3) or a fresh vision read of the callout/arrow color (rules
4/5 have no scripted checker):

```js
const node = await figma.getNodeByIdAsync("<nodeId>");
const token = { r: 0xF2 / 255, g: 0x28 / 255, b: 0x00 / 255 }; // #F22800
if (recolorStroke && node.strokes?.length) {
  node.strokes = node.strokes.map(s => s.type === "SOLID" ? { ...s, color: token } : s);
}
if (recolorFill && node.fills?.length) {
  node.fills = node.fills.map(f => f.type === "SOLID" ? { ...f, color: token } : f);
}
return { nodeId, strokes: node.strokes, fills: node.fills };
```

* Rule 3 wrong-color: stroke only, never fill (the rubric's highlight has no
  fill).
* Rule 4: fill only, on the circle — never touch the white digit's own
  color.
* Rule 5: stroke, and the arrowhead's fill too if it's a separate node.

Re-export via `download_assets(fileKey, nodeId)` — no
`defaultFormat`/`defaultScale` override (per the re-export rule in
   `auto-fix-procedure.md`) — and overwrite (after backup).

Verification: rule 3 re-runs `check_red.py` (`red: ok #F22800`);
rules 4/5 have no scripted checker — verify with a fresh vision read against
the rubric's rule 4/5 criteria and mark the report line "(vision-verified)";
when in doubt, treat as failed.
