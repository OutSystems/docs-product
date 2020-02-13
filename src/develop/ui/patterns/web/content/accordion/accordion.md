---
tags: runtime-traditionalweb; 
summary: Accordion expands vertically-stacked content by clicking on the header.
---

# Accordion

Expand content that is vertically stacked by clicking on the header.

Use an Accordion when you need to organize information by displaying part of the content first and then expanding it to see more.

**How to use**

Add the Accordion block to your screen. Then add Accordion Items inside the block to create content.

1. Drag the Accordion into the preview.
1. Drag as many Accordion Items as you need.
1. Set the content you need in the placeholders. 

    ![](<images/accordion-image-1.png>)

1. Publish and test.

    ![](<images/accordion-image-2.png>)

## Demo

<iframe src="https://drive.google.com/file/d/1_uTh7xhqZ2vqwHE2Hsd9mp6NUsF7S829/preview" width="750" height="500"></iframe>


## Input Parameters

### Accordion
| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| MultipleItems  |  Allows multiple Accordion Items to be opened having the effect of Section Expandables. |  Boolean | False | False |
| ExtendedClass  |  Add custom style classes to this block. |  Text | False | none |

### Accordion Item
| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| IsOpen  |  If true, when rendering the Accordion Item is open. |  Boolean | False | False |
| IsDisable  |  Doesn't allow the Accordion Item to be clickable. |  Boolean | False | False |
| ExtendedClass  |  Add custom style classes to this block. |  Text | False | none |

## Layout and Classes

![](<images/accordion-image-3.png>)

## CSS Selectors
| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .accordion-item | .accordion-item.is--open |  When AccordionItem is Open  |
| .accordion-item | accordion-item-content.is--expanded |  When AccordionItem is Open  |
| .accordion-item | .accordion-item.is--closed |  When AccordionItem is Closed  |
| .accordion-item | accordion-item-content.is--collapsed |  When AccordionItem is Closed  |
| .accordion-item | .accordion-item.is--disabled |  When IsDisabled parameter is True  |

## Advanced Use Case

### Use Accordion with ListRecords

1. Drag the Accordion Pattern into preview.
1. In the Content placeholder, drag a ListRecords widget.
1. In the ListRecords widget, drag an AccordionItem Pattern.
1. Inside the AccordionItem Pattern, use expressions to display the database content you need.
1. Publish and test.

    ![](<images/accordion-image-4.png>)

### Change arrow position to left

It is possible to change the arrow position on AccordionItems by using custom CSS. To do this in your application, you need to copy the CSS and put it in your theme.

```css
.accordion-item .accordion-item-header {
    flex-direction: row-reverse;
}

.accordion-item .accordion-item-title {
    padding-left: var(--space-base);
}
```
![](<images/accordion-image-5.png>)

### Add margin between each Accordion Item

You need to use custom CSS to add a margin between each Accordion Item. To do this in your application, you need to copy the CSS and put it in your theme.

```css
.accordion {
    background-color: transparent;
}

.accordion-item {
    background-color: var(--color-neutral-0);
    border-bottom-width: var(--border-size-s);
}

.accordion-item:not(:last-child) {
    margin-bottom: var(--space-base);
}
```
![](<images/accordion-image-6.png>)

## Notes

Line Separator from ListRecords should be None.

![](<images/accordion-image-7.png>)


