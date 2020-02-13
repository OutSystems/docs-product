---
tags: runtime-traditionalweb; 
summary: AlignCenter places content horizontally or vertically within a container.
---

# AlignCenter

Place content to horizontally or vertically align to the center of the container.

Use AlignCenter to center content horizontally or vertically within a container and to align many elements with different heights or widths.  

**How to use**

Add two or more elements inside the placeholder and they will be centered according to the selected orientation.

1. Drag AlignCenter pattern into the preview.

1. Drag the UserInitials pattern into AlignCenter placeholder.

1. In the Name input parameter, type "Scott Ritchie" (for instance).

    ![](<images/aligncenter-image-1.png>)

1. Drag the Text widget into AlignCenter placeholder and type "Scott Ritchie".

    ![](<images/aligncenter-image-2.png>)

1. Publish and test.

![](<images/aligncenter-image-3.png>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Orientation  |  Set the orientation of the content inside. | Orientation Identifier | False | Entities.Orientation.Horizontal |
| ExtendedClass  |  Add custom style classes to this Block. | Text | False | none |

## Layout and Classes

![](<images/aligncenter-image-4.png>)

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .center-align | .center-align.flex-direction-row | When Orientation parameter is Horizontal |
| .center-align | .center-align.flex-direction-column | When Orientation parameter is Vertical |

## Advanced Use Case

### Set vertical align with custom content

1. Drag the AlignCenter pattern into the preview.

1. Set the Orientation parameter to Vertical.

    ![](<images/aligncenter-image-5.png>)

1. Drag an image into the AlignCenter placeholder and add the `border-radius-circle` class.

1. Drag a container into AlignCenter placeholder and set the horizontal alignment to Center.

1. In the container, add a Text widget with the text "Scott Ritchie" and have its Style Class set to `heading-4`.

1. Add another Text widget with the text "Marketing Communications Manager" and enclose it in a container.
    
    ![](<images/aligncenter-image-6.png>)

1. Drag a container into the AlignCenter placeholder and add a Text widget.

1. Type the text "02 Jan" and have its Style Class set to `font-size-xs text-neutral-6`.

    ![](<images/aligncenter-image-7.png>)

1. Publish and test.

    ![](<images/aligncenter-image-8.png>)
