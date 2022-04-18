---
tags: runtime-mobileandreactiveweb;  
summary: Date Picker Range allows the end user to select a range of dates using a calendar.
locale: en-us
guid: f130d36f-74c0-450f-99b8-6f5e986c555c
app_type: mobile apps, reactive web apps
---

# Date Picker Range

<div class="info" markdown="1">

Applies only to Mobile Apps and Reactive Web Apps

</div>

You can use the Date Picker Range UI Pattern to allow users select a range date using a calendar. The Date Picker Range Pattern is based on the [flatpickr library](https://flatpickr.js.org/). For more advanced options, you can refer to this library.

In this example, the user selects a range of dates from the calendar. The dates are saved in a variable and then displayed in an input widget.

1. In Service Studio, in the Toolbox, search for `Date Picker Range`.

    The Date Picker Range widget is displayed.

    ![Date Picker Range widget](<images/datepickerrange-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Date Picker Range widget into the Main Content area of your application's screen.

    By default, the Date Picker Range contains an **Input** widget (type Text).

    ![Drag the widget to the screen](<images/datepickerrange-drag-ss.png>)

1. Create a variable by selecting the **Input** widget, and on the **Properties** tab, select **New Local Variable** from the **Variable** dropdown.

    This variable stores any value entered into or received by the Input widget.

    ![Create a new variable](<images/datepickerrange-inputvar-ss.png>)

1. Enter a name for the variable (in this example **DateVar**) and select **Date** as the **Data Type**.

    ![Enter variable name and data type](<images/datepickerrange-datevar-ss.png>)

1. Right-click your main screen and add 2 local variables (one to store the start date and one to store the end date selected by the user).

    This variable stores the date selected by the user.

    ![Add another local variable](<images/datepickerrange-addvar-ss.png>)

1. Enter a name for the variables (in this example **PickedStartDate** and **PickedEndDate**) and select **Date** as the **Data Type**.

    ![Enter variable name and data type](<images/datepickerrange-pickedstart-pickedend-ss.png>)
   

1. To create an **OnSelect** event for the Date Picker Range, on the **Properties** tab, from the **Handler** dropdown, select New **Client Action**.

    ![Create onSelect event for Date Picker Range](<images/datepickerrange-handler-ss.png>)

1. To access the date range selected by the user, create an **Assign** and set the **PickedStartDate** to **Start Date** and **PickedEndDate** to **EndDate**.

    ![Add assign and variable value](<images/datepickerrange-assign-ss.png>)

1. You can configure the Date Picker Range by selecting the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the **OptionalConfigs** property.

    ![Set properties](<images/datepickerrange-properties-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

**Result**

![Date Picker Range result](<images/datepickerrange-result.png>)

## Properties

|Properties|Description|
|---|---|
|DateFormat (Text): Optional| Set the input date format. If empty, the date format will be the same as the server format. When using formats with time, make sure to set the **TimeFormat** property. The following are some examples:<ul><li>"DD/MM/YYYY" - 15/05/2022 </li> <li>"MM/DD/YYYY" - 05/15/2022</li><li>"DD MMM YYYY" - 15 May 2022</li><li>"DD-MMM-YYYY" - 15-May-2022</li><li>"DD.MMM.YYYY" - 15.May.2022</li><li>"MMM DDD, YYYY" - May Sun, 2022</li><li>"MMM DDD, YY" - May Sun, 22</li></ul> |
|ShowTodayButton (Boolean): Optional | If True, the **Today** button is displayed below the Date Picker Range.  This button allows users to pick the date of the current day. If False, the **Today** Button is not displayed. The default value is False.|
|OptionalConfigs.InitialStartDate (Date): Optional|The preselected start date for the Date Picker Range. If not set, no start date or end date is preselected.|
|OptionalConfigs.InitialEndDate (Date): Optional|The preselected end date for the Date Picker Range. If not set, no start date or end date is preselected.|
|OptionalConfigs.MinDate (DateTime): Optional|All days before this date are disabled. |
|OptionalConfigs.MaxDate (DateTime): Optional|All days before this date are disabled. |
|OptionalConfigs.FirstWeekDay (DatePickerWeekDay Identifier): Optional|Defines which week day is displayed first.|
|ExtendedClass (Text): Optional| Adds custom style classes to the Pattern. You define your [custom style classes](../../../../look-feel/css.md) in your application using CSS. <br/><br/>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Framework Cheat Sheet](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/CheatSheet).|
