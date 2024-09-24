---
tags: runtime-mobileandreactiveweb;  
summary: Section separates content into groups, easing visual organization.
locale: en-us
guid: f8eb7c31-9003-4675-85a1-8c09a8aeafd8
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=205:54
---

# Section

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Section UI Pattern to organize on-screen content into different sections. This pattern can also be used with the Section Index UI Pattern to create anchors for each section.

![Screenshot of an example using the Section UI Pattern in a mobile or reactive web app](images/section-5-ss.png "Section UI Pattern Example")

**How to use the Section UI Pattern**

1. In Service Studio, in the Toolbox, search for `Section`.
  
    The Section widget is displayed.

    ![Service Studio interface showing the Section widget in the toolbox](images/section-1-ss.png "Section Widget in Service Studio") 

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. To From the Toolbox, drag the Section widget into the Main Content area of your application's screen.

    ![Dragging the Section widget from the toolbox into the main content area of an application screen](images/section-2-ss.png "Dragging Section Widget into Main Content Area")

    By default, the Section widget contains Title and Content placeholders.

1. Add your content to the placeholders.

    In this example, we add a title to the Title placeholder as well as  text and a button to the Content placeholder. We also set the button to redirect the user to a new page when clicked.

    ![Section widget with a title in the Title placeholder and text with a button in the Content placeholder](images/section-3-ss.png "Section Widget with Title and Content Placeholders")

1. On the **Properties** tab, you can customize the Section's look and feel by setting any of the (optional) properties.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UsePadding (Boolean): Optional | If set to True, padding is applied to the content area. This is the default value. If set to False, the content area has no padding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
