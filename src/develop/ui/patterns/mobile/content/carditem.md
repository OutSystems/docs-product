---
tags: runtime-mobileandreactiveweb;  
summary: Card Item lists items with multiple content types, such as an image or icon, a title and description, and an action to the right.
---

# Card Item

You can use the Card Item UI Pattern to list items with multiple content types, such as image or icon (to the left), a title and description, and an action to the right.

![](<images/carditem-1.png>)

**How to use the Card UI Pattern**

1. In Service Studio, in the Toolbox, search for `Card Item`.

    The Card Item widget is displayed.

    ![](<images/carditem-2-ss.png>)

1. From the Toolbox, drag the Card widget into the Main Content area of your application's screen.

    In this example, we drag the widget into the Card widget that's already in the Main Content area of the screen. You can add as many Card Item widgets as required (we add 4). 

    ![](<images/carditem-3-ss.png>)

    By default, the Card Item widget contains a Left, Title, Content, and Right placeholder. 

1. Add your content to each of the placeholders. 

    In this example, we add an icon to the Left placeholder, text to the Title and Content placeholders, and a phone icon to the Right placeholder. 

    ![](<images/carditem-4-ss.png>)

1. On the **Properties** tab, you can customize the Card Item's look and feel by setting any of the (optional) properties.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| ExtendedClass (Text): Optional  |  Add custom style classes to the Card Item UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Card Item UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Card Item UI styles being applied. </li></ul> |
