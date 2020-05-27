---
tags: runtime-traditionalweb; 
summary: Card Background groups short pieces of information and highlights them on the screen while providing additional relevance by using a background image.
---

# Card Background

You can use the Card Background UI Pattern to group small pieces of information and highlight them on the screen using a background image. The information is grouped into a small block that is easily noticeable on-screen. 

![](<images/cardbackground-image-1.png>)


**How to use the Card Background UI Pattern**

1. In Service Studio, in the Toolbox, search for `Card Background`.

    The Card Background widget is displayed.

    ![](<images/cardbackground-image-3.png>)
    
1. From the Toolbox, drag the Card Background widget into the Main Content area of your application's screen.

    ![](<images/cardbackground-image-4.png>)

    By default, the Card Background widget contains a Content placeholder with some text and a Background Image placeholder with an image. 

1. Add your content to the placeholder. In this example we change the image. To do this, from the Widget Tree, select the Image, and on the **Properties** tab, from the **Image** drop-down, select the image you want to display. 

    ![](<images/cardbackground-image-5.png>)

1. On the **Properties** tab, you can change the look and feel of the Card Background widget, by setting the (optional) properties, for example, the background color that overlays the image, the content's position and a minimum height for the card.

    ![](<images/cardbackground-image-6.png>)

After following these steps and publishing the module, you can test the pattern in your app. 

## Properties

|**Property** | **Description** | 
|---|---|
| Color (Color Identifier): Optional  | Set the background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - No background color is applied. This is the default (Entities.Color.Transparent).</li><li>_Entities.Color.Red_ - Applies a red background color to the card.</li></ul></p> | 
| Position (PositionExtended Identifier): Optional| Sets the widget position. <p>Examples</p><ul><li>_Entities.PositionExtended.BottomRight_ - The widget displays on the bottom right of the screen. </li><li>_Entities.PositionExtended.Center_ - The widget displays in the center of the screen. </li></ul> |  
| Height (Integer): Optional | Set the height of the Card (in pixels). By default, the content is vertically aligned. <p>Examples</p><ul><li>_Blank_ - The Card height is 300 pixels. </li><li>_500_ - The Card height is 500 pixels. </li></ul>| 
| ExtendedClass (Text): Optional  |  Add custom style classes to the Card Background UI Pattern. You define your [custom style classes](../../../../../../develop/ui/look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ Adds the _myclass_ style to the Card Background UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Card Background UI styles being applied. </li></ul> |



