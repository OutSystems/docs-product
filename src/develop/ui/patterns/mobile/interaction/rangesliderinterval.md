---
tags: runtime-mobileandreactiveweb;  
summary: the Range Slider Interval UI Pattern allows users select a single value between two range values.
---

# Range Slider Interval

You can use the Range Slider Interval Pattern to allow users select a single value between two range values. This pattern enables the adjustment of content by predetermined intervals and within a chosen range. Moving the slider along the track increases or decreases the value.

## How to use the Range Slider Interval UI Pattern

In this example, we create a Range Slider Interval that allows the user select a price range between 1-50.

1. In Service Studio, in the Toolbox, search for `Range Slider Interval`.

    The Range Slider Interval widget is displayed.

    ![Range SLider Intrval widget](images/rangesliderinterval-widget-ss.png)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Range Slider Interval widget into the Main Content area of your application's screen, and on the **Properties** tab, enter the **MinValue**, **MaxValue**, **StartingValueStart**, and **StartingValueEnd** values. 

    In this example, we add static values.

    ![Add mandatory values on the Properties tab](images/rangesliderinterval-3-ss.png)

1. To create a new client action, from the **OnValueChange** drop-down, select **New Client Action**.

    ![Create a new client action](images/rangesliderinterval-5-ss.png)

    By default, the **InitialIntervalStart** and **InitialIntervalEnd** input parameters are created.

    ![](images/rangesliderinterval-4-ss.png)

1. From the Toolbox, drag the Container widget into the Main Content area of your application's screen, and add your content to the Container placeholder. In this example, we add some text and an expression for each of the input paramters.

    ![](images/rangesliderinterval-6-ss.png)

1. To create a variable for each of the expressions, right-click your screen name, select **Add Local Variable**, and on the **Properties** tab, enter a name and data type. In this example we create the **LowerPrice** and **HighestPrice** variables with the **Currency** data type.

    ![](images/rangesliderinterval-8-ss.png)

1. To bind the **IntervalStart** variable to the expression, double-click the expression widget, and in the **Expression Value** editor, select the variable you just have created, and click **Done**.

    ![](images/rangesliderinterval-9-ss.png)

1. Repeat step 6 for the **IntervalEnd** input parameter.

1. So that the parameter read the range slider selections, double-click your client action, and from the Toolbox, add the **Assign** action to the client action.

    ![](images/rangesliderinterval-11-ss.png)

1. Set the variable and value assignments for the Assign action.

    ![](images/rangesliderinterval-12-ss.png)

1. From the **Properties** tab, you can change the Range Slider's look and feel by setting the (optional) properties.

    ![](images/rangesliderinterval-13-ss.png)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| MinValue (Decimal): Mandatory  |  Slider's minimum value. <p>Examples <ul><li>0 - The slider's minimum value is 0.</li><li>12 - The slider's minimum value is 12</li> </ul></p> |
| MaxValue (Decimal): Mandatory  |  Slider's maximum value. <p>Examples <ul><li>100 - The slider's maximum value is 100.</li></ul></p> |
| StartingValueStart (Decimal): Mandatory | Slider's default start value. Must be between min and max values. <p>Examples <ul><li>10 - Slider's default start value when the page is rendered is 10.</li></ul></p> |
| StartingValueEnd (Decimal): Mandatory | Slider's default end value. Must be between min and max values. <p>Examples <ul><li>10 - Slider's default end value when the page is rendered is 10.</li></ul></p> |
|Orientation (Orientation Identifier): Optional|Set the direction of the RangeSliderInterval. By default, horizontal.|
|Size (Text): Optional|Set the RangeSliderInterval size. If horizontal, the size is the width. Otherwise (vertical), the size is the height.  Accepts any kind of unit (px, %, vw). By default, ‘100%’.|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the myclass style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the myclass1 and myclass2 styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
|OptionalConfigs.ShowFloatingLabel (Boolean): Optional|Set True to add a floating label above the handler.|
|OptionalConfigs.Step (Decimal): Optional|Slider moves in increments of Step. If Step is 10, the slider will go from 0 to 10, to 20, to 30, etc.|
|OptionalConfigs.ShowTickMarks
 (Boolean): Optional
|Show tick marks below the slider. To generate the tick marks, you will need to set the TickMarksInterval.|
|---|---|
|---|---|

