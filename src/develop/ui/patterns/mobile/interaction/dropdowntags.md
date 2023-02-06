---
tags: runtime-mobileandreactiveweb;
summary: The Dropdown Tags UI Pattern offers multiple choice options to the user when using a dropdown search.
locale: en-us
guid: 6b79cc3c-d89b-40df-ba5f-c04038639d4b
app_type: mobile apps, reactive web apps
---

# Dropdown Tags

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

<div class="info" markdown="1">

**This component is deprecated for versions of OutSystems UI lower than 2.8.3.** For more information on how to migrate old versions, see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).

To find out what version of OutSystems UI you are using, see [OutSystems UI version](../../intro.md#outsystems-ui-version).

</div>

The Dropdown Tags UI Pattern offers multiple choice options to the user when when using a dropdown search.

**How to use the Dropdown Tags UI Pattern**

In this example, we create a dropdown tags search for a list of employees and a message that displays the number of selected items.

1. In Service Studio, in the Toolbox, search for `Dropdown Tags`.

    The Dropdown Tags widget is displayed.

    ![Dropdown Tag widget](<images/dropdowntags-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Dropdown Search widget into the Main Content area of your application's screen.

    ![Drag widget to screen](<images/dropdowntags-drag-ss.png>)

1. Select and right-click your screen name, and select **Fetch Data from Database**.

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant database entity and click **Select**.

    In this example, the **Sample_Employee** entity is selected. 

    ![Select database entity](<images/dropdowntags-source-ss.png>)

    The **GetEmployees** aggregate is automatically created.

    ![Aggregate automatically created](<images/dropdowntags-aggregate-ss.png>)

1. Return to your screen by double-clicking the screen name, select the **Dropdown Tags** widget, and on the **Properties** tab, set the mandatory properties (**ItemList**, **Value**, **Text**).

    ![Set mandatory properties](<images/dropdowntags-mandprops-ss.png>)

1. Staying on the **Properties** tab, from the **Handler** dropdown, select **New Client Action**.

    ![Create new client action](<images/dropdowntags-handler-ss.png>)

1. Add the relevant logic to the client action. 

    In this example:
    
    1. Add a Message to the client action.
    1. Add the following logic to the expression editor:

        `CurrentList.Length`

    1. Click **Close**. 
    
        This displays the number of selected items selected.

        ![Add logic](<images/dropdowntags-message-ss.png>)

1. You can configure the Dropdown Tags by selecting the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the **OptionalConfigs** property.

    ![Set properties](<images/dropdowntags-properties-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. The result of this example should look something like the following:

![Dropdown Tag result](<images/dropdowntags-result.png>)

## Properties

|Property|Description|
|---|---|
|OptionsList (DropdownOption List): Mandatory| Defines the list of options to show in dropdown.|
|OptionsList.Value (Text): Mandatory|Defines the items's value.|
|OptionsList.Label (Text): Mandatory|Defines the items's text.|
|OptionsList.ImageUrlOrIconClass (Text): Optional|Defines an image URL or a CSS class. If you define a an image URL, an image is added, otherwise the information is used as a class selector and an icon is added.|
|OptionsList.GroupName (Text): Optional|Defines the name of the group where the item belongs.</br>Use this property to divide the dropdown options into groups. The Group Name appears in the heading of the group.|
|OptionsList.Description (Text): Optional|Defines the text that displays below the option value in the Dropdown options list.</br>Use this property to give more details about the option.|
|StartingSelection (DropdownOption List): Optional|Defines the list of options that appears pre-selected in the Dropdown Tags.</br>The property is static. It is only valid for the initial Dropdown Tags state and is not updated dynamically.|
|StartingSelection.Value (Text): Mandatory|Defines the items's value.|
|StartingSelection.Label (Text): Mandatory|Defines the items's text.|
|StartingSelection.ImageUrlOrIconClass (Text): Optional|Defines an image URL or a CSS class. If you define a an image URL, an image is added, otherwise the information is used as a class selector and an icon is added.|
|StartingSelection.GroupName (Text): Optional|Defines the name of the group where the item belongs.</br>Use this property to divide the dropdown options into groups. The Group Name appears in the heading of the group.|
|StartingSelection.Description (Text): Optional| Defines the text that displays below the option value in the Dropdown options list.</br>Use this property to give more details about the option.|
|Prompt (Text): Optional|Define the text to display when there are no items selected and to serve as an empty value.<br/><br/>The default message is: **Select...** |
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
