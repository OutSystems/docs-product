---
tags: runtime-mobileandreactiveweb;  
summary:  The Columns UI Pattern splits content into separate columns.
locale: en-us
guid: 1c4edd42-f577-4475-ad7c-72fbe2a849a8
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=201:22
---

# Columns

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Columns UI Pattern to split content into separate columns, improving the way information is displayed on-screen.

## How to use the Columns UI Pattern

1. In Service Studio, in the Toolbox, search for `Columns`.

    The various Columns widgets are displayed. 

    ![Screenshot of Columns widgets displayed in Service Studio](images/columnsmob-image-1.png "Columns Widgets in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the required Column widget into the Main Content area of your application's screen. The following example uses the Columns 2 widget.

    ![Example of dragging a Columns 2 widget into the main content area of an application screen](images/columnsmob-image-3.png "Dragging Columns Widget into Main Content Area")

1. Add the required content to the Columns widget. In this example we add an image and text.

    ![Adding an image and text to a Columns widget in an application screen](images/columnsmob-image-4.png "Adding Content to Columns Widget")

1. On the **Properties** tab, you can customize the Column's look and feel by setting any of the (optional) properties, for example, the size of the space between each of the columns (GutterSize), and in what order the columns display on different devices. 

    ![Customization options for Columns widget properties in Service Studio](images/columnsmob-image-2.png "Customizing Columns Properties")

1. After following these steps, and publishing the module, you can test the pattern in your app. 

## Properties

**Property** |  **Description** |  
---|---
GutterSize (GutterSizeIdentifier): Optional | Defines the space between columns.<br/><br/>Examples<br/><br/><ul><li>_Empty_ - Leaves a space of 16px between columns. This is the default (Entities.GutterSize.Base).</li><li>_Entities.GutterSize.None_ - No space between columns.</li></ul> |
TabletBehavior (BreakColumns Identifier): Optional | Defines how the columns are displayed on tablets. The predefined options for the tablet behavior are:<br/><br/><ul><li>All</li><li>First</li><li>Last</li><li>Middle</li><li>None</li></ul>See below for an example of how each of the options look. |
PhoneBehavior (BreakColumns Identifier): Optional | Defines how the columns are displayed on phones. The predefined options for the phone behavior are:<br/><br/><ul><li>All</li><li>First</li><li>Last</li><li>Middle</li><li>None</li></ul>See below for an example of how each of the options look. |
ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

**Entities.ColumnBreak.BreakNone (default)**

![Illustration of default column break behavior with no breaks between columns](images/Column_break_none.png "Default Column Break Behavior")  

**Entities.ColumnBreak.BreakMiddle**

![Illustration of column break behavior with a break in the middle column](images/Column_break_middle.png "Column Break Middle Behavior")

**Entities.ColumnBreak.BreakLast**

![Illustration of column break behavior with a break in the last column](images/Column_break_last.png "Column Break Last Behavior")

**Entities.ColumnBreak.BreakFirst**

![Illustration of column break behavior with a break in the first column](images/Column_break_first.png "Column Break First Behavior")
