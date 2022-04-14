---
tags: runtime-traditionalweb;
summary: Advanced use cases for the Responsive Table UI Pattern.
locale: en-us
guid: 7b507cb7-8c2c-4705-a564-69e0bda38397
---

# Responsive Table Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/responsivetable-4-diag.png>)

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .table-records-responsive |  .table-records-responsive.scrollable-row|  When the ResponsiveBehavior parameter is set to scrollable  |
| .table-records-responsive |  .table-records-responsive.expandable-row|  When the ResponsiveBehavior parameter is set to expandable  |
| table tbody tr |  .TableRecords_ExpandedRow |  When using the expandable-row option, identifies when the row is expanded  |

## Advanced use case

### Change the responsive behavior parameter according to device

1. Drag the ResponsiveTable Pattern into the page.

1. Set the ResponsiveBehaviour parameter to `If(IsPhone(), Entities.ResponsiveTableRecords.ExpandableRows, Entities.ResponsiveTableRecords.ScrollabeRows)`.

    We use the server action IsPhone as the condition to set the property for phone devices. You can also use the IsTablet action, or invert the False & True statements as required.

1. Publish and test.

### Change expandable-row's arrow color

To implement this, you can use either method described below.

* Write the following CSS in the CSS editor and change `yourcolor` accordingly.

```css
.tablet.portrait .expandable-row .TableRecords tbody tr td:first-child:after,
.phone .expandable-row .TableRecords tbody tr td:first-child:after {
    color: yourcolor;
}
```

* Use CSS variables like `var(--color-yourcolor)`.

```css
.tablet.portrait .expandable-row .TableRecords tbody tr td:first-child:after,
.phone .expandable-row .TableRecords tbody tr td:first-child:after {
    color: var(--color-yourcolor);
}
```
