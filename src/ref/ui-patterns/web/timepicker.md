---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Time Picker UI Pattern
---

# Time Picker UI Pattern Reference

## Layout and Classes

![](<images/timepicker-image-2.png>)

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnSelect | Event will be triggered when a time is selected returning it.  |  False  |

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .time-option | .time-option-selected |  When the time option is selected  |
| .time-option | .time-picker .dropdown-content-list .time-option[disabled="disabled"] |  When the time option is disabled  |

## Advanced Use Case

### Use the OnSelect event

1. Drag the TimePicker pattern into the preview.

    ![](<images/timepicker-image-1.png>)

1. Set a variable of type Time to the input.
1. Set the StartTime Parameter to a variable Time.

    ![](<images/timepicker-image-3.png>)

1. In the preparation, set the Time variable to the start time you want for the picker. 

    ![](<images/timepicker-image-4.png>)

1. Set the OnSelect Event to TimePatternOnSelect.

    ![](<images/timepicker-image-5.png>)

1. In the TimePatternOnSelect action, assign  TimeSelected to the Time variable. 

    ![](<images/timepicker-image-6.png>)

1. Set a Feedback_Message action and show the Timein the message.

1. Create a container Timepicker_Container around the TimePicker. 

    ![](<images/timepicker-image-7.png>)

1. In the action TimePatternOnSelect, add an Ajax refresh for the Timepicker_Container.

    ![](<images/timepicker-image-8.png>)

![](<images/timepicker-gif-2.gif>)

### Disable specific times

1. Drag the TimePicker pattern into the preview.

    ![](<images/timepicker-image-1.png>)

1. Set a variable of type Time to the input.
1. Click the plus before the AdvancedFormat parameter.

    ![](<images/timepicker-image-9.png>)

1. Click the plus before the DisabledTimes parameter.

    ![](<images/timepicker-image-10.png>)

1. Add the times NewTime(4,0,0) and NewTime(7,0,0).

    ![](<images/timepicker-image-11.png>)

1. Publish and test.

    ![](<images/timepicker-gif-3.gif>)

### Start Input as Empty

1. Drag the TimePicker pattern into the preview.

    ![](<images/timepicker-image-1.png>)

1. Set a variable of type time to the input.

1. Click the plus before the AdvancedFormat parameter.

    ![](<images/timepicker-image-9.png>)

1. Set the StartEmpty parameter to True.

    ![](<images/timepicker-image-12.png>)

1. Publish and test.

    ![](<images/timepicker-image-13.png>)





