---
tags: runtime-mobileandreactiveweb;
summary: Displays the current progress of a task using circular or semi-circular progress indicators.
---

# Progress Circle

You can use the Progress Circle UI Pattern to show the current progress of an operation flow. The progress is incremented in fractions of the circular badge. <!-- You can also show progress in a Progress Bar or Progress Circle Fraction display type.  When using the Progress Circle Pattern, you must be consistent, for example, if an action displays a linear indicator on one screen, that same action should not use a circular indicator elsewhere in the app. -->

 ![](<images/progresscircle-2-ss.png>)

**How to use the Progress Circle UI Pattern**

In this example, we display the percentage of shipped orders from an existing Customer Order Database.

1. In Service Studio, in the Toolbox, search for `Progress Circle`.

    The Progress Circle widget is displayed.

    ![](<images/progresscircle-8-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Progress Circle widget into the Main Content area of your application's screen.

    ![](<images/progresscircle-9-ss.png>)

1. Right-click your screen name and select **Add Preparation**.

1. From the Toolbox, drag an Aggregate onto the screen preparation, and enter a name for the aggregate. In this example, we call the aggregate **GetTotalOrders**.

    ![](<images/progresscircle-10-ss.png>)

1. To add a database entity, double-click the aggregate you just created and click on the aggregate screen.

1. From the **Select Source** pop-up, choose the source entity and click **OK**. In this example, we select the **Order** database.

    ![](<images/progresscircle-11-ss.png>)

1. Return to the screen preparation, and add another aggregate (See step 4). In this example we call the second aggregate **GetShippedOrders**.

    ![](<images/progresscircle-12-ss.png>)

1. To add the relevant database entity, repeat steps 5 and 6.

1. On the aggregate screen, click **Filters**, then **Add Filter**.

1. In the **Filter Condition** pop-up, add the relevant logic for the filter and click **DONE**. In this example, to get all of the shipped orders, we add the following logic:

    `Order.Status = Entities.OrderStatus.Shipped`

    ![](<images/progresscircle-14-ss.png>)

1. Double-click your screen name, and on the **Properties** tab, from the **Progress** drop-down, select **Expression Editor**. Enter the logic for the progress circle and click **DONE**. This displays the percentage value as the stroke on the Progress Circle.

    In this example, to show the percentage of shipped orders, we add the following:

    `GetShippedOrders.Count / GetTotalOrders.Count * 100`

    ![](<images/progresscircle-16-ss.png>)

1. From the Toolbox, drag an Expression widget into the Progress Circle's **Content** placeholder, and on the **Properties** tab, from the **Value** drop-down, select **Expression Editor**.

1. In the Expression Editor, enter the same logic as in step 11 (`GetShippedOrders.Count / GetTotalOrders.Count * 100`), and click **DONE**. This displays the percentage value inside the Progress Circle.

    ![](<images/progresscircle-15-ss.png>)

1. On the **Properties** tab, you can also change the Progress Circle's look and feel by setting the (optional) properties, for example, the color and animation settings.

    ![](<images/progresscircle-17-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| Progress (Integer): Mandatory  |  Percentage to display. You can use functions or local variables.  |
| ProgressColor (Color Identifier): Optional  |  The color of the stroke on progress circle. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available. <p>Examples <ul><li>_Blank_ - The stroke color displays in the color you chose when creating the app (default value).</li><li>_Entities.Color.Red_ - The stroke color is red.</li></ul></p> |
| TrailColor (Color Identifier): Optional  |  The color of the empty part of the progress circle. <p>Examples <ul><li>_Blank_ - The empty part of the circle is a light gray (Entities.Color.Neutral5). This is the default value.</li><li>_Entities.Color.Blue_ - The empty part of the progress circle is blue.</li></ul></p> |
| CircleThickness (Integer): Optional  |  The thickness of the circle that marks the progress. <p>Examples <ul><li>_Blank_ - The circle thickness is 4px. This is the default value.</li><li>_8_ - The circle thickness is 8px.</li></ul></p> |
| AnimateInitialProgress (Boolean): Optional  | If set to True, the progress from zero to the progress value is animated. This is the default value. If set to False, the progress is not animated. |
| IsSemiCircle (Boolean): Optional  | If True, the Progress Circle is changed from a circle to semi circle. If False, it remains a circle. This is the default value. |
| AdvancedFormat (Text): Optional  |  Allow for more options beyond what is provided through the input parameters. For more information, visit: <https://kimmobrunfeldt.github.io/progressbar.js/>. Example: `{ easing: 'bounce' }` |
