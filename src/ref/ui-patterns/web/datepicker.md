---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Date Picker UI Pattern.
locale: en-us
guid: f0fe14e4-6f11-4000-aa5b-81344f784447
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=615%3A442&mode=design&t=Cx8ecjAITJrQMvRn-1
---

# Date Picker Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and Classes

![Screenshot of the Date Picker layout for Traditional Web Apps](images/datepicker-image-3.png "Date Picker Layout")

![Image showing the CSS classes used in the Date Picker component](images/datepicker-image-4.png "Date Picker Classes")

### Month Picker

![Example of the Month Picker interface in the Date Picker component](images/datepicker-image-5.png "Month Picker")

### Year Picker

![Example of the Year Picker interface in the Date Picker component](images/datepicker-image-6.png "Year Picker")

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

    ![Illustration of the Advanced Format property expansion in the Date Picker settings](images/datepicker-image-9.png "Advanced Format Property")

1. Add `{ BeginEmpty: true }` in the AdvancedFormatJSON. 


    ![Configuration setting for starting with a blank input in the Date Picker](images/datepicker-image-11.png "Blank Input Configuration")

### Have a flat datepicker

1. Drag the DatePicker to the preview.

1. Expand the AdvancedFormat property.

    ![Illustration of the Advanced Format property expansion in the Date Picker settings](images/datepicker-image-9.png "Advanced Format Property")

1. Add `{ bound: false }` in the AdvancedFormatJSON. 

1. To use events to pick the chosen date, use OnSelect instead of OnClose.

    ![Configuration setting for having a flat Date Picker without bounding to an input field](images/datepicker-image-10.png "Flat Datepicker Configuration")

### Add Events

1. Drag the DatePicker to the preview.

1. Expand the AdvancedFormat property.

    ![Illustration of the Advanced Format property expansion in the Date Picker settings](images/datepicker-image-9.png "Advanced Format Property")

1. Add your date time list in the EventList.

### Use Date Format

1. Drag the DatePicker to the preview.

1. Set the format of the date (for instance, `"DD MMM of YYYY"` will be displayed as 12 Dec of 2018). 

1. Create an onClose or OnSelect event and use the date for your logic.

    ![Example of setting a custom date format in the Date Picker component](images/datepicker-image-12.png "Date Format Configuration")

