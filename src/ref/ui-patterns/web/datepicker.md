---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Date Picker UI Pattern.
locale: en-us
guid: f0fe14e4-6f11-4000-aa5b-81344f784447
---

# Date Picker Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and Classes

![](<images/datepicker-image-3.png?width=600>)

![](<images/datepicker-image-4.png?width=600>)

### Month Picker

![](<images/datepicker-image-5.png?width=600>)

### Year Picker

![](<images/datepicker-image-6.png?width=600>)

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| onClose | Event that will be triggered once you close the date picker which returns the last selected date.  |  False  |
| onOpen | Event that will be triggered once you open the date picker.  |  False  |
| OnSelect | Event will be triggered when a date is selected returning it.  |  False  |


## Advanced Use Case

### Start with a blank input

1. Drag the DatePicker to the preview.

1. Expand the AdvancedFormat property.

    ![](<images/datepicker-image-9.png>)

1. Add `{ BeginEmpty: true }` in the AdvancedFormatJSON. 


    ![](<images/datepicker-image-11.png>)

### Have a flat datepicker

1. Drag the DatePicker to the preview.

1. Expand the AdvancedFormat property.

    ![](<images/datepicker-image-9.png>)

1. Add `{ bound: false }` in the AdvancedFormatJSON. 

1. To use events to pick the chosen date, use OnSelect instead of OnClose.

    ![](<images/datepicker-image-10.png>)

### Add Events

1. Drag the DatePicker to the preview.

1. Expand the AdvancedFormat property.

    ![](<images/datepicker-image-9.png>)

1. Add your date time list in the EventList.

### Use Date Format

1. Drag the DatePicker to the preview.

1. Set the format of the date (for instance, `"DD MMM of YYYY"` will be displayed as 12 Dec of 2018). 

1. Create an onClose or OnSelect event and use the date for your logic.

    ![](<images/datepicker-image-12.png>)

