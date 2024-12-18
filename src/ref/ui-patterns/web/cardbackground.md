---
tags: ui design, css, ui patterns, web development, style customization
summary: Explore CSS class alignment options for the Card Background UI Pattern in Traditional Web Apps using OutSystems 11 (O11).
locale: en-us
guid: 1c3ead1f-e810-47d0-993a-743656d4d4f1
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:410
audience:
  - frontend developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Card Background Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout and classes for the Card Background UI Pattern in Traditional Web Apps](images/cardbackground-6-diag.png "Card Background Layout Diagram")

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .card-background-content | .bottom-center | Vertically aligns the content to Bottom and Horizontally align it to Center. |
| .card-background-content | .bottom-left |  Vertically aligns the content to Bottom and Horizontally align it to Left. |
| .card-background-content | .bottom-right |  Vertically aligns the content to Bottom and Horizontally align it to Right. |
| .card-background-content | .center |  Vertically aligns the content to Center and Horizontally align it to Center. |
| .card-background-content | .center-left |  Vertically aligns the content to Center and Horizontally align it to Left. |
| .card-background-content | .center-right |  Vertically aligns the content to Center and Horizontally align it to Right. |
| .card-background-content | .top-center | Vertically aligns the content to Top and Horizontally align it to Center. |
| .card-background-content | .top-left |  Vertically aligns the content to Top and Horizontally align it to Left. |
| .card-background-content | .top-right |  Vertically aligns the content to Top and Horizontally align it to Right. |

## Advanced use case

### Add a new style to the Counter pattern

1. Drag the Counter pattern into the preview.

1. Set the Input Parameters to the following values:
    - Color: `Entities.Color.Neutral10`
    - Position: `Entities.PositionExtended.BottomCenter`
    - Height: `400`
    - ExtendedClass: `shadow-xl`

    ![Screenshot of the Counter pattern configuration with specific input parameters for color, position, height, and extended class](images/cardbackground-7-ss.png "Counter Pattern Style Configuration")

1. Add a text widget into the Content placeholder and set the Style Classes property to `heading4 text-neutral-0`.

    ![Screenshot showing the addition of a text widget with heading4 and text-neutral-0 style classes in the Content placeholder](images/cardbackground-8-ss.png "Text Widget Style Setting")

1. Drag an image to the BackgroundImage placeholder.

    ![Screenshot depicting the process of dragging an image into the BackgroundImage placeholder of the Card Background pattern](images/cardbackground-9-ss.png "Image Placeholder in Card Background")

1. Publish and test.

    ![Screenshot of the published Card Background with a new style applied to the Counter pattern](images/cardbackground-10-ss.png "Published Card Background")

## Notes

The object-fit property is not supported in Internet Explorer.


