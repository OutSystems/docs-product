---
tags: runtime-traditionalweb; 
summary: Progress Bar displays the progress of a task by incrementing values in a bar.
---

# Progress Bar

You can use the Progress Bar to display percentage values by incrementing values in a bar, and to show the current progress of a task flow. <!--You can also show progress in a Progress Circle or a Progress Circle Fraction. When using the Progress Bar UI Pattern, be consistent, for example, if an action displays a linear indicator on one screen, that same action should not use a circular indicator elsewhere in the app. -->

![](<images/progressbar-1-ss.png>)

**How to use the Progress Bar UI Pattern**

In this example, we display the percentage of shipped orders from an existing Customer Order Database.

1. In Service Studio, in the Toolbox, search for `Progress Bar`.

    The Progress Bar widget is displayed.

    ![](<images/progressbar-2-ss.png>)

1. From the Toolbox, drag the Progress Bar widget into the Main Content area of your application's screen.

    ![](<images/progressbar-3-ss.png>)

    By default, the Progress Bar widget contains a Title and Value placeholder.

    ![](<images/progressbar-4-ss.png>)

1. Right-click your screen name and select **Add Preparation**.

1. From the Toolbox, drag an Aggregate onto the screen preparation, and enter a name for the aggregate. In this example, we call the aggregate **GetTotalOrders**.

    ![](<images/progressbar-10-ss.png>)

1. To add a database entity, double-click the aggregate you just created and click on the aggregate screen.

1. From the **Select Source** pop-up, choose the source entity and click **OK**. In this example, we select the **Order** database.

    ![](<images/progressbar-11-ss.png>)

1. Return to the screen preparation, and add another aggregate (See step 4). In this example we call the second aggregate **GetShippedOrders**.

    ![](<images/progressbar-12-ss.png>)

1. To add the relevant database entity, repeat steps 5 and 6.

1. On the aggregate screen, click **Filters**, then **Add Filter**.

1. In the **Filter Condition** pop-up, add the relevant logic for the filter and click **DONE**. In this example, to get all of the shipped orders, we add the following logic:

    `Order.Status = Entities.OrderStatus.Shipped`

    ![](<images/progressbar-13-ss.png>)

1. Double-click your screen name, and on the **Properties** tab, from the **Percentage** drop-down, select **Expression Editor**.
Enter the logic for the Progress Bar and click **DONE**.  This displays the percentage value as the stroke on the Progress Bar.

    In this example, to show the percentage of shipped orders, we add the following:

    `GetShippedOrders.Count / GetTotalOrders.Count * 100`

    ![](<images/progressbar-14-ss.png>)

1. From the Toolbox, drag an Expression widget into the **Value** placeholder, and on the **Properties** tab, from the **Value** drop-down, select **Expression Editor**.

1. In the Expression Editor, enter the same logic as in step 11 (`GetShippedOrders.Count / GetTotalOrders.Count * 100`), and click **DONE**. This displays the percentage value on the Progress Bar.

    ![](<images/progressbar-15-ss.png>)

1. Add the text you want to appear as the Progress Bar title to the **Title** placeholder. In this example, we add "Total % of shipped Orders".

    ![](<images/progressbar-16-ss.png>)

1. On the **Properties** tab, you can customize Progress Bar's look and feel by setting any of the optional properties, for example, the shape, color, size, and orientation of the Progress Bar.

    ![](<images/progressbar-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| Percentage (Integer): Optional  |  Percentage to display. You can use functions or local variables. |
| Color (Color Identifier): Optional  | Progress bar color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - The progress bar color  is the color you chose when creating the app (default value).</li><li>_Entities.Color.Red_ - The progress bar color is red.</li></ul></p>  |
| Shape (Shape Identifier): Optional  |  Set the Progress Bar shape. The predefined options are: <ul><li>Rounded</li><li> Soft Rounded </li> <li>Sharp</li></ul><p>Examples <ul><li>_Blank_ - The Progress Bar has a rounded shape (Entities.Shape.Rounded). This is the default.</li><li>_Entities.Shape.Sharp_ - The Progress Bar has a sharp shape.</li></ul></p> | 
| Size (ProgressBarSize Identifier): Optional  |  Set the Progress Bar size. The predefined options are: <ul><li>Extra Small</li><li>Small</li> <li>Base (default)</li></ul> |
| IsInline (Boolean): Optional  | If True, the value placeholder is placed at the end of the line and the label placeholder is hidden. If False, the value and label of the placeholder are placed over the line. This is the default.|
| ExtendedClass (Text): Optional  | Add custom style classes to the Progress Bar UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Progress Bar UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Progress Bar UI styles being applied.</li></ul></p> |
