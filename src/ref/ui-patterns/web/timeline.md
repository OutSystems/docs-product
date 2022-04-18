---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Timeline UI Pattern.
locale: en-us
guid: c0cdbad2-39c2-434e-afc5-6f05acf4901d
app_type: traditional web apps
---

# Timeline Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](images/timeline-5-diag.png?width=750)

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

![](<images/timeline-6.png>)
