---
tags: runtime-mobileandreactiveweb;  
summary: The Horizontal Scroll displays a subset of a category, a finite amount of sections, slides, or content that's larger than the screen.
---

# Horizontal Scroll

You can use the Horizontal Scroll UI Pattern to display a subset of a category, a finite amount of sections, slides, or content that's larger than the screen such as a map.

![](<images/horizontalscroll-1-ss.png>)

**How to use the Horizontal Scroll UI Pattern**

1. In Service Studio, in the Toolbox, search for `Horizontal Scroll`.

    The Horizontal Scroll widget is displayed.

    ![](<images/horizontalscroll-2-ss.png>)

1. From the Toolbox, drag the Horizontal Scroll widget into the Main Content area of your application's screen.

    ![](<images/horizontalscroll-3-ss.png>)

    By default, the Horizontal Scroll widget contains a Content placeholder.

1. Add the relevant content to the Content placeholder. 

    In this example, we add some images by dragging the Image widget into the Content placeholder, and on the **Properties** tab, from the **Image** dropdown, import the relevant images.

    ![](<images/horizontalscroll-5-ss.png?width=800>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property |  Description |
|---|---|
| ExtendedClass (Text): Optional  |   Add custom style classes to the Horizontal Scroll UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the myclass style to the Horizontal Scroll UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Horizontal Scroll UI styles being applied.</li></ul></p> |
