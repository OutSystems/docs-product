---
tags: runtime-mobileandreactiveweb;
summary: Displays the current progress of a task using circular or semi-circular progress indicators.
---

# Progress Circle

You can use the Progress Circle UI Pattern to show the current progress of an operation flow. The progress is incremented in fractions of the circular badge.

![](<images/progresscircle-1-ss.png>)

**How to use the Progress Circle UI Pattern**

In this example, we create a button that increments the progress circle each time it's clicked.

1. In Service Studio, in the Toolbox, search for `Progress Circle`.

    The Progress Circle widget is displayed.

    ![](<images/progresscircle-2-ss.png>)
  
1. From the Toolbox, drag the Progress Circle widget into the Main Content area of your application's screen.

    ![](<images/progresscircle-3-ss.png>)

1. Right-click your screen name, select **Add Local Variable**, and enter a name. In this example, we enter `Count`.

    ![](<images/progresscircle-4-ss.png>)

1. Select the Progress Circle widget, and on the **Properties** tab, in the **Progress** property, enter the relevant logic for the progress percentage.

    In this example, we enter the following logic which sets the progress percentage to 4%:

    `Count / 25 * 100`

1. From the Toolbox, drag the Button widget into the Main Content area of your application's screen. In this example, call the button Increment and set the **On Click** property to a  **New Client Action** that assigns the Count variable to `Count + 1`.

    ![](<images/progresscircle-6-ss.png>)

    ![](<images/progresscircle-5-ss.png>)

1. Select the Progress Circle widget, and on the **Properties** tab, you can change the Progress Circle's look and feel by setting the (optional) properties, for example, the color settings.

    ![](<images/progresscircle-8-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. The result of this example should look something like the following:

![](<images/progresscircle-7-ss.png>)

## Properties

| Property | Description |
|---|---|
| Progress (Integer): Mandatory | Progress percentage to display. You can use functions or local variables. Usually a number between 0 and 100. |
| Text (Text): Optional | Text that displays inside the circle. If no text is specified, the progress percentage is displayed. |
| ProgressColor (Text): Optional | The color of the stroke on progress circle. The default value is: "rgba (0,0,0,0.6)".
| TrailColor (Text): Optional | The color of the empty part of the progress circle. The default value is "rgba (0,0,0,0.2)". |
| TextColor (Text): Optional | The color of the text inside the circle. The default value is "#333". |
| CircleThickness (Integer): Optional | The thickness of the circle that marks the progress. <p>Examples <ul><li>_Blank_ - The circle thickness is 8px. This is the default value.</li><li>_4_ - The circle thickness is 8px.</li></ul></p> |
| AnimateInitialProgress (Boolean): Optional  | If set to True, the progress from zero to the progress value is animated. This is the default. If set to False, the progress is not animated. |
| ExtendedClass (Text): Optional | Add custom style classes to the Progress Circle UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Progress Circle UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Progress Circle UI styles being applied.</li></ul></p> |
