---
tags: runtime-traditionalweb; 
summary: Card groups small pieces of information and highlights them on the screen.
---

# Card

Groups information in a small block that is easily noticeable in the screen.

Use Cards to group small pieces of information and highlight them on the screen. 

**How to use**

Drag the pattern to the screen and edit the content to match your requirements.

1. Drag the Card pattern into the preview.

    ![](<images/card-image-1.png>)

1. Set the content you need in the placeholder.
1. Publish and test.


## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| ExtendedClass  |  Add custom style classes to this Block. | Text | _False_ | none |
  
## Layout and Classes

![](<images/card-image-2.png>)

## Advanced Use Case

### Change background-color

1. Write the following classes in the ExtendedClass property of the card.
    `background-yourcolor text-neutral-0 border-size-none `

    ![](<images/card-image-3.png>)
    
    The class `text-neutral-0` is to set the text-color to white, in contrast with the new background. The `border-size-none` class is to remove the border.
    
1. Publish and test.

Before:

![](<images/card-image-4.png>)

After:

![](<images/card-image-5.png>)

