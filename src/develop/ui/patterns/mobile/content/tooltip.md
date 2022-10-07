---
tags: runtime-mobileandreactiveweb;   
summary: Tooltip dynamically displays simple informative content on end user interaction.
locale: en-us
guid: 44f1bcc8-d2bd-4174-ae3d-8813092a4bac
app_type: mobile apps, reactive web apps
---

# Tooltip

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

<div class="info" markdown="1">

If you are using an OutSystems UI version lower than 2.8.0, see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).
                            
</div>

You can use the Tooltip UI Pattern to dynamically display informative text when a user hovers over, clicks, or taps an on-screen element.

![Example tooltip](<images/tooltip-example.png>)

**How to use the Tooltip UI Pattern**

1. In Service Studio, in the Toolbox, search for `Tooltip`.
  
    The Tooltip widget is displayed.

    ![Tooltip widget](<images/tooltip-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Tooltip widget into the Main Content area of your application's screen.

    ![Drag tooltip widget to screen](<images/tooltip-drag-ss.png>)

    By default, the Tooltip widget contains Content and Tooltip placeholders.

1. Add your content to the placeholders. 
    
    In this example, we add a **Save** button to the Content placeholder and enter the tooltip text ``Save your details`` in the Tooltip placeholder.

    ![Add content to tooltip](<images/tooltip-content-ss.png>)
    
1. Select the **Save** button and add the relevant **On Click** event.

    ![Add OnClick event to Save button](<images/tooltip-onclick-ss.png>)

1. On the **Properties** tab, from the **Position** dropdown, select where you want the tooltip to appear. In this example we want the tooltip to appear on top of the **Save** button. You can also change the look and feel of the Tooltip by setting the (optional) properties.

    ![Set optional properties](<images/tooltip-properties-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Properties                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Position (Position Identifier): Optional | Set the tooltip's position, for example, top, right, or left.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| StartsOpen (Boolean): Optional           | If True, the tooltip is visible when the page is first loaded (without the need for the initial trigger). If False, the tooltip is not visible. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Trigger (TriggerIdentifier): Optional    | Set how the tooltip is triggered. By default, the tooltip is triggered by hovering over the element.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ExtendedClass (Text): Optional           | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the _myclass_ style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Framework Cheat Sheet](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/CheatSheet). |
