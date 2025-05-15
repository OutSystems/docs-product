---
tags: ui design, widgets, web development, dependency management, instructional guide
summary: Explore how to organize content using the Bullets UI Pattern in OutSystems 11 (O11) for Traditional Web Apps.
locale: en-us
guid: 0028c775-3531-4d78-b693-124fb9f1c70e
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=222%3A51&mode=design&t=ANpsYvOCthr9AWot-1
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Bullets

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Bullets UI Pattern to organize topics into separate bullet points.

**How to use the Bullets UI Pattern**

1. In Service Studio, in the Toolbox, search for `Bullets`.

    The Bullets widget is displayed.

    ![Screenshot showing the Bullets widget in the Service Studio toolbox](images/bullets-1-ss.png "Bullets Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**.
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Bullets widget into the Main Content area of your application's screen.

    ![Screenshot of dragging the Bullets widget into the main content area of an application screen](images/bullets-2-ss.png "Dragging Bullets Widget into Main Content Area")

    By default, the Bullets widget contains 3 Bullet Items. You can add or delete Bullet Items as required. To create sub-bullets, you can drag the Bullets widget into the Bullet Item placeholder.

1. Add your content to the placeholders. In this example we add text to each of the placeholders.

    **Note**: If you leave any placeholder blank, it will not be displayed when the page is rendered.

    ![Screenshot with text added to each placeholder of the Bullets widget](images/bullets-5-ss.png "Adding Content to Bullets Placeholders")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** | **Description** |
|---|---|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
