---
tags: runtime-mobileandreactiveweb;  
summary: The Mouse Events UI Pattern Enable click events on a specific widget or pattern.
---

# Mouse Events

You can use the Mouse Events UI Pattern when the user needs to select elements on the interface with high precision.

![](images/mouseevents-1-ss.png)

## How to use the Mouse Events UI Pattern

1. In Service Studio, in the Toolbox, search for `Mouse Events`.

    The Mouse Events widget is displayed.

    ![](<images/mouseevents-2-ss.png>)

1. From the Toolbox, drag the Mouse Events widget into the Main Content area of your application's screen.

    ![](<images/mouseevents-3-ss.png>)

1. On the Align Center **Properties** tab, you can set the content's orientation (either vertical or horizontal).

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| IsHorizontal (Boolean): Optional | If True, content is displayed horizontally. This is the default. If False, the content is displayed vertically. |
| ExtendedClass (Text): Optional  | <p>Add custom style classes to the Align Center UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Align Center UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Align Center UI styles being applied.</li></ul></p> |
