---
tags: ide usage, reactive web apps, tutorials for beginners, ui design patterns, navigation
summary: Explore the Section Index UI Pattern in OutSystems 11 (O11) for efficient content organization and navigation on screens.
locale: en-us
guid: f2009318-b804-4f98-88b9-3a654a6835b7
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=215:0
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Section Index

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

<div class="info" markdown="1">

**This documentation is not valid for deprecated components.** To check if your component is deprecated and how to migrate old versions, see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).

To find out what version of OutSystems UI you are using, see [OutSystems UI version](../../intro.md#outsystems-ui-version).

</div>

You can use the Section Index UI Pattern to organize the content of a screen, enabling quick navigation within the page.

![Example of a screen organized using the Section Index UI Pattern](images/sectionindex-example.png "Section Index Example")

**How to use the Section Index UI Pattern**

1. In Service Studio, in the Toolbox, search for `Section Index`.

    The Section Index widget is displayed.

    ![Service Studio displaying the Section Index widget in the Toolbox](images/sectionindex-widget-ss.png "Section Index Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the **Remove Unused Dependencies** setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Section Index widget into the Main Content area of your application's screen.

    In this example, we drag the Section Index widget into a column (ColumnsSmallLeft). By default, the Section Index widget contains 2 Section Index Items. You can add or delete as many as required. In this example, 4 Section Index Items are required.

    ![Dragging the Section Index widget into the Main Content area of a screen in Service Studio](images/sectionindex-dragwidget-ss.png "Dragging Section Index Widget to Screen")

1. In the Toolbox, search for and drag the Section widget onto the screen. Add as many sections as you require for your app.

    In this example, we drag 4 Section widgets (to match the number of Section Index Items) onto the screen (Column2). Each section widget contains a **Title** and **Content** placeholder. 

    ![Dragging Section widgets onto the screen to match the number of Section Index Items](images/sectionindex-section-ss.png "Adding Section Widgets to Screen")

1. Add the relevant content to Section widget's **Title** and **Content** placeholders.

    In this example, we add employee names to the **Title** placeholders, and Card Sectioned widgets with some text and images to the **Content** placeholder. 

    ![Adding employee names and Card Sectioned widgets to the Section widget's placeholders](images/sectionindex-card-ss.png "Adding Content to Section Widget")

1. Enter a name for each of the Card Sectioned widgets.
    
    This is so you can link them to each of the Section Index Items.

    ![Entering names for Card Sectioned widgets to link with Section Index Items](images/sectionindex-cardname-ss.png "Naming Card Sectioned Widgets")
   
1.  In the Toolbox, search for and drag the Text widget into the first Section Index Item and enter a title (in this example, the employee's name). 

    ![Entering a title for the first Section Index Item in Service Studio](images/sectionindex-item-ss.png "Entering Section Index Item Title")

1. To link the Section with the Section Index Item, select the Section Index Item, and on the **Properties** tab, set the **ScrollToWidgetId** property as the Section Id. In this example,  **AmosTesen.Id**.

    ![Setting the ScrollToWidgetId property to link the Section with the Section Index Item](images/sectionindex-id-ss.png "Setting Section Id")

1. Repeat steps 5,6 and 7 to add content and link your sections to the remaining Section Index Items.

1. On the **Properties** tab, you can customize the Section Index's look and feel by setting any of the optional properties.

    ![Customizing the look and feel of the Section Index by setting properties in Service Studio](images/sectionindex-properties-ss.png "Customizing Section Index Properties")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

### Section Index

| **Property** | **Description** |
|---|---|
|SmoothScrolling (Boolean): Optional | If True, navigation to the destination is animated. If False, the navigation is instant. The default value is True.|
|IsFixed (Text): Optional | If True, the Section Index Pattern is always in the same position on the screen. This is the default.<br/>If False, the Section Index Pattern scrolls with the page content. The default value is False.|
|ExtendedClass (Text): Optional| Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |


### Section Index Item

| **Property** | **Description** |
|---|---|
|ScrollToWidgetId (Text): Mandatory | The element the page navigates to.  |
| ExtendedClass (Text): Optional|Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |



