---
tags: runtime-mobileandreactiveweb;  
summary: The Card Item widget allows you to list items with multiple content types, such as an image or icon, a title and description, and an action to the right.
locale: en-us
guid: 434a7ae9-243a-47b8-ae7c-e2f424a5411b
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=205:26
---

# Card Item

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Card Item UI Pattern to list items with multiple content types, such as image or icon (to the left), a title and description, and an action to the right.

![Example of a Card Item UI Pattern with multiple content types](images/carditem-1.png "Card Item UI Pattern Example")

**How to use the Card UI Pattern**

1. In Service Studio, in the Toolbox, search for `Card Item`.

    The Card Item widget is displayed.

    ![Screenshot showing the Card Item widget in Service Studio](images/carditem-2-ss.png "Service Studio Card Item Widget")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Card widget into the Main Content area of your application's screen.

    In this example, we drag the widget into the Card widget that's already in the Main Content area of the screen. You can add as many Card Item widgets as required (we add 4). 

    ![Process of dragging the Card Item widget into the Main Content area in Service Studio](images/carditem-3-ss.png "Adding Card Item to Main Content Area")

    By default, the Card Item widget contains a Left, Title, Content, and Right placeholder. 

1. Add your content to each of the placeholders. 

    In this example, we add an icon to the Left placeholder, text to the Title and Content placeholders, and a phone icon to the Right placeholder. 

    ![Example of adding content to the placeholders of the Card Item widget in Service Studio](images/carditem-4-ss.png "Customizing Card Item Content")

1. On the **Properties** tab, you can customize the Card Item's look and feel by setting any of the (optional) properties.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
