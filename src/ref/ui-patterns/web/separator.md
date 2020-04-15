---
tags:
summary: 
---

# Separator UI Pattern Reference

## Layout and classes

![](<images/separator-image-2.png>)

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .separator | .separator-horizontal |  When IsVertical parameter is False  |
| .separator | .separator-vertical |  When IsVertical parameter is True  |

## Advanced use case

### Use the vertical separator

1. Drag a container into the preview.

1. Create a class called "separator-height".

    ```css
    .separator-height {
        height: 100px;
    }
    ```
1. Drag the Separator pattern into the container.

1. Set the IsVertical parameter to True.

1. Publish and test.

    ![](<images/separator-image-3.png>)

 ## See also

* OutSystems UI Pattern Documentation: [Separator](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Patterns/Using_Web_Patterns/Utilities/Separator)

