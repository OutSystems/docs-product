---
tags: runtime-traditionalweb; 
summary: Progress Bar displays the progress of a task by incrementing values in a bar.
locale: en-us
guid: 2a589d5e-0cd8-4dab-b9fa-bc7d12cacf23
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=243%3A28&mode=design&t=u4ANW5BJS7Flsdmg-1
---

# Progress Bar

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Progress Bar to display percentage values by incrementing values in a bar, and to show the current progress of a task flow. <!--You can also show progress in a Progress Circle or a Progress Circle Fraction. When using the Progress Bar UI Pattern, be consistent, for example, if an action displays a linear indicator on one screen, that same action should not use a circular indicator elsewhere in the app. -->

![Screenshot of a progress bar example in a Traditional Web App](images/progressbar-1-ss.png "Progress Bar Example")

**How to use the Progress Bar UI Pattern**

In this example, we display the percentage of shipped orders from an existing Customer Order Database.

1. In Service Studio, in the Toolbox, search for `Progress Bar`.

    The Progress Bar widget is displayed.

    ![Image showing the Progress Bar widget in the Service Studio toolbox](images/progressbar-2-ss.png "Progress Bar Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Progress Bar widget into the Main Content area of your application's screen.

    ![Dragging the Progress Bar widget into the Main Content area of an application screen](images/progressbar-3-ss.png "Dragging Progress Bar Widget")

    By default, the Progress Bar widget contains a Title and Value placeholder.

    ![Default Progress Bar widget with Title and Value placeholder](images/progressbar-4-ss.png "Default Progress Bar Widget")

1. Right-click your screen name and select **Add Preparation**.

1. From the Toolbox, drag an Aggregate onto the screen preparation, and enter a name for the aggregate. In this example, we call the aggregate **GetTotalOrders**.

    ![Creating an aggregate called GetTotalOrders in Service Studio](images/progressbar-10-ss.png "Aggregate in Service Studio")

1. To add a database entity, double-click the aggregate you just created and click on the aggregate screen.

1. From the **Select Source** pop-up, choose the source entity and click **OK**. In this example, we select the **Order** database.

    ![Selecting the source entity for an aggregate in Service Studio](images/progressbar-11-ss.png "Select Source Entity for Aggregate")

1. Return to the screen preparation, and add another aggregate (See step 4). In this example we call the second aggregate **GetShippedOrders**.

    ![Adding a second aggregate called GetShippedOrders in Service Studio](images/progressbar-12-ss.png "Adding Second Aggregate")

1. To add the relevant database entity, repeat steps 5 and 6.

1. On the aggregate screen, click **Filters**, then **Add Filter**.

1. In the **Filter Condition** pop-up, add the relevant logic for the filter and click **DONE**. In this example, to get all of the shipped orders, we add the following logic:

    `Order.Status = Entities.OrderStatus.Shipped`

    ![Adding a filter to the GetShippedOrders aggregate in Service Studio](images/progressbar-13-ss.png "Adding Filter to Aggregate")

1. Double-click your screen name, and on the **Properties** tab, from the **Percentage** drop-down, select **Expression Editor**.
Enter the logic for the Progress Bar and click **DONE**.  This displays the percentage value as the stroke on the Progress Bar.

    In this example, to show the percentage of shipped orders, we add the following:

    `GetShippedOrders.Count / GetTotalOrders.Count * 100`

    ![Setting the percentage value for the Progress Bar using an expression in Service Studio](images/progressbar-14-ss.png "Setting Progress Bar Percentage")

1. From the Toolbox, drag an Expression widget into the **Value** placeholder, and on the **Properties** tab, from the **Value** drop-down, select **Expression Editor**.

1. In the Expression Editor, enter the same logic as in step 11 (`GetShippedOrders.Count / GetTotalOrders.Count * 100`), and click **DONE**. This displays the percentage value on the Progress Bar.

    ![Adding an expression widget to display the percentage value on the Progress Bar](images/progressbar-15-ss.png "Expression Widget for Progress Bar Value")

1. Add the text you want to appear as the Progress Bar title to the **Title** placeholder. In this example, we add "Total % of shipped Orders".

    ![Adding a title to the Progress Bar's Title placeholder in Service Studio](images/progressbar-16-ss.png "Progress Bar Title Placeholder")

1. On the **Properties** tab, you can customize Progress Bar's look and feel by setting any of the optional properties, for example, the shape, color, size, and orientation of the Progress Bar.

    ![Customizing the look and feel of the Progress Bar in Service Studio](images/progressbar-5-ss.png "Customizing Progress Bar Properties")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Percentage (Integer): Optional              | Percentage to display. You can use functions or local variables.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Color (Color Identifier): Optional          | Progress bar color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>Blank - The progress bar color  is the color you chose when creating the app (default value).</li><li>Entities.Color.Red - The progress bar color is red.</li></ul></p>                                                                                                                                                                                                                                                                                               |
| Shape (Shape Identifier): Optional          | Set the Progress Bar shape. The predefined options are: <ul><li>Rounded</li><li> Soft Rounded </li> <li>Sharp</li></ul><p>Examples <ul><li>Blank - The Progress Bar has a rounded shape (Entities.Shape.Rounded). This is the default.</li><li>Entities.Shape.Sharp - The Progress Bar has a sharp shape.</li></ul></p>                                                                                                                                                                                                                                                                                                            |
| Size (ProgressBarSize Identifier): Optional | Set the Progress Bar size. The predefined options are: <ul><li>Extra Small</li><li>Small</li> <li>Base (default)</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| IsInline (Boolean): Optional                | If True, the value placeholder is placed at the end of the line and the label placeholder is hidden. If False, the value and label of the placeholder are placed over the line. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ExtendedClass (Text): Optional              | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
