---
tags: runtime-mobileandreactiveweb;  
summary: Card groups small pieces of information and highlights them on the screen.
---

# Card

You can use the Cards UI Pattern to group small pieces of information and highlight them on the screen. The information is grouped into a small block that is easily noticeable on-screen.

![](<images/card-1.png>)

**How to use the Card UI Pattern**

1. In Service Studio, in the Toolbox, search for `Card`.

    The Card widget is displayed.

    ![](<images/card-2-ss.png>)

1. From the Toolbox, drag the Card widget into the Main Content area of your application's screen.

    ![](<images/card-3-ss.png>)

1. Add your content to the placeholder. In this example we add some text.

    ![](<images/card-4-ss.png>)

1. On the **Properties** tab, you can customize the Card's look and feel by setting any of the (optional) properties.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| UsePadding (Boolean): Optional  |  If set to True, padding is applied to the content area. This is the default value. If set to False, the content area has no padding. |
| ExtendedClass (Text): Optional  |  Add custom style classes to the Card UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Card UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Card UI styles being applied. </li></ul> |
