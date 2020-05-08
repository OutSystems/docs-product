---
tags: runtime-traditionalweb; 
summary: Animate adds default animations to emphasize elements as they appear on the screen.
---

# Animate

You can use the Animate UI Pattern to create animations within your app. This UI pattern allows you to emphasize elements as they appear on screen which enhances the overall usability of the app. 

![](<images/animate-image-10.png>)

**How to use the Animate UI Pattern**

1. In Service Studio, in the Toolbox, search for `Animate`. 

    The Animate widget is displayed.

    ![](<images/animate-image-11.png>)

1. From the Toolbox, drag the Animate widget into the Main Content area of your application's screen.

    ![](<images/animate-image-1.png>)

1. Add the content you want to animate to Animate widget. 

    In this example, we add an image by dragging the Image widget into Animate widget and selecting an image from the sample OutSystems UI images.

    ![](<images/animate-image-12.png>)

1. Select the Animate widget, and on the **Properties** tab, set the relevant properties, for example, where you want the animation to enter and leave the screen and at what speed. 

    ![](<images/animate-image-2.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| EnterAnimation (EnterAnimation Identifier): Optional | Set how the animation enters the screen. <p><ul><li>EnterBottom</li> <li>EnterFade (default)</li><li>EnterLeft</li><li>EnterRight</li><li>EnterScale</li><li>EnterTop</li></ul></p> <p>Examples <ul><li>_Entities.EnterAnimation.EnterLeft_ - Enters from the left of the screen</li><li>_Entities.EnterAnimation.EnterTop_ - Enters from the top of the screen</li></ul></p> | 
| LeaveAnimation (LeaveAnimation Identifier): Optional | Set how the animation leaves the screen. The predefined options available are:<p><ul><li>LeaveBottom</li> <li>LeaveFade (default)</li><li>LeaveLeft</li><li>LeaveRight</li><li>LeaveScale</li><li>LeaveTop</li></ul></p> <p>Examples <ul><li>_Entities.LeaveAnimation.LeaveBottom_ - Leaves from the bottom of the screen</li><li>_Entities.LeaveAnimation.LeaveRight_ - Leaves from the right of the screen</li></ul></p> |
| Speed (Speed Identifier): Optional | Animation duration. Fast, normal, and slow are the predefined speeds available for the animation.| 
| Delay (Integer): Optional | Time to wait before animation starts (in milliseconds). The default value is 0. | 
| ExtendedClass (Text): Optional  |   Add custom style classes to the Animate UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the myclass style to the Animate UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Animate UI styles being applied.</li></ul></p> | 
