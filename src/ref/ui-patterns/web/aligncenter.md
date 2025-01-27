---
tags: ui design, css customization, web development, layout management
summary: Learn how to use the Align Center UI pattern in Traditional Web Apps with OutSystems 11 (O11) for effective layout management and customization.
locale: en-us
guid: b4a62bda-9298-473c-bc03-c0acc4de20f3
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:357
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Align Center Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout and classes for Align Center UI Pattern in Traditional Web Apps](images/aligncenter-8-diag.png "Align Center Layout Diagram")

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .center-align | .center-align.flex-direction-row | When Orientation parameter is Horizontal |
| .center-align | .center-align.flex-direction-column | When Orientation parameter is Vertical |

## Advanced use case

### Set vertical align with custom content

1. Drag the AlignCenter pattern into the preview.

1. Set the Orientation parameter to Vertical.

    ![Screenshot demonstrating setting vertical align with custom content using Align Center pattern](images/aligncenter-9-ss.png "Align Center Vertical Orientation Screenshot")

1. Drag an image into the Align Center placeholder and add the `border-radius-circle` class.

1. Drag a container into AlignCenter placeholder and set the horizontal alignment to Center.

1. In the container, add a Text widget with the text "Scott Ritchie" and have its Style Class set to `heading-4`.

1. Add another Text widget with the text "Marketing Communications Manager" and enclose it in a container.

    ![Screenshot showing Align Center pattern with an image and text widgets for a user profile](images/aligncenter-10-ss.png "Align Center with Custom Content Screenshot")

1. Drag a container into the AlignCenter placeholder and add a Text widget.

1. Type the text "02 Jan" and have its Style Class set to `font-size-xs text-neutral-6`.

    ![Screenshot of Align Center placeholder with a Text widget displaying the date in a small font size](images/aligncenter-11-ss.png "Align Center Text Widget Screenshot")

1. Publish and test.

    ![Image of the published result after testing the Align Center UI Pattern with custom content](images/aligncenter-12.png "Align Center Published Result")
