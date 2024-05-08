---
tags: runtime-traditionalweb; 
summary: Explore accordion customization options in OutSystems 11 (O11) for traditional web apps, including CSS modifications and advanced use cases.
locale: en-us
guid: 535efa42-703f-4913-a0e6-d452ac259513
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=615%3A353&mode=design&t=Cx8ecjAITJrQMvRn-1
---

# Accordion Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and Classes

![Screenshot of an accordion layout in a traditional web app](images/accordion-image-3.png "Accordion Layout")

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

    ![Example of using Accordion with ListRecords in a traditional web app](images/accordion-image-4.png "Accordion with ListRecords")

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

![Illustration of custom CSS applied to change the arrow position to the left in an AccordionItem](images/accordion-image-5.png "Custom CSS for Arrow Position")

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

![Demonstration of custom CSS to add margin between Accordion Items](images/accordion-image-6.png "Custom CSS for Accordion Item Margin")

## Notes

Line Separator from ListRecords should be None.

![Visual representation of the line separator setting for ListRecords in an accordion](images/accordion-image-7.png "Accordion Line Separator")
