---
tags: runtime-mobileandreactiveweb;
summary: Allows users to rate a particular item.
---

# Rating

You can use the Rating UI Pattern to allow users to rate a particular item. 

![](<images/rating-4-ss.png>)

**How to use the Rating UI Pattern**

1. In Service Studio, in the Toolbox, search for `Rating`.

    The Rating widget is displayed.

    ![](<images/rating-1-ss.png>)

1. From the Toolbox, drag the Rating widget into the Main Content area of your application's screen.

    ![](<images/rating-2-ss.png>)

    By default, the pattern is already prepared to work as a 5-Star rating pattern. However, you can change the icons to hearts, smiles, thumbs, or any other content.

1. On the **Properties** tab, from the **RatingValue** dropdown, enter the rating number you want displayed. In this example, we enter `7`.  
    
    ![](<images/rating-5-ss.png>)

1. Additionally, on the **Properties** tab, you can customize the Rating's look and feel by setting any of the optional properties.

    ![](<images/rating-3-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| RatingValue (Decimal): Mandatory | Rating number to display. |
| RatingScale (Integer): Optional | The number of items to display. The default is 5 which means the rating is from 0 to 5. If set to 1, the item behaves as a view only element and the **IsEdit** property is automatically set to False. |
| IsEdit (Boolean): Optional | If True, the user can interact with the pattern. If False, the user can't interact with the pattern. This is the default. |
| Size (Size Identifier): Optional | The size of the rating pattern. There are 3 sizes available; small, medium, and base. Base is the default size.  |
| ExtendedClass (Text): Optional | Add custom style classes to the Rating UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Rating UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Rating UI styles being applied.</li></ul></p> |
