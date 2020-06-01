---
tags: runtime-traditionalweb; 
summary: Progress Bar displays the progress of a task by incrementing values in a bar.
---

# Progress Bar

You can use the Progress Bar to display percentage values by incrementing values in a bar, and to show the current progress of a task flow. You can also show progress in a Progress Circle or a Progress Circle Fraction. When using the Progress Bar UI Pattern, be consistent, for example, if an action displays a linear indicator on one screen, that same action should not use a circular indicator elsewhere in the app. 

![](<images/progressbar-1.png>)

**How to use the Progress Bar UI Pattern**

1. In Service Studio, in the Toolbox, search for `Progress Bar`. 

    The Progress Bar widget is displayed.

    ![](<images/progressbar-2-ss.png>)

1. From the Toolbox, drag the Progress Bar widget onto your application's screen.

    ![](<images/progressbar-3-ss.png>)

    By default, the Progress Bar widget contains a Title and Value placeholder. 

    ![](<images/progressbar-4-ss.png>)

1. Add the required content to the Title and Value placeholders. You can use a [function](../../../../../ref/lang/auto/builtinfunctions.md) or [local variable](<../../../../../ref/lang/auto/Class.Local Variable.final.md>) to set the percentage value to display.

1. On the **Properties** tab, you can customize Progress Bar's look and feel by setting any of the optional properties, for example, the shape, color, size, and orientation of the Progress Bar.

    ![](<images/progressbar-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. 

## Properties

| **Property** |  **Description** |  
|---|---|
| Percentage (Integer): Optional  |  Percentage to display. You can use functions or local variables. | 
| Color (Color Identifier): Optional  | Progress bar color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - The progress bar color  is the color you chose when creating the app (default value).</li><li>_Entities.Color.Red_ - The progress bar color is red.</li></ul></p>  
| Shape (Shape Identifier): Optional  |  Set the Progress Bar shape. The predefined options are: <li>Rounded</li><li> Soft Rounded </li> <li>Sharp</li><p>Examples</p><ul><li>_Blank_ - The Progress Bar has a rounded shape (Entities.Shape.Rounded). This is the default. </li><li>_Entities.Shape.Sharp_ - The Progress Bar has a sharp shape.</li></ul>| 
| Size (ProgressBarSize Identifier): Optional  |  Set the Progress Bar size. The predefined options are: <li>Extra Small</li><li>Small</li> <li>Base (default)</li>|  
| IsInline (Boolean): Optional  | If True, the value placeholder is placed at the end of the line and the label placeholder is hidden. If False, the value and label of the placeholder are placed over the line. This is the default.|
| ExtendedClass (Text): Optional  | <p>Add custom style classes to the Progress Bar UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Progress Bar UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Progress Bar UI styles being applied.</li></ul></p> |


