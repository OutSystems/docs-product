---
tags: runtime-mobileandreactiveweb;
summary: The Dropdown Search UI Pattern offers a choice of available options that the user can search.
locale: en-us
guid: 5dc860b5-4361-4991-8c3a-4ffba28c55ff
app_type: mobile apps, reactive web apps
---

# Dropdown Search

<div class="info" markdown="1">

Applies only to Mobile Apps and Reactive Web Apps

</div>

<div class="info" markdown="1">

If you are using an OutSystems UI version lower than 2.8.2, please see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).

</div>

The Dropdown Search UI Pattern offers a choice of available options that the user can search. 

**How to use the Dropdown Search UI Pattern**

In this example, we create a dropdown search for a list of employees. When the user selects an employee, a message displays the employee's  name and ID.

1. In Service Studio, in the Toolbox, search for `Dropdown Search`.

    The Dropdown Search widget is displayed.

    ![Dropdown Search widget](<images/dropdownsearch-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Dropdown Search widget into the Main Content area of your application's screen.

    ![Drag the widget to the screen](<images/dropdownsearch-drag-ss.png>)

1. Select and right-click your screen name, and select **Fetch Data from Database**.

    ![Fetch data from database](<images/dropdownsearch-fetch-ss.png>)

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant database entity and click **Select**.

    In this example, the **Sample_Employee** entity is selected. 

    ![Select database entity](<images/dropdownsearch-source-ss.png>)

    The **GetEmployees** aggregate is automatically created.

    ![The GetEmployees aggregates is automatically created](<images/dropdownsearch-aggregate-ss.png>)

1. Return to your screen by double-clicking the screen name. Select the Dropdown Search widget, and on the **Properties** tab, set the mandatory properties (**OptionsList**, **Value**, **Label**).

    ![Set the mandatory properties](<images/dropdownsearch-logic-ss.png>)

1. Staying on the **Properties** tab, from the OnChanged event **Handler** dropdown, select **New Client Action**.

    ![Create a new client action](<images/dropdownsearch-handler-ss.png>)

1. Add the relevant logic to the client action. 

    For this example:
    1. Add a **Message** to the client action.
    1. Add the following logic to the expression editor:

        `SelectedItem.Text + "(Employee ID: " + SelectedItem.Value + ")`

    1. Click **Close**. 
    
        This displays the selected employee's name and their ID.

        ![Add message logic](<images/dropdownsearch-message-ss.png>)

1. You can configure the Dropdown Search by selecting the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the OptionalConfigs property.

    ![Set optional properties](<images/dropdownsearch-properties-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. The results from this example should look something like the following:

![Dropdown result](<images/dropdownsearch-result.png>)

## Properties

|Property|Description|
|---|---|
|OptionsList (DropdownSearchOptionList): Mandatory | List of items to show in the dropdown. |
|SelectedOptions (DropdownSearchOption List): Optional| Defines preselected items in the dropdown list.|
|Prompt (Text): Optional|Text that is displayed when no items are selected and serves as an empty value.|
|OptionalConfigs.AllowMultipleSelection (Boolean): Optional|Set to True to allow the selection of multiple options. Default value is False.|
|OptionalConfigs.IsDisabled (Boolean): Optional|Set to True to disable the dropdown.|
|OptionalConfigs.NoResultsText (Text): Optional|Text that is displayed when there are no results to show.|
|OptionalConfigs.SearchPrompt (Text): Optional|Prompt text displayed in the search input box.|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
