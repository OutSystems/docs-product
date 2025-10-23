---
tags: ui patterns, dropdown implementation, ui design, service studio widgets, dependency management
summary: Explore the Dropdown Search UI Pattern in OutSystems 11 (O11) for enhanced user selection capabilities in mobile and reactive web apps.
locale: en-us
guid: 5dc860b5-4361-4991-8c3a-4ffba28c55ff
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=212:0
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Dropdown Search

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

<div class="info" markdown="1">

**This documentation is not valid for deprecated components.** To check if your component is deprecated and how to migrate old versions, see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).

To find out what version of OutSystems UI you are using, see [OutSystems UI version](../../intro.md#outsystems-ui-version).

</div>

The Dropdown Search UI Pattern offers a choice of available options that the user can search.

**How to use the Dropdown Search UI Pattern**

In this example, we create a dropdown search for a list of employees. When the user selects an employee, a message displays the employee's name and ID.

1. In Service Studio, in the Toolbox, search for `Dropdown Search`.

    The Dropdown Search widget is displayed.

    ![Screenshot of the Dropdown Search widget in the Service Studio toolbox](images/dropdownsearch-widget-ss.png "Dropdown Search Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUI** module and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Dropdown Search widget into the Main Content area of your application's screen.

    ![Dragging the Dropdown Search widget from the toolbox into the Main Content area of the application screen](images/dropdownsearch-drag-ss.png "Dragging the Dropdown Search Widget to the Screen")

1. Select and right-click your screen name, and select **Fetch Data from Database**.

    ![Selecting the Fetch Data from Database option for the Dropdown Search in Service Studio](images/dropdownsearch-fetch-ss.png "Fetching Data from Database for Dropdown Search")

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant database entity and click **Select**.

    In this example, the **Sample_Employee** entity is selected.

    ![Selecting the Sample_Employee database entity for the Dropdown Search data source](images/dropdownsearch-source-ss.png "Selecting Database Entity for Dropdown Search")

    The **GetEmployees** aggregate is automatically created.

    ![Automatic creation of the GetEmployees aggregate after selecting the database entity for Dropdown Search](images/dropdownsearch-aggregate-ss.png "GetEmployees Aggregate Created")

1. Return to your screen by double-clicking the screen name. Select the Dropdown Search widget, and on the **Properties** tab, set the mandatory properties (**OptionsList**, **Value**, **Label**).

    ![Setting the OptionsList, Value, and Label mandatory properties in the Properties tab for Dropdown Search](images/dropdownsearch-logic-ss.png "Setting Mandatory Properties for Dropdown Search")

1. Staying on the **Properties** tab, from the OnChanged event **Handler** dropdown, select **New Client Action**.

    ![Creating a new client action from the OnChanged event handler dropdown for Dropdown Search](images/dropdownsearch-handler-ss.png "Creating a New Client Action for Dropdown Search")

    The **DropdownWidgetId** and **SelectedOptionList** input parameters are automatically generated.

    ![Automatic generation of DropdownWidgetId and SelectedOptionList input parameters for Dropdown Search](images/dropdownsearch-inputparams-ss.png "Dropdown Search Input Parameters")

1. Add the relevant logic to the client action.

    For this example:
    1. Add a **Message** to the client action.
    1. Add the following logic to the expression editor:

        `SelectedOptionList.Current.Label + "(Employee ID: " + SelectedOptionList.Current.Value + ")"`

    1. Click **Close**.

        This displays the selected employee's name and ID.

        ![Adding a message to display the selected employee's name and ID in the Dropdown Search client action](images/dropdownsearch-message-ss.png "Adding Message Logic to Dropdown Search")

1. You can configure the Dropdown Search by selecting the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the OptionalConfigs property.

    ![Configuring optional properties for the Dropdown Search pattern in the Properties tab](images/dropdownsearch-properties-ss.png "Setting Optional Properties for Dropdown Search")

After following these steps and publishing the module, you can test the pattern in your app. The results from this example should look something like the following:

![Example of the Dropdown Search result displaying a list of employees](images/dropdownsearch-result.png "Dropdown Search Result Example")

## Properties

| Property| Description|
|---|---|
|OptionsList (DropdownOption List): Mandatory|Defines the list of options to show in dropdown.|
|OptionsList.Value (Text): Mandatory|Defines the items's value.|
|OptionsList.Label (Text): Mandatory |Defines the items's text.|
|OptionsList.ImageUrlOrIconClass (Text): Optional|Defines an image URL or a CSS class. If you define a URL, an image is added, otherwise the information is used as a class selector and an icon is added.|
|OptionsList.GroupName (Text): Optional|Defines the name of the group where the item belongs.<br/>Use this property to divide the dropdown options into groups. The Group Name appears in the heading of the group.|
|OptionsList.Description (Text): Optional|Defines the text that displays below the option value in the Dropdown options list.<br/>Use this property to give more details about the option.|
|StartingSelection (DropdownOption List): Optional| Defines the list of options that appear pre-selected in the Dropdown Search.<br/>The property is static and is only valid for the initial Dropdown Search state and is not  updated dynamically.|
|StartingSelection.Value (Text): Mandatory|Defines the items's value.|
|StartingSelection.Label (Text): Mandatory|Defines the items's text.|
|StartingSelection.ImageUrlOrIconClass (Text): Optional |Define an image URL or a CSS class. If you define a URL, an image is added, otherwise the information is used as a class selector and an icon is added.|
|StartingSelection.GroupName (Text): Optional|Defines the name of the group where the item belongs.<br/>Use this property to divide the dropdown options into groups. The Group Name appears in the heading of the group.|
|StartingSelection.Description (Text): Optional| Defines the text that displays below the option value in the Dropdown options list.<br/>Use this property to give more details about the option.|
|Prompt (Text): Optional| Defines the text that is displayed when no items are selected and serves as an empty value.<br/><br/>The default message is: **Select...** |
|OptionalConfigs (DropdownOptionalConfigs): Optional |Extra configurations.|
|OptionalConfigs.AllowMultipleSelection (Boolean): Optional|Defines if multiple options can be selected. If True, multiple options can be selected. If False, only one option can be selected. The default value is False.|
|OptionalConfigs.IsDisabled (Boolean): Optional|Set to True to disable the dropdown.|
|OptionalConfigs.NoResultsText (Text): Optional|Defines the text that is displayed when there are no results to show.<br/><br/>The default message is: **There are no options to show.**|
|OptionalConfigs.SearchPrompt (Text): Optional|Defines the prompt text that appears in the search input. <br/><br/>The default message is: **Search...**|
|OptionalConfigs.NoOptionsText (Text): Optional |Defines the message that displays in the Dropdown list when there are no options available.<br/><br/>The default message is: **There are no options to show.** |
|OptionalConfigs.SanitizeDropdownValues (Boolean): Optional |Set true to assure the values inputted in the dropdown will be sanitized or false if you want to explicitly allow custom code to run.<br/>By setting it to true it will replace HTML tags from option's text (value and label) to prevent potential injected code execution.<br/>This option is not enabled by default to avoid performance issues.<br/><br/>**Note:** When using OutSystems UI prior to version 2.23.0 and do not explicitly need to use HTML, ensure that the client action ``SetVirtualSelectConfigs`` is executed in the ``Initialized`` event handler of the Dropdown Search block, with ``enableSecureText = Entities.BooleanTypes.True`` to prevent potential injected code execution.|
|ExtendedClass (Text): Optional| Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples:<br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet).|

## Events

|Event| Description|
|---|---|
|Initialized: Optional| Event triggered after the Dropdown Search instance is ready.|
|OnChanged: Mandatory| Event triggered each time an option is selected.|
