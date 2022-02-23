---
tags: runtime-mobileandreactiveweb;
summary: Displays the current progress of a task using circular or semi-circular progress indicators.
---

# Progress Circle

You can use the Progress Circle UI Pattern to show the current progress of an operation flow. The progress is incremented in fractions of the circular badge.

![Example progress circle](<images/progresscircle-example-ss.png>)

**How to use the Progress Circle UI Pattern**

In this example, we create a button that increments the progress circle each time it's clicked.

1. In Service Studio, in the Toolbox, search for `Progress Circle`.

    The Progress Circle widget is displayed.

    ![Progress Circle widget](<images/progresscircle-widget-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Progress Circle widget into the Main Content area of your application's screen.

    ![Drag widget to screen](<images/progresscircle-dragwidget-ss.png>)

1. Right-click your screen name, select **Add Local Variable**, and enter a name. 

    In this example, we enter `Count`.

    ![Add local variable](<images/progresscircle-variable-ss.png>)

1. Select the Progress Circle widget, and on the **Properties** tab, in the **Progress** property, enter the relevant logic for the progress percentage.

    In this example, we enter the following logic which sets the progress percentage to 4%:

    `Count / 25 * 100`

    ![Add progress logic](<images/progresscircle-logic-ss.png>)

1. From the Toolbox, drag the Button widget into the Main Content area of your application's screen. 

    In this example, we call the button **Increment** and set the **On Click** event to a  **New Client Action** that assigns the **Count** variable to `Count + 1`.

    ![Add a button to the screen](<images/progresscircle-button-ss.png>)

    ![Set the on click action logic](<images/progresscircle-assign-ss.png>)

1. Select the Progress Circle widget, and on the **Properties** tab, you can change the Progress Circle's look and feel by setting the (optional) properties, for example, the color settings.

    ![Set optional properties](<images/progresscircle-properties-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. The result of this example should look something like the following:

![Published app result](<images/progresscircle-result-ss.png>)

## Properties

| Property | Description |
|---|---|
| Progress (Integer): Mandatory | Progress percentage to display. You can use functions or local variables. Usually a number between 0 and 100. |
| Text (Text): Optional | Text that displays inside the circle. If no text is specified, the progress percentage is displayed. |
| ProgressColor (Color Identifier): Optional | The color of the stroke on progress circle. The default value is: "rgba (0,0,0,0.6)".
| TrailColor (Text): Optional | The color of the empty part of the progress circle. The default value is "rgba (0,0,0,0.2)". |

| Thickness (Integer): Optional | The thickness of the circle that marks the progress. <p>Examples <ul><li>_Blank_ - The circle thickness is 8px. This is the default value.</li><li>_4_ - The circle thickness is 8px.</li></ul></p> |
| AnimateInitialProgress (Boolean): Optional  | If set to True, the progress from zero to the progress value is animated. This is the default. If set to False, the progress is not animated. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>``"myclass"`` - Adds the ``myclass`` style to the UI styles being applied.</li><li>``"myclass1 myclass2"`` - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
