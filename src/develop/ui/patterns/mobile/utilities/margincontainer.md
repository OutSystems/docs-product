---
tags: runtime-mobileandreactiveweb;  
summary: Use the Margin Container and easily add symmetrical padding around a container.
---

# Margin Container

You can use the Margin Container UI Pattern to add symmetrical padding around a container.

![](<images/margincontainer-1-ss.png>)

**How to use the Margin Container UI Pattern**

1. In Service Studio, in the Toolbox, search for `Margin Container`.

    The Margin Container widget is displayed.

    ![](<images/margincontainer-2-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.
    
    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Margin Container widget into the Main Content area of your application's screen.

    ![](<images/margincontainer-3-ss.png>)

    You can add as many Margin Container widgets as you want. In this example, we add 2.

1. Add the relevant content to the Margin Container placeholder.

    In this example we add an image widget to each of the placeholders and on the **Properties** tab, import an image using the **Image** dropdown.

    ![](<images/margincontainer-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| ExtendedClass (Text): Optional | <p>Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
