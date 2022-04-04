---
tags: runtime-traditionalweb; 
summary: Flip Content prioritizes information display, keeping the interface uncluttered.
---

# Flip Content

 You can use the Flip Content UI Pattern to display information that when, for example, is clicked, flips and displays different information.

![](<images/flipcontent-1.gif?width=500>)

**How to use the Flip content UI Pattern**

1. In Service Studio, in the Toolbox, search for `Flip Content`.

    The Flip Content widget is displayed.

    ![](<images/flipcontent-2-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Flip Content widget into the Main Content area of your application's screen.

    ![](<images/flipcontent-3-ss.png>)

1. Add the required content for the front and back placeholders inside the Flip Content widget.

    In this example, we add images by dragging the Image widget into the front and back placeholders in the Flip Content widget and selecting an image from the sample OutSystems UI images.

    ![](<images/flipcontent-4-ss.png>)

1. On the **Properties** tab, from the **Trigger** drop-down, you can customize when the Flip Content widget is triggered, for example, when it is clicked.  

    ![](<images/flipcontent-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| Trigger (Trigger Identifier): Optional  | Define when the flip event is triggered. The predefined options are:<p><ul><li>Click</li><li>Hover</li><li>Manual</li></ul></p><p>Examples <ul><li>_Blank_ - The flip event is triggered when the hovers over it (default value).</li><li>_Entities.Trigger.Click_ - The flip event is triggered when the user clicks it.</li><li>_Entities.Trigger.Hover_ -  The flip event is triggered when the user hovers over it.</li></ul></p> |  
| ExtendedClass (Text): Optional  | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the myclass style to the UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |  
