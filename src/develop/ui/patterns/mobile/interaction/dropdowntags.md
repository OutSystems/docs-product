---
tags: runtime-mobileandreactiveweb;
summary: The Dropdown Tags UI Pattern offers multiple choice options to the user when using a dropdown search.
locale: en-us
guid: 6b79cc3c-d89b-40df-ba5f-c04038639d4b
---

# Dropdown Tags

<div class="info" markdown="1">

If you are using an OutSystems UI version lower than 2.8.2, please see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).

</div>

The Dropdown Tags UI Pattern offers multiple choice options to the user when when using a dropdown search.

**How to use the Dropdown Tags UI Pattern**

In this example, we create a dropdown tags search for a list of employees and a message that displays the number of selected items.

1. In Service Studio, in the Toolbox, search for `Dropdown Tags`.

    The Dropdown Tags widget is displayed.

    ![Dropdown Tag widget](<images/dropdowntags-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

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
|OptionsList (DropdownTagsOption List): Mandatory |  List of items to show in the dropdown. |  
|SelectedOptions (DropdownTagsOption List): Optional | Defines preselected items in the dropdown list. |  
|Prompt (Text): Optional | Text that is displayed when no items are selected. |
|OptionalConfigs.IsDisabled (Boolean): Optional |Set as True to disable the Dropdown. |
|OptionalConfigs.NoResultsText (Text): Optional |Text that is displayed when there are no results to show.|
|OptionalConfigs.SearchPrompt (Text): Prompt text displayed in the search input box.|  
|ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
