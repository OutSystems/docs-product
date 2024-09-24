---
tags: runtime-mobileandreactiveweb;  
summary: the Range Slider Interval UI Pattern allows users select a single value between two range values.
locale: en-us
guid: 69f1f6e5-318f-4da2-aa8f-912a7b8e66c2
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=213:55
---

# Range Slider Interval

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

<div class="info" markdown="1">

**This documentation is not valid for deprecated components.** To check if your component is deprecated and how to migrate old versions, see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).

To find out what version of OutSystems UI you are using, see [OutSystems UI version](../../intro.md#outsystems-ui-version).

</div>

You can use the Range Slider Interval Pattern to allow users select a single value between two range values. This pattern enables the adjustment of content by predetermined intervals and within a chosen range. Moving the slider along the track increases or decreases the value.

<div class="info" markdown="1">
 
The Range Slider Interval Pattern is based on v15.5.1 of the [noUiSlider library](https://refreshless.com/nouislider/). For more information about the Range Slider Interval’s behaviors and extensibility methods, see the provider’s documentation.  
 
</div>

## How to use the Range Slider Interval UI Pattern

In this example, we create a Range Slider Interval that allows the user to select a price range between 1-50.

1. In Service Studio, in the Toolbox, search for `Range Slider Interval`.

    The Range Slider Interval widget is displayed.

    ![Screenshot of the Range Slider Interval widget in the Service Studio toolbox](images/rangesliderinterval-widget-ss.png "Range Slider Interval Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the **Range Slider Interval** widget into the Main Content area of your application's screen, and on the **Properties** tab, enter the **MinValue**, **MaxValue**, **StartingValueFrom**, and **StartingValueTo** values. 

    In this example, we add static values.

    ![Screenshot showing how to drag the Range Slider Interval widget into the Main Content area in Service Studio](images/rangesliderinterval-dragwidget-ss.png "Dragging Range Slider Interval Widget")

1. To create a new client action, from the **OnValueChange** drop-down, select **New Client Action**.

    ![Screenshot of creating a new client action for the Range Slider Interval from the OnValueChange dropdown](images/rangesliderinterval-clientaction-ss.png "Creating a New Client Action for Range Slider Interval")

    By default, the **IntervalStart** and **IntervalEnd** input parameters are created.

    ![Screenshot displaying the default IntervalStart and IntervalEnd input parameters for the Range Slider Interval](images/rangesliderinterval-inputparameters-ss.png "Default Input Parameters for Range Slider Interval")

1. From the Toolbox, drag the **Container** widget into the Main Content area of your application's screen, and add your content to the Container placeholder. 

    In this example, we add some text and an expression for each of the input parameters.

    ![Screenshot showing a Container widget being added to the Main Content area with text and expressions for input parameters](images/rangesliderinterval-container-ss.png "Adding Content to Range Slider Interval Container")

1. To create a variable for each of the expressions, right-click your screen name, select **Add Local Variable**, and on the **Properties** tab, enter a name and data type. In this example we create the **LowerPrice** and **HighestPrice** variables with the **Currency** data type.

    ![Screenshot illustrating the creation of LowerPrice and HighestPrice local variables with Currency data type for the Range Slider Interval](images/rangesliderinterval-locvar-ss.png "Creating Local Variables for Range Slider Interval")

1. To bind the **IntervalStart** variable to the expression, double-click the expression widget, and in the **Expression Value** editor, select the variable you just have created, and click **Close**.

    ![Screenshot demonstrating how to bind the IntervalStart variable to an expression in the Range Slider Interval](images/rangesliderinterval-bindvar-ss.png "Binding Variables to Range Slider Interval Expressions")

1. Repeat step 6 for the **IntervalEnd** input parameter.

1. So that the parameters read the range slider selections, double-click your client action, and from the Toolbox, add the **Assign** action to the client action and set the variable and value assignments.

    ![Screenshot of assigning values to variables in a client action for the Range Slider Interval](images/rangesliderinterval-assign-ss.png "Assigning Values in Range Slider Interval Client Action")

1. You can configure the  Range Slider Interval by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties, for example, the orientation. For more configurations, expand the **OptionalConfigs** property.   

    ![Screenshot showing the properties configuration for the Range Slider Interval in Service Studio](images/rangesliderinterval-properties-ss.png "Configuring Properties of Range Slider Interval")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property| Description |
|---|---|
| MinValue (Decimal): Mandatory| Defines the slider's minimum value.|
| MaxValue (Decimal): Mandatory| Defines the slider's maximum value.|
| StartingValueFrom (Decimal): Mandatory |Defines the default value for the interval's start. Must be between min and max values. |
| StartingValueTo (Decimal): Mandatory| Defines the default value for the interval's end. Must be between min and max values. |
| Orientation (Orientation Identifier): Optional| Defines the Range Slider direction. The default direction is horizontal. |
| Size (Text): Optional| Defines the size of the Range Slider Interval. If the slider's orientation is horizontal, the size you set will be the width of the Range Slider Interval. Otherwise (vertical), the size you set will be the height. Accepts any kind of unit (px, %, vw). Default value is 100%. |
| OptionalConfigs (RangeSliderOptionalConfigs): Optional | Defines additional parameters to customize the RangeSlider behavior and functionality. |
| OptionalConfigs.ShowFloatingLabel (Boolean): Optional | Set to True to add a floating label above the handler. The default value is False.|
| OptionalConfigs.Step (Decimal): Optional|Slider moves in increments of Step. If Step is 10, the slider will go from 0 to 10, to 20, to 30, etc. Default value is 1.|
| OptionalConfigs.ShowTickMarks (Boolean): Optional | Show tick marks below the slider. To generate the tick marks, you must set the TickMarksInterval. The default value is True.|
| OptionalConfigs.TickMarksInterval (Integer): Optional | Defines the range interval after which a tick mark is drawn (when ShowTickMarks is enabled).<br/>Example: If TickMarksInterval = 5, a tick mark is shown for every 5 steps.<br/>The value can not be less than 0 (library restraint).<br/>If you do not want the tick marks to show, set the ShowTickMarks parameter to False.  |
| OptionalConfigs.IsDisabled (Boolean): Optional| Set as True to disable the Range Slider. The default value is False.|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

## Events

|Event| Description  | 
|---|---|
|Initialized: Optional  | Event triggered after the RangerSliderInterval instance is ready.<br/>With this event, you get the element Id that can be used to call methods from the RangeSliderAPI:<br/>``OutSystems.OSUI.Patterns.RangeSliderAPI`` | 
|OnValueChange: Mandatory  | Event triggered after selecting a new value on the slider. By default, the event is triggered while the user is dragging the RangeSliderInterval handler. You can use the SetRangeSliderIntervalChangeOnDragEnd to trigger the event only after the user releases it.  | 
