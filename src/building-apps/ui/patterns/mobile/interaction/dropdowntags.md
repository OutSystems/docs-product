---
tags: ui patterns, dropdown components, widget configuration, ui development, dependency management
summary: Explore the Dropdown Tags UI Pattern in OutSystems 11 (O11) for enhanced dropdown search functionality in mobile and reactive web apps.
locale: en-us
guid: 6b79cc3c-d89b-40df-ba5f-c04038639d4b
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=213:0
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Dropdown Tags

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

<div class="info" markdown="1">

**This documentation is not valid for deprecated components.** To check if your component is deprecated and how to migrate old versions, see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).

To find out what version of OutSystems UI you are using, see [OutSystems UI version](../../intro.md#outsystems-ui-version).

</div>

The Dropdown Tags UI Pattern offers multiple choice options to the user when using a dropdown search.

**How to use the Dropdown Tags UI Pattern**

In this example, we create a dropdown tags search for a list of employees and a message that displays the number of selected items.

1. In Service Studio, in the Toolbox, search for `Dropdown Tags`.

    The Dropdown Tags widget is displayed.

    ![Screenshot of the Dropdown Tags widget in the Service Studio toolbox](images/dropdowntags-widget-ss.png "Dropdown Tags Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Dropdown Search widget into the Main Content area of your application's screen.

    ![Dragging the Dropdown Tags widget from the toolbox into the main content area of an application screen](images/dropdowntags-drag-ss.png "Dragging Dropdown Tags Widget to Screen")

1. Select and right-click your screen name, and select **Fetch Data from Database**.

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant database entity and click **Select**.

    In this example, the **Sample_Employee** entity is selected. 

    ![Selecting the Sample_Employee database entity for the Dropdown Tags widget](images/dropdowntags-source-ss.png "Selecting Database Entity for Dropdown Tags")

    The **GetEmployees** aggregate is automatically created.

    ![GetEmployees aggregate automatically created after selecting a database entity for Dropdown Tags](images/dropdowntags-aggregate-ss.png "Automatically Created Aggregate for Dropdown Tags")

1. Return to your screen by double-clicking the screen name, select the **Dropdown Tags** widget, and on the **Properties** tab, set the mandatory properties (**OptionsList**, **Value**, **Label**).

    ![Setting the OptionsList, Value, and Label mandatory properties for the Dropdown Tags widget](images/dropdowntags-mandprops-ss.png "Setting Mandatory Properties for Dropdown Tags")

1. From the **Handler** dropdown of the OnChanged event, select **New Client Action**.

    ![Creating a new client action for the Dropdown Tags widget from the properties tab](images/dropdowntags-handler-ss.png "Creating New Client Action for Dropdown Tags")

1. Add the relevant logic to the client action. 

    In this example:
    
    1. Add a Message to the client action.
    1. Add the following logic to the expression editor:

        `CurrentList.Length`

    1. Click **Close**. 
    
        This displays the number of selected items.

        ![Adding logic to display the number of selected items in the Dropdown Tags client action](images/dropdowntags-message-ss.png "Adding Logic to Client Action in Dropdown Tags")

1. To configure the Dropdown Tags, select the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the **OptionalConfigs** property.

    ![Setting optional properties for the Dropdown Tags widget in the properties tab](images/dropdowntags-properties-ss.png "Configuring Optional Properties for Dropdown Tags")

After following these steps and publishing the module, you can test the pattern in your app. The result of this example should look something like the following:

![Final result showing the Dropdown Tags UI pattern in use within an application](images/dropdowntags-result.png "Result of Configured Dropdown Tags")

## Properties

|Property|Description|
|---|---|
|OptionsList (DropdownOption List): Mandatory| Defines the list of options to show in dropdown.|
|OptionsList.Value (Text): Mandatory|Defines the item's value, which specifies the value submitted from the dropdown when you select an option. Examples of what you can define as the item's value are the item's ID, the item's index, etc.|
|OptionsList.Label (Text): Mandatory|Defines the item's label, which is the text displayed on the dropdown.|
|OptionsList.ImageUrlOrIconClass (Text): Optional|Defines an image URL or a CSS class. If you define a an image URL, an image is added, otherwise the information is used as a class selector and an icon is added.|
|OptionsList.GroupName (Text): Optional|Defines the name of the group where the item belongs.<br/>Use this property to divide the dropdown options into groups. The Group Name appears in the heading of the group.|
|OptionsList.Description (Text): Optional|Defines the text that displays below the option value in the Dropdown options list.<br/>Use this property to give more details about the option.|
|StartingSelection (DropdownOption List): Optional|Defines the list of options that appears pre-selected in the Dropdown Tags.<br/>The property is static. It is only valid for the initial Dropdown Tags state and is not updated dynamically.|
|StartingSelection.Value (Text): Mandatory|Defines the item's value.|
|StartingSelection.Label (Text): Mandatory|Defines the item's text.|
|StartingSelection.ImageUrlOrIconClass (Text): Optional|Defines an image URL or a CSS class. If you define a an image URL, an image is added, otherwise the information is used as a class selector and an icon is added.|
|StartingSelection.GroupName (Text): Optional|Defines the name of the group where the item belongs.<br/>Use this property to divide the dropdown options into groups. The Group Name appears in the heading of the group.|
|StartingSelection.Description (Text): Optional| Defines the text that displays below the option value in the Dropdown options list.<br/>Use this property to give more details about the option.|
|Prompt (Text): Optional|Defines the text to display when there are no items selected and to serve as an empty value.<br/><br/>The default message is: **Select...** |
|OptionalConfigs (DropdownTagsOptionalConfigs): Optional | Extra configurations.|
|OptionalConfigs.IsDisabled (Boolean): Optional | Set as True to disable the Dropdown. the default value is False.| 
|OptionalConfigs.NoResultsText (Text): Optional|Defines the text that is displayed when there are no results to show.<br/><br/>The default message is: **There are no options to show.**|
|OptionalConfigs.SearchPrompt (Text): Optional| Defines the prompt text that appears in the search input. <br/><br/>The default message is: **Search...**|
|OptionalConfigs.NoOptionsText (Text): Optional |Defines the message that displays in the Dropdown list when there are no options available.<br/><br/>The default message is: **There are no options to show.**|
|ExtendedClass (Text): Optional| Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet).|

## Events

### Dropdown Tags

|Event| Description| 
|---|---|
|Initialized: Optional | Event triggered after the DropdownTags instance is ready. | 
|OnChanged: Mandatory| Event triggered each time an option is selected.| 
