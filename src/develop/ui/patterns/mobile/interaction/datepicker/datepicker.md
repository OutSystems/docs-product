---
tags: runtime-mobileandreactiveweb;  
summary: Date Picker allows the end user to select a single or a range of dates using a calendar.
---

# How to use the Date Picker UI Pattern

You can use the Date Picker UI Pattern to allow users to select a single date using a calendar. The Date Picker Pattern is based on the [flatpickr](https://flatpickr.js.org/) library. For more advanced options, you can refer to this library.

In this example, the user selects a date from the calendar, the date is saved in a variable and then displayed in an input widget.

1. In Service Studio, in the Toolbox, search for `Date Picker`.

    The Date Picker widget is displayed.

    ![Date Picker widget](<images/datepicker-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Date Picker widget into the Main Content area of your application's screen.

    By default, the Date Picker contains an **Input** widget (type Text).

    ![Drag the widget to the screen](<images/datepicker-drag-ss.png>)

1. Create a variable by selecting the **Input** widget, and on the **Properties** tab, select **New Local Variable** from the **Variable** dropdown.

    This variable stores any value entered into or received by the Input widget.

    ![Create a new variable](<images/datepicker-var-ss.png>)

1. Enter a name for the variable (in this example **DateTimeVar**) and select **Date Time** as the **Data Type**.

    ![Enter variable name and data type](<images/datepicker-varname-ss.png>)

1. Right-click your main screen and add another local variable.

    This variable stores the date selected by the user.

    ![Add another local variable](<images/datepicker-localvar-ss.png>)

1. Enter a name for the variable (in this example **DatePicked**) and select **Date Time** as the **Data Type**.

    ![Enter variable name and data type](<images/datepicker-locvarname-ss.png>)

1. To create an **OnSelect** event for the Date Picker, on the **Properties** tab, from the **Handler** dropdown, select New **Client Action**.

    ![Create onSelect event for Date Picker](<images/datepicker-clientaction-ss.png>)

1. To access the date selected by the user, create an **Assign** and set the **DatePicked** to **SelectedDateTime**.

    ![Add assign and variable value](<images/datepicker-assign-ss.png>)

1. You can configure the Datepicker by selecting the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the **OptionalConfigs** property.

    ![Set properties](<images/datepicker-properties-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

**Result**

![Datepicker result](<images/datepicker-result.png>)

## Properties

|Properties|Description|
|---|---|
|DateFormat (Text): Optional| Set the input date format. If empty, the date format will be the same as the server format. When using formats with time, make sure to set the **TimeFormat** property. The following are some examples:<ul><li>"DD/MM/YYYY" - 15/05/2022 </li> <li>"MM/DD/YYYY" - 05/15/2022</li><li>"DD MMM YYYY" - 15 May 2022</li><li>"DD-MMM-YYYY" - 15-May-2022</li><li>"DD.MMM.YYYY" - 15.May.2022</li><li>"MMM DDD, YYYY" - May Sun, 2022</li><li>"MMM DDD, YY" - May Sun, 22</li></ul> |
|ShowTodayButton (Boolean): Optional | If True, the **Today** button is displayed below the Date Picker.  This button allows users to pick the date of the current day. If False, the **Today** Button is not displayed. The default value is False.|
|TimeFormat (DatePickerTimeFormat Identifier): Optional|Select the time format (12 or 24 hours). By default, no time is shown.|
|OptionalConfigs.InitialDate (Date Time): Optional|The initial selected date for the Date Picker. If not set, no initial date is selected.|
|OptionalConfigs.MinDate (DateTime): Optional|All days before this date are disabled.|
|OptionalConfigs.MaxDate (DateTime): Optional|All days after this date are disabled.|
|OptionalConfigs.FirstWeekDay (DatePickerWeekDay Identifier): Optional|Defines which week day is displayed first.|
|ExtendedClass (Text): Optional| Adds custom style classes to the Pattern. You define your [custom style classes](../../../../look-feel/css.md) in your application using CSS. <br/><br/>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Framework Cheat Sheet](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/CheatSheet).|
