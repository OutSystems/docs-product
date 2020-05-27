---
tags: runtime-traditionalweb; 
summary: Card Sectioned groups short pieces of information in sections and highlights them on the screen.
---

# Card Sectioned

Groups information in a small block organized with different sections for title, image and content that can be easily noticeable in the screen.

Use the Card Sectioned pattern to group short pieces of information and highlight them on the screen.

![](<images/cardsection-image-3.png>)

**How to use the Card Sectioned UI Pattern**

1. In Service Studio, in the Toolbox, search for `Card Sectioned`.

    The Card Sectioned widget is displayed.

    ![](<images/cardsection-image-1.png>)
    
1. From the Toolbox, drag the Card Sectioned widget into the Main Content area of your application's screen.

    ![](<images/cardsection-image-2.png>)

    By default, the Card Sectioned widget contains an Image, Title, Content, and Footer placeholder.

1. Add your content to the placeholders. In this example we add an image, a title, some text, and a link. 

    ![](<images/cardsection-image-4.png>)
    
1. On the **Properties** tab, you can change the look and feel of the Card Sectioned widget, for example, the orientation, direction and padding properties.

    ![](<images/cardsection-image-5.png>)

After following these steps and publishing the module, you can test the pattern in your app. 


## Properties

| **Property** |  **Description** |  
|---|---|
| Orientation (Orientation Identifier): Optional | Sets the orientation of the card. <p>Examples</p><ul><li>_Blank_ - The content displays vertically. This is the default.</li><li>_Entities.Orientation.Horizontal_ - The content is displayed horizontally. </li> </ul>|  
| ImagePadding (Boolean): Optional  | If True, a padding of 24px is applied. This is the default. If False, no padding is applied.| 
| IsRight (Boolean): Optional  | If True, content is left aligned. If False, content is right aligned. This is the default. **Note**: This property is only applicable if the **Orientation** property is set to **Horizontal**.| 
| ExtendedClass (Text): Optional  |  Add custom style classes to the Card Sectioned UI Pattern. You define your [custom style classes](../../../../../../develop/ui/look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ Adds the _myclass_ style to the Card Sectioned UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Card Sectioned UI styles being applied. </li></ul> |
  
