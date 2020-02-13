---
tags: runtime-traditionalweb; 
summary: ResponsiveTable displays information in a logical and organized way that is easy to scan and read.
---

# ResponsiveTable

Display information in a logical and organized way.

Use Table Records to display information in a logical and organized way that is easy to scan and read. It should allow interaction, such as sorting, so that end-users can customize their view of the information.

**How to use**

1. Drag ResponsiveTable pattern into the preview.

    ![](<images/responsivetable-image-1.png?width=500>)

1. Drag the Table Widget you want to change to the Content placholder.

    ![](<images/responsivetable-image-2.png>)

1. Set the mandatory values.

    ![](<images/responsivetable-image-3.png>)

1. Publish and test.


## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| ResponsiveBehavior  |  TableRecords responsive behavior. | ResponsiveTableRecords Identifier | Yes | none |
  
## Layout and Classes

![](<images/responsivetable-image-4.png>)


## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .table-records-responsive |  .table-records-responsive.scrollable-row|  When the ResponsiveBehavior parameter is set to scrollable  |
| .table-records-responsive |  .table-records-responsive.expandable-row|  When the ResponsiveBehavior parameter is set to expandable  |
| table tbody tr |  .TableRecords_ExpandedRow |  When using the expandable-row option, identifies when the the row is expanded  |


## Advanced Use Case

### Change Responsive Behavior parameter according to device

1. Drag the ResponsiveTable Pattern into the page.

1.  Set the ResponsiveBehaviour parameter to `If(IsPhone(), Entities.ResponsiveTableRecords.ExpandableRows, Entities.ResponsiveTableRecords.ScrollabeRows)`. 

    We use the server action IsPhone as the condition to set the property for phone devices. You can also use the IsTablet action, or invert the False & True statements as required.

1. Publish and test.

### Change expandable-row's arrow color

To implement this, you can use either method described below.

1. Write the following CSS in the CSS editor and change `yourcolor` accordingly.

```css
.tablet.portrait .expandable-row .TableRecords tbody tr td:first-child:after, 
.phone .expandable-row .TableRecords tbody tr td:first-child:after {
    color: yourcolor;
}
```

2. Use CSS variables like `var(--color-yourcolor)`.

```css
.tablet.portrait .expandable-row .TableRecords tbody tr td:first-child:after, 
.phone .expandable-row .TableRecords tbody tr td:first-child:after {
    color: var(--color-yourcolor);
}
```
