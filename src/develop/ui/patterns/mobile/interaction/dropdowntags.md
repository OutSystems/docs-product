---
tags: runtime-mobileandreactiveweb;
summary: The Dropdown Tags UI Pattern offers multiple choice options to the user when using a dropdown search.
---

# Dropdown Tags

The Dropdown Tags UI Pattern offers multiple choice options to the user when when using a dropdown search.

![](<images/dropdowntags-1-ss.png>)

**How to use the Dropdown Tags UI Pattern**

In this example, we create a dropdown tags search for a list of application users and a message that displays the number of selected items.

1. In Service Studio, in the Toolbox, search for `Dropdown Tags`.

    The Dropdown Tags widget is displayed.

    ![](<images/dropdowntags-2-ss.png>)

1. From the Toolbox, drag the Dropdown Search widget into the Main Content area of your application's screen.

    ![](<images/dropdowntags-3-ss.png>)

1. Select and right-click your screen name, and select **Fetch Data from Database**.

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant database entity and click **Select**.

    In this example, we select the User entity. 

    ![](<images/dropdowntags-4-ss.png>)

    The **GetUser** aggregate is automatically created.

    ![](<images/dropdowntags-5-ss.png>)

1. Return to your screen by double-clicking the screen name, select the Dropdown Tags widget, and on the **Properties** tab, set the mandatory properties (ItemList, Value, Text).

    ![](<images/dropdowntags-6-ss.png>)

1. Staying on the **Properties** tab, from the **Handler** dropdown, select **New Client Action**.

1. Add the relevant logic to the client action. 

    In this example, we add a Message to the client action and in the Expression Editor enter the following logic and click **Close**. This will display the the number of items as they are selected.

    `CurrentList.Length`

    ![](<images/dropdowntags-7-ss.png>)

1. You can change the Dropdown Search's look and feel by setting the (Optional) properties on the **Properties** tab.

    ![](<images/dropdowntags-8-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. The result of this example should look something like the following:

![](<images/dropdowntags-9-ss.png>)

## Properties

| Property | Description |
|---|---|
| ItemList (DropdownItem List): Mandatory |  List of items to show in the dropdown. |  
| SelectedItemsList (DropdownItem List): Optional | Use this parameter to set preselected items. |  
| IsRemoveItems (Boolean): Optional | If True, the option to remove items is enabled. This is the default. If False, the option to remove items is disabled. |
| IsDisabled (Boolean): Optional | If True, the dropdown search option is disabled. If False, the dropdown search is enabled. This is the default. |
| SearchPrompt (Text): Optional | Text to display on the search prompt/placeholder. "Search" is the default value.|  
| NoResultsText (Text): Optional | Text to display on the search prompt/placeholder. "No results found" is the default value. |
| AdvancedFormat (Text): Optional | Allow for more options beyond what's provided through the inputs. Default value is `{}`. <p> Example</p> `{"searchEnabled": false}`. <p> For more information, visit: [Choices library](https://github.com/jshjohnson/Choices). </p><p>You can also use fuse.js options to change the search configuration. For more information about configurations, visit: [Fuse](https://fusejs.io/) </p> |
| ExtendedClass (Text): Optional | Add custom style classes to the Dropdown Tags UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Dropdown Tags UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Dropdown Tags UI styles being applied.</li></ul> |
