---
tags: ide usage, reactive web apps, tutorials for beginners, mobile app development, ui patterns
summary: Explore the Scrollable Area Pattern in OutSystems 11 (O11) for creating scrollable content blocks in mobile and reactive web apps.
locale: en-us
guid: 3ecfdec5-b135-4faa-8c1f-110595075a02
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=653:417
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Scrollable Area

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

The Scrollable Area Pattern is a simple scrollable block with a placeholder for content. You can use this pattern to display multiple elements in a single, scrollable row or column.

**How to use the Separator UI Pattern**

1. In Service Studio, in the Toolbox, search for `Scrollable Area`.

    The Scrollable Area is displayed.

    ![Screenshot of the Scrollable Area widget in the Service Studio toolbox](images/scrollwidget-ss.png "Scrollable Area Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Scrollable Area widget into the Main Content area of your application's screen,

    ![Dragging the Scrollable Area widget into the Main Content area of an application screen](images/scrolldrag-ss.png "Dragging Scrollable Area Widget to Screen")

    By default, the Scrollable Area widget contains a Content placeholder.

1. Add the relevant content to the Content placeholder.

    In this example, we add some images by dragging the Image widget into the Content placeholder, and on the **Properties** tab, from the **Image** dropdown, select the relevant images.

    ![Adding images to the Content placeholder of the Scrollable Area widget](images/scrollimage-ss.png "Adding Images to Content Placeholder")

1. On the **Properties** tab, you can customize the Scrollable Area's look and feel by setting any of the optional properties, for example, the height and width of the scrollable area.

    ![Customizing the Scrollable Area's properties in the Properties tab](images/scrollprop-ss.png "Setting Optional Properties of Scrollable Area")

After following these steps and publishing the module, you can test the pattern in your app.

Example result:

![Example result showing a Scrollable Area with content in an application](images/scrollexample.png "Example of Scrollable Area in an App")

## Properties

| **Property**                                       | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Orientation (Orientation Identifier): Optional     | Set the orientation to either horizontal or vertical. Note that, when the Orientation is set to vertical, a fixed height value must be added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Height (Text): Optional                            | Define the height of the scrollable area. If not defined, the height of the of the parent wrapper is used (100%).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Width (Text): Optional                             | Define the width of the scrollable area. If not defined, the width of the parent wrapper is used (100%).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ScrollbarType (ScrollbarType Identifier): Optional | Choose between different scrollbar types - Compact, Default, and None. If None is selected, the scrollbar is invisible, but you can still scroll. Horizontal scroll is not enabled with the mouse wheel but can be done with mousepad gestures.                                                                                                                                                                                                                                                                                                                                                                                         |
| ExtendedClass (Text): Optional                     | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
