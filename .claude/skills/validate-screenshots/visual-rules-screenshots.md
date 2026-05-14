# Screenshot validation rubric

**Calibrated:** 2026-04-23 by Bernardo (12-image sample from
`docs-next/src/eap/building-apps/data/fetch-data/images/`, PNGs only,
excluding `-diag`).

Focus areas (from the calibration brief): highlight component, shadow, naming
convention, format. A few adjacent rules are included where they were obvious
from the reference set (cursor, PII) — these can be kept or deleted on review.

The skill uses this file as a checklist. Each rule has:

* **Severity** — `❌` means fail; `⚠️` means warn.
* **Check** — what the skill verifies on each screenshot.
* **Pass example / Fail example** — filenames from the reference set where
  possible.

## 1. File format — must be PNG

* **Severity:** ❌
* **Check:** the file extension is `.png` (lowercase). Other raster formats
  (`.jpg`, `.jpeg`, `.gif`, `.webp`, `.bmp`) and `.svg` are not valid for a UI
  screenshot in `docs-next`. **Verdict comes from `scripts/check_metadata.py`
  (`format.verdict`).**
* **Pass example:** `aggregate-create-ss.png`
* **Fail example:** any image ending in `.jpg`, `.gif`, etc.

## 2. Naming — lowercase, digits, hyphens, surface suffix

* **Severity:** ❌
* **Check (scripted):** the filename (without extension) matches
  `^[a-z0-9]+(-[a-z0-9]+)*$` and ends with exactly one of the documented
  source suffixes: `-ss`, `-odcs`, `-pl`, `-lt`, `-sc`, `-usr`, `-fg`,
  `-at`, `-ct`, `-af`, `-gc`, `-ams`, `-ib`, `-eb`, `-we`, `-az`, `-vs`,
  `-ok`, `-fc`, `-diag`, `-sa`, `-is`. Double suffixes are rejected.
  (`-diag` is for diagrams, not screenshots, so if a screenshot uses it the
  skill warns.) **Verdict comes from `scripts/check_metadata.py`
  (`naming.verdict`).**
* **Check (vision):** the suffix must also match the surface actually shown
  in the image — e.g. a screenshot of ODC Studio should end in `-odcs`, not
  `-ss`. This part is vision-only; the script can't see the pixels.
* **Pass example:** `mashup-join-odcs.png`, `database-columns-aggregate-ss.png`
* **Fail example:** `LastExternalWrite-odcs.png` (mixed case),
  `start-ExternalWrite-odcs.png` (mixed case), `crossjoin-example.png` (no
  surface suffix), `emanuel-rodrigues-ss-odcs.png` (double suffix),
  `action1-ss.png` (suffix says Service Studio but image shows ODC Studio).

## 3. Highlight — red rectangle outline on the focal element

* **Severity:** ❌ when the screenshot illustrates a specific click or focused
  element and no highlight is present; ⚠️ when a highlight is present but the
  red doesn't match the design-system token (a sign the rectangle was drawn
  by hand instead of dropped from the Figma library).
* **Check (vision):** for screenshots that are part of a step ("click X",
  "open the Y panel"), the focal element is surrounded by a red rectangle
  outline — sharp corners, uniform ~2–3 px stroke, no fill. Multiple red
  rectangles are fine when there are multiple focal elements. Reference
  images never use a filled highlight, a dashed stroke, or any other color.
* **Check (scripted):** any closed red rectangle in the image must use the
  design-system token `#F22800`. **Verdict comes from
  `scripts/check_red.py`** — it looks for thin axis-aligned strokes ≥20 px
  long that appear on BOTH the horizontal and vertical axes (i.e. a closed
  rectangle outline, not a single underline or filled region) and reports
  the dominant rectangle stroke color. Verdicts: `red: ok #RRGGBB`,
  `red: wrong #RRGGBB (token #F22800)`, `red: none`. Older / hand-drawn
  variants observed in the corpus include `#CC2200`, `#BB1F00`, `#FF0000`,
  `#A00000`; all flag as ⚠️ with the actual hex shown.

  Native red UI that the captured product happens to render — Service
  Studio's MERGE button (filled), the OutSystems logo, red error text in
  TrueChange (glyph shapes), the active tab underline in Service Center
  (horizontal-only), pink conflict-row backgrounds — are intentionally
  ignored: none of them match the closed-rectangle geometry. Diagonal red
  arrows and very small Figma rectangles (<20 px on a side) are also
  out of scope; vision still catches a wrong-coloured arrow.

  Vision can't reliably distinguish `#F22800` from `#CC2200` from `#BB1F00`
   — trust the script's hex over your own color read.
* **Alignment (when multiple rectangles form a grid layout):** rectangles
  that map to side-by-side or stacked regions of the UI should share edges —
  rectangles in the same row share top/bottom edges; rectangles in the same
  column share left/right edges. Misaligned edges within a group are ⚠️
  (a designer should re-snap them in Figma). Vision-only check; the skill
  has no programmatic detector for this yet.
* **Pass example:** `aggregate-create-ss.png` (three red outlines over the
  right-click menu item + a fourth around the tree node);
  `select-source-ss.png` (red outline on the selected row + red outline on
  the **Select** button).
* **Fail example:** would be a green or blue highlight, a filled rectangle,
  or the whole screenshot reshot without any highlight on an obvious
  step-target.

## 4. Numbered callouts — red circle, white digit

* **Severity:** ⚠️
* **Check:** when steps have an explicit order, each step is tagged with a
  red-filled circle containing a white digit. Same red `#F22800` as rule 3.
  Digits start at `1`. Placement options, in order of preference:
    * top-left corner of the red rectangle (preferred);
    * top-right corner of the red rectangle;
    * centered inside the red rectangle, when the highlighted region is
      large and mostly empty (corner placement would float in whitespace).

    If the article enumerates steps in prose (1., 2., 3.), the image should
    carry matching numbered callouts.
* **Pass example:** `nl-get-data-ss.png` (circles labelled **1** and **2**,
  top-right of each highlighted control).
* **Fail example:** would be numbered labels that don't use the circle
  component, white circle with red digit, or sequence gaps (1, 3).

## 5. Arrows — red solid line with arrowhead

* **Severity:** ⚠️
* **Check:** when the screenshot shows a drag or a "goes here" relationship,
  the connection is a solid red line with a filled arrowhead on the
  destination. Same red `#F22800` as rule 3. Dashed or double-headed arrows are not
  used in the reference set.
* **Pass example:** `aggregate-server-side-ss.png` (red arrow from the
  Aggregate tool tile to the destination node).
* **Fail example:** would be a black arrow, a dashed line, or an arrow in a
  non-standard color.

## 6. Shadow / outer frame — mandatory on full-surface captures

* **Severity:** ❌
* **Check:** every screenshot that captures a large surface (editor canvas,
  full modal, full browser window, full app page) **must** carry the
  design-system frame applied in Figma on top of the raster capture. The
  frame is one of:
    * a subtle grey outer border (≈ `#CCCCCC`, 1 px), and/or
    * a soft outer drop shadow that separates the image from the article's
      white background.
  Close crops of a single bounded component (a dropdown, a context menu, a
  button with its label, a single tab strip) don't need the frame — their
  own borders do the job.
* **OS window chrome is NOT the shadow.** macOS traffic lights, Windows
  titlebars, browser tabs, and any chrome captured as part of the raster
  pixel are content, not frame. The design-system shadow is a separate
  element added **in Figma, outside** the captured rectangle — it lives on
  the image border, not inside it. If the image ends abruptly at the edge
  of the OS window with no extra pixels of grey border or soft shadow around
  it, rule 6 fails regardless of how polished the captured chrome looks.
* **How the skill detects it:** call `scripts/has_shadow.py <image>` and use
  its verdict as authoritative. The script walks inward from each edge
  mid-point and measures the _feather length_ — the band of partially-
  transparent pixels between optional fully-transparent padding and the
  first opaque content pixel. The OutSystems shadow token produces an
  asymmetric feather (top 5 px, left 5 px, right 15 px, bottom 15 px),
  so the script accepts only profiles within tolerance of those values.
  Possible verdicts:
    * `shadow: true` — feather present on all four edges and matches the
      asymmetric token. ✅
    * `shadow: wrong` — feather present but the profile doesn't match
      (symmetric shadow, too narrow, too wide, missing on one side, etc).
      Treat this as ❌: the image has a shadow-like effect but it isn't
      the design-system frame. Common causes: a CSS box-shadow captured
      inside the screenshot pixels, a manually drawn shadow, or an export
      from a non-Figma source.
    * `shadow: false` — no feathered alpha on any edge (content runs
      straight to the border, or there's only a 1-px hard border). ❌ for
      large-surface captures, ⚠️ otherwise — never a clean pass. The
      close-crop exemption is a reviewer call, not a skill call: surface
      every `false` verdict so the designer can decide. Note that a 1-px
      gray border alone — which the rule allows as an alternative to the
      soft shadow — also reads as `false`.
    * `shadow: unknown` — the image has no alpha channel (typically a JPG
      saved as `.png`). Rule 1 already fails this case.

  Vision cannot reliably detect any of this on dark-theme images, so do
  not second-guess the script.
* **Pass example:** `aggregate-server-side-ss.png`, `data-mashup-odcs.png`
  (both have a visible grey outer border around a full-editor capture).
* **Fail example:** `action1-ss.png` — full ODC Studio window with macOS
  chrome visible, but no grey border or drop shadow outside that chrome;
  the dark-theme background runs to the image edge.

## 7. Cursor — present on interaction screenshots

* **Severity:** ⚠️
* **Check:** screenshots that document a click, drag, or hover include a
  cursor icon positioned on or immediately next to the highlighted element.
  Use one of the three Figma cursor components — never a raw vector:
  `cursor-white`, `cursor-black`, `cursor-hand`. Informational screenshots
  (output panels, result views, overviews) don't need a cursor.
* **Pass example:** `aggregate-create-ss.png` (cursor on the right edge of
  the highlighted menu item); `add-source-ss.png` (cursor just below the
  **Add source** button).
* **Fail example:** a "click **Save**" step screenshot with no cursor at all.

## 8. No PII / customer data

* **Severity:** ❌
* **Check:** any personal data shown is obviously synthetic — no real names
  or email addresses, no tenant IDs that look like customers, no real
  telephone numbers. The reference set uses placeholder data
  (`Sample_Employee`, `Mr John Watson`, `john.watson@company.com`,
  `MarketPlace` app).
* **Pass example:** `data-mashup-odcs.png`, `listed-products-by-category-odcs.png`
* **Fail example:** would be a screenshot showing `@outsystems.com` emails
  of real people, or a support ticket with a customer's company name.

## 9. No internal environment URLs or hostnames

* **Severity:** ❌
* **Check:** no internal OutSystems environment URL, staging subdomain,
  development-only tenant, or infrastructure hostname is visible in the
  screenshot. This includes browser address bars, application tabs, footer
  status bars, and any overlay chrome. Common leaks spotted in the reference
  fail set:
    * `eng-stage-us-01.outsystems.dev`, `*.outsystems.dev`, `*.outsystems.app`
    * internal tenant names like `eng-stage-*`, `qa-*`, `internal-*`
    * development server IPs or private VPN hostnames
    * internal Jira / ticket IDs (`RDTKF-*`, `TK-*`) visible on screen
  Use the public OutSystems demo/training environments instead, or blur the
  hostname before export.
* **Pass example:** the browser tab reads `training-prd.outsystems.app` or a
  generic demo URL.
* **Fail example:** `action-odcs.png` (browser tab shows
  `eng-stage-us-01 - eng-stage-us-01.out...`), `emanuel-rodrigues-odcs.png`
  (footer shows `eng-stage-us-01.outsystems.dev`).

## 10. Theme must match the captured surface

* **Severity:** ❌ when the theme contradicts the mandate in the table
  below; ⚠️ when the suffix isn't listed yet.
* **Check:** the theme (light vs dark) must match what the surface
  mandates. The surface is identified by the filename suffix, so this rule
  reads together with rule 2.

| Suffix | Surface | Theme mandate |
| --- | --- | --- |
| `-ss` | Service Studio | light only |
| `-odcs` | ODC Studio | light only |
| `-pl` | ODC Portal | dark only |
| `-lt` | LifeTime | light only (no dark mode exists) |
| `-sc` | Service Center | light only (no dark mode exists) |
| `-usr` | Users | light or dark (both allowed) |
| `-fg` | Forge | light only |
| `-we` | Workflow editor | dark only |

  Surfaces not listed (e.g. `-at`, `-ams`, `-ib`, etc.) have no theme
  mandate yet — flag as ⚠️ and ask the designer. Confirmed mandates are
  added to the table as they come up.

* **Pass example:** `apps-pl.png` (dark-mode ODC Portal), any light-mode
  Service Studio capture like `aggregate-create-ss.png`.
* **Fail example:** `apps-lalal-pl.png` (light-mode, but `-pl` must be
  dark), `data-mashup-odcs.png` (dark-mode, but `-odcs` must be light).

## 11. Maximum width — 1200 px

* **Severity:** ⚠️
* **Check:** the PNG's pixel width is at most 1200 px. Wider captures render
  poorly on the docs site and are hard to re-use. Heights are not
  constrained. **Verdict comes from `scripts/check_metadata.py`
  (`width.verdict` and `width.px`; numbered `width` in the JSON refers to
  this rule even though it's now rule 11).**
* **Pass example:** `aggregate-server-side-ss.png` (533 × 593).
* **Fail example:** any export wider than 1200 px — e.g. a full retina
  editor grab at 2560 × 1440.

## Rules the skill should treat as informational only

The following aren't rules per se, but the skill can surface them as ⚠️ when
clearly off:

* **Theme consistency**: the reference set mixes light (Service Studio,
  Portal) and dark (ODC Studio editor) themes. Within a single article,
  screenshots should use a consistent theme unless the article explicitly
  contrasts the two.
