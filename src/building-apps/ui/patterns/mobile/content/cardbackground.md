---
tags: runtime-mobileandreactiveweb;  
summary: OutSystems 11 (O11) supports the Card Background UI Pattern for grouping and highlighting information in Mobile and Reactive Web Apps.
locale: en-us
guid: e34c8b4b-958b-498e-b8c8-459c60d5c98f
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=205:20
---

# Card Background

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Card Background UI Pattern to group small pieces of information and highlight them on the screen using a background image. The information is grouped into a small block that is easily noticeable on-screen. 

![Screenshot of a card background example in a mobile app or reactive web app](images/cardbackground-1-ss.png "Card Background Example")

**How to use the Card Background UI Pattern**

1. In Service Studio, in the Toolbox, search for `Card Background`.

    The Card Background widget is displayed.

    ![Service Studio interface showing the Card Background widget in the toolbox](images/cardbackground-2-ss.png "Card Background Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Card Background widget into the Main Content area of your application's screen.

    ![Dragging the Card Background widget into the Main Content area of an application screen](images/cardbackground-3-ss.png "Dragging Card Background Widget")

    By default, the Card Background widget contains Content and Background Image placeholders.

1. Add your content to the placeholder.

    In this example, we add text to the Content placeholder and an image to the Background Image placeholder. To do this, from the Widget Tree, select the Image, and on the **Properties** tab, from the **Image** drop-down, select the image you want to display.

    ![Adding text and an image to the Content and Background Image placeholders of the Card Background widget](images/cardbackground-4-ss.png "Adding Content to Card Background")

1. On the **Properties** tab, you can change the look and feel of the Card Background widget, by setting the (optional) properties, for example, the background color and a minimum height for the card.

    ![Properties tab in Service Studio for customizing the Card Background widget's appearance](images/cardbackground-5-ss.png "Card Background Properties")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Color (Color Identifier): Optional | Set the background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - No background color is applied. This is the default (Entities.Color.Transparent).</li><li>_Entities.Color.Red_ - Applies a red background color to the card.</li></ul></p>                                                                                                                                                                                                                                                               |
| MinHeight (Integer): Optional      | Sets the minimum height of the card (in pixels).  <p>Examples</p><ul><li>_500_ - The Card height is 500 pixels. </li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Height (Integer): Optional         | Set the height of the Card (in pixels). By default, the content is vertically aligned. <p>Examples</p><ul><li>_Blank_ - The Card height is 300 pixels. </li><li>_500_ - The Card height is 500 pixels. </li></ul>                                                                                                                                                                                                                                                                                                                                                                                                     |
| ExtendedClass (Text): Optional     | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
