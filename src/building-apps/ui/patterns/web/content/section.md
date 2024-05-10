---
tags: runtime-traditionalweb; 
summary: Explore how to effectively use the Section UI Pattern in OutSystems 11 (O11) to organize content in Traditional Web Apps.
locale: en-us
guid: 838dea96-eace-422c-8430-3a86522d2449
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=4762%3A22956&mode=design&t=ANpsYvOCthr9AWot-1
---

# Section

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Section UI Pattern to organize on-screen content into different sections. This pattern can also be used with the Section Index UI Pattern to create anchors for each section.

![Preview image showing the Section UI Pattern in a Traditional Web App](images/section-5-ss.png "Section UI Pattern Preview")

**How to use the Section UI Pattern**

1. In Service Studio, in the Toolbox, search for `Section`.
  
    The Section widget is displayed.

    ![Screenshot of the Section widget in the Service Studio toolbox](images/section-1-ss.png "Section Widget in Service Studio") 

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. To From the Toolbox, drag the Section widget into the Main Content area of your application's screen.

    ![Process of dragging the Section widget into the Main Content area of an application's screen](images/section-2-ss.png "Dragging Section Widget into Main Content")

    By default, the Section widget contains Title, Actions, and Content placeholders.

1. Add your content to the placeholders. In this example, we add a title to the Title placeholder, text to the Content placeholder, and a button to the Actions placeholder.

    ![Example of adding a title, text, and a button to the placeholders of the Section widget](images/section-3-ss.png "Adding Content to Section Widget Placeholders")

1. Add the desired action to the content you have added to the Actions placeholder. In this example, the button we added redirects the user to a new page.

    ![Demonstration of adding an action to a button in the Actions placeholder of the Section widget](images/section-6-ss.png "Configuring Action in Section Widget")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** | **Description** |
|---|---|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
