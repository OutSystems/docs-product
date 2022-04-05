---
tags: runtime-traditionalweb; 
summary: RangeSliderInterval selects a single value or a range between two values.
---

# Range Slider Interval

You can use the Range Slider Interval Pattern to allow users select a single value between two range values. This pattern enables the adjustment of content by predetermined intervals and within a chosen range. Moving the slider along the track, increases or decreases the value. 

## How to use the Range Slider Interval UI Pattern

In this example, we create a Range Slider Interval that allows the user select a price range between 1-50.

1. In Service Studio, in the Toolbox, search for `Range Slider Interval`.

    The Range Slider Interval widget is displayed.

    ![](images/rangesliderinterval-2-ss.png)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Range Slider Interval widget into the Main Content area of your application's screen, and on the **Properties** tab, enter the **MinValue**, **MaxValue**, **InitialIntervalStart**, and **InitialIntervalEnd** values. In this example, we add static values.

    ![](images/rangesliderinterval-3-ss.png?width=800)

1. To create an **OnChange** event, on the **Properties** tab, from the **Handler** drop-down, select **New Screen Action**.

    ![](images/rangesliderinterval-5-ss.png?width=800)

    By default, the **SelectedMinValue** and **SelectedMaxValue** input parameter are created.  

    ![](images/rangesliderinterval-1-ss.png)

1. To create a variable for each of the expressions, right-click your screen name, select **Add Local Variable**, and on the **Properties** tab, enter a name and data type. In this example we create the **LowerPrice** and **HighestPrice** variables with the **Currency** data type.

    ![](images/rangesliderinterval-8-ss.png) 

1. So that the parameters read the range slider selections, double-click your screen action, from the Toolbox, add the **Assign** action to the screen action, and set the variable and value assignments for the Assign action. 

    ![](images/rangesliderinterval-7-ss.png?width=800) 

1. To display your selection, go back to your screen, and from the Toolbox, drag the Container widget into the Main Content area of your application's screen, enter a name and add your content to the Container placeholder. In this example, we enter ``DisplayValue`` for the name and add some text and an expression for each of the input parameters.

    ![](images/rangesliderinterval-6-ss.png?width=800)

1. Go back to the screen action, and from the Toolbox, add the **Ajax Refresh** action to the screen action, and in the **Select Widget** pop-up, navigate to and select the Container widget name (in this example, DisplayValue), and click **OK**.

    ![](images/rangesliderinterval-12-ss.png?width=800)

1. To bind the **SelectedMinValue** variable to the expression, double-click the expression widget, and in the **Expression Value** editor, select the variable you just have created, and click **Done**.

    ![](images/rangesliderinterval-9-ss.png)

1. Repeat step 8 for the **SelectedMaxValue** input parameter.

1. From the **Properties** tab, you can change the Range Slider's look and feel by setting the (optional) properties.

    ![](images/rangesliderinterval-13-ss.png)

After following these steps and publishing the module, you can test the pattern in your app. 

## Properties

| **Property** |  **Description** |  
|---|---|
|MinValue (Decimal): Mandatory  |  Slider's minimum value. <p>Examples <ul><li>_0_ - The slider's minimum value is 0.</li><li>_12_ - The slider's minimum value is 12</li> </ul></p> |
|MaxValue (Decimal): Mandatory  |  Slider's maximum value. <p>Examples <ul><li>_100_ - The slider's maximum value is 100.</li></ul></p> |
|InitialIntervalStart  |  Start value selected by default when the page is rendered. Must be between min and max values. <p>Examples <ul><li>_10_ - Slider's default start value when the page is rendered is 10.</li></ul></p> 
|InitialIntervalEnd  |  End value selected by default when the page is rendered. Must be between min and max values. <p>Examples <ul><li>_10_ - Slider's default end value when the page is rendered is 10.</li></ul></p> 
|Step (Decimal): Optional  | The slider moves in increments of steps.<p>Examples <ul><li>_Blank_ - The slider increases in steps of 1. This is the default value. </li><li>_10_ - The slider increases in steps of 10.</li></ul></p>
|ShowPips (Boolean): Optional  | If True, pips are shown below the slider. This is the default value. If False, no pips are shown. |
|PipsStepNumber (Integer): Optional  | Sets the number of Pip steps. This property is only applicable if the ShowPips property is set to True. |
|IsVertical (Boolean): Optional | If True, the slider orientation is vertical. If False, the slider orientation is horizontal. |
|VerticalHeight (Integer): Optional | If IsVertical is True, use this property to set the height (in px) of the slider. <p>Examples <ul><li>_Blank_ - The slider is 100px high. This is the default value. </li><li>_250_ - The slider is 250px high.</li></ul></p> |
|IsDisabled (Boolean): Optional | If True, the slider is disabled. If False, the slider is enabled. This is the default value. |
|ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - No custom styles are added (default value). </li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |  
|AdvancedFormat (Text): Optional | Allows you to use more options than what is provided in the input parameters. For more information, see [noUiSlider library](https://refreshless.com/nouislider/). <p> Example <ul><li> `{ pips: { density: 1 } }` </li></ul></p> |
