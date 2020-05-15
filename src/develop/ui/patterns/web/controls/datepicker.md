---
tags: runtime-traditionalweb; 
summary: Date Picker allows the end user to select a single or a range of dates using a calendar.
---

# Date Picker 

You can use the Date Picker UI Pattern to allow the user to select a single or a range of dates using a calendar.

![](<images/datepicker-image-13.png>)

**How to use the Date Picker UI Pattern**

<!-- Drag an input and the DatePicker to the screen and set up the parameters. Only the InputWidgetId parameter is mandatory and must reference an input widget that will show the date picked on the page. -->

1. In Service Studio, from the Toolbox, drag an Input widget into the Main Content area of your application's screen.

1. On the **Properties** tab, enter the Input **Name**. In this example we call it **datepicker**. 

    ![](<images/datepicker-image-14.png>)

1. From the **Variable** drop-down, select **New Local Variable**.

1. On the properties tab, set the Variable **Data Type** to **Date**.

    ![](<images/datepicker-image-16.png>)
 
1. From the Toolbox, drag the Date Picker widget into the Main Content area of your application's screen.

1. Set the **InputWidgetId** to the input Id. 

    ![](<images/datepicker-image-2.png>)

1. In the Events, create the OnClose and OnSelect events.

    ![](<images/datepicker-image-7.png>)

1. Use the date in the input parameter in your logic.

    ![](<images/datepicker-image-8.png>)

1. Publish and test.


For advanced options, you can check the official documentation of the [Pikaday library](https://github.com/dbushell/Pikaday).

## Properties

| **Property** |  **Description** |  
|---|---|
| InputWidgetId (Text): Mandatory  | Input element Id that triggers the element so it is visible.  |
| ButtonWidgetId (Text): Optional  |  Element name (example: button) that  triggers the element so it is visible. |
| DisabledDates (Date List):Optional  |  List of dates for the disabled days.  | 
| MinDate (Date): Optional | Dates from this date onwards are enabled and  dates before this date are disabled. |
| MaxDate (Date): Optional| Dates before this date are enabled and dates after this date are disabled.  | 
| InitialDate (Date Time): Optional| If set, the calendar will initially display the set date, otherwise it will display the current Date (default).| 
| DateFormat (Text): Optional | Defaults to the date format defined in the server configuration. The default is the server date format. | 
| SelectInterval (Boolean): Optional  |  Allows the selection between two dates. If set to True, the Block Event "On Select" has the values for both parameters.  |
| AdvancedFormat (DatePickerAdvancedFormat): Optional | Allows for more options than the ones given in the input parameters. |
 

### Date Picker Advanced Format information

| **Property** |  **Description** | 
|---|---|
| EventsList | A list of events (type Date Time) | Date Time List | False | none |
| AdvancedFormatJSON | A string with options such as: `{ disableWeekends: true,  BeginEmpty: true }`. For more advanced options, read the official documentation: https://github.com/dbushell/Pikaday | Date Time List | False | none |


![](<images/datepicker-gif-1.gif>)

## Device Compatibility

When used on mobile devices, it should be used horizontally to avoid issues related to the positioning of the DatePicker.
