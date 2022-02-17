---
tags: runtime-mobileandreactiveweb;  
summary: Use the Center Content pattern to align the content to the center of its container.
---

# Center Content

You can use the Center Content UI Pattern to vertically align content to the center of its container.

![](<images/centercontent-1.png>)

**How to use the Center Content UI Pattern**

1. In Service Studio, in the Toolbox, search for `Center Content`.

    The Center Content widget is displayed.

    ![](<images/centercontent-2-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.
    
    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Center Content widget into the Main Content area of your application's screen.

    ![](<images/centercontent-3-ss.png>)

    By default, the Center Content widget contains Top, Center, and Bottom placeholders.

1. Add the relevant content to each of the placeholders. In this example we add some images and text.

    ![](<images/centercontent-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| ExtendedClass (Text): Optional | <p>Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
