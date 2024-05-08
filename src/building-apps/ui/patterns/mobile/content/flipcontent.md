---
summary: Learn how to use the Flip Content UI Pattern in OutSystems 11 (O11) to enhance interactive content display in mobile and reactive web apps.
tags: runtime-mobileandreactiveweb;
locale: en-us
guid: 714b1496-4c20-47fd-afcb-a0f2007ad984
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=205:37
---

# Flip Content

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

<div class="info" markdown="1">

**This documentation is not valid for deprecated components.** To check if your component is deprecated and how to migrate old versions, see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).

To find out what version of OutSystems UI you are using, see [OutSystems UI version](../../intro.md#outsystems-ui-version).

</div>

You can use the Flip Content UI Pattern to display information that when, for example, is clicked, flips and displays different information.

![Animated example of the Flip Content UI pattern in action, showing the front and back content flipping.](images/flipcontent-example.gif "Flip Content Interaction Example")

**How to use the Flip content UI Pattern**

1. In Service Studio, in the Toolbox, search for `Flip Content`.

    The Flip Content widget is displayed.

    ![Screenshot of the Flip Content widget in the OutSystems Service Studio toolbox.](images/flipcontent-widget-ss.png "Flip Content Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Flip Content widget into the Main Content area of your application's screen.

    ![Screenshot showing the process of dragging the Flip Content widget into the Main Content area of an application's screen.](images/flipcontent-dragwidget-ss.png "Dragging Flip Content Widget to Screen")

    By default, the Flip Content widget contains **CardFront** and **CardBack** placeholders.

1. Add the required content for the front and back placeholders inside the Flip Content widget.

    In this example, we add images by dragging the Image widget into the **CardFront** and **CardBack** placeholders and from the **Image** dropdown, selecting an image from the sample OutSystems UI images.

    ![Screenshot demonstrating how to add images to the CardFront and CardBack placeholders inside the Flip Content widget.](images/flipcontent-addimage-ss.png "Adding Content to Flip Content Widget")

1. On the **Properties** tab, you can customize the Flip Content's look and feel by setting any of the (optional) properties.

    ![Screenshot of the Properties tab for customizing the Flip Content's appearance and behavior in OutSystems Service Studio.](images/flipcontent-properties-ss.png "Flip Content Properties")

## Properties

| Property| Description|
|---|---|
|StartsFlipped (Boolean): Optional | Defines the initial state of the pattern. If True, the Card Front content is displayed first before flipping. If False, the Card Back content is displayed first before flipping. This is the default.<br/><br/>Use one of the following actions to change the value afterwards: <ul><li>FlipContentBack</li><li>FlipContentFront</li><li>FlipContentToggle</li></ul> |
|FlipOnClick (Boolean): Optional| If True, the flip event is triggered when the Flip Content card (front or back) is clicked. This is the default. If False, you can define the action that triggers the flip event.|
|ExtendedClass (Text): Optional| Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

## Events

|Event| Description| 
|---|---|
|OnFlip: Optional| Event triggered after the content is flipped.| 




