---
tags: runtime-traditionalweb; 
summary: ProgressBar displays the progress of a task by incrementing values in a bar.
---

# Progress Bar

You can use the Progress Bar to display percentage values by incrementing values in a bar, and to show the current progress of a task flow. You can also show progress in a Progress Circle or a Progress Circle Fraction. When using the Progress Bar UI Pattern, be consistent, for example, if an action displays a linear indicator on one screen, that same action should not use a circular indicator elsewhere in the app. 

![](<images/progressbar-image-8.png>)

**How to use the Progress Bar UI Pattern**

1. In Service Studio, in the Toolbox, search for `Progress Bar`. 

    The Progress Bar widget is displayed.

    ![](<images/progressbar-image-9.png>)

1. From the Toolbox, drag the Progress Bar widget onto your application's screen.

1. Use a variable to set the percentage value to display.
1. On the **Properties** tab, set the  shape, size, orientation and color of the progress bar.

1. Set the content in the placeholders. 

    ![](<images/progressbar-image-1.png>)

After following these steps and publishing the module, you can test the pattern in your app. 

## Properties

| **Property** |  **Description** |  **Usage** |
|---|---|---|
| Percentage (Integer): Optional  |  Percentage to display, you can use functions or local variables. | 
| Color (Color Identifier): Optional  |  Set the background color. |  
| Shape (Shape Identifier): Optional  |  Set the shape. | 
| Size(ProgressBarSize Identifier): Optional  |  Set the size. |  
| IsInline (Boolean): Optional  |  Set the orientation of the value placeholder. When True, the value placeholder is placed at the end of the line and the label placeholder is hidden. When False, value and label of the placeholder is placed over the line. |
| ExtendedClass (Text): Optional  |  Add custom style classes to the block. |  



## See also
* OutSystems UI Live Style Guide: [Progress Bar](https://outsystemsui.outsystems.com/WebStyleGuidePreview/ProgressBar.aspx)
* OutSystems UI Pattern Page: [Progress Bar](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/PatternDetail?PatternId=57)
