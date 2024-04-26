---
tags: runtime-mobileandreactiveweb;
summary: Allows users to rate a particular item or service.
locale: en-us
guid: f0a35dfd-ff8e-4e04-8a4b-2407efaca4f6
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=644:9
---

# Rating

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Rating UI Pattern to allow users rate, for example, products and services.

![Screenshot showing an example of the Rating UI Pattern in use](images/rating-example-ss.png "Rating Example Screenshot")

**How to use the Rating UI Pattern**

1. In Service Studio, in the Toolbox, search for `Rating`.

    The Rating widget is displayed.

    ![Screenshot of the Rating widget in the Service Studio toolbox](images/rating-widget-ss.png "Rating Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the **Rating** widget into the Main Content area of your application's screen.

    ![Screenshot illustrating how to drag the Rating widget onto the application screen](images/rating-dragwidget-ss.png "Dragging the Rating Widget")

    By default, the pattern is already prepared to work as a 5-Star rating pattern. However, you can change the icons to hearts, smiles, thumbs, or any other content.

1. On the **Properties** tab, from the **RatingValue** dropdown, enter the rating number you want displayed. In this example, we enter `3`.  
    
    ![Screenshot showing the RatingValue property being set to 3 in the properties tab](images/rating-value-ss.png "Setting the Rating Value Property")

1. You can customize the Rating's look and feel by setting any of the optional properties.

    ![Screenshot displaying the customization options for the Rating's look and feel in the properties tab](images/rating-properties-ss.png "Rating Properties Customization")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
|RatingValue (Decimal): Mandatory|Defines the rating number to display. |
|RatingScale (Integer): Optional|Defines the rating scale that determines the number of items to display. By default, the scale is 5.<br/>If set to 1, the scale behaves as a view only element, with IsEdit automatically set to False.<br/>The parameter maximum value is 100. If the value introduced is bigger, only 100 items are displayed. |
|IsEdit (Boolean): Optional| Set to True to allow users interact with the pattern. the default value is False.|
|Size (Size Identifier): Optional | Defines the size of the Rating pattern. There are 3 sizes available; Small, Medium, and Base. The default size is Base. |
|ExtendedClass (Text): Optional| Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

## Events

|Event| Description  | 
|---|---|
|OnSelect: Optional  | Event that returns the current rating value. | 

