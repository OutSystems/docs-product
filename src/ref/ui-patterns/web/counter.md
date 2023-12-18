---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Counter UI Pattern.
locale: en-us
guid: c41f4255-ed4b-4aae-a934-9eebbcfcc129
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:437
---

# Counter Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout and classes of the Counter UI Pattern](images/counter-2-diag.png "Counter Pattern Layout Diagram")

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .center-align | .flex-direction-column |  When Orientation is Vertical  |

## Advanced use case

### Add a new style to the Counter Pattern

1. Drag the Counter pattern into the preview.

1. Set the Orientation to `Vertical`, Height to `200` and ExtendedClass property to `background-blue shadow-xl`.

    ![Screenshot of the Counter pattern with vertical orientation and custom styles applied](images/counter-3-ss.png "Counter Pattern Vertical Orientation")

1. Drag a container into Counter placeholder and type '26'.

1. Set the Style Classes property of the container to `font-size-display text-neutral-0`.

1. Drag a container into Counter placeholder and type 'Completed Requests'.

1. Drag another container into Counter placeholder.

1. Drag an Icon Widget into the container and set the Name property to `Entities.IconName.check` and Size to `Entities.IconSize.Size_3x`.
    
    ![Screenshot showing the Counter pattern with a number, text label 'Completed Requests', and a check icon widget](images/counter-4-ss.png "Counter Pattern with Icon Widget")

1. Publish and test.
    
    ![Screenshot of the published Counter pattern in a Traditional Web App interface](images/counter-5-ss.png "Published Counter Pattern")
