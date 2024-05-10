---
tags: runtime-traditionalweb; 
summary: Learn how to integrate the Button Group UI Pattern in Traditional Web Apps using OutSystems 11 (O11).
locale: en-us
guid: 42dbee79-dfe8-4f57-8fb7-d5a19e8bf87d
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:402
---

# Button Group Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and Classes

![Screenshot illustrating the layout and classes of the Button Group UI Pattern in a Traditional Web App](images/buttongroup-image-3.png "Button Group Layout")

## Advanced Use Case

### Use ButtonGroup with ListRecords

1. Drag the ButtonGroup Pattern into the preview.

1. In the Content placeholder, drag a ListRecords widget.

1. In the ListRecords widget, drag a ButtonGroupItem.

1. In the ButtonGroupItem, use expressions with the class btn to display the content.

    ![Step-by-step visual guide on using ButtonGroup with ListRecords in a Traditional Web App](images/buttongroup-image-4.png "ButtonGroup with ListRecords")

1. In the ListRecords Widget, set the Line Separator to None in order to avoid additional margin between elements.

1. Publish and test.


## Note

When used inside List Records or Table Records, you must manually add the attribute name for each radio button that is part of a Button Group so that the platform binds them correctly: 


![Example of a Button Group used inside List Records or Table Records with manually added attribute names for radio buttons](images/buttongroup-image-5-ss.png "Button Group Usage Example")

