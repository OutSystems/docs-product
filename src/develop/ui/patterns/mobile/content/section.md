---
tags: runtime-mobileandreactiveweb;  
summary: Section separates content into groups, easing visual organization.
---

# Section

You can use the Section UI Pattern to organize on-screen content into different sections. This pattern can also be used with the Section Index UI Pattern to create anchors for each section.

![](<images/section-5-ss.png>)

**How to use the Section UI Pattern**

1. In Service Studio, in the Toolbox, search for `Section`.
  
    The Section widget is displayed.

    ![](<images/section-1-ss.png>) 

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. To From the Toolbox, drag the Section widget into the Main Content area of your application's screen.

    ![](<images/section-2-ss.png?width=800>)

    By default, the Section widget contains Title and Content placeholders.

1. Add your content to the placeholders.

    In this example, we add a title to the Title placeholder as well as  text and a button to the Content placeholder. We also set the button to redirect the user to a new page when clicked.

    ![](<images/section-3-ss.png?width=800>)

1. On the **Properties** tab, you can customize the Section's look and feel by setting any of the (optional) properties.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| UsePadding (Boolean): Optional | If set to True, padding is applied to the content area. This is the default value. If set to False, the content area has no padding. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
