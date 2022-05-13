---
tags: runtime-mobileandreactiveweb;
summary: Section Index organizes the content of a screen, enabling quick navigation within the page.
locale: en-us
guid: f2009318-b804-4f98-88b9-3a654a6835b7
app_type: mobile apps, reactive web apps
---

# Section Index

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Section Index UI Pattern to organize the content of a screen, enabling quick navigation within the page.

![](<images/sectionindex-widget-ss.png>)

**How to use the Section Index UI Pattern**

1. In Service Studio, in the Toolbox, search for `Section Index`.

    The Section Index widget is displayed.

    ![](<images/sectionindex-dragwidget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the **Remove Unused Dependencies** setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Section Index widget into the Main Content area of your application's screen.

    In this example, we drag the Section Index widget into a column. 

    ![](<images/sectionindex-index-ss.png?width=800>)

1. In the Toolbox, search for and drag the Section widget into the Main Content area of your application's screen. Add as many sections as you require for your app.

    In this example, we drag 4 Section widgets into a column. Each section widget contains Title and Content placeholders. 

    ![](<images/sectionindex-section-ss.png>)

1. Add the relevant content to Section widget's **Title** and **Content** placeholders.

    In this example, we add employee names to the **Title** placeholders, and Card Sectioned widgets with some text and images to the **Content** placeholder.

    ![](<images/sectionindex-id-ss.png>)
   
1. On the **Properties** tab, you can customize the Section Index's look and feel by setting any of the optional properties.

    ![](<images/sectionindex-properties-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** | **Description** |
|---|---|
|SmoothScrolling (Boolean): Optional |  If True, the navigation to the destination is animated. This is the default. If False, the navigation is instant.|
|IsFixed (Text): Optional | If True, the Section Index Pattern is always in the same position on the screen. This is the default. If False, the Section Index Pattern scrolls with the page content.|
|ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1" "myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
