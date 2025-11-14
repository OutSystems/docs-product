---
tags: ui patterns, widgets, ui design, service studio tools, dependency management
summary: Explore how to implement the Margin Container UI Pattern in OutSystems 11 (O11) for adding symmetrical padding in Mobile and Reactive Web Apps.
locale: en-us
guid: 8099782f-c5ac-4a8f-a70a-fa9946d834a3
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=218:95
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Margin Container

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Margin Container UI Pattern to add symmetrical padding around a container.

![Screenshot of an example using the Margin Container UI Pattern in Service Studio](images/margincontainer-1-ss.png "Margin Container Example")

**How to use the Margin Container UI Pattern**

1. In Service Studio, in the Toolbox, search for `Margin Container`.

    The Margin Container widget is displayed.

    ![Screenshot showing the Margin Container widget in the Service Studio Toolbox](images/margincontainer-2-ss.png "Margin Container Widget in Toolbox")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Margin Container widget into the Main Content area of your application's screen.

    ![Screenshot of dragging the Margin Container widget into the Main Content area in Service Studio](images/margincontainer-3-ss.png "Dragging Margin Container Widget")

    You can add as many Margin Container widgets as you want. In this example, we add 2.

1. Add the relevant content to the Margin Container placeholder.

    In this example we add an image widget to each of the placeholders and on the **Properties** tab, import an image using the **Image** dropdown.

    ![Screenshot demonstrating how to add content to the Margin Container placeholders in Service Studio](images/margincontainer-4-ss.png "Adding Content to Margin Container")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| ExtendedClass (Text): Optional | <p>Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

## Accessibility – WCAG 2.2 AA compliance

The default version of this pattern complies with WCAG 2.2 AA accessibility standards. No changes or manual work are required. If you customize the pattern, validate your implementation to confirm it still meets accessibility requirements.
