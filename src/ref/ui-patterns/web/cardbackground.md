---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Card Background UI Pattern.
locale: en-us
guid: 1c3ead1f-e810-47d0-993a-743656d4d4f1
app_type: traditional web apps
---

# Card Background Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/cardbackground-6-diag.png>)

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

    ![](<images/cardbackground-7-ss.png>)

1. Add a text widget into the Content placeholder and set the Style Classes property to `heading4 text-neutral-0`.

    ![](<images/cardbackground-8-ss.png>)

1. Drag an image to the BackgroundImage placeholder.

    ![](<images/cardbackground-9-ss.png>)

1. Publish and test.

    ![](<images/cardbackground-10-ss.png>)

## Notes

The object-fit property is not supported in Internet Explorer.


