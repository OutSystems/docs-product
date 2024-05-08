---
tags: runtime-traditionalweb; 
summary: Explore UI customization options for the Progress Circle in OutSystems 11 (O11).
locale: en-us
guid: 26092480-0d4f-441c-aeca-c82f31a3df51
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=615%3A541&mode=design&t=Cx8ecjAITJrQMvRn-1
---

# Progress Circle Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of the Progress Circle UI pattern for Traditional Web Apps](images/progresscircle-3-diag.png "Progress Circle Layout Diagram")

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .progress-circle | .progress-circle .progress-circle-content |  When IsSemiCircle parameter is False  |
| .progress-circle | .progress-circle .progress-semi-circle-content |  When IsSemiCircle parameter is True  |

## Advanced use case

### Change color of progress circle based on value

1. On your screen, create a local variable called Progress (Integer type).

1. Drag the Progress Circle pattern into the preview.

1. Set the Value of the Progress Circle's Progress parameter.

1. To change the color of the Progress Circle based on values, create a condition and set limits. 

    In this example, 3 colors represent different states of progress. Set the value of the ProgressColor parameter to `If(Progress <= 50, Entities.Color.Red, If( Progress > 50 and Progress < 75,  Entities.Color.Yellow ,  Entities.Color.Green))`.
    
    ![Screenshot showing how to set the Progress Circle color based on value conditions in Traditional Web Apps](images/progresscircle-4-ss.png "Progress Circle Color Change Example")

1. Publish and test.

    ![Animated GIF demonstrating the color change in the Progress Circle based on different value conditions](images/progresscircle-5-ss.gif "Progress Circle Color Change Demonstration")

### Remove the round corners of the Progress Circle

To remove the round corners, use this CSS snippet.

```css
.progress-circle svg {
    stroke-linecap: square;
}
```

![Screenshot displaying the Progress Circle with square corners after CSS modification to remove round corners](images/progresscircle-6-ss.png "Progress Circle Without Round Corners")

### Change the trail thickness of the Progress Circle

To change the trail thickness, set the AdvancedFormat property to `{trailWidth: 1}`.

![Screenshot showing the Progress Circle with a customized trail thickness using the AdvancedFormat property](images/progresscircle-7-ss.png "Progress Circle Trail Thickness Adjustment")
