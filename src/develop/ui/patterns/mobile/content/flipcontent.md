---
summary: Flip Content prioritizes information display, keeping the interface uncluttered.
tags:
---

# Flip Content

<div class="info" markdown="1">

If you are using an OutSystems UI version lower than 2.8.0, please see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).
                            
</div>

You can use the Flip Content UI Pattern to display information that when, for example, is clicked, flips and displays different information.

![](<images/flipcontent-example.gif?width=500>)

**How to use the Flip content UI Pattern**

1. In Service Studio, in the Toolbox, search for `Flip Content`.

    The Flip Content widget is displayed.

    ![Flip Content widget](<images/flipcontent-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure **Show All** is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure **Show All** is selected.
    
    d. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    e. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Flip Content widget into the Main Content area of your application's screen.

    ![Drag widget to screen](<images/flipcontent-dragwidget-ss.png>)

    By default, the Flip Content widget contains **CardFront** and **CardBack** placeholders.

1. Add the required content for the front and back placeholders inside the Flip Content widget.

    In this example, we add images by dragging the Image widget into the **CardFront** and **CardBack** placeholders and from the **Image** dropdown, selecting an image from the sample OutSystems UI images.

    ![Add content to widget](<images/flipcontent-addimage-ss.png>)

1. On the **Properties** tab, you can customize the Flip Content's look and feel by setting any of the (optional) properties.

    ![Properties](<images/flipcontent-properties-ss.png>)

## Properties
| Property | Description |
|---|---|
| StartsFlipped (Boolean): Optional | If True, the CardFront content is displayed first before flipping. If False, the CardBack content is displayed first before flipping. This is the default.|  
| FlipOnClick (Boolean): Optional | If True, the flip event is triggered when the Flip Content card (front or back) is clicked. This is the default. If False, you can define the action that triggers the flip event. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the myclass style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Framework Cheat Sheet](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/CheatSheet)|
