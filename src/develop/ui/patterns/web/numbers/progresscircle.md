---
tags: runtime-traditionalweb; 
summary: Displays the current progress of a task using circular or semi-circular progress indicators.
---

# Progress Circle

You can use the Progress Circle UI Pattern to show the current progress of an operation flow. The progress is incremented in fractions of the circular badge. <!-- You can also show progress in a Progress Bar or Progress Circle Fraction display type.  When using the Progress Circle Pattern, you must be consistent, for example, if an action displays a linear indicator on one screen, that same action should not use a circular indicator elsewhere in the app. -->

 ![](<images/progresscircle-2-ss.png>)

**How to use the Progress Circle UI Pattern**

1. In Service Studio, in the Toolbox, search for `Progress Circle`. 

    The Progress Circle widget is displayed.

    ![](<images/progresscircle-8-ss.png>)
  
1. From the Toolbox, drag the Breadcrumbs widget into the Main Content area of your application's screen.
    
    ![](<images/progresscircle-9-ss.png>)

    
1. On the **Properties** tab, define the progress value using the **Progress** property. You can use a [function](../../../../../ref/lang/auto/builtinfunctions.final.md) of [local variable](<../../../../../ref/lang/auto/Class.Local Variable.final.md>).

    ![](<images/progresscircle-1-ss.png>)

1. On the **Properties** tab, you can also change the Progress Circle's look and feel by setting the (optional) properties, for example, the color and animation settings. 

After following these steps and publishing the module, you can test the pattern in your app.


## Properties

| **Property** |  **Description** |  
|---|---|
| Progress (Integer): Mandatory  |  Percentage to display. You can use functions or local variables.  |
| ProgressColor (Color Identifier): Optional  |  The color of the stroke on progress circle. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available. <p>Examples <ul><li>_Blank_ - The stroke color displays in the color you chose when creating the app (default value).</li><li>_Entities.Color.Red_ - The stroke color is red.</li></ul></p> |  
| TrailColor (Color Identifier): Optional  |  The color of the empty part of the progress circle. <p>Examples <ul><li>_Blank_ - The empty part of the circle is a light gray (Entities.Color.Neutral5). This is the default value.</li><li>_Entities.Color.Blue_ - The empty part of the progress circle is blue.</li></ul></p>| 
| CircleThickness (Integer): Optional  |  The thickness of the circle that marks the progress. <p>Examples <ul><li>_Blank_ - The circle thickness is 4px. This is the default value.</li><li>_8_ - The circle thickness is 8px.</li></ul></p> |  
| AnimateInitialProgress (Boolean): Optional  | If set to True, the progress from zero to the progress value is animated. This is the default value. If set to False, the progress is not animated.|  
| IsSemiCircle (Boolean): Optional  | If set to True, the Progress Circle is changed from circle to semi circle. If set to False, it remains a circle. This is the default value.|  
| AdvancedFormat (Text): Optional  |  Allow for more options beyond what is provided through the input parameters. For more information, visit: https://kimmobrunfeldt.github.io/progressbar.js/. Example: `{ easing: 'bounce' }` |  
