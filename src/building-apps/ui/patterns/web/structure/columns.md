---
tags: runtime-traditionalweb; 
summary: Columns split content into multiple columns with responsive capabilities to improve the way information is displayed.
locale: en-us
guid: 0488b53b-190d-4467-83a4-76bae70bf4c2
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=245%3A67&mode=design&t=u4ANW5BJS7Flsdmg-1
---

# Columns

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Columns UI Pattern to split content into separate columns, improving the way information is displayed on screen.

![Example of content split into multiple columns using the Columns UI Pattern](images/columns-1.png "Columns UI Pattern Example")

**How to use the Columns UI Pattern**

1. In Service Studio, in the Toolbox, search for `Columns`.

    The various Column widgets are displayed.

    ![Screenshot showing Column widgets in Service Studio's Toolbox](images/columns-2-ss.png "Service Studio Column Widgets")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the required Column widget into the Main Content area of your application's screen. In this example, we drag the Columns 2 widget onto the screen.

    ![Process of dragging a Column widget into the main content area of an application's screen](images/columns-3-ss.png "Dragging Column Widget into Main Content Area")

1. Add the required content to the Column widget, for example, images, forms, text. In this example, we add some images and text.

    ![Example of adding images and text to a Column widget in an application](images/columns-4-ss.png "Adding Content to Column Widget")

1. On the **Properties** tab, you can  customize the Colums's look and feel by setting any of the optional properties, for example, the size of columns and space between each of the columns (GutterSize), and in what order the columns display on different device types.

    ![Customization of Columns properties in the Properties tab](images/columns-5-ss.png "Customizing Columns Properties")

After following these steps and publishing the module, you can test the pattern in your app.
  
## Properties

| **Property**                                       | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GutterSize (GutterSize Identifier): Optional       | Set the gutter size. The default Gutter size is large.<p>Examples <ul><li>Blank - A large white space between each column (default value).</li><li>_Entities.GutterSize.Gutter_None - No white space between each of the columns</li><li>Entities.GutterSize.Gutter_XS - An extra small white space between each of the columns</li></ul></p>                                                                                                                                                                                                                                                                                      |
| TabletBehavior (BreakColumns Identifier): Optional | Defines how the columns are displayed on tablets. The predefined options for the tablet behavior are: <p><ul><li>All</li><li>First</li><li>Last</li><li>Middle</li><li>None (default).</li></ul></p><p>See below for an example of how each setting displays.</p>                                                                                                                                                                                                                                                                                                                                                                  |
| PhoneBehavior (BreakColumns Identifier): Optional  | Defines how the columns are displayed on phones. The predefined options for the phone behavior are: <p><ul><li>All (default).</li><li>First</li><li>Last</li><li>Middle</li><li>None</li></ul></p><p>See below for an example of how each setting displays.</p>                                                                                                                                                                                                                                                                                                                                                                    |
| ExtendedClass (Text): Optional                     | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

The following are examples of how the columns are displayed on each of the devices, depending on which property you select.

**Entities.BreakColumns.None**

![Example of column layout with no breaks on a device screen](images/Column_break_none.png "Column Break None Behavior")

**Entities.BreakColumns.Middle**

![Example of column layout with a break in the middle on a device screen](images/Column_break_middle.png "Column Break Middle Behavior")

**Entities.BreakColumns.Last**

![Example of column layout with the last column breaking on a device screen](images/Column_break_last.png "Column Break Last Behavior")

**Entities.BreakColumns.First**

![Example of column layout with the first column breaking on a device screen](images/Column_break_first.png "Column Break First Behavior")
