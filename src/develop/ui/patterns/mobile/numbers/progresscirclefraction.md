---
tags: runtime-mobileandreactiveweb;
summary: Display fraction values by incrementing values in a circular badge.
---

# Progress Circle Fraction

Use the Progress Circle Fraction UI Pattern to show the current progress of an operation flow. The progress is incremented in fractions of the circular badge.

![](<images/progresscirclefraction-1-ss.png>)

**How to use the Progress Circle UI Pattern**

In this example, we create a button that increments the progress circle fraction each time it's clicked.

1. In Service Studio, in the Toolbox, search for `Progress Circle Fraction`.

    The Progress Circle Fraction widget is displayed.

    ![](<images/progresscirclefraction-2-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Progress Circle Fraction widget into the Main Content area of your application's screen.

    ![](<images/progresscirclefraction-3-ss.png>)

1. Right-click your screen name, select **Add Local Variable**, and enter a name. In this example, we enter `Count`.

1. Select the Progress Circle widget, and on the **Properties** tab, enter values for the **Numerator** and **Denominator** properties.

    In this example, we enter the `Count` variable as the numerator value, and `25` as the denominator value.

    ![](<images/progresscirclefraction-5-ss.png>)

1. From the Toolbox, drag the Button widget into the Main Content area of your application's screen. In this example, call the button Increment and set the **On Click** property to a  **New Client Action** that assigns the Count variable to `Count + 1`.

    ![](<images/progresscirclefraction-6-ss.png>)

    ![](<images/progresscirclefraction-7-ss.png>)

1. Select the Progress Circle Fraction widget, and on the **Properties** tab, you can change the Progress Circle Fraction's look and feel by setting the (optional) properties, for example, the color settings.

    ![](<images/progresscirclefraction-9-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. The result of this example should look someting like the following:

![](<images/progresscirclefraction-8-ss.png>)

## Properties

| Property | Description |
|---|---|
| Progress (Integer): Mandatory | Progress percentage to display. You can use functions or local variables. Usually a number between 0 and 100. |
| Text (Text): Optional | Text that displays inside the circle. If no text is specified, the progress percentage is displayed. |
| ProgressColor (Text): Optional | The color of the stroke on progress circle. The default value is: "rgba (0,0,0,0.6)".
| TrailColor (Text): Optional | The color of the empty part of the progress circle. The default value is "rgba (0,0,0,0.2)". |
| TextColor (Text): Optional | The color of the text inside the circle. The default value is "#333". |
| CircleThickness (Integer): Optional | The thickness of the circle that marks the progress. <p>Examples <ul><li>_Blank_ - The circle thickness is 8px. This is the default value.</li><li>_4_ - The circle thickness is 8px.</li></ul></p> |
| AnimateInitialProgress (Boolean): Optional | If set to True, the progress from zero to the progress value is animated. This is the default. If set to False, the progress is not animated. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
