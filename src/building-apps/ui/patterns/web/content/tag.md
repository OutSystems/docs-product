---
tags: ui component customization, styling interfaces, ui patterns, web design, user experience
summary: Explore how to use the Tag UI Pattern in OutSystems 11 (O11) to enhance user interfaces by styling texts with customizable colors, sizes, and shapes.
locale: en-us
guid: b448e71a-760c-46b3-9fed-b3b97229d351
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=226%3A0&mode=design&t=ANpsYvOCthr9AWot-1
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Tag

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Tag UI Pattern to style small texts in a colored tag format. Use the Tags UI Pattern to display statuses, labels, or categories thus providing great user experience.

**How to use the Tag UI Pattern**

1. In Service Studio, in the Toolbox, search for `Tag`.
  
    The Tag widget is displayed.

    ![Screenshot of Service Studio showing the Tag widget in the Toolbox](images/tag-1-ss.png "Service Studio Tag Widget")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. To From the Toolbox, drag the Tag widget into the Main Content area of your application's screen.

    ![Dragging the Tag widget from the Toolbox into the Main Content area in Service Studio](images/tag-2-ss.png "Drag Tag Widget to Main Content")

1. Add your content to the placeholders. In this example, we add some text.

    ![Adding text content to the Tag widget's placeholder in Service Studio](images/tag-3-ss.png "Add Content to Tag Placeholder")

1. On the properties tab, you can change the Tag's look and feel by setting the (optional) properties, for example, size and color.

    ![Service Studio properties tab showing options to change the Tag's size and color](images/tag-4-ss.png "Tag Properties Configuration")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** | **Description** |
|---|---|
| Color (Color Identifier): Optional | Set the Tag's background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available. <p>Examples <ul><li>Blank - Displays the badge in the color you chose when creating the app (default value).</li><li>Entities.Color.Red - The Tag's background is red.</li></ul></p> |
| Shape (Shape Identifier): Optional | Set the Tag's shape. Rounded, soft rounded, and sharp are the predefined shapes available. <p>Examples <ul><li>Blank - Displays a rounded shaped Tag (default value).</li><li>Entities.Shape.Sharp - Displays a square shaped Tag.</li></ul></p> |
| Size (Size Identifier): Optional | Set the Tag's size. Small and medium are the predefined sizes available. <p>Examples <ul><li>Entities.Size.Medium - Displays a medium-sized badge.</li><li>Entities.Size.Small - Displays a small sized Tag.</li></ul></p> |
| IsLight (Boolean): Optional | Specify the Tag's background color. <p>Examples <ul><li>_Blank_ - A darker hue of the color is applied to the Tag and a lighter color to the text (default value).</li><li>True - A brighter hue of the color is applied to the Tag and a darker color to the text.</li><li>False - A darker hue of the color is applied to the Tag and a lighter color to the text.</li></ul></p> |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
