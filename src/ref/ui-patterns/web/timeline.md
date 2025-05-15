---
tags: ui patterns, css customization, web development, traditional web, outsystems ui
summary: Explore how to integrate the Timeline UI Pattern with ListRecords in Traditional Web Apps using OutSystems 11 (O11).
locale: en-us
guid: c0cdbad2-39c2-434e-afc5-6f05acf4901d
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:589
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Timeline Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of the Timeline UI Pattern in a Traditional Web App](images/timeline-5-diag.png "Timeline Layout Diagram")

## Advanced Use Case

### Use the Timeline Pattern with ListRecords

1. Drag the Timeline Pattern into the preview.
1. In the Content placeholder, drag a ListRecords widget.
1. In the ListRecords widget, drag a TimelineItem.
1. In the TimelineItem, use expressions to display the database content you need.
1. To disable the vertical line on the last TimelineItem, write the following CSS code in the application Theme:

        .ListRecords .timeline-item:last-of-type .timeline-item-separator {
            display: none; 
        }

1. In the ListRecords Widget, set Line Separator to None to avoid additional margin between elements.

1. Publish and test.

![Screenshot showing the Timeline Pattern used with ListRecords widget in a Traditional Web App](images/timeline-6.png "Timeline Pattern with ListRecords")
