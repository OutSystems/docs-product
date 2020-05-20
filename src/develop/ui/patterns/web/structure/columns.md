---
tags: runtime-traditionalweb; 
summary: Columns split content into multiple columns with responsive capabilities to improve the way information is displayed.
---

# Columns

You can use the Columns UI Pattern to split content into separate columns, improving the way information is displayed on screen.

 ![](<images/columns-image-4.png>)

**How to use the Columns UI Pattern**

1. In Service Studio, in the Toolbox, search for `Columns`. 

    The various Column widgets are displayed.

    ![](<images/columns-image-6.png>)

1. From the Toolbox, drag the required Column widget into the Main Content area of your application's screen. The following example uses the Columns 3 widget.

    ![](<images/columns-image-7.png>)

1. Add the required content to the Column widget, for example, [counters](../../../../../develop/ui/patterns/web/numbers/counter.md).

    ![](<images/columns-image-1.png>)

1. On the **Properties** tab, you can  customize the Colums's look and feel by setting any of the optional properties, for example, the size of columns and space between each of the columns (GutterSize), and in what order the columns display on different device types.

    ![](<images/columns-image-2.png>)

After following these steps and publishing the module, you can test the pattern in your app.
  
## Properties

| **Property** |  **Description** |
|---|---|
| GutterSize (GutterSize Identifier): Optional | Set the gutter size. The default Gutter size is large.<p>Examples <ul><li>_Blank_ - A large white space between each column (default value).</li><li>_Entities.GutterSize.Gutter_None_ - No white space between each of the columns<li>_Entities.GutterSize.Gutter_XS_ - An extra small white space between each of the columns</li></ul></p> | 
| TabletBehavior (BreakColumns Identifier): Optional | Defines how the columns are displayed on tablets. The predefined options for the tablet behavior are: <p><ul><li>All</li><li>First</li><li>Last</li><li>Middle</li><li>None (default).</li></ul></p><p>See below for an example of how each setting displays.</p>|
| PhoneBehavior (BreakColumns Identifier): Optional | Defines how the columns are displayed on phones. The predefined options for the phone behavior are: <p><ul><li>All (default).</li><li>First</li><li>Last</li><li>Middle</li><li>None</li></ul></p><p>See below for an example of how each setting displays.</p>|
| ExtendedClass (Text): Optional  |Add custom style classes to the Columns UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value)</li><li>_''myclass''_ - Adds the _myclass_ style to the Columns UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Columns UI styles being applied.</li></ul></p> |

**Entities.BreakColumns.None**

![](images/Column_break_none.png)  

**Entities.BreakColumns.Middle**

![](images/Column_break_middle.png)

**Entities.BreakColumns.Last**

![](images/Column_break_last.png)

**Entities.BreakColumns.First**

![](images/Column_break_first.png)