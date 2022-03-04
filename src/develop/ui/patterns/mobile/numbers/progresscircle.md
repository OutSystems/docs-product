---
tags: runtime-mobileandreactiveweb;
summary: Displays the current progress of a task using circular or semi-circular progress indicators.
---

# Progress Circle

<div class="info" markdown="1">

If you are using an OutSystems UI version lower than 2.8.0, please see the [Patterns and Versions Overview](https://outsystemsui-dev.outsystemsenterprise.com/OutSystemsUIWebsite/MigrationOverview).
                            
</div>

You can use the Progress Circle UI Pattern to show the current progress of an operation flow. The progress is incremented in fractions of the circular badge.

![Example progress circle](<images/progresscircle-example-ss.png>)

**How to use the Progress Circle UI Pattern**

In this example, we create a button that increments the progress circle each time it's clicked and displays the progress as a fraction.

1. In Service Studio, in the Toolbox, search for `Progress Circle`.

    The Progress Circle widget is displayed.

    ![Progress Circle widget](<images/progresscircle-widget-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure **Show All** is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure **Show All** is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Progress Circle widget into the Main Content area of your application's screen.

    ![Drag widget to screen](<images/progresscircle-dragwidget-ss.png>)

1. Right-click your screen name, select **Add Local Variable**, and enter a name. for example, `Count`.

    ![Add local variable](<images/progresscircle-variable-ss.png>)

1. Select the Progress Circle widget, and on the **Properties** tab, in the **Progress** property, enter the **Count** variable. 

    ![Add progress logic](<images/progresscircle-logic-ss.png>)

1. Select the **Expression** widget inside the Progress Circle, and on the **Properties** tab, in the **Value** property, enter the relevant logic for the progress. In this example, enter the local variable **Count**. 

    ![Add expression logic](<images/progresscircle-expression-ss.png>)

1. From the Toolbox, drag the **Separator** widget into the Progress Circle.

    ![Add the separator widget](<images/progresscircle-separator-ss.png>)

1. From the Toolbox, drag an **Expression** widget under the **Separator** widget and enter the relevant logic for the denominator. In this example, enter ``"100"``.

    ![Add an expression widget for the denominator](<images/progresscircle-denominator-ss.png>)

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
|Progress (Integer): Mandatory | Progress percentage. Usually a number between 0 and 100. You can also use functions or local variables.|
|ProgressColor (Color Identifier): Optional | The color that fills the circle, as progress goes up, using the OutSystems UI Color palette.
|TrailColor (Text): Optional | The color of the empty part of the progress circle, using the OutSystems UI Color palette.  |
|Thickness (Integer): Optional | The thickness of the circle that marks the progress. |
|OptionalConfigs.Shape (Shape Identifier): Optional  | Set the progress circle shape.|
|OptionalConfigs.AnimateInitialProgress (Boolean): Optional  | If True, the progress from zero to the progress value is animated. This is the default.|
|ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>``"myclass"`` - Adds the ``myclass`` style to the UI styles being applied.</li><li>``"myclass1 myclass2"`` - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
