---
tags: runtime-mobileandreactiveweb;
summary: Submenu is used to create a menu contained within another menu.
---

# Submenu

<div class="info" markdown="1">

If you are using an OutSystems UI version lower than 2.8.0, see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).
                            
</div>

You can use the Submenu UI Pattern to create a menu that is contained within another menu.

![Example submenu](<images/submenu-example-ss.png>)

**How to use the Submenu UI Pattern**

1. In Service Studio, in the Toolbox, search for `Submenu`.

    The Submenu widget is displayed.

    ![Submenu widget](<images/submenu-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Submenu widget into the Main Content area of your application's screen.

    ![Drag widget to screen](<images/submenu-dragwidget-ss.png>)

    By default, the Submenu widget contains a Menu placeholder and an Items placeholder that contains a link. You can add as many Items placeholders as required. In this example we add 3 more.

1. Add the relevant content to the Menu and Items placeholders.

    In this example, we add text to the Menu placeholder, and set the links in the Items placeholders to navigate to different pages in the app.

    ![Add content](<images/submenu-additems-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Framework Cheat Sheet](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/CheatSheet). |
