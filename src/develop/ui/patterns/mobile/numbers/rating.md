---
tags: runtime-mobileandreactiveweb;
summary: Allows users to rate a particular item or service.
locale: en-us
guid: f0a35dfd-ff8e-4e04-8a4b-2407efaca4f6
app_type: mobile apps, reactive web apps
---

# Rating

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Rating UI Pattern to allow users rate, for example, products and services.

![Example of Rating pattern](<images/rating-example-ss.png>)

**How to use the Rating UI Pattern**

1. In Service Studio, in the Toolbox, search for `Rating`.

    The Rating widget is displayed.

    ![Rating widget](<images/rating-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the **Rating** widget into the Main Content area of your application's screen.

    ![Drag widget onto the screen](<images/rating-dragwidget-ss.png>)

    By default, the pattern is already prepared to work as a 5-Star rating pattern. However, you can change the icons to hearts, smiles, thumbs, or any other content.

1. On the **Properties** tab, from the **RatingValue** dropdown, enter the rating number you want displayed. In this example, we enter `3`.  
    
    ![Set the Rating Value property](<images/rating-value-ss.png>)

1. You can customize the Rating's look and feel by setting any of the optional properties.

    ![Set additional properties](<images/rating-properties-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RatingValue (Decimal): Mandatory | Rating number to display.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| RatingScale (Integer): Optional  | The number of items to display. The default is 5 which means the rating is from 0 to 5. If set to 1, the item behaves as a view only element and the **IsEdit** property is automatically set to False. The maximum value is 100. If the value introduced is bigger, only 100 items are displayed.                                                                                                                                                                                                                                                                                                                     |
| IsEdit (Boolean): Optional       | If True, the user can interact with the pattern. Default value is False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Size (Size Identifier): Optional | The size of the rating pattern. There are 3 sizes available; small, medium, and base. Default size is Base.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ExtendedClass (Text): Optional   | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
