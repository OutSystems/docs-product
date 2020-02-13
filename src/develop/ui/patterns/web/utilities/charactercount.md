---
tags: runtime-traditionalweb; 
summary: CharacterCount displays the number of characters left to be entered in a target input field.
---

# CharacterCount

Displays the number of characters left to be entered in a target input field.

Use CharacterCount to inform users about the maximum number of characters they can enter in a given text area. Also show how many more characters can be entered.

**How to use**

1. Drag an input into the preview.

1. Give a name to the input (for instance, CharacterCount).

1. Set a variable type **text** to the input.

1. Drag the CharacterCount pattern into the preview.

1. Set the InputWidgetId to the input name. 

1. Set the Limit property (for instance, 50).

    ![](<images/charactercount-image-1.png>)

1. Publish and test.

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| InputWidgetId  | Input Element Name that will trigger the count. | Text | True | none |
| Limit  | The character count limit. This value should be the same as the Max Length property in the input. | Integer | True | none |
| IsDescending  | When set to false, the count will go from 0 to the limit that has been chosen on the Limit parameter. | Boolean | True | True

## Layout and Classes

![](<images/charactercount-image-2.png>)
