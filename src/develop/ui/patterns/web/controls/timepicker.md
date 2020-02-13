---
tags: runtime-traditionalweb; 
summary: TimePicker selects a single time from a list.
---

# TimePicker 

Selects a single time from a list.

Use the Time Picker to enable end-users to select a single time from a dropdown.

**How to use**

1. Drag the TimePicker pattern into the preview.

    ![](<images/timepicker-image-1.png>)

1. Set a variable of type Time to the input.

1. Publish and test.

    ![](<images/timepicker-gif-1.gif>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| StartTime  |  The time that the dropdown options will scroll to in order to have it as the first item. Make sure that the time is according to the interval that you set to begin with. Default is NewTime(0,0,0) -> 12:00am. Example: If you set the interval as 30, but the Start Time as 10:05:00. Then while it will be the time that it'll appear on the input, the drop down won't scroll down to the hour since it doesn't match the interval. | Time | No | NewTime(0,0,0) |
| Interval  |  Interval of time (in minutes) between options. Example: If 30, then the options will appear as: 08:00:00, 08:30:00, 09:00:00... | Integer | No | 30 |
| Is24hFormat |  If true, then time format will be 24 hour. If false, then 12 hour. | Boolean | No | True |
| AdvancedFormat | Allows for more options than the ones given in the input parameters. Inputs: TimePickerAdvancedFormat:  DisabledTimes (Time List), MinTime (Time), MaxTime (Time), StartEmpty (Boolean) | TimePickerAdvancedFormat | No | none |
  
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
