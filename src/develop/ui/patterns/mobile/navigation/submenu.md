---
tags: runtime-mobileandreactiveweb;
summary: Submenu is used to create a menu contained within another menu.
---

# Submenu

You can use the Submenu UI Pattern to create a menu that is contained within another menu.

![](<images/submenu-3-ss.png>)

**How to use the Submenu UI Pattern**

1. In Service Studio, in the Toolbox, search for `Submenu`.

    The Submenu widget is displayed.

    ![](<images/submenu-1-ss.png>)

1. From the Toolbox, drag the Submenu widget into the Main Content area of your application's screen.

    ![](<images/submenu-2-ss.png?width=800>)

    By default, the Submenu widget contains a Menu placeholder and an Items placeholder that contains a link. You can add as many Items placeholders as required. In this example we add 3 more.

1. Add the relevant content to the Menu and Items placeholders.

    In this example, we add text to the Menu placeholder, and set the links in the Items placeholders to navigate to a different pages in the app. 
   
    ![](<images/submenu-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| ExtendedClass (Text): Optional | Add custom style classes to the Submenu UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Submenu UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Submenu UI styles being applied.</li></ul></p> |
