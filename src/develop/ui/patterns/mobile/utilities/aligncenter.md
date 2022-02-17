---
tags: runtime-mobileandreactiveweb;  
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

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.
    
    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Align Center widget into the Main Content area of your application's screen.

    ![](<images/aligncenter-3-ss.png>)

    By default, the Align Center widget contains a Content placeholder.

1. From the Toolbox, drag the User Avatar pattern into Content placeholder.

    ![](<images/aligncenter-9-ss.png>)

1. On the **Properties** tab, in the **Name** property, enter a name. In this example, we enter `Scott Richie`.

    ![](<images/aligncenter-4-ss.png>)

1. Add any other relevant content to the Content placeholder. In this example we add some text (Scott Richie) and an image.

    ![](<images/aligncenter-5-ss.png>)

1. On the Align Center **Properties** tab, you can set the content's orientation (either vertical or horizontal).

    ![](<images/aligncenter-6-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

**Without Align Center UI Pattern** 

![](<images/aligncenter-7-ss.png>)

**With Align Center UI Pattern**

![](<images/aligncenter-8-ss.png>)

## Properties

| Property | Description |
|---|---|
| IsHorizontal (Boolean): Optional | If True, content is displayed horizontally. This is the default. If False, the content is displayed vertically. |
| ExtendedClass (Text): Optional  | <p>Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
