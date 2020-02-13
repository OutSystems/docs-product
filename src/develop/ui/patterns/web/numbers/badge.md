---
tags: runtime-traditionalweb; 
summary: Badge display numerical information as notification.
---

# Badge

Display numerical information as notification.

Use the Badge to notify the user about numerical information such as new messages or tasks. 

**How to use**

Use the parameters to choose some options such as color, shape, size and light theme.

1. Drag Badge pattern into the preview.

1. Set the Input Parameters to extend the default values.

1. Publish and test.

    ![](<images/badge-image-1.png>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Number  | Number that will appear inside the badge. | Integer | False | 8 |
| Color  | Set the color. | Color Identifier | False | Entities.Color.Primary |
| Shape  | Set the shape. | Shape Identifier | False | Entities.Shape.Rounded |
| Size  | Set the size. | Size Identifier | False | none |
| IsLight  | Use the lightest color version for the background and the darker color version for the text. | Boolean | False | False |
| ExtendedClass  |  Add custom style classes to this Block. |  Text | False | none |

## Layout and Classes

![](<images/badge-image-2.png>)

## Advanced Use Case

### Use a transparent Badge Pattern with a border

1. Use Transparent in Color Value.

1. In the ExtendedClass Input Parameter, choose the desired text color.

    ![](<images/badge-image-3.png>)

1. Choose the border size of the Badge.

    ![](<images/badge-image-4.png>)
    
1. Publish and test.
    
    ![](<images/badge-image-5.png>)


## Notes

If the number on Badge pattern is greater then 99, it is displayed as 99+.

![](<images/badge-image-6.png>)


