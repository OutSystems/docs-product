---
tags: ui patterns, web development, breadcrumbs integration, outsystems ui, ui design
summary: Explore breadcrumb integration in Traditional Web Apps using OutSystems 11 (O11).
locale: en-us
guid: 4e6390a2-3d56-4b65-aabe-aa7588ff2253
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:395
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Breadcrumbs Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of the Breadcrumbs UI Pattern](images/breadcrumbs-3-diag.png "Breadcrumbs Layout Diagram")

## Advanced use case

### Use breadcrumbs with ListRecords

1. Drag the Breadcrumbs Pattern into preview.

1. In the Content placeholder, drag a ListRecords widget.

1. In the ListRecords widget, drag a Breadcrumbs Item.

1. Inside the BreadcrumbsItem Pattern, use expressions to display the content.

1. Publish and test.

    ![Screenshot showing the Breadcrumbs UI Pattern used with a ListRecords widget](images/breadcrumbs-4-ss.png "Breadcrumbs with ListRecords")

## Additional notes

The Line Separator property of the ListRecords widget should be set to **None**.

![Screenshot highlighting the Line Separator property setting for the ListRecords widget in Breadcrumbs](images/breadcrumbs-5-ss.png "Breadcrumbs Line Separator Setting")