---
summary: Flip Content prioritizes information display, keeping the interface uncluttered.
tags:
---

# Flip Content

 You can use the Flip Content UI Pattern to display information that when, for example, is clicked, flips and displays different information.

![](<images/flipcontent-1.gif?width=500>)

**How to use the Flip content UI Pattern**

1. In Service Studio, in the Toolbox, search for `Flip Content`.

    The Flip Content widget is displayed.

    ![](<images/flipcontent-2-ss.png>)

1. From the Toolbox, drag the Flip Content widget into the Main Content area of your application's screen.

    ![](<images/flipcontent-3-ss.png>)

    By default, the Flip Content widget contains CardFront and CardBack placeholders.

1. Add the required content for the front and back placeholders inside the Flip Content widget.

    In this example, we add images by dragging the Image widget into the CardFront and CardBack placeholders and from the **Image** dropdown, selecting an image from the sample OutSystems UI images.

    ![](<images/flipcontent-4-ss.png?width=800>)

1. On the **Properties** tab, you can customize the Flip Content's look and feel by setting any of the (optional) properties.

    ![](<images/flipcontent-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| IsFlipped (Boolean): Optional | If True, the CardFront content is displayed first before flipping. If False, the CardBack content is displayed first before flipping. This is the default. |  
| FlipSelf (Boolean): Optional | If True, the content flips event is triggered with on click. This is the default. If False, you can define the action that triggers the flip. |
| ExtendedClass (Text): Optional | Add custom style classes to the Flip Content UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the myclass style to the Flip Content UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Flip Content UI styles being applied.</li></ul></p> |
