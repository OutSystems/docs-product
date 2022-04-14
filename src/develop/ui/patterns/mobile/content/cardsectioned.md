---
tags: runtime-mobileandreactiveweb;  
summary: Card Sectioned groups short pieces of information in sections and highlights them on the screen.
locale: en-us
guid: db5e39c5-f5ee-4e18-9754-14fef2f95533
---

# Card Sectioned

<div class="info" markdown="1">

Applies only to Mobile Apps and Reactive Web Apps

</div>

Groups information in a small block organized with different sections for title, image and content that can be easily noticeable in the screen.

Use the Card Sectioned pattern to group short pieces of information and highlight them on the screen.

![](<images/cardsection-3.png>)

**How to use the Card Sectioned UI Pattern**

1. In Service Studio, in the Toolbox, search for `Card Sectioned`.

    The Card Sectioned widget is displayed.

    ![](<images/cardsection-1-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Card Sectioned widget into the Main Content area of your application's screen.

    ![](<images/cardsection-2-ss.png>)

    By default, the Card Sectioned widget contains an Image, Title, Content, and Footer placeholder.

1. Add your content to the placeholders.

    In this example we add an image, a title, some text, and a link.

    ![](<images/cardsection-4-ss.png>)

1. On the **Properties** tab, you can change the look and feel of the Card Sectioned widget, for example, the orientation, and padding properties.

    ![](<images/cardsection-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
|UsePadding (Boolean): Optional  | If True, content has padding. This is the default. If False, the content has no padding. |
|IsVertical (Boolean): Optional  | If True, the Card Sectioned pattern displays vertically. This is the default. If false, the pattern displays horizontally. |
|ImagePadding (Boolean): Optional  | If True, a padding of 24px is applied to the image. This is the default. If False, no padding is applied to teh image. |
|ExtendedClass (Text): Optional  |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
