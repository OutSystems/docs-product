---
tags: runtime-traditionalweb; 
summary: Card Background groups short pieces of information and highlights them on the screen while providing additional relevance by using a background image.
---

# Card Background

You can use the Card Background UI Pattern to group small pieces of information and highlight them on the screen using a background image. The information is grouped into a small block that is easily noticeable on-screen. 

![](<images/cardbackground-1-ss.png>)

**How to use the Card Background UI Pattern**

1. In Service Studio, in the Toolbox, search for `Card Background`.

    The Card Background widget is displayed.

    ![](<images/cardbackground-2-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.
    
    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Card Background widget into the Main Content area of your application's screen.

    ![](<images/cardbackground-3-ss.png>)

    By default, the Card Background widget contains a Content placeholder with some text and a Background Image placeholder with an image.

1. Add your content to the placeholder. In this example we change the image. To do this, from the Widget Tree, select the Image, and on the **Properties** tab, from the **Image** drop-down, select the image you want to display.

    ![](<images/cardbackground-4-ss.png>)

1. On the **Properties** tab, you can change the look and feel of the Card Background widget, by setting the (optional) properties, for example, the background color that overlays the image, the content's position and a minimum height for the card.

    ![](<images/cardbackground-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

|**Property** | **Description** |
|---|---|
| Color (Color Identifier): Optional  | Set the background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - No background color is applied. This is the default (Entities.Color.Transparent).</li><li>_Entities.Color.Red_ - Applies a red background color to the card.</li></ul></p> |
| Position (PositionExtended Identifier): Optional| Sets the widget position. <p>Examples</p><ul><li>_Entities.PositionExtended.BottomRight_ - The widget displays on the bottom right of the screen. </li><li>_Entities.PositionExtended.Center_ - The widget displays in the center of the screen. </li></ul> |  
| Height (Integer): Optional | Set the height of the Card (in pixels). By default, the content is vertically aligned. <p>Examples</p><ul><li>_Blank_ - The Card height is 300 pixels. </li><li>_500_ - The Card height is 500 pixels. </li></ul>|
| ExtendedClass (Text): Optional  |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
