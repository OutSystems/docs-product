---
tags: runtime-traditionalweb; 
summary: Tag styles small texts in a colored tag format.
---

# Tag

Style small texts in a colored tag format.

Use Tags to display status, labels or categories thus providing great user experience. 

**How to use**

Drag the pattern to the screen and add the text in the placeholder.

1. Drag the Tag pattern into the preview.

1. Drag your text to this placeholder.

    ![](<images/tag-image-1.png?width=500>)

1. Set the Input Parameters to extend the default values.

    ![](<images/tag-image-2.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Color | Set the backgound color. | Color Identifier | _False_ | Entities.Color.Primary |
| Shape | Set the shape. | Shape Identifier | _False_ | Entities.Shape.Rounded |
| Size | Set the size. | Size Identifier | _False_ | None |
| IsLight | Use the lightest color version for the background and the darker color  version for the text. | Boolean | _False_ | False |
| ExtendedClass  |  Add custom style classes to this Block. |  Text | _False_ | None |

## Layout and Classes

![](<images/tag-image-3.png>)

## Advanced Use Case

### Use only border in Tag Pattern

1. Set the Color parameter to Transparent.
1. In the ExtendedClass property, set the text color.

    ![](<images/tag-image-4.png>)

1. Set the border size.

    ![](<images/tag-image-5.png>)

1. Publish and test.

    ![](<images/tag-image-6.png>)
