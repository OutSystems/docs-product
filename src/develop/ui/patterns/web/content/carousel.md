---
tags: runtime-traditionalweb; 
summary: Carousel shows a subset of items in a cyclic view.
---

# Carousel

<div class="info" markdown="1">

We’ve been working on this article. Please let us know how useful this new version is by voting.

</div>

You can use the Carousel UI Pattern to display multiple items in a horizontal slide. This pattern is ideal for creating horizontal slides in smaller screens. You can also use this pattern for dynamic content, by placing a List directly inside the placeholder.

**How to use the Carousel UI Pattern**

1. In Service Studio, in the Toolbox, search for `Carousel`.
  
     The Carousel widget is displayed.

    ![](images/carousel-3-ss.png)

1. To From the Toolbox, drag the Carousel widget into the Main Content area of your application's screen. 

   ![](images/carousel-9-ss.png)

1. Place the content you want to appear in the Carousel into the Items placeholder. (In this example we use images.) 

1. From the Toolbox, drag the [Image widget](<../../../../../ref/lang/auto/Class.Image Widget.final.md>) into the Light Box Image widget. This is a thumbnail image. 

    The **Select Image** pop-up is displayed.

1. Select or import the image you want to display. In this example, we use the sample OutSystems UI images.

    ![](<images/carousel-10-ss.png>)

    Note: In this example, the image property Type is set to **Static**. You can also choose [External URL or Database](../../../../../develop/ui/image/display-image.md).

    To use a Carousel with items from a database, drag a [ListRecords widget](<../../../../../ref/lang/auto/Class.List Records Widget.final.md>) into Items placeholder and create your custom content.

    ![](<images/carousel-2-ss.png>)

1. Repeat steps 4 and 5 for each of the Carousel items.

1. From the Element tree, select the Carousel widget, and on the **Properties** tab, set the relevant (optional) properties, for example, navigation arrows and the number of items to display on different devices.

    ![](images/carousel-11-ss.png)  

1. After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
|Margin(Integer): Optional  |  Set the distance between each Carousel item. Default value is 0.<p>Examples<ul><li>_Blank_ - A distance of 16 pixels between each Carousel item.</li><li>_32_ - A distance of 32 pixels between each Carousel item.</li></ul></p>  |
|Padding(Integer): Optional |  Set the distance between the screen edges and the visible items on the screen. <p>Examples<ul><li>_Blank_ - No distance between the screen edges and the on screen item. This is the default value.</li><li>_5_ - A distance of 5 pixels between the screen edges and the on screen item.</li></ul></p> |
| Pagination(Boolean): Optional  | Enable or disable navigational dots that represent items on the Carousel.<p>Examples<ul><li>_Blank_ - Navigational dots are displayed. This is the default value.</li><li>_True_ - Navigational dots are displayed.</li><li>_False_ - No navigational dots are displayed.</li></ul></p> |
| Autoplay(Boolean): Optional  | If set to True, the items in the Carousel are displayed automatically (with a 5 second time delay between each item). If set to False, the autoplay functionality is disabled. This is the default value.| 
| Rewind(Boolean): Optional  | If True, a rewind effect is applied when the Carousel reaches the end and the Loop property is enabled. The default behavior is to show the first item without rewinding through the remaining. | 
| Loop(Boolean): Optional  | If set to True, once the last item in the Carousel is reached, it loops around to the first item and begins displaying the all of the items again. If set to False, the slide of the Carousel items ends when the last item is reached. This is the default value.|
| InitialPosition(Integer): Optional  |  Set which element you want to show first in the Carousel. <p>Examples <ul><li>_Blank_ - The first element in the Carousel is displayed. This is the default value.</li><li>_3_ - The 4th element in the Carousel is displayed. </li></ul></p>|
|ItemsDesktop(Integer): Optional  |  Number of Carousel items visible at the same time on a desktop.<p>Examples<ul><li>_Blank_ - 1 item is displayed. This is the default value.</li><li>_4_ - 4 items are displayed.</li></ul></p> |  
|ItemsTablet(Integer): Optional  | Number of Carousel items visible at the same time on a tablet.<p>Examples<ul><li>_Blank_ - 1 item is displayed. This is the default value.</li><li>_4_ - 4 items are displayed.</li></ul></p>| 
|ItemsPhone(Integer): Optional  | Number of Carousel items visible at the same time on a phone.<p>Examples<ul><li>_Blank_ - 1 item is displayed. This is the default value.</li><li>_4_ - 4 items are displayed.</li></ul></p> |
| ExtendedClass (Text): Optional |  Add custom style classes to the Carousel UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Carousel UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Carousel UI styles being applied.</li></ul></p> |
| AdvancedFormat(Text):Optional  |  Enables you to use more options than what is provided in the properties. For more information, visit: <https://github.com/ganlanyuan/tiny-slider>. <p>Example `{ axis: 'vertical' }`</p> |
