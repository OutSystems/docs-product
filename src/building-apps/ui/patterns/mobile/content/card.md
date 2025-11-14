---
tags: ide usage, reactive web apps, tutorials for beginners, ui patterns, outsystemsui
summary: Learn how to use the Card UI Pattern in OutSystems 11 (O11) to effectively group and display information in Mobile Apps and Reactive Web Apps.
locale: en-us
guid: a44ab647-aef4-44ba-b68b-d7a0d421a92c
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=205:15
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Card

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Cards UI Pattern to group small pieces of information and highlight them on the screen. The information is grouped into a small block that is easily noticeable on-screen.

![Example of a Card UI Pattern in a mobile app or reactive web app](images/card-1.png "Card UI Pattern Example")

## How to use the Card UI pattern

1. In Service Studio, in the Toolbox, search for `Card`.

    The Card widget is displayed.

    ![Service Studio interface showing the Card widget in the Toolbox](images/card-2-ss.png "Service Studio Card Widget")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Card widget into the Main Content area of your application's screen.

    ![Dragging the Card widget from the Toolbox into the Main Content area in Service Studio](images/card-3-ss.png "Dragging Card Widget to Main Content")

1. Add your content to the placeholder. In this example we add some text.

    ![Adding text content to the Card widget placeholder in Service Studio](images/card-4-ss.png "Adding Content to Card Placeholder")

1. On the **Properties** tab, you can customize the Card's look and feel by setting any of the (optional) properties.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UsePadding (Boolean): Optional | If set to True, padding is applied to the content area. This is the default value. If set to False, the content area has no padding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

## Accessibility – WCAG 2.2 AA compliance

The default version of this pattern complies with WCAG 2.2 AA accessibility standards. No changes or manual work are required. If you customize the pattern, validate your implementation to confirm it still meets accessibility requirements.
