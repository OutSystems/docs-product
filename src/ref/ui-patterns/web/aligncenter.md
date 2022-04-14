---
tags: runtime-traditionalweb; 
summary: Advanced uses cases for the Align Center UI Pattern.
locale: en-us
guid: b4a62bda-9298-473c-bc03-c0acc4de20f3
---

# Align Center Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/aligncenter-8-diag.png>)

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .center-align | .center-align.flex-direction-row | When Orientation parameter is Horizontal |
| .center-align | .center-align.flex-direction-column | When Orientation parameter is Vertical |

## Advanced use case

### Set vertical align with custom content

1. Drag the AlignCenter pattern into the preview.

1. Set the Orientation parameter to Vertical.

    ![](<images/aligncenter-9-ss.png>)

1. Drag an image into the Align Center placeholder and add the `border-radius-circle` class.

1. Drag a container into AlignCenter placeholder and set the horizontal alignment to Center.

1. In the container, add a Text widget with the text "Scott Ritchie" and have its Style Class set to `heading-4`.

1. Add another Text widget with the text "Marketing Communications Manager" and enclose it in a container.

    ![](<images/aligncenter-10-ss.png>)

1. Drag a container into the AlignCenter placeholder and add a Text widget.

1. Type the text "02 Jan" and have its Style Class set to `font-size-xs text-neutral-6`.

    ![](<images/aligncenter-11-ss.png>)

1. Publish and test.

    ![](<images/aligncenter-12.png>)
