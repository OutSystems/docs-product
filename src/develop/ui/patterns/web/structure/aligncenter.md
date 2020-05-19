---
tags: runtime-traditionalweb; 
summary: Align Center places content horizontally or vertically within a container.
---

# Align Center

You can use Align Center UI Pattern to center content horizontally or vertically on the screen. 

![](<images/aligncenter-image-10.png>)

**How to use the Align Center UI Pattern**

This example shows you how to center align a user's name and initials.

1. In Service Studio, in the Toolbox, search for `Align Center`. 

    The Align Center widget is displayed.

    ![](<images/aligncenter-image-11.png>)

1. From the Toolbox, drag the Align Center widget onto your application’s screen.
    
    ![](<images/aligncenter-image-12.png>)
   
1. From the Toolbox, drag the User Initials pattern into the Align Center placeholder.

1. On the **Properties** tab, in the Name property, enter a name, for example **Scott Ritchie**.

    ![](<images/aligncenter-image-1.png>)

1. Drag the Text widget into the Align Center placeholder and enter  ``Scott Ritchie``.

    ![](<images/aligncenter-image-2.png>)

1. On the Align Center **Properties** tab, you can set the content's orientation.

    ![](<images/aligncenter-image-13.png>)

1. After following these steps and publishing the module, you can test the pattern in your app. It should look something like the following:
   
![](<images/aligncenter-image-3.png>)

## Properties

| **Property** |  **Description** |  
|---|---|
| Orientation (Orientation Identifier): Optional | Set the content orientation. | 
| ExtendedClass (Text): Optional  | <p>Add custom style classes to the Align Center UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Align Center UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Align Center UI styles being applied.</li></ul></p> |



