---
tags: runtime-traditionalweb; 
summary: Align Center places content horizontally or vertically within a container.
---

# Align Center

You can use Align Center UI Pattern to center content horizontally or vertically on the screen. 

![](<images/aligncenter-1.png>)

**How to use the Align Center UI Pattern**

This example shows you how to center align a user's name and initials.

1. In Service Studio, in the Toolbox, search for `Align Center`. 

    The Align Center widget is displayed.

    ![](<images/aligncenter-2-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Align Center widget into the Main Content area of your application's screen.
    
    ![](<images/aligncenter-3-ss.png>)
   
1. From the Toolbox, drag the User Initials pattern into the Align Center placeholder.

1. On the **Properties** tab, in the Name property, enter a name. In this example, we enter **Scott Ritchie**.

    ![](<images/aligncenter-4-ss.png>)

1. Add the relevant content to the Align Center widget. In this example we add some text (Scott Richie) and an image. 

    ![](<images/aligncenter-5-ss.png>)

1. On the Align Center **Properties** tab, you can set the content's orientation (either vertical or horizontal).

    ![](<images/aligncenter-6-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. 


**Without Align Center UI Pattern** 

![](<images/aligncenter-7-ss.png>)

**With Align Center UI Pattern**

![](<images/aligncenter-8-ss.png>)


## Properties

| **Property** |  **Description** |  
|---|---|
| Orientation (Orientation Identifier): Optional | Set the content orientation, either horizontal or vertical. | 
| ExtendedClass (Text): Optional  | <p>Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |



