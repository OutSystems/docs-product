---
tags: runtime-mobileandreactiveweb;  
summary: Inline SVG changes fill and stroke properties or animates the SVG paths.

---

# Inline SVG

You can use the Inline SVG UI Pattern to change fill and stroke properties or animate the SVG paths.

**How to use the Inline SVG UI Pattern**

1. In Service Studio, in the Toolbox, search for `Inline SVG`.

    The Inline SVG widget is displayed.

    ![](<images/inlinesvg-2-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.
    
    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Inline SVG widget into the Main Content area of your application's screen.

    ![](<images/inlinesvg-3-ss.png>)

1. On the **Properties** tab, in the **SVGCode** property, set your SVG code. 

    In this example, we enter the following:

    ``"<svg height=""100"" width=""350"" fill=""yellow"">
    <circle cx=""50"" cy=""50"" r=""30"" stroke=""red"" stroke-width=""25"" fill=""white"" />
    <text x=""110"" y=""60"" fill=""black"" font-size=""40"" font-weight=""bold"" font-family=""open sans"">outsystems</text>
    Sorry, your browser does not support inline SVG.  
    </svg>"``

    ![](<images/inlinesvg-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.



Using the example above, the results are as follows:

![](<images/inlinesvg-1-ss.png>)


## Properties

| Property | Description |
|---|---|
| SVGCode (Text): Optional | SVG markup code that is appended onto the HTML.|
| ExtendedClass (Text): Optional  | <p>Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
