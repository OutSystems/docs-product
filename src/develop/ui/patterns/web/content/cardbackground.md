---
tags: runtime-traditionalweb; 
summary: CardBackground groups short pieces of information and highlights them on the screen while providing additional relavance by using a background image.
---

# CardBackground

Similar to a Card but allows you to define a background image that blends in with the content.

Use a Card Background to group short pieces of information and highlight them on the screen while providing additional relavance by using a background image.

**How to use**

Add content to the placeholder and set the background image. Alternatively, in the parameters, you can define a background color that overlays the image, the content's position and a minimum height for the card.

1. Drag the CardBackground pattern into the preview.

1. Set the Input Parameters to extend the default values.

1. Publish and test.

    ![](<images/cardbackground-image-1.png>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Color  | Set the backgound color. | Color Identifier | False | Entities.Color.Transparent |
| Position  | Set the position around the widget element. | PositionExtended Identifier | False | none |
| Height  | Set the height of the Card, in pixels. Content will be vertically aligned by default. | Integer | False | 300 |
| ExtendedClass  |  Add custom style classes to this Block. | Text | False | none |

## Layout and Classes

![](<images/cardbackground-image-2.png>)

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .card-background-content | .bottom-center | Vertically aligns the content to Bottom and Horizontally align it to Center. |
| .card-background-content | .bottom-left |  Vertically aligns the content to Bottom and Horizontally align it to Left. |
| .card-background-content | .bottom-right |  Vertically aligns the content to Bottom and Horizontally align it to Right. |
| .card-background-content | .center |  Vertically aligns the content to Center and Horizontally align it to Center. |
| .card-background-content | .center-left |  Vertically aligns the content to Center and Horizontally align it to Left. |
| .card-background-contente | .center-right |  Vertically aligns the content to Center and Horizontally align it to Right. |
| .card-background-content | .top-center | Vertically aligns the content to Top and Horizontally align it to Center. |
| .card-background-content | .top-left |  Vertically aligns the content to Top and Horizontally align it to Left. |
| .card-background-content | .top-right |  Vertically aligns the content to Top and Horizontally align it to Right. |

## Advanced Use Case

### Add a new style to the Counter pattern

1. Drag the Counter pattern into the preview.

1. Set the Input Parameters to the following values:
    - Color: `Entities.Color.Neutral10`
    - Position: `Entities.PositionExtended.BottomCenter`
    - Height: `400`
    - ExtendedClass: `shadow-xl`

    ![](<images/cardbackground-image-3.png>)

1. Add a text widget into the Content placeholder and set the Style Classes property to `heading4 text-neutral-0`.

    ![](<images/cardbackground-image-4.png>)

1. Drag an image to the BackgroundImage placeholder.

    ![](<images/cardbackground-image-5.png>)

1. Publish and test.

    ![](<images/cardbackground-image-6.png>)

## Notes

The object-fit property is not supported in Internet Explorer.


