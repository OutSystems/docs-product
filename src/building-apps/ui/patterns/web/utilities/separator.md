---
tags: ui design, user interface patterns, web development, visual organization, ui components
summary: Learn how to use the Separator UI Pattern in OutSystems 11 (O11) to enhance visual organization in Traditional Web Apps.
locale: en-us
guid: c2f627d5-7dbf-4c75-a18e-43635917c6e6
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=249%3A5&mode=design&t=u4ANW5BJS7Flsdmg-1
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Separator

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Separator UI Pattern to separate content clearly and ease visual organization.

  ![Example of Separator UI Pattern used to divide content in a Traditional Web App](images/separator-1.png "Separator UI Pattern Example")

**How to use the Separator UI Pattern**

1. In Service Studio, in the Toolbox, search for `Separator`.

    The Separator widget is displayed.

    ![Service Studio displaying the Separator widget in the Toolbox](images/separator-5-ss.png "Service Studio Separator Widget")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Separator widget into the Main Content area of your application's screen, where you want to separate content. In this example, we drag the widget in between an image and some text.

    ![Dragging the Separator widget into the Main Content area in Service Studio](images/separator-7-ss.png "Dragging Separator Widget in Service Studio")

1. On the **Properties** tab, set the relevant (optional) properties, for example, the color and the amount of space separating the content.

    ![Properties tab in Service Studio for customizing the Separator widget](images/separator-8-ss.png "Separator Widget Properties")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property**                       | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Color (Color Identifier): Optional | Set the color for the separator line. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>Blank - Displays a gray (Neutral4) line (default value).</li><li>Entities.Color.Red - Displays a red line.</li></ul></p>                                                                                                                                                                                                                                                                                                                            |
| Space (Space Identifier): Optional | Set the space around the separator line. The predefined vales are: <p><ul><li>None</li><li>Extra small</li><li>Small</li><li>Base</li><li>Medium</li><li>Large</li><li>Extra large</li><li>Extra extra large</li></ul></p><p>Examples <ul><li>Blank - Displays a space of 16px (Entities.Space.Base) around the line separator. This is the default value.</li><li>Entities.Space.Large - Displays a space of 32px around the line separator.</li></ul></p>                                                                                                                                                                        |
| IsVertical (Boolean): Optional     | If False, the separator line displays horizontally (default). If True, the separator line displays vertically.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ExtendedClass (Text): Optional     | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
