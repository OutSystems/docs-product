---
tags: runtime-traditionalweb; 
summary: Gallery enables the users to sequentially browse the content when there are many cards grouped into one or more collections.
---

# Gallery

Display groups of content as scannable collections.

Use the Gallery to enable the users to sequentially browse information, with a notion of beginning and end. It's helpful when there is a large number of cards you need to group into one or more scannable collections. 

**How to use**

Use static data or a List widget inside this block to display items in a gallery pattern.

1. Drag a list or static content.
    
    ![](<images/gallery-image-1.png>)

1. Set the number of items in Input Parameters.
    
    ![](<images/gallery-image-2.png>)

## Input parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| ItemsDesktop |  Number of Items per line on Desktop. | Integer | False | 5 |
| ItemsTablet |  Number of Items per line on Tablet. | Integer | False | 3 |
| ItemsPhone |  Number of Items per line on Phone. | Integer | False | 1 |
| ExtendedClass  |  Adds custom style classes to the Tabs Block. |  Text | False | none |

## Layout and classes

![](<images/gallery-image-3.png>)

## Notes

Line Separator from ListRecords should be None.

![](<images/gallery-image-4.png>)

