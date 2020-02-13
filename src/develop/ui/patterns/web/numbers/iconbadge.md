---
tags: runtime-traditionalweb; 
summary: IconBadge displays numerical information as notification.
---

# IconBadge

Display numerical information as notification.

Use the Icon Badge to notify the user of numerical information. It is frequently used to notify users about new messages or tasks. 

**How to use**

Add an icon to the placeholder, then set the color and apply the light theme.

1. Drag IconBadge pattern into the preview.

1. Change the pattern values and icon.

1. Publish and test.

    ![](<images/iconbadge-image-1.png>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Number  |  Number that will appear inside the badge over the icon. | Integer | False | 0 |
| Color  |  Color of the badge over the icon. | Color Identifier | False | Entities.Color.Primary |
| IsLight  |  Use the lightest color version for the background and the darker color version for the text. | Boolean | False | False |
| ExtendedClass  |  Add custom style classes to this Block. | Text | False | none |

## Layout and Classes

![](<images/iconbadge-image-2.png?width=650>)

