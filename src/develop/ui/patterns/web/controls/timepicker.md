---
tags: runtime-traditionalweb; 
summary: Time Picker selects a single time from a drop-down list.
---

# Time Picker 

You can use the Time Picker UI Pattern to select a single time from a drop-down list.

  ![](<images/timepicker-gif-1.gif>)


**How to use the Time Picker UI Pattern**

1. In Service Studio, in the Toolbox, search for `Time Picker`.

    The Time Picker widget is displayed.

    ![](<images/timepicker-image-14.png>)

1. From the Toolbox, drag the Time Picker widget into the Main Content area of your application's screen.

    ![](<images/timepicker-image-15.png>)

1. By default, the Time Picker widget contains an Input widget. It is mandatory to create a new local variable for this Input widget.

    ![](<images/timepicker-image-16.png>)

1. Set the variable **Data Type** to **Time**.

    ![](<images/timepicker-image-17.png>)

1. On the **Properties** tab, you can change the look and feel of the Time Picker widget by setting the (optional) properties.

    ![](<images/timepicker-image-18.png>)

1. After following these steps and publishing the module, you can test the pattern in your app. 


## Properties

| **Property** |  **Description** |  
|---|---|
| StartTime (Time): Optional  |  The first time option that appears in the drop-down. Make sure that the time is set according to the **Interval** property (if set). <!--Default is NewTime(0,0,0) -> 12:00am. Example: If you set the interval as 30, but the Start Time as 10:05:00. Then while it will be the time that it'll appear on the input, the drop down won't scroll down to the hour since it doesn't match the interval. --><br/><br/>Examples<br/><br/><ul><li>_Blank_ - 12:00am is displayed as the first option in the drop-down. This is the default. </li><li>_15:00_ - 15:00 is displayed as the first option in the drop-down.</li></ul> | 
| Interval (Integer): Optional  |  Interval of time (in minutes) between the drop-down options.<br/><br/>Example<ul><li>_Blank_ - The interval between each option is set to 30 minutes. This is the default.</li><li>_60_ - The interval between each option is set to 60 minutes.</li></ul> |
| Is24hFormat (Boolean): Optional|  If True, the time format is 24 hour. This is the default. If False, the time format is 12 hour. |
| AdvancedFormat (TimePickerAdvancedFormat): Optional | Allows for more options than the ones given in the input parameters.<br/><br/>**Inputs**<br/><br/>TimePickerAdvancedFormat<br/><br/><ul><li> DisabledTimes (Time List)</li><li> MinTime (Time)</li> <li>MaxTime (Time)</li> <li>StartEmpty (Boolean)</li></ul> |
  
