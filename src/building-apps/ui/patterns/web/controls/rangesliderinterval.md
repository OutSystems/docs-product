---
tags: runtime-traditionalweb; 
summary: Implement the Range Slider Interval UI pattern in OutSystems 11 (O11) for value selection in web apps.
locale: en-us
guid: 94ed04bf-3e70-41d6-9d40-713927750c02
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=234%3A25&mode=design&t=KpVEJMvnBwiukqql-1
---

# Range Slider Interval

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Range Slider Interval Pattern to allow users select a single value between two range values. This pattern enables the adjustment of content by predetermined intervals and within a chosen range. Moving the slider along the track, increases or decreases the value.

## How to use the Range Slider Interval UI Pattern

In this example, we create a Range Slider Interval that allows the user select a price range between 1-50.

1. In Service Studio, in the Toolbox, search for `Range Slider Interval`.

    The Range Slider Interval widget is displayed.

    ![Screenshot of the Range Slider Interval widget in the Service Studio toolbox](images/rangesliderinterval-2-ss.png "Range Slider Interval Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Range Slider Interval widget into the Main Content area of your application's screen, and on the **Properties** tab, enter the **MinValue**, **MaxValue**, **InitialIntervalStart**, and **InitialIntervalEnd** values. In this example, we add static values.

    ![Image showing where to enter MinValue, MaxValue, InitialIntervalStart, and InitialIntervalEnd for the Range Slider Interval](images/rangesliderinterval-3-ss.png "Setting Properties for Range Slider Interval")

1. To create an **OnChange** event, on the **Properties** tab, from the **Handler** drop-down, select **New Screen Action**.

    ![Screenshot of the Properties tab in Service Studio for creating an OnChange event for the Range Slider Interval](images/rangesliderinterval-5-ss.png "Creating OnChange Event for Range Slider Interval")

    By default, the **SelectedMinValue** and **SelectedMaxValue** input parameter are created.  

    ![Image displaying the default SelectedMinValue and SelectedMaxValue input parameters for the Range Slider Interval](images/rangesliderinterval-1-ss.png "Default Input Parameters for Range Slider Interval")

1. To create a variable for each of the expressions, right-click your screen name, select **Add Local Variable**, and on the **Properties** tab, enter a name and data type. In this example we create the **LowerPrice** and **HighestPrice** variables with the **Currency** data type.

    ![Screenshot showing the process of adding LowerPrice and HighestPrice local variables with Currency data type](images/rangesliderinterval-8-ss.png "Adding Local Variables for Price Range") 

1. So that the parameters read the range slider selections, double-click your screen action, from the Toolbox, add the **Assign** action to the screen action, and set the variable and value assignments for the Assign action. 

    ![Image illustrating how to set variable and value assignments for the Assign action in a screen action](images/rangesliderinterval-7-ss.png "Assign Action in Service Studio") 

1. To display your selection, go back to your screen, and from the Toolbox, drag the Container widget into the Main Content area of your application's screen, enter a name and add your content to the Container placeholder. In this example, we enter ``DisplayValue`` for the name and add some text and an expression for each of the input parameters.

    ![Screenshot of a Container widget named DisplayValue showing text and expressions for input parameters](images/rangesliderinterval-6-ss.png "Displaying Selection in Range Slider Interval")

1. Go back to the screen action, and from the Toolbox, add the **Ajax Refresh** action to the screen action, and in the **Select Widget** pop-up, navigate to and select the Container widget name (in this example, DisplayValue), and click **OK**.

    ![Image showing how to add an Ajax Refresh action to a screen action and select the DisplayValue Container widget](images/rangesliderinterval-12-ss.png "Ajax Refresh Action in Service Studio")

1. To bind the **SelectedMinValue** variable to the expression, double-click the expression widget, and in the **Expression Value** editor, select the variable you just have created, and click **Close**.

    ![Screenshot of the Expression Value editor with a variable selected for binding to an expression](images/rangesliderinterval-9-ss.png "Binding Variables to Expressions")

1. Repeat step 8 for the **SelectedMaxValue** input parameter.

1. From the **Properties** tab, you can change the Range Slider's look and feel by setting the (optional) properties.

    ![Image showing the Properties tab with optional properties for customizing the Range Slider Interval's appearance](images/rangesliderinterval-13-ss.png "Optional Properties for Range Slider Interval")

After following these steps and publishing the module, you can test the pattern in your app. 

## Properties

| **Property** | **Description** |
|---|---|
| MinValue (Decimal): Mandatory | Slider's minimum value. <p>Examples <ul><li>0 - The slider's minimum value is 0.</li><li>12 - The slider's minimum value is 12</li> </ul></p> |
| MaxValue (Decimal): Mandatory | Slider's maximum value. <p>Examples <ul><li>100 - The slider's maximum value is 100.</li></ul></p> |
|InitialIntervalStart | Start value selected by default when the page is rendered. Must be between min and max values. <p>Examples <ul><li>10 - Slider's default start value when the page is rendered is 10.</li></ul></p> 
|InitialIntervalEnd | End value selected by default when the page is rendered. Must be between min and max values. <p>Examples <ul><li>10 - Slider's default end value when the page is rendered is 10.</li></ul></p> 
|Step (Decimal): Optional | The slider moves in increments of steps.<p>Examples <ul><li>Blank - The slider increases in steps of 1. This is the default value. </li><li>10 - The slider increases in steps of 10.</li></ul></p>
|ShowPips (Boolean): Optional | If True, pips are shown below the slider. This is the default value. If False, no pips are shown. |
|PipsStepNumber (Integer): Optional | Sets the number of Pip steps. This property is only applicable if the ShowPips property is set to True. |
|IsVertical (Boolean): Optional | If True, the slider orientation is vertical. If False, the slider orientation is horizontal. |
|VerticalHeight (Integer): Optional | If IsVertical is True, use this property to set the height (in px) of the slider. <p>Examples <ul><li>Blank - The slider is 100px high. This is the default value. </li><li>250 - The slider is 250px high.</li></ul></p> |
|IsDisabled (Boolean): Optional | If True, the slider is disabled. If False, the slider is enabled. This is the default value. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
|AdvancedFormat (Text): Optional | Allows you to use more options than what is provided in the input parameters. For more information, see [noUiSlider library](https://refreshless.com/nouislider/). <p> Example <ul><li> `{ pips: { density: 1 } }` </li></ul></p> |
