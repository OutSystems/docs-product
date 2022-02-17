---
tags: runtime-traditionalweb; 
summary: Tooltip dynamically displays simple informative content on end user interaction.
---

# Tooltip

You can use the Tooltip UI Pattern to dynamically display informative text when a user hovers over, clicks, or taps an on-screen element.

![](<images/tooltip-1.png>)

**How to use the Tooltip UI Pattern**

1. In Service Studio, in the Toolbox, search for `Tooltip`.
  
    The Tooltip widget is displayed.

    ![](<images/tooltip-2-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.
    
    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Tooltip widget into the Main Content area of your application's screen.

    ![](<images/tooltip-3-ss.png>)

    By default, the Tooltip widget contains Widget and Content placeholders.

1. Add your content to the placeholders. 
    
    In this example, we add a Save button to the Widget placeholder and enter the tooltip text 'Save your details' in the Content placeholder.

    ![](<images/tooltip-4-ss.png>)

1. On the **Properties** tab, change the look and feel of the Tooltip by setting the (optional) properties.

    ![](<images/tooltip-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Properties** |  **Description** |  
|---|---|
| Trigger (Trigger Identifier): Optional | Set the trigger type for the content. The predefined options are:<ul><li>Click</li><li>Hover</li><li>Manual</li></ul><p>Examples <ul><li>_Blank_ - The tooltip is triggered by hovering over the element (_Entities.Trigger.Hover_). This is the default.</li><li>_Entities.Trigger.Click_ - The tooltip is triggered by clicking the element.</li></ul></p> |
| IsVisible (Boolean): Optional | If True, the tooltip is visible when the page is first loaded (without the need for the initial trigger). If False, the tooltip is not visible. This is the default. |
| Position ( PositionBase Identifier): Optional | Set the tooltip's position. The predefined options are:<ul><li>Bottom</li><li>Left</li><li>Right</li><li>Top</li></ul><p>Examples <ul><li>_Blank_ - The tooltip is displayed on top of the element. (_Entities.PositionBase.Top_). This is the default.</li><li>_Entities.PositionBase.Right_ - The tooltip is displayed to the right of the element.</li></ul></p> |
| ExtendedClass (Text): Optional |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
| AdvancedFormat (Text): Optional | Allows for more options beyond what is provided through the input parameters. Example: `{ arrow: false }`. For more information, visit <https://atomiks.github.io/tippyjs/>. |
