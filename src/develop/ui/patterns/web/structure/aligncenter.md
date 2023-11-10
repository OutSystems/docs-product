---
tags: runtime-traditionalweb; 
summary: Align Center places content horizontally or vertically within a container.
locale: en-us
guid: 88f0dd67-0dcf-44c3-ad3e-41977550015c
app_type: traditional web apps
platform-version: o11
---

# Align Center

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use Align Center UI Pattern to center content horizontally or vertically on the screen. 

![](<images/aligncenter-1.png>)

**How to use the Align Center UI Pattern**

This example shows you how to center align a user's name and initials.

1. In Service Studio, in the Toolbox, search for `Align Center`. 

    The Align Center widget is displayed.

    ![](<images/aligncenter-2-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Align Center widget into the Main Content area of your application's screen.
    
    ![](<images/aligncenter-3-ss.png>)
   
1. From the Toolbox, drag the User Initials pattern into the Align Center placeholder.

1. On the **Properties** tab, in the Name property, enter a name. In this example, we enter **Scott Ritchie**.

    ![](<images/aligncenter-4-ss.png>)

1. Add the relevant content to the Align Center widget. In this example we add some text (Scott Richie) and an image. 

    ![](<images/aligncenter-5-ss.png>)

1. On the Align Center **Properties** tab, you can set the content's orientation (either vertical or horizontal).

    ![](<images/aligncenter-6-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. 

**Without Align Center UI Pattern** 

![](<images/aligncenter-7-ss.png>)

**With Align Center UI Pattern**

![](<images/aligncenter-8-ss.png>)

## Properties

| **Property**                                   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Orientation (Orientation Identifier): Optional | Set the content orientation, either horizontal or vertical.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ExtendedClass (Text): Optional                 | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |



