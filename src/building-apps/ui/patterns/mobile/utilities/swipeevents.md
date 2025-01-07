---
tags: ide usage, reactive web apps, tutorials for beginners, ui patterns, swipe gesture
summary: Learn how to implement swipe functionality in OutSystems 11 (O11) to manipulate data through user interactions with the Swipe Events UI Pattern.
locale: en-us
guid: 388d64de-604e-47a8-b533-8f2900ed21d9
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=222:0
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Swipe Events

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Swipe Events UI Pattern to enable swiping on a specific widget.

## How to use the Swipe Events UI Pattern

The following example shows how you can use the Swipe Events UI pattern to increase (swipe right) and decrease (swipe left) a number.

1. In Service Studio, in the Toolbox, search for  `Swipe Events`.

    The Swipe Events widget is displayed.

    ![Service Studio interface showing the Swipe Events widget in the search results.](images/swipeevents-1-ss.png "Swipe Events Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Swipe Events widget into the Main Content area of your application's screen.

    ![Dragging the Swipe Events widget into the Main Content area of an application screen.](images/swipeevents-2-ss.png "Dragging Swipe Events Widget")

1. Add a local variable by right-clicking on your screen name and selecting **Add Local Variable**.

    ![Context menu option to add a local variable in Service Studio.](images/swipeevents-3-ss.png "Adding a Local Variable")

1. Enter a name, a data type, and a default value for the new variable. In this example, we enter `Number`, `Integer`, and `0` repsectively.

    ![Local variable configuration with the name 'Number', data type 'Integer', and default value '0'.](images/swipeevents-4-ss.png "Local Variable Configuration")

1. Drag the new variable into the Main Content area of your application's screen.

    ![Local variable 'Number' dragged into the Main Content area of an application screen.](images/swipeevents-5-ss.png "Local Variable on Application Screen")

1. From the Toolbox, drag the Container widget into the Main Content area of your application's screen and on the **Properties** tab, enter a name. In this example we enter `SwipeContainer`. We also add the text `Swipe left or right` inside the Container widget.

    ![Container widget named 'SwipeContainer' with text 'Swipe left or right' inside it.](images/swipeevents-6-ss.png "Container Widget Configuration")

1. From the **Widget Tree**, select the Swipe Events widget, and on the **Properties** tab, from the **WidgetId** drop-down, select the Id of the container you just created. In this example, we select **SwipeContainer.Id**.

    ![Properties tab of Swipe Events widget with 'SwipeContainer.Id' selected as the WidgetId.](images/swipeevents-7-ss.png "Setting Swipe Events WidgetId")

1. To set the action for when the user swipes left, remaining on the **Properties** tab, from the **SwipeLeft Handler** drop-down, select **New Client Action**.

    ![Swipe Events properties tab showing the option to select a new client action for SwipeLeft Handler.](images/swipeevents-8-ss.png "Configuring SwipeLeft Handler")

1. Assign the relevant logic you want the swipe left action to perform. In this example, we want the number to decrease by 1 every time the user swipes left. To do this, we drag an Assign onto the client action, set the **Variable** to **Number**, and enter ``Number - 1`` for the **Value**.

    ![Client action logic to decrease the 'Number' variable by 1 on a swipe left event.](images/swipeevents-9-ss.png "Assigning Logic to SwipeLeft Action")

1. Repeat steps 8 and 9 for the **SwipeRightHandler** and so that the number increases when the user swipes right, enter `Number + 1`.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** | **Description** |
|---|---|
| WidgetId (Text): Mandatory | Element that's swipeable. |
