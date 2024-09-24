---
tags: runtime-mobileandreactiveweb;  
summary: Accordion expands vertically-stacked content by clicking on the header.
locale: en-us
guid: 4cdf1677-f152-4afc-ac90-75901d2e9055
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=205:0
---

# Accordion

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

<div class="info" markdown="1">

**This documentation is not valid for deprecated components.** To check if your component is deprecated and how to migrate old versions, see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).

To find out what version of OutSystems UI you are using, see [OutSystems UI version](../../intro.md#outsystems-ui-version).

</div>

You can use the Accordion UI Pattern to allow users expand and hide content when clicked.

**How to use the Accordion UI Pattern**

1. In Service Studio, in the Toolbox, search for `Accordion`.

    The Accordion widget is displayed.

    ![Screenshot of the Accordion widget in the Service Studio toolbox](images/accordion-widget-ss.png "Accordion Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Accordion widget into the Main Content area of your application's screen.

    ![Dragging the Accordion widget from the toolbox into the main content area of the application screen](images/accordion-dragwidget-ss.png "Dragging Accordion Widget to Screen")

    **Note:** By default, the Accordion widget contains 3 **AccordionItem** widgets. You can add or delete Accordion Items as required.

1. Add the relevant content to the **AccordionItem** placeholders. In this example, some FAQs are added.
  
    ![Adding FAQ content to AccordionItem placeholders in Service Studio](images/accordion-addcontent-ss.png "Adding Content to AccordionItem Placeholders")

1. On the **Properties** tab, you can customize the Accordion's look and feel by setting any of the (optional) properties.

    ![Setting properties of the Accordion widget in Service Studio](images/accordion-properties-ss.png "Accordion Properties")

    ![Setting properties for an individual AccordionItem in Service Studio](images/accordion-properties-item-ss.png "Accordion Item Properties")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

### Accordion

| Property | Description  |
|---|--- |
| MultipleItems (Boolean): Optional | Set to True to allow multiple Accordion items to be expanded simultaneously. By default, False. |
| ExtendedClass (Text): Optional| Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

### Accordion Item

|Property|Description|
|---|---|
|StartsExpanded (Boolean): Optional| Defines the initial state of the block. If set to True, when the page is rendered, the Accordion Item is open. If set to False, the Accordion Item is closed. The default value is False.|
|Icon (AccordionIconType Identifier): Optional|Defines the icons shown in the Accordion Item.<br/><br/>You can choose between the following:<ul><li>Carets - Arrow up icon when the item is expanded and arrow down icon when the item is collapsed. This is the default.</li><li> Plus/Minus - Minus icon (-) when the item is expanded and plus icon (+) when the item is collapsed.</li><li>Custom - Advanced option to customize the Accordion icons. To use custom icons, set the Icon property to Custom and drag and drop the Icon widget to the Accordion Item placeholder.</li></ul>|
|IconPosition (AccordionIconPosition): Optional|Defines the position of the accordion icon. By default, the icon appears on the right.|
|IsDisabled (Boolean): Optional| Prevents the Accordion Item from being clickable. If set to True, the Accordion Item is not clickable. If set to False, the Accordion Item is clickable. The default value is False.|
|ExtendedClass (Text): Optional| Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

## Events

### Accordion Item

|Event|Description| 
|---|---|
|OnToggle: Optional|Event triggered when the section is expanded or collapsed.| 
