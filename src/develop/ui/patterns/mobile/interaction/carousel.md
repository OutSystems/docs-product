---
tags: runtime-mobileandreactiveweb;  
summary: Displays multiple items in a horizontal slide.
---

# Carousel

You can use the Carousel UI Pattern to display multiple items in a horizontal slide.  The Carousel Pattern optimizes screen space by displaying only a few images from a larger collection which you can view using the navigation controls. 

![Example Carousel](images/carousel-example.png)

**Note:** The Carousel Pattern is based on the Splide.js library (v3). For more information about the Carousel’s behaviors and extensibility methods, see [Splide.js](https://splidejs.com/).  

## How to use the Carousel UI Pattern

1. In Service Studio, in the Toolbox, search for `Carousel`.
  
     The Carousel widget is displayed.

    ![Carousel widget](images/carousel-widget-ss.png)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUI module**, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Carousel widget into the Main Content area of your application's screen. 

    ![Drag widget to the screen](images/carousel-dragwidget-ss.png)

    By default, the Carousel pattern contains a **CarouselItems** placeholder with a **List** widget and **Image** widget. If you want a Carousel with static images, you can remove the **List** widget and add your images inside the **CarouselItems** placeholder.

1. Add your content to the **Carousel Items** placeholder. 

    In this example, the List is deleted and 3 Image widgets are added.  

    ![Add image widgets](images/carousel-addimages-ss.png) 

1. Select the **Image** widget, and on the **Properties** tab, from the **Image** drop-down, select or import the image you want in the Carousel. 

    **Note:** In this example, the image Type is set to Local image. You can also add External and Binary Data images. In this example, the image property Type is set to **Local** image. You can also add [External and Binary Data](../../../image/display-image.md) images.   

    ![](images/carousel-imagetype-ss.png)   

1. Repeat step 4 for each of the images in the Carousel. 

1. You can configure the Carousel by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties, for example, **Navigation** or **ItemsPerSlide**.For more configurations, expand the **OptionalConfigs** property.

    ![Set properties](images/carousel-properties-ss.png)  

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

|**Property**|**Description**|
|---|---|
|Navigation(Boolean): Optional | Enable or disable arrow buttons to navigate left and right. <p>Examples<ul><li>_Blank_ - No navigation arrows are displayed.</li><li>_True_ - Navigation arrows are displayed.</li><li>_False_ - No navigation arrows are displayed. This is the default value.</li></ul></p> |
|Dots(Boolean): Optional | Enable or disable navigational dots that represent items on the Carousel.<p>Examples<ul><li>_Blank_ - Navigational dots are displayed. This is the default value.</li><li>_True_ - Navigational dots are displayed.</li><li>_False_ - No navigational dots are displayed.</li></ul></p> |
|Margin(Integer): Optional  |  Set the distance between each Carousel item. <p>Examples<ul><li>_Blank_ - No distance between each Carousel item. this is the default</li><li>_2_ - A distance of 2 pixels between each Carousel item.</li></ul></p>  | 
|Padding(Integer): Optional |  Set the distance between the screen edges and the visible items on the screen. <p>Examples<ul><li>_Blank_ - No distance between the screen edges and the on screen item. This is the default value.</li><li>_5_ - A distance of 5 pixels between the screen edges and the on screen item.</li></ul></p> |
|AutoPlay(Autoplay Identifier): Optional | Enable or disable the autoplay functionality which displays the items in the Carousel automatically. You can also set the autoplay velocity. The predefined autoplay values are: <p><ul><li>Disabled</li><li>Fast (2 seconds)</li><li>Normal (5 seconds)</li><li>Slow (8 seconds)</li></ul></p><p>Examples<ul><li>_Blank_ - Autoplay is disabled.</li><li>_Entities.Autoplay.Fast_ - Items are displayed with a time wait of 2 seconds between each item.</li><li>_Entities.Autoplay.Slow_ - Items are displayed with a time wait of 8 seconds between each item.</li></ul></p> |  
|Scale(Boolean): Optional | Use this setting for the active Carousel items. If set to True, when navigating through the images, the size of the active item begins to decrease and the size of the next element that becomes the active item increases. The default value is False.  | 
|Loop(Boolean): Optional  | If set to True, once the last item in the Carousel is reached, it loops around to the first item and begins displaying the all of the items again. If set to False, the slide of the Carousel items ends when the last item is reached. This is the default value.| 
|Center(Boolean): Optional  | If set to True, the active item in the Carousel is displayed centered horizontally. If set to False, the active item is not centered horizontally. This is the default value.  |
|InitialPosition(Integer): Optional  |  Set which element you want to show first in the Carousel. <p>Examples <ul><li>_Blank_ - The first element in the Carousel is displayed. This is the default value.</li><li>_3_ - The 4th element in the Carousel is displayed. </li></ul></p>  | 
|ItemsPhone(Integer): Optional | Number of Carousel items visible at the same time on a phone.<p>Examples<ul><li>_Blank_ - 1 item is displayed. This is the default value.</li><li>_4_ - 4 items are displayed.</li></ul></p> |  
|ItemsTablet(Integer): Optional  | Number of Carousel items visible at the same time on a tablet.<p>Examples<ul><li>_Blank_ - 1 item is displayed. This is the default value.</li><li>_4_ - 4 items are displayed.</li></ul></p>| 
|ItemsDesktop(Integer):Optional  |  Number of Carousel items visible at the same time on a desktop.<p>Examples<ul><li>_Blank_ - 1 item is displayed. This is the default value.</li><li>_4_ - 4 items are displayed.</li></ul></p> | 
  
## Compatibility with other patterns

Avoid using the Carousel inside patterns with swipe events, such as the Tabs and Stacked Cards Patterns.
