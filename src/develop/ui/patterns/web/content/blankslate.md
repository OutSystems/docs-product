---
tags: runtime-traditionalweb; 
summary: Blank Slate informs end users when they start using the application, complete a task or when there is no data available for display.
---

# Blank Slate
You can use the Blank State UI Pattern to inform end users when they start using the application, complete a task, or when there is no data available for display.

![](<images/blankslate-image-1.png>)

**How to use the Blank Slate UI Pattern**

1. In Service Studio, in the Toolbox, search for `Blank Slate`.

    The Blank Slate widget is displayed.

    ![](<images/blankslate-image-2.png>)

1. From the Toolbox, drag the Blank Slate widget into the Main Content area of your application's screen.

    ![](<images/blankslate-image-3.png>)

    By default, the Blank Slate widget contains an icon and some text. You can change these if required.

1. Add your content to the placeholder. In this example we change the icon. To do this, from the Widget Tree, select the Icon, and on the **Properties** tab, from the **Name** drop-down, select the icon you want to display. 

    ![](<images/blankslate-image-4.png>)

After following these steps and publishing the module, you can test the pattern in your app. 

## Properties

| **Property** |  **Description** |
|---|---|
| Position (PositionExtended Identifier): Optional| Sets the widget position. <p>Examples</p><ul><li>_Blank_ - The widget displays in the center of the screen. This is the default.</li><li>_Entities.PositionExtended.BottomRight_ - The widget displays on the bottom right of the screen. </li></ul> |  
| ExtendedClass (Text): Optional  |  Add custom style classes to the Blank Slate UI Pattern. You define your [custom style classes](../../../../../../develop/ui/look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ Adds the _myclass_ style to the Blank Slate UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Blank Slate UI styles being applied. </li></ul> |
  
