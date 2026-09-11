---
summary: OutSystems 11 (O11) UI patterns and widgets that require extra configuration to meet WCAG 2.2 AA accessibility compliance.
tags:
  - Accessibility
  - OutSystems UI
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
  - unblock
topic:
  - accessibility-screen-reader
isautopublish: true
---

# UI patterns accessibility

Most OutSystems UI patterns and widgets are **WCAG 2.2 AA** compliant by default. However, a few of them rely on complex interactions that assistive technologies don't always interpret correctly, so they need additional configuration to stay accessible.

## Known issues {#known-issues}

This section indicates the UI patterns and widgets that might require manual effort to be fully compliant with WCAG 2.2 AA, according to your version of **OutSystems UI** and **Platform Server**. All other patterns and widgets are WCAG 2.2 compliant by default.

### OutSystems UI patterns

The table below lists the UI patterns that might require manual effort to be compliant with WCAG 2.2 AA, depending on your [OutSystems UI version](../patterns/intro.md#version). Follow the documentation link in the **UI pattern** column to see the detailed accessibility guidelines for each pattern.

Patterns not listed in this table are compliant by default since **OutSystems UI 2.24.0**.

<div class="info" markdown="1">

If you're upgrading OutSystems UI to a version that includes WCAG 2.2 AA compliance for a pattern, you must remove any manual workaround from that pattern before upgrading. See the pattern's accessibility guidelines for specific details.

</div>

| UI pattern | WCAG 2.2 AA compliant by default? | Compliant since OutSystems UI version |
| --- | --- | --- |
| [Accordion](../patterns/mobile/content/accordion.md#accessibility) | Yes | 2.29.0 |
| [Action Sheet](../patterns/mobile/interaction/actionsheet.md#accessibility) | Yes | 2.29.0 |
| [Animated Label](../patterns/mobile/interaction/animatedlabel.md#accessibility) | No<br/> (requires manual effort) | - |
| [Badge](../patterns/mobile/numbers/badge.md#accessibility) | No<br/> (requires manual effort) | - |
| [Blank Slate](../patterns/mobile/content/blankslate.md#accessibility) | Yes | 2.29.0 |
| [Card Background](../patterns/mobile/content/cardbackground.md#accessibility) | No<br/> (requires manual effort) | - |
| [Carousel](../patterns/mobile/interaction/carousel.md#accessibility) | Yes | 2.29.0 |
| [Counter](../patterns/mobile/numbers/counter.md#accessibility) | No<br/> (requires manual effort) | - |
| [Inline SVG](../patterns/mobile/utilities/inlinesvg.md#accessibility) | Yes | 2.29.0 |
| [Lightbox](../patterns/mobile/interaction/lightboximage.md#accessibility) | No<br/> (requires manual effort) | - |
| [Master Detail](../patterns/mobile/adaptive/masterdetail.md#accessibility) | No<br/> (requires manual effort) | - |
| [Notification](../patterns/mobile/interaction/notification.md#accessibility) | No<br/> (requires manual effort) | - |
| [Progress circle](../patterns/mobile/numbers/progresscircle.md#accessibility) | No<br/> (requires manual effort) | - |
| [Range Slider Interval](../patterns/mobile/interaction/rangesliderinterval.md#accessibility) | No<br/> (requires manual effort) | - |
| [Submenu](../patterns/mobile/navigation/submenu.md#accessibility) | Yes, optional improvements recommended | 2.24.0 |
| [Tabs](../patterns/mobile/navigation/tabs.md#accessibility) | Yes | 2.29.0 |
| [Tag](../patterns/mobile/content/tag.md#accessibility) | No<br/> (requires manual effort) | - |
| [Tooltip](../patterns/mobile/content/tooltip.md#accessibility) | No<br/> (requires manual effort) | - |
| [User Avatar](../patterns/mobile/content/useravatar.md#accessibility) | Yes | 2.29.0 |
| [Wizard](../patterns/mobile/navigation/wizard.md#accessibility) | No<br/> (requires manual effort) | - |

### Widgets

From Platform Server 11.43.0, you can [enable built-in WCAG 2.2 AA compliance](intro.md#enable-widgets) for the widgets that weren't yet built-in compliant.

The table below lists the widgets that might require manual effort to be compliant with WCAG 2.2 AA, depending on your [Platform Server version](https://www.outsystems.com/tk/redirect?g=98a6a460-e03e-4610-ab03-d9e1eda2239c). Follow the documentation link in the **Widget** column to see the detailed accessibility guidelines for each widget.

Widgets not listed in this table are WCAG 2.2 compliant by default.

<div class="info" markdown="1">

When upgrading to Platform Server 11.43.0 or higher, if you enable built-in WCAG 2.2 AA compliance, you must remove any manual workaround from that widget before upgrading. See the widget's accessibility  guidelines for specific details.

</div>

| Widget | Compliant since Platform Server version |
| --- | --- |
| [Button](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-button.md#accessibility) | 11.43.0, optional improvements recommended |
| [Checkbox](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-checkbox.md#accessibility) | 11.43.0 |
| [Dropdown](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-dropdown.md#accessibility) | 11.43.0 |
| [Input](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-input.md#accessibility) | 11.43.0 |
| [Link](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-link.md#accessibility) | 11.43.0 |
| [List](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-list.md#accessibility) | 11.43.0 |
| [List item](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-listitem.md#accessibility) | 11.43.0 |
| [Popover menu](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-popover.md#accessibility) | 11.43.0 |
| [Popup](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-popup.md#accessibility) | 11.43.0 |
| [Radio button](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-radiobutton.md#accessibility) | 11.43.0 |
| [Radio group](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-radiogroup.md#accessibility) | 11.43.0 |
| [Switch](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-switch.md#accessibility) | 11.43.0 |
| [Upload](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-upload.md#accessibility) | 11.43.0 |
