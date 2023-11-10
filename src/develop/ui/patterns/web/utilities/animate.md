---
tags: runtime-traditionalweb; 
summary: Animate adds default animations to emphasize elements as they appear on the screen.
locale: en-us
guid: 297aaf40-3584-4ed5-b1d4-7bfbbe3bbfaa
app_type: traditional web apps
platform-version: o11
---

# Animate

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Animate UI Pattern to create animations within your app. This UI pattern allows you to emphasize elements as they appear on screen which enhances the overall usability of the app.

![](<images/animate-10-ss.png>)

**How to use the Animate UI Pattern**

1. In Service Studio, in the Toolbox, search for `Animate`.

    The Animate widget is displayed.

    ![](<images/animate-11-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Animate widget into the Main Content area of your application's screen.

    ![](<images/animate-1-ss.png>)

1. Add the content you want to animate to Animate widget.

    In this example, we add an image by dragging the Image widget into Animate widget and selecting an image from the sample OutSystems UI images.

    ![](<images/animate-12-ss.png>)

1. Select the Animate widget, and on the **Properties** tab, set the relevant properties, for example, where you want the animation to enter and leave the screen and at what speed.

    ![](<images/animate-2-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EnterAnimation (EnterAnimation Identifier): Optional | Set how the animation enters the screen. <p><ul><li>EnterBottom</li> <li>EnterFade (default)</li><li>EnterLeft</li><li>EnterRight</li><li>EnterScale</li><li>EnterTop</li></ul></p> <p>Examples <ul><li>Entities.EnterAnimation.EnterLeft - Enters from the left of the screen</li><li>Entities.EnterAnimation.EnterTop - Enters from the top of the screen</li></ul></p>                                                                                                                                                                                                                                                          |
| LeaveAnimation (LeaveAnimation Identifier): Optional | Set how the animation leaves the screen. The predefined options available are:<p><ul><li>LeaveBottom</li> <li>LeaveFade (default)</li><li>LeaveLeft</li><li>LeaveRight</li><li>LeaveScale</li><li>LeaveTop</li></ul></p> <p>Examples <ul><li>Entities.LeaveAnimation.LeaveBottom - Leaves from the bottom of the screen</li><li>Entities.LeaveAnimation.LeaveRight - Leaves from the right of the screen</li></ul></p>                                                                                                                                                                                                             |
| Speed (Speed Identifier): Optional                   | Animation duration. Fast, normal, and slow are the predefined speeds available for the animation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Delay (Integer): Optional                            | Time to wait before animation starts (in milliseconds). The default value is 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ExtendedClass (Text): Optional                       | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
