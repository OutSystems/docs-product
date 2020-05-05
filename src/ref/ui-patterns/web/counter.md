---


tags: runtime-traditionalweb; 
summary: Advanced Use Cases for the Counter UI Pattern
---

# Counter UI Pattern Reference

## Layout and classes

![](<images/counter-image-2.png>)

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .center-align | .flex-direction-column |  When Orientation is Vertical  |

## Advanced use case

### Add a new style to the Counter Pattern

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
