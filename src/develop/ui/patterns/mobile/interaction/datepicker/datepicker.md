---
tags: runtime-mobileandreactiveweb;  
summary: Date Picker allows the end user to select a single or a range of dates using a calendar.
---

# How to use the Date Picker UI Pattern

This example binds the Date Picker widget to an input. When the user selects a date from the calendar it is displayed in the input widget.

1. In Service Studio, in the Toolbox, search for `Date Picker`.

    The Date Picker widget is displayed.

    ![Date Picker widget](<images/datepicker-image-2.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Date Picker widget into the Main Content area of your application's screen.

    By default, the Date Picker contains an **Input** widget.

    ![Drag the widget to the screen](<images/datepicker-image-1.png>)

1. Create a variable by selecting the Input widget, and on the Properties tab, select **New Local Variable** from the **Variable** dropdown.

    This variable stores any value entered into or received by the Input widget.

1. Enter a name for the variable (in this example **DateTimeVar**) and select **Date Time** as the **Data Type**.

1. Right-click your main screen and add another local variable.

    This variable stores the date selected by the user.

1. Enter a name for the variable (in this example **PickedDate**) and select **Date Time** as the **Data Type**.

1. To create an **OnSelect** event for the Date Picker, on the **Properties** tab, from the **Handler** dropdown, select New **Client Action**.

    <div class="info" markdown="1">

    The **DateFormat** property only formats the date that appears on the bound input. The date that is thrown on the OnSelect event defaults to the server format and can be customized using the [Data Conversion](<../../../../../../ref/lang/auto/builtinfunction.Data Conversion.final.md>) functions.
    
    </div>

1. To access the date selected by the user, create an **Assign** and set the **PickedDate** to **SelectedDateTime**.

1. On the **Properties** tab, you can customize the Date Picker's look and feel by setting any of the (optional) properties.

After following these steps and publishing the module, you can test the pattern in your app.

**Result**

![](<images/datepicker-result.png>)

## Properties

|Properties|Description|
|---|---|
|DateFormat (Text): Optional| Set the input date format. If empty, the date format will be the same as the server format. When using formats with time, make sure to set the TimeFormat property. Here's some of the examples that you can use:<ul><li>DD/MM/YYYY - 15/05/2020 </li> <li>MM/DD/YYYY - 05/15/2020</li><li>DD MMM YYYY - 15 May 2020</li></ul>If using an input/variable of type **Date** or **DateTime**, due to form validations,the only options available are the following:<ul><li>Server Format</li> <li>YYYY-MM-DDTHH:mm:ss.ssss</li><li>YYYY-MM-DD HH:mm:ss</li><li>YYYY/MM/DD HH:mm:ss</li><li>YYYY.MM.DD HH:mm:ss</li><li>YYYY.MM.DD</li><li>YYYY/MM/DD</li><li>YYYY-MM-DD</li></ul> |
|ShowTodayButton (Boolean): Optional | If True, the **Today** button is displayed below the Date Picker. This button allows the user pick the current day date. If False, the Today Button is not displayed. The default value is False.|
|TimeFormat (DatePickerTimeFormat Identifier): Optional|Select the format of the time (12 hours or 24 hours). By default, no time is shown (Disabled).|
|InitialDate (Date Time): Optional|The initial selected date for the DatePicker. If not set, no initial date is selected.|
|MinDate (Date Time): Optional|Days before this date will be disabled.|
|MaxDate (Date Time): Optional|Days after this date will be disabled.|
|FirstWeekDay (DatePickerWeekDay Identifier): Optional|Defines which week day should be displayed first.|
|ExtendedClass (Text): Optional|Examples
Blank - No custom styles are added (default value).
"myclass" - Adds the myclass style to the UI styles being applied.
"myclass1 myclass2" - Adds the myclass1 and myclass2 styles to the UI styles being applied.
You can also use the classes available on the OutSystems UI. For more information, see the https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet|


