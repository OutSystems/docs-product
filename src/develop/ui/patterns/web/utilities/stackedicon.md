---
tags: runtime-traditionalweb; 
summary: Stacked Icon expands the icon set and creates new graphical representation of concepts.
locale: en-us
guid: 163fef6d-6b13-4479-baaa-25c27569832d
app_type: traditional web apps
platform-version: o11
---

# Stacked Icon

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Stacked Icon UI Pattern to stack one icon on top of another, thus creating a new icon with its own distinctive meaning.

![](<images/stackedicon-8-ss.png>)

**How to use the Stacked Icon UI Pattern**

In this example, we create a **NO PHOTOGRAPHY** icon by stacking a ban icon on top of a camera icon.

1. In Service Studio, in the Toolbox, search for `Stacked Icon`.

    The Stacked Icon widget is displayed.

    ![](<images/stackedicon-9-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Stacked Icon widget into the Main Content area of your application's screen.

    ![](<images/stackedicon-10-ss.png>)

1. On the **Properties** tab, select the relevant icons. In this example, we select a ban icon for the front icon, and a camera icon for the back icon. We also set the front and back icon colors and size.

    ![](<images/stackedicon-7-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property**                                | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IconFront (IconName Identifier): Optional   | The icon that displays in front of the other icon. Some of the predefined values include:<p><ul><li>Android</li><li>Bell</li><li>Camera</li><li>Desktop</li><li>Envelope</li></ul></p><p>Examples <ul><li>Blank - Displays a camera icon (default value).</li><li>Entities.IconName.instagram - Displays the Instagram icon.</li></ul></p>                                                                                                                                                                                                                                                                                         |
| IconBack (IconName Identifier): Optional    | The icon that displays behind the icon. Some of the predefined values include:<p><ul><li>Circle</li><li>Square</li><li>Heart</li></ul></p><p>Examples <ul><li>Blank - Displays a ban icon.</li><li>Entities.IconName.birthday_cake - Displays a birthday cake icon.</li></ul></p>                                                                                                                                                                                                                                                                                                                                                  |
| IconFrontColor (Color Identifier): Optional | Front icon color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>Blank - Displays a black (Neutral10) icon (default value).</li><li>Entities.Color.Red - Displays a red icon.</li></ul></p>                                                                                                                                                                                                                                                                                                                                              |
| IconBackColor (Color Identifier): Optional  | Back Icon color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>Blank - Displays a black (Neutral10) icon (default value).</li><li>Entities.Color.Green - Displays a green icon.</li></ul></p>                                                                                                                                                                                                                                                                                                                                           |
| IconSize (IconSize Identifier): Optional    | Sets the icon size. The predefined values are:<p><ul><li>Size_2x</li><li>Size_3x</li><li>Size_4x</li><li>Size_5x</li><li>Percent_33</li></ul></p><p>Examples <ul><li>Entities.IconSize.Size_2x - Increases the font to two times larger relative to the icon container.</li><li>Entities.IconSize.Size_Percent_33 - Increases the font to 33% larger relative to the icon container.</li></ul></p>                                                                                                                                                                                                                                 |
| InvertSize (Boolean): Optional              | If True, the icon sizes are swapped. If False, they are not swapped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ExtendedClass (Text): Optional              | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
