---
tags: ide usage, reactive web apps, tutorials for beginners, ui patterns, date handling
summary: Explore the Month Picker UI Pattern in OutSystems 11 (O11) for user-friendly month selection based on the flatpickr library.
locale: en-us
guid: 81E3194C-9817-4A14-81C5-5E3F3CDDE4E3
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=3248:26842
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Month Picker

You can use the Month Picker UI Pattern to allow users input a month of the year. The Month Picker Pattern is based on the [flatpickr library](https://flatpickr.js.org/) For more advanced options, you can refer to this library.

## How to use the Month Picker UI Pattern

1. In Service Studio, in the Toolbox, search for `Month Picker`.

    The Month Picker widget is displayed.

    ![Screenshot of the Month Picker widget in the Service Studio toolbox](images/monthpicker-widget-ss.png "Month Picker Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Month Picker widget into the Main Content area of your application's screen.

    ![Dragging the Month Picker widget into the Main Content area of an application's screen](images/monthpicker-dragwidget-ss.png "Dragging Month Picker Widget to Screen")

    By default, the Month Picker contains an **Input** widget (type Text).

1. Create a local variable by selecting the Input widget, and, on the **Properties** tab, select **New Local Variable** from the **Variable** dropdown.

    This variable stores any value entered into or received by the input widget.

    ![Creating a local variable for the Month Picker input widget in Service Studio](images/monthpicker-variable-ss.png "Creating a New Local Variable for Month Picker")

1. Enter a name for the variable (in this example **MonthVar**) and select **Text** as the **Data Type**.

    ![Naming the local variable as 'MonthVar' and selecting 'Text' as the data type](images/monthpicker-monthvar-ss.png "Naming the Month Variable")

1. Right-click your main screen and add another local variable.

    This variable stores the month selected by the user.

    ![Creating another local variable to store the month selected by the user](images/monthpicker-localvar-ss.png "Creating Another Local Variable")

1. Enter a name for the variable (in this example **MonthPicked**) and select **MonthYear** as the **Data Type**.

    ![Naming the new local variable as 'MonthPicked' and selecting 'MonthYear' as the data type](images/monthpicker-monthpicked-ss.png "Naming the Month Picked Variable")

1. To create an **OnSelect** event for the Month Picker, select the Month Picker widget, and on the **Properties** tab, from the **Handler** dropdown, select **New Client Action**.

    ![Creating an OnSelect event client action for the Month Picker widget](images/monthpicker-client-action-ss.png "Creating a Client Action for Month Picker")

1. To access the month selected by the user, create an **Assign** and set the **MonthPicked** to **SelectedMonth**.

    ![Adding an Assign to set the 'MonthPicked' variable to 'SelectedMonth' in the client action](images/monthpicker-assign-ss.png "Adding an Assign to Client Action")

1. You can configure the Month Picker by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties.

    ![Configuring the Month Picker properties in Service Studio](images/monthpicker-properties-ss.png "Setting Properties for Month Picker")

After following these steps and publishing the module, you can test the pattern in your app.

![Final result showing the Month Picker implemented in an application](images/monthpicker-result.png "Month Picker Result")

## Properties

| Property  | Description  |
|---|---|
|DateFormat (Text): Optional | Defines the input date format. If empty, the date format will be the same as the server format.<br/>When using formats with time, make sure to set the TimeFormat property.<br/><br/>Here are some of the examples that you can use: <ul><li>"MM/YYYY" -> 03/2022</li><li>"MMM YYYY" -> Mar 2022</li><li>"MMM-YYYY" -> Mar-2022</li><li>"MMM.YYYY" -> Mar.2022</li><li>"MMM, YY" -> Mar, 22</li></ul>|
|InitialMonth (MonthYear): Optional | Defines the initial selected month and year for the Month Picker. If not set, no initial month is selected.|  
|MinMonth (MonthYear): Optional| Defines the minimum month that can be selected. Any month before this is disabled and cannot be selected.|
|MaxMonth (MonthYear): Optional | Defines the maximum month that can be selected. Any month after this is disabled and cannot be selected.|
|ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples: <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet).  |

## Events

|Event| Description  |
|---|---|
|Initialized: Optional  | Event triggered after the MonthPicker instance is ready. |
|OnSelected: Mandatory  | Event triggered when the user selects a month.  |
