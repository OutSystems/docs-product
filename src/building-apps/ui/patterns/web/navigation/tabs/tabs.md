---
tags: runtime-traditionalweb; 
summary: Tabs separate content into flat structure sections.
locale: en-us
guid: 61ddaa14-5f08-44b8-95a5-9527a7649449
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=238%3A55&mode=design&t=u4ANW5BJS7Flsdmg-1
---

# Tabs

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Tabs UI Pattern to display large sets of information, which can be split into different areas, while always remaining a click away.

![Animated GIF showing the interaction with the Tabs UI Pattern in a Traditional Web App](images/tabs-1.gif "Tabs UI Pattern Interaction")

**How to use the Tabs UI Pattern**

1. In Service Studio, in the Toolbox, search for `Tabs`.

    The Tabs widget is displayed.

    ![Screenshot of the Tabs widget in the Service Studio toolbox](images/tabs-2-ss.png "Tabs Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Tabs widget into the Main Content area of your application's screen.

    ![Screenshot showing how to drag the Tabs widget into the main content area of an application's screen](images/tabs-3-ss.png "Dragging Tabs Widget into Main Content Area")

    By default, the Tabs widget contains 3 Header Items (tab titles) and 3 Content Items (tab content). You can add or delete as many as required.
  
1. Add the relevant content to each of the Header Item and Content Item placeholders. In this example, we add text. You can add forms, images, labels, etc.

1. On the **Properties** tab, you can customize the Tabs look and feel by setting any of the optional properties, for example, which tab is displayed as the active tab when the page loads and whether the tabs are displayed vertically or horizontally.

    ![Screenshot of the Properties tab for customizing the Tabs widget in Service Studio](images/tabs-4-ss.png "Tabs Widget Properties")

After following these steps and publishing the module, you can test the pattern in your app.

## Demo

<iframe width="750" height="500" src="https://www.youtube.com/embed/97uPVx-Q1lQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen">
</iframe>

## Properties

### Tabs

| **Property**                                   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ActiveTab (Text): Optional                     | Defines which tab is active when the page loads. <p>Examples</p><ul><li>Blank - The first tab is the active tab.</li><li>"tab-two" - The second tab is the active tab. </li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Orientation (Orientation Identifier): Optional | If Vertical, the tabs are displayed vertically. If Horizontal, the tabs are displayed horizontally. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| IsJustified (Boolean): Optional                | If True, the Tabs are evenly distributed in the space available. If False, the Tabs are left aligned. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| IsRight (Boolean): Optional                    | If True, the Tabs are displayed to the right of the Tab content. If False, the Tabs are displayed to the left of the Tab content. This is the default. **Note**: This setting is only applicable if the **Orientation** property is set to **Vertical**.                                                                                                                                                                                                                                                                                                                                                                                               |
| ExtendedClass (Text): Optional                 | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

### Tabs Header Item

| **Property**              | **Description**                                                                                             |
|---------------------------|-------------------------------------------------------------------------------------------------------------|
| DataTab (Text): Mandatory | Sets the name to connect to the Tabs Content Item. Should be the same as the paired Header Item and unique. |

### Tabs Content Item

| **Property**              | **Description**                                                                                          |
|---------------------------|----------------------------------------------------------------------------------------------------------|
| DataTab (Text): Mandatory | Value that connects with the Tabs Header Item. Should be the same as the paired Content Item and unique. |
