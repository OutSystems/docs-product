---
tags: runtime-traditionalweb; 
summary: Explore the features and advanced use cases of the Time Picker UI component in OutSystems 11 (O11).
locale: en-us
guid: 19d186e8-664b-4066-9e83-e866c45cbba7
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:592
---

# Time Picker Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and Classes

![Screenshot showing the layout and CSS classes of the Time Picker UI component](images/timepicker-image-2.png "Time Picker Layout")

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

    ![Preview image of dragging the TimePicker pattern into the workspace](images/timepicker-image-1.png "Time Picker Pattern Preview")

1. Set a variable of type Time to the input.

1. Set the StartTime Parameter to a variable Time.

    ![Screenshot demonstrating how to set the StartTime parameter to a variable of type Time](images/timepicker-image-3.png "Setting StartTime Parameter")

1. In the preparation, set the Time variable to the start time you want for the picker. 

    ![Image showing the setting of the Time variable to the start time in preparation for the Time Picker](images/timepicker-image-4.png "Preparation Time Variable")

1. Set the OnSelect Event to TimePatternOnSelect.

    ![Screenshot of setting the OnSelect event to the TimePatternOnSelect function in the Time Picker configuration](images/timepicker-image-5.png "OnSelect Event Setup")

1. In the TimePatternOnSelect action, assign  TimeSelected to the Time variable. 

    ![Image depicting the assignment of TimeSelected to the Time variable in the TimePatternOnSelect action](images/timepicker-image-6.png "TimePatternOnSelect Action")

1. Set a Feedback_Message action and show the Timein the message.

1. Create a container Timepicker_Container around the TimePicker. 

    ![Screenshot showing the creation of a container around the TimePicker UI component](images/timepicker-image-7.png "TimePicker Container")

1. In the action TimePatternOnSelect, add an Ajax refresh for the Timepicker_Container.

    ![Image illustrating the addition of an Ajax refresh for the Timepicker_Container in the TimePatternOnSelect action](images/timepicker-image-8.png "Ajax Refresh Setup")

<iframe src="https://player.vimeo.com/video/998212683" width="750" height="388" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video demonstrating interaction with the Time Picker UI component.</iframe>

### Disable specific times

1. Drag the TimePicker pattern into the preview.

    ![Preview image of dragging the TimePicker pattern into the workspace](images/timepicker-image-1.png "Time Picker Pattern Preview")

1. Set a variable of type Time to the input.

1. Click the plus before the AdvancedFormat parameter.

    ![Screenshot showing how to access the AdvancedFormat parameter of the TimePicker](images/timepicker-image-9.png "AdvancedFormat Parameter")

1. Click the plus before the DisabledTimes parameter.

    ![Image displaying the process of accessing the DisabledTimes parameter of the TimePicker](images/timepicker-image-10.png "DisabledTimes Parameter")

1. Add the times NewTime(4,0,0) and NewTime(7,0,0).

    ![Screenshot illustrating the addition of specific times to be disabled in the TimePicker](images/timepicker-image-11.png "Disabling Specific Times")

1. Publish and test.

    <iframe src="https://player.vimeo.com/video/998212655" width="750" height="388" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video showing the Time Picker with specific times disabled.</iframe>

### Start Input as Empty

1. Drag the TimePicker pattern into the preview.

    ![Preview image of dragging the TimePicker pattern into the workspace](images/timepicker-image-1.png "Time Picker Pattern Preview")

1. Set a variable of type time to the input.

1. Click the plus before the AdvancedFormat parameter.

    ![Screenshot showing how to access the AdvancedFormat parameter of the TimePicker](images/timepicker-image-9.png "AdvancedFormat Parameter")

1. Set the StartEmpty parameter to True.

    ![Image demonstrating how to set the StartEmpty parameter to True in the TimePicker](images/timepicker-image-12.png "StartEmpty Parameter Setup")

1. Publish and test.

    ![Preview of the TimePicker with an empty input field indicating the StartEmpty parameter is set to True](images/timepicker-image-13.png "Empty Time Picker Input")
