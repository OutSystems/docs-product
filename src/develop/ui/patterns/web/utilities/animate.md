---
tags: runtime-traditionalweb; 
summary: Animate adds default animations to emphasize elements as they appear on the screen.
---

# Animate

Create animations on elements inside the placeholder.

Use Animate to add default animations to emphasize elements as they appear on the screen. Animations should resemble familiar real-life movements, helping the user understand the interface.  

**How to use**

Drag the content inside the placeholder and configure the animation type of the Block. You can also define the start time and duration of the animation.

1. Drag the Animate pattern into the preview.

1. Set the content you need on the placeholder.

    ![](<images/animate-image-1.png>)

1. Set the Input Parameters to extend the default values.

    ![](<images/animate-image-2.png>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| EnterAnimation | Set the enter animation.| EnterAnimation Identifier | _False_ | Entities.EnterAnimation.EnterFade |
| LeaveAnimation | Set the leave animation.| LeaveAnimation Identifier | _False_ | Entities.LeaveAnimation.LeaveFade |
| Speed | Time necessary for the animation reach the end. | Speed Identifier | _False_ | None |
| Delay | Time to wait before animation starts, in miliseconds | Integer | _False_ | 0 |
| ExtendedClass  |  Add custom style classes to this Block. | Text | _False_ | None |

## Layout and Classes

![](<images/animate-image-3.png>)

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .animate-wrapper | .is--visible |  When the animation will enter in the screen  |
| .animate-wrapper | .is--hidden |  When the animation will leave in the screen |
| .animate | .enter-bottom |  When the animation will enter in the screen from bottom |
| .animate | .enter-fade |  When the animation will enter in the screen with fade |
| .animate | .enter-left |  When the animation will enter in the screen from left |
| .animate | .enter-right |  When the animation will enter in the screen from right |
| .animate | .enter-scale |  When the animation will enter in the screen with scale |
| .animate | .enter-top |  When the animation will enter in the screen from top |
| .animate | .leave-bottom |  When the animation will leave the screen from bottom |
| .animate | .leave-fade |  When the animation will leave the screen with fade |
| .animate | .leave-left |  When the animation will leave the screen from left |
| .animate | .leave-right |  When the animation will leave the screen from right |
| .animate | .leave-scale |  When the animation will leave the screen with scale |
| .animate | .leave-top |  When the animation will leave the screen from top |
| .animate | .animate-slow | The animation will reach the end in 1500ms |
| .animate | .animate-fast | The animation will reach the end in 500ms |


## Advanced Use Case

### Use the ToggleAnimate Server Action

It is possible to hide elements in the screen using an Animation.

1. Set a name to the Animate pattern.

1. Set the method of the On Click function to Submit and in the Destination property, create a new Action.

    ![](<images/animate-image-4.png>)

1. In the Action created, drag the ToggleAnimate Action and set the Widget ID.

    ![](<images/animate-image-5.png>)

1. Publish and test.

    ![](<images/animate-image-6.gif?width=600>)

### Use Animations On Scroll

It is possible to load and animate the elements when they are not visible in the screen.

1. Drag the LoadOnVisible Pattern. Add the Animate Pattern with the desired content inside LoadOnVisible.

    ![](<images/animate-image-7.png>)

1. Publish and test.

    ![](<images/animate-image-8.gif?width=600>)

