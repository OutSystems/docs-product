---
tags: runtime-mobileandreactiveweb;  
summary: Date Picker allows the end user to select a single or a range of dates using a calendar.
---

# How to use the Date Picker UI Pattern

This example binds the Date Picker widget to an input. When the user selects a date from the calendar it is displayed in the input widget.

1. In Service Studio, in the Toolbox, search for `Date Picker`.

    The Date Picker widget is displayed.

    ![](<images/datepicker-image-2.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Date Picker widget into the Main Content area of your application's screen.

    ![](<images/datepicker-image-1.png>)

3. Drag an Input widget to the screen and on the **Properties** tab, enter a name (in this example Input_Text), and leave the **Input Type** property as **Text**.

    **Note**: Ensure you place the Input widget before the DatePicker block to avoid rendering errors. 

    ![](<images/datepicker-input.png>)

1. Create a variable by selecting **New Local Variable** from the **Variable** dropdown. 

    This variable stores any value entered into/received by the input widget.

    ![](<images/datepicker-variable.png>)

1. Enter a name for the variable (in this example TextInput) and select **Text** as the **Data Type**.

    ![](<images/datepicker-input-text.png>)

1. Select the DatePicker block, and set the **InputWidgetId** property to the Input Id (the Input widget name).

    ![](<images/datepicker-input-id.png>)

    <div class="info" markdown="1">
  
    When using the **InputWidgetId** property, you must always set the **Input Type** property to **Text** (not **Date**) for the following reasons:

    * To avoid conflicts with the html native Date Picker available for inputs of type ["date"](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date) and ["local-datetime"](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/datetime-local)

    * To simplify the advanced date format options available in the Date Picker, you must always use input and variables of type text. Although this forces you to use [Data Conversion](<../../../../../../ref/lang/auto/builtinfunction.Data Conversion.final.md>), it brings you more flexibility when controlling the date format as well as an overall improved user experience during runtime. 

    </div>

1. To create an **OnSelect** event for the Date Picker, on the **Properties** tab, from the **Handler** dropdown, select **New Client Action**.

    ![](<images/datepicker-action.png>)

    <div class="info" markdown="1">

     The **DateFormat** property only formats the date that appears on the bound input. The date that is thrown on the **OnSelect** event defaults to the server format and can be customized using the [Data Conversion](<../../../../../../ref/lang/auto/builtinfunction.Data Conversion.final.md>) functions.
    
    </div>

1. To access the date selected by the user, create an Assign and set the **StartDate** and **EndDate** **Data Type** property to **Date**.

    ![](<images/datepicker-assign.png>)

1. Right-click your main screen and add another local variable.

    This variable stores the date selected by the user.

    ![](<images/datepicker-add-var.png>)

1. Enter a name for the variable (in this example PickedDate) and select **Date** as the **Data Type**.

    ![](<images/datepicker-picked-date.png>)

1. Select the Assign (created in step 8) and assign the PickedDate variable (created in step 9) to the **StartDate**.

    ![](<images/datepicker-assign-var.png>)

1. On the **Properties** tab, you can customize the Date Picker's look and feel by setting any of the (optional) properties.

After following these steps and publishing the module, you can test the pattern in your app.

**Result**

![](<images/datepicker-result.png>)

## Properties

| **Properties** | **Description** |
|---|---|
| InputWidgetId (Text): Optional | Input element Id that triggers the element so it is visible.  |
| ButtonWidgetId (Text): Optional  |  Element name (example: button) that  triggers the element so it is visible. | 
| EventList (Date Time List): Optional  |  Receives a List of DateTime records that are used to highlight days as event days. |  
| MinDate (Date Time): Optional  |  Days before this date will be disabled. |  
| MaxDate (Date Time): Optional  |  Days after this date will be disabled.  |   
| InitialDate (Date Time): Optional |  The initially selected day for the Date Picker. If not set, it will be the current day by default.  | 
| ShowWeekNumbers (Boolean): Optional  | If True, the week number is displayed on the left side of the Date Picker. If False, the week number is not displayed. (False is the default.) |  
| FirstWeekDay (Integer): Optional  |  Defines which weekday is displayed first.<br/><ul><li>0: Sunday</li> <li>1: Monday (default)</li><li>2: Tuesday</li> <li>3: Wednesday</li><li>4: Thursday</li><li>5: Friday</li><li>6: Saturday</li></ul> | 
| ShowTime (Boolean): Optional  | If True, a time picker is displayed below the Date Picker. If False, there is no time picker displayed. (False is the default.) |   
| Show24HourFormat (Boolean): Optional | If True, the time picker is displayed in a 24-hour format. If False, the time picker is displayed in a 12-hour format. (True is the default.) |  
| DisabledDaysList (Date Time List): Optional  |  Receives a List of DateTime records that will be disabled on the DatePicker. If this parameter is not set, all days between the MinDate and MaxDate are enabled. No default value.  |  
| DisabledWeekDays (Text): Optional  |  String containing disabled weekdays.<br/><ul><li>0: Sunday </li><li>1: Monday </li><li>2: Tuesday </li><li>3: Wednesday </li><li>4: Thursday</li><li> 5: Friday </li><li>6: Saturday </li></ul>Example<br/><br/><ul><li>_Blank_ - All weekdays are active. </li><li>_"0,5"_ - Sunday and Friday are disabled.</li></ul> | 
| SelectInterval (Boolean): Optional |  Allows the selection between two dates. If True, the block event **OnSelect** has the values for both parameters.  |   
| StartEmpty (Boolean): Optional |  Defines whether the input for the Date Picker starts as empty.   | 
| DateFormat (Text): Optional| The Date Picker uses the [Moment.js](https://momentjs.com/docs/#/parsing/) library to handle the date format. It defaults to YYYY-MM-DD format which is accepted by OutSystems form validations.For better compatibility we advise using an input and variable of type "text". If that's the case, here's some of the examples that you can use:<ul><li>DD/MM/YYYY - 15/05/2020 </li> <li>MM/DD/YYYY - 05/15/2020</li><li>DD MMM YYYY - 15 May 2020</li></ul>If using an input/variable of type **Date** or **DateTime**, due to form validations,the only options available are the following:<ul><li>Server Format</li> <li>YYYY-MM-DDTHH:mm:ss.ssss</li><li>YYYY-MM-DD HH:mm:ss</li><li>YYYY/MM/DD HH:mm:ss</li><li>YYYY.MM.DD HH:mm:ss</li><li>YYYY.MM.DD</li><li>YYYY/MM/DD</li><li>YYYY-MM-DD</li></ul> |
|ShowTodayButton (Boolean): Optional | If True, the Today button is displayed. If False, the Today Button is not displayed. (False is the default.) |
|AdvancedFormat (Text): Optional | Allows for more options beyond what is provided through the inputs. For more information, see [Pikaday Configuration](https://github.com/Pikaday/Pikaday#configuration)|

For more information on how to implement more advanced use cases, see [Date Picker advanced use cases](datepicker-advanced.md).
