---
summary: OutSystems 11 (O11) UI patterns that require extra configuration to meet WCAG 2.2 AA accessibility compliance.
tags:
  - Accessibility
  - OutSystems UI
  - UI
  - UI Patterns
  - Widgets
locale: en-us
guid: 41f4db30-ace4-4972-8cad-f954f43cd831
app_type: reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=186:35
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - service studio
coverage-type:
  - remember
topic:
  - accessibility-screen-reader
isautopublish: true
---

# UI patterns accessibility

Most OutSystems widgets and OutSystems UI patterns are **WCAG 2.2 AA** compliant by default. However, a few patterns rely on complex interactions that assistive technologies don't always interpret correctly, so they need additional configuration to stay accessible.

## Known issues {#known-issues}

Depending on your [OutSystems UI version](../patterns/intro.md#version), the UI patterns listed in this section might require additional work to be fully compliant with WCAG 2.2 AA. Patterns not listed in the table below are compliant by default since **OutSystems UI 2.24.0**.

In the table below, follow the link for each **UI pattern** to see the pattern's guidelines for these situations:

* Accessibility workaround for patterns that are not WCAG 2.2 AA compliant by default and require manual effort.

* Guidelines for patterns that are compliant since a specific OutSystems UI version, in case you previously adapted or customized it.

<div class="info" markdown="1">

If you're upgrading OutSystems UI to a version that includes WCAG 2.2 AA compliance for a pattern, you must remove any manual workaround from that pattern before upgrading. See the pattern guidelines for specific details.

</div>

| UI pattern | WCAG 2.2 AA compliant by default? | Compliant since OutSystems UI version |
| --- | --- | --- |
| [Accordion](../patterns/mobile/content/accordion.md#accessibility) | Yes | 2.29.0 |
| [Action Sheet](../patterns/mobile/interaction/actionsheet.md#accessibility) | Yes | 2.29.0 |
| [Animated Label](../patterns/mobile/interaction/animatedlabel.md#accessibility) | No<br/> (requires manual effort) | - |
| [Badge](../patterns/mobile/numbers/badge.md#accessibility) | No<br/> (requires manual effort) | - |
| [Blank Slate](../patterns/mobile/content/blankslate.md#accessibility) | Yes | 2.29.0 |
| [Button](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-button.md#accessibility) | No<br/> (requires manual effort) | - |
| [Card Background](../patterns/mobile/content/cardbackground.md#accessibility) | No<br/> (requires manual effort) | - |
| [Carousel](../patterns/mobile/interaction/carousel.md#accessibility) | Yes | 2.29.0 |
| [Counter](../patterns/mobile/numbers/counter.md#accessibility) | No<br/> (requires manual effort) | - |
| [Dropdown](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-dropdown.md#accessibility) | No, if **Options Content** = **Custom**<br/> (requires manual effort) | - |
| [Inline SVG](../patterns/mobile/utilities/inlinesvg.md#accessibility) | Yes | 2.29.0 |
| [Lightbox](../patterns/mobile/interaction/lightboximage.md#accessibility) | No<br/> (requires manual effort) | - |
| [List](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-list.md#accessibility) | No<br/> (requires manual effort) | - |
| [Master Detail](../patterns/mobile/adaptive/masterdetail.md#accessibility) | No<br/> (requires manual effort) | - |
| [Notification](../patterns/mobile/interaction/notification.md#accessibility) | No<br/> (requires manual effort) | - |
| [Popover menu](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-popover.md#accessibility) | No<br/> (requires manual effort) | - |
| [Popup](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-popup.md#accessibility) | No<br/> (requires manual effort) | - |
| [Progress circle](../patterns/mobile/numbers/progresscircle.md#accessibility) | No<br/> (requires manual effort) | - |
| [Range Slider Interval](../patterns/mobile/interaction/rangesliderinterval.md#accessibility) | No<br/> (requires manual effort) | - |
| [Submenu](../patterns/mobile/navigation/submenu.md#accessibility) | Yes, optional improvements recommended | 2.24.0 |
| [Switch](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-switch.md#accessibility) | No<br/> (requires manual effort) | - |
| [Tabs](../patterns/mobile/navigation/tabs.md#accessibility) | Yes | 2.29.0 |
| [Tag](../patterns/mobile/content/tag.md#accessibility) | No<br/> (requires manual effort) | - |
| [Tooltip](../patterns/mobile/content/tooltip.md#accessibility) | No<br/> (requires manual effort) | - |
| [User Avatar](../patterns/mobile/content/useravatar.md#accessibility) | Yes | 2.29.0 |
| [Wizard](../patterns/mobile/navigation/wizard.md#accessibility) | No<br/> (requires manual effort) | - |
