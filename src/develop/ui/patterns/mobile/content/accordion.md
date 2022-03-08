---
tags: runtime-mobileandreactiveweb;  
summary: Accordion expands vertically-stacked content by clicking on the header.
---

# Accordion

You can use the Accordion UI Pattern to allow users expand and hide content when clicked.

**How to use the Accordion UI Pattern**

1. In Service Studio, in the Toolbox, search for `Accordion`.

    The Accordion widget is displayed.

    ![Accordion widget](<images/accordion-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Accordion widget into the Main Content area of your application's screen.

    ![Drag widget to screen](<images/accordion-dragwidget-ss.png>)

   **Note:** By default, the Accordion widget contains 3 Accordion Item widgets. You can add or delete Accordion Items as required.

1. Add the relevant content to the Accordion Item placeholders. In this example, some FAQs are.
  
    ![](<images/accordion-addcontent-ss.png>)

1. On the **Properties** tab, you can customize the Accordion's look and feel by setting any of the (optional) properties.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

### Accordion

| Property | Description |
|---|---|
|MultipleItems (Boolean): Optional|  If set to True, multiple Accordion Items can be open at the same time. If set to False, only one Accordion Item can be open at any time. This is the default value.|
|ExtendedClass (Text): Optional|  Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet).|

### Accordion Item

| Property | Description |
|---|---|
|IsExpanded (Boolean): Optional |  If set to True, when rendering, the Accordion Item is open. If set to False, the Accordion Item is closed. This is the default value. |
|UsePadding (Boolean): Optional |  If set to True, padding is applied to the content area. This is the default value. If set to False, the content area has no padding. |
|IsDisabled (Boolean): Optional |  If set to True, the Accordion Item cannot be clicked. If set to False, the Accordion Item is clickable. This is the default value. |
|ExtendedClass (Text): Optional|  Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
