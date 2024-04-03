---
tags: runtime-traditionalweb; 
summary: Card Sectioned groups short pieces of information in sections and highlights them on the screen.
locale: en-us
guid: 1ba59808-a9ca-45c3-8f9c-3b68edccaef4
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=222%3A65&mode=design&t=ANpsYvOCthr9AWot-1
---

# Card Sectioned

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

Groups information in a small block organized with different sections for title, image and content that can be easily noticeable in the screen.

Use the Card Sectioned pattern to group short pieces of information and highlight them on the screen.

![Example of a Card Sectioned pattern in a Traditional Web App](images/cardsection-3.png "Card Sectioned Example")

**How to use the Card Sectioned UI Pattern**

1. In Service Studio, in the Toolbox, search for `Card Sectioned`.

    The Card Sectioned widget is displayed.

    ![Screenshot showing the Card Sectioned widget in OutSystems Service Studio](images/cardsection-1-ss.png "Card Sectioned Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Card Sectioned widget into the Main Content area of your application's screen.

    ![Dragging the Card Sectioned widget into the Main Content area of an application screen](images/cardsection-2-ss.png "Dragging Card Sectioned Widget")

    By default, the Card Sectioned widget contains an Image, Title, Content, and Footer placeholder.

1. Add your content to the placeholders. In this example we add an image, a title, some text, and a link.

    ![Adding an image, title, text, and link to the Card Sectioned widget placeholders](images/cardsection-4-ss.png "Adding Content to Card Sectioned")

1. On the **Properties** tab, you can change the look and feel of the Card Sectioned widget, for example, the orientation and padding properties.

    ![Properties tab for the Card Sectioned widget showing options for orientation and padding](images/cardsection-5-ss.png "Card Sectioned Properties")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** | **Description** |
|---|---|
| Orientation (Orientation Identifier): Optional | Sets the orientation of the card. <p>Examples</p><ul><li>Blank - The content displays vertically. This is the default.</li><li>Entities.Orientation.Horizontal - The content is displayed horizontally.</li></ul> |
| ImagePadding (Boolean): Optional | If True, a padding of 24px is applied to the image. This is the default. If False, no padding is applied to the image. |
| IsRight (Boolean): Optional | If True, content is left aligned. If False, content is right aligned. This is the default. **Note**: This property is only applicable if the **Orientation** property is set to **Horizontal**. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2"_ - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
