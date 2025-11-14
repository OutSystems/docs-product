---
tags: ide usage, reactive web apps, mobile app development, ui patterns, tutorials for beginners
summary: Learn how to organize content effectively in mobile and reactive web apps using the List Item Content UI Pattern in OutSystems 11 (O11).
locale: en-us
guid: 1c561d9b-7797-4365-b605-9c56261bfe04
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=205:49
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# List Item Content

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only.

</div>

You can use the List Item Content UI Pattern to quickly organize critical content in a readable way, helping the user understand the content. The List Item Content pattern is often used to organize content such as icons, text, and actions inside a list in a readable way.

![Screenshot of the List Item Content UI Pattern in use](images/listitemcontent-1-ss.png "List Item Content UI Pattern Example")

## How to use the List Item Content UI pattern

1. In Service Studio, in the Toolbox, search for `List Item Content`.

    The List Item Content widget is displayed.

    ![Image showing the List Item Content widget in the Service Studio toolbox](images/listitemcontent-2-ss.png "List Item Content Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the List Item Content widget into the Main Content area of your application's screen.

    ![Screenshot of dragging the List Item Content widget into the Main Content area](images/listitemcontent-3-ss.png "Dragging List Item Content Widget")

1. Add the relevant content to the placeholders.

    In this example, we add some texts and icons.

    ![Example of adding texts and icons to the List Item Content widget placeholders](images/listitemcontent-4-ss.png "Adding Content to List Item Content Widget")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

## Accessibility – WCAG 2.2 AA compliance

The default version of this pattern complies with WCAG 2.2 AA accessibility standards. No changes or manual work are required. If you customize the pattern, validate your implementation to confirm it still meets accessibility requirements.
