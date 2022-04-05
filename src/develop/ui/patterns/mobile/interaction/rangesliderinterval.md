---
tags: runtime-mobileandreactiveweb;  
summary: the Range Slider Interval UI Pattern allows users select a single value between two range values.
---

# Range Slider Interval

<div class="info" markdown="1">

If you are using an OutSystems UI version between 2.3.0 and 2.8.1, see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).

</div>

You can use the Range Slider Interval Pattern to allow users select a single value between two range values. This pattern enables the adjustment of content by predetermined intervals and within a chosen range. Moving the slider along the track increases or decreases the value.

<div class="info" markdown="1">
 
The Range Slider Interval Pattern is based on the [noUiSlider library](https://refreshless.com/nouislider/) (v15.5.1). For more information about the Range Slider Interval’s behaviors and extensibility methods, see the provider’s documentation.  
 
</div>

## How to use the Range Slider Interval UI Pattern

In this example, we create a Range Slider Interval that allows the user to select a price range between 1-50.

1. In Service Studio, in the Toolbox, search for `Range Slider Interval`.

    The Range Slider Interval widget is displayed.

    ![Range SLider Interval widget](images/rangesliderinterval-widget-ss.png)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the **Range Slider Interval** widget into the Main Content area of your application's screen, and on the **Properties** tab, enter the **MinValue**, **MaxValue**, **StartingValueFrom**, and **StartingValueTo** values. 

    In this example, we add static values.

    ![Add mandatory values on the Properties tab](images/rangesliderinterval-dragwidget-ss.png)

1. To create a new client action, from the **OnValueChange** drop-down, select **New Client Action**.

    ![Create a new client action](images/rangesliderinterval-clientaction-ss.png)

    By default, the **IntervalStart** and **IntervalEnd** input parameters are created.

    ![Default input parameters created](images/rangesliderinterval-inputparameters-ss.png)

1. From the Toolbox, drag the **Container** widget into the Main Content area of your application's screen, and add your content to the Container placeholder. 

    In this example, we add some text and an expression for each of the input parameters.

    ![Add container with text and expressions](images/rangesliderinterval-container-ss.png)

1. To create a variable for each of the expressions, right-click your screen name, select **Add Local Variable**, and on the **Properties** tab, enter a name and data type. In this example we create the **LowerPrice** and **HighestPrice** variables with the **Currency** data type.

    ![Create local variables](images/rangesliderinterval-locvar-ss.png)

1. To bind the **IntervalStart** variable to the expression, double-click the expression widget, and in the **Expression Value** editor, select the variable you just have created, and click **Close**.

    ![Bind local variables](images/rangesliderinterval-bindvar-ss.png)

1. Repeat step 6 for the **IntervalEnd** input parameter.

1. So that the parameters read the range slider selections, double-click your client action, and from the Toolbox, add the **Assign** action to the client action and set the variable and value assignments.

    ![Add an assign to the client action](images/rangesliderinterval-assign-ss.png)

1. You can configure the  Range Slider Interval by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties, for example, the orientation. For more configurations, expand the **OptionalConfigs** property.   

    ![Set optional properties](images/rangesliderinterval-properties-ss.png)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| MinValue (Decimal): Mandatory | Slider's minimum value. <br/>Examples: <ul><li>0 - The slider's minimum value is 0.</li><li>12 - The slider's minimum value is 12</li></ul> |
| MaxValue (Decimal): Mandatory  | Slider's maximum value. <br/>Examples: <ul><li>100 - The slider's maximum value is 100.</li></ul> |
| StartingValueFrom (Decimal): Mandatory | Slider's default start value. Must be between min and max values. <br/>Examples: <ul><li>10 - Slider's default start value when the page is rendered is 10.</li></ul> |
| StartingValueTo (Decimal): Mandatory | Slider's default end value. Must be between min and max values. <br/>Examples: <ul><li>10 - Slider's default end value when the page is rendered is 10.</li></ul> |
|Orientation (Orientation Identifier): Optional|Set the direction of the Range Slider Interval. Default value is horizontal.|
|Size (Text): Optional|Set the size of the Range Slider Interval. If the slider's orientation is horizontal, the size you set will be the width of the Range Slider Interval. Otherwise (vertical), the size you set will be the height. Accepts any kind of unit (px, %, vw). Default value is 100% .|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <br/>Examples: <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul><br/>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
|OptionalConfigs.ShowFloatingLabel (Boolean): Optional|Set to True to add a floating label above the handler.|
|OptionalConfigs.Step (Decimal): Optional|Slider moves in increments of steps. If the step is set to 10, the slider increases or decreases in units of 10, for example, 0 to 10, to 20, to 30, and so on.|
|OptionalConfigs.ShowTickMarks (Boolean): Optional|Set to True to display tick marks below the slider. Set to True to display tick marks below the slider. Default value is False. To generate the tick marks, you must set the TickMarksInterval to True.|
|OptionalConfigs.TickMarksInterval (Integer): Optional|Range interval after which a tick mark is displayed (when ShowTickMarks is set to True). For example, if TickMarksInterval = 5, a tick mark is shown for each 5 steps. The value can not be less than 0 (library restraint).|
|OptionalConfigs.IsDisabled (Boolean): Optional|Set as True to disable the Range Slider Interval. Default value is True.build|

