---
tags: runtime-mobileandreactiveweb;
summary: Allows users to rate a particular item or service.
---

# Rating

You can use the Rating UI Pattern to allow users rate, for example, products and services.

![Example of Rating pattern](<images/rating-example-ss.png>)

**How to use the Rating UI Pattern**

1. In Service Studio, in the Toolbox, search for `Rating`.

    The Rating widget is displayed.

    ![Rating widget](<images/rating-widget-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the **Rating** widget into the Main Content area of your application's screen.

    ![Drag widget onto the screen](<images/rating-dragwidget-ss.png>)

    By default, the pattern is already prepared to work as a 5-Star rating pattern. However, you can change the icons to hearts, smiles, thumbs, or any other content.

1. On the **Properties** tab, from the **RatingValue** dropdown, enter the rating number you want displayed. In this example, we enter `3`.  
    
    ![Set the Rating Value property](<images/rating-value-ss.png>)

1. You can customize the Rating's look and feel by setting any of the optional properties.

    ![Set additional properties](<images/rating-properties-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
|RatingValue (Decimal): Mandatory | Rating number to display. |
|RatingScale (Integer): Optional | The number of items to display. The default is 5 which means the rating is from 0 to 5. If set to 1, the item behaves as a view only element and the **IsEdit** property is automatically set to False. The maximum value is 100. If the value introduced is bigger, only 100 items are displayed.|
|IsEdit (Boolean): Optional | If True, the user can interact with the pattern. Default value is False. |
|Size (Size Identifier): Optional | The size of the rating pattern. There are 3 sizes available; small, medium, and base. Base is the default size.  |
|ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>``"myclass"`` - Adds the ``myclass`` style to the UI styles being applied.</li><li>``"myclass1 myclass2"`` - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
