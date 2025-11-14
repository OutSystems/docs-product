---
tags: ux/ui design, css customization, ui patterns, user interaction, outsystems ui framework
summary: Explore the features and functionalities of tabs in OutSystems 11 (O11) for Mobile and Reactive Web Apps, including events, layout, and CSS selectors.
locale: en-us
guid: 8b2184cf-f3d0-4bbc-a6f8-b78509902cf0
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=612:392
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Tabs Reference

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

## Events

| **Event Name** |  **Description** |  **Mandatory** |
| ---|---|--- |
| OnTabChange  |  Triggered when switching tabs.  |  _False_ |

## Layout and Classes

![Diagram illustrating the layout and CSS classes for the Tabs UI pattern in mobile and reactive web apps](images/tabs-layout-classes-diag.png "Tabs Layout and Classes Diagram")

## CSS Selectors

| **Element** |  **CSS Class** |  **Description** |
| ---|---| --- |
| Tabs Wrapper  |  .tabs  |  Container that wraps all Tabs elements. |
| Active tab header  |  .tabs-header-tab-active  |  Represents the header of the active element. |
| Open tab content  |  .tabs-content-tab-open  |  The dot that represents the content of the open item. |
