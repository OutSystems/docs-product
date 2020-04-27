---
tags: runtime-traditionalweb; 
summary: ProgressCircle shows the current progress of a task using circular or semi-circular progress indicators.
---

# Progress Circle

You can use the Progress Circle UI Pattern to show the current progress of an operation flow. The progress is incremented in fractions of the circular badge. You can also show progress in a Progress Bar or Progress Circle Fraction display type. When using the Progress Circle be consistent, for example, if an action displays a linear indicator on one screen, that same action should not use a circular indicator elsewhere in the app. 

 ![](<images/progresscircle-image-2.png>)


**How to use the Progress Circle UI Pattern**


1. In Service Studio, in the Toolbox, search for `Progress Circle`. 

    The Progress Circle widget is displayed.

    ![](<images/progresscircle-image-8.png>)
  

1. From the Toolbox, drag the Progress Circle widget onto your application's screen.

1. Define the progress value.

    ![](<images/progresscircle-image-1.png>)

1. Set the required content in the placeholder.

After following these steps and publishing the module, you can test the pattern in your app.


## Properties

| **Property** |  **Description** |  **Usage** |
|---|---|---|
| Progress (Integer): Mandatory  |  Percentage to display, you can use functions or local variables. |
| ProgressColor (Color Identifier): Optional  |  The color of the stroke on progress circle. |  
| TrailColor (Color Identifier): Optional  |  The color of the empty part of the progress circle. | 
| CircleThickness (Integer): Optional  |  The thickness of the circle that marks the progress. |  
| AnimateInitialProgress (Boolean): Optional  |  Animate the progress circle from zero to progress value. |  
| IsSemiCircle (Boolean): Optional  |  Change the type of progress bar from circle to semi circle. |  
| AdvancedFormat (Text): Optional  |  Allow for more options beyond what it's provided through the input parameters. For more information visit: https://kimmobrunfeldt.github.io/progressbar.js/. Example: `{ easing: 'bounce' }` |  

## See also
* OutSystems UI Live Style Guide: [Progress Circle](https://outsystemsui.outsystems.com/WebStyleGuidePreview/ProgressCircle.aspx)
* OutSystems UI Pattern Page: [Progress Circle](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/PatternDetail?PatternId=58)
