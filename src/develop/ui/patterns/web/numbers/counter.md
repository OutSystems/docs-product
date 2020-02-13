---
tags: runtime-traditionalweb; 
summary: Counter shows the total number of occurrences of several values regarding a single topic.
---

# Counter

Give feedback about the current count of several elements.

Use the Counter to show the total number of occurrences of several values regarding a single topic.

**How to use**

Add content to the placeholder and set the orientation and height of the pattern.

1. Drag the Counter pattern into the preview.

1. Set the Input Parameters to extend the default values.

1. Publish and test.

    ![](<images/counter-image-1.png>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Orientation  | Set the orientation. | Orientation Identifier | False | Entities.Orientation.Horizontal |
| Height  | Height of the block, use Pixel units. | Text | False | 100 |
| ExtendedClass  |  Add custom style classes to this Block. |  Text | False | none |

## Layout and Classes

![](<images/counter-image-2.png>)

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .center-align | .flex-direction-column |  When Orientation is Vertical  |

## Advanced Use Case

### Add a new style to the Counter pattern

1. Drag the Counter pattern into the preview.

1. Set the Orientation to `Vertical`, Height to `200` and ExtendedClass property to `background-blue shadow-xl`.

    ![](<images/counter-image-3.png>)

1. Drag a container into Counter placeholder and type '26'.

1. Set the Style Classes property of the container to `font-size-display text-neutral-0`.

1. Drag a container into Counter placeholder and type 'Completed Requests'.

1. Drag another container into Counter placeholder.

1. Drag an Icon Widget into the container and set the Name property to `Entities.IconName.check` and Size to `Entities.IconSize.Size_3x`.
    
    ![](<images/counter-image-4.png>)

1. Publish and test.
    
    ![](<images/counter-image-5.png>)
