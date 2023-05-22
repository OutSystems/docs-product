---
tags: runtime-mobileandreactiveweb;
summary: The Dropdown Server Side UI Pattern offers a choice of available options that the user can search. This version of the dropdown block has no logic functionality, leaving the logic to be fully implemented by the developers.
locale: en-us
guid: 8B9A073C-74E8-4019-84DE-C686AAFAC59A
app_type: mobile apps, reactive web apps
platform-version: o11
---

# Dropdown Server Side

The Dropdown Server Side UI Pattern offers a choice of options that the user can search for. You must implement the logic functionality for this version of the Dropdown block as it comes with no preloaded logic.

## How to use the Dropdown Server Side UI Pattern

In this example, we create a Dropdown Server Side for a list of employees. When the user selects an employee, a message displays the employee's name and ID.

1. In Service Studio, in the Toolbox, search for `Dropdown Server Side`.

    The Dropdown Server Side widget is displayed.

    ![Dropdown Server Side widget](<images/dropdownserver-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Dropdown Server Side widget into the Main Content area of your application's screen.

    ![Drag widget to the screen](<images/dropdownserver-drag-ss.png>)

1. Select and right-click your screen name, and select **Fetch Data from Database**.

    ![Fetch database](<images/dropdownserver-db-ss.png>)

1. To add a database entity, click the **Aggregate editor** window, and from the **Select Source** pop-up, select the relevant database entity and click **Select**.

    In this example, we select the **Sample_Employee** entity.

    ![Add database entity](<images/dropdownserver-aggregate-ss.png>)

    The **GetEmployees** aggregate is automatically created.

    ![Get Employee Aggregate](<images/dropdownserver-getemployee-ss.png>)

1. Return to your screen by double-clicking the screen name. Select the **Dropdown Server Side** widget, go to the **Widget Tree** tab, expand **Balloon Content**, and select **List**. 

    ![Navigate to List](<images/dropdownserver-list-ss.png>)

1. On the **Properties** tab, set the list’s source.  

    In this example, we use **GetEmployees.List**.

    ![Enter the List source](<images/dropdownserver-source-ss.png>)

1. Staying on the **Widget Tree** tab, expand the **List**, and select the **DropdownServerSideItem**. In the **ItemId** field, enter **GetEmployees.List.Current.Sample_Employee.Id.**

    ![Enter ItemId](<images/dropdownserver-itemid-ss.png>)

1. To get the employee's name, select the expression inside the **DropdownItemContent** placeholder and enter the following logic:

    ``GetEmployees.List.Current.Sample_Employee.FirstName + " " + GetEmployees.List.Current.Sample_Employee.LastName``

    ![Enter logic for Dropdown Item ](<images/dropdownserver-itemcontent-ss.png>)

1. Select the **DropdownServerSideItem** and staying on the **Properties** tab, from the **Handler** dropdown, select **New Client Action**.

    ![New client action ](<images/dropdownserver-clientaction-ss.png>)

1. Return to your main screen, add a local variable called **SelectedValue**, and set the **Data Type** to **DropdownItem**. 

1. Select the expression inside of the **True** node of the **If** statement inside the **SelectedValues** placeholder and change the **Value** to the **SelectedValue.Text** variable.

    ![Add expression to Selected Value variable](<images/dropdownserver-selectedvalues-ss.png>)

1. Add the relevant logic to the client action.

For this example:

   1. Add an input parameter (in this example, **EmployeeName**) and set the **Data Type** to **Text**. 

       ![Add input parameter to client action](<images/dropdownserver-inputpar-ss.png>)
   
   1. Select the expression inside the **DropDownItem** placeholder and add the following logic in the expression editor: 

        ``GetEmployees.List.Current.Sample_Employee.FirstName + " " + GetEmployees.List.Current.Sample_Employee.LastName``

       ![Add logic to input parameter](<images/dropdownserver-logic-exp-ss.png>)

   1. Add an **Assign** node to the client action and assign the following values:

        * SelectedValue.Text = EmployeeName
    
        * SelectedValue.Value = ItemId

   1. Add a **Message** to the client action.

   1. Add the following logic to the expression editor:

        ``SelectedValue.Text + "(Employee ID: " + SelectedValue.Value + ")"``

        This displays the selected employee's name and ID.

        ![Add a message to the client action](<images/dropdownserver-message-ss.png>)
    
   1. Set the **If** statement inside the **BalloonContent** to **GetEmployees.List.Empty**.

        ![Set Balloon Content If condition](<images/dropdownserver-ballooncontent-ss.png>)

   1. Set the remaining properties for the **DropdownServerSide** placeholders. In this example, they are deleted as they are not needed.

        ![Set remaining properties in placeholders](<images/dropdownserver-placeholders-ss.png>)

   1. Click **Close**.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

### Dropdown Server Side

| Property  | Description  | 
|---|---|
|AllowMultipleSelection (Boolean): Optional|If true, users can select multiple options. If False, users can only select one option. This is the default. <br/>If AllowMultipleSelection is False, the dropdown automatically closes after the user picks an option, otherwise it remains open.| 
|IsDisabled (Boolean): Optional|Set as True to disable the Dropdown. False is the default value (the dropdown is active).| 
|ExtendedClass (Text): Optional|Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet).|

### Dropdown Server Side Item

|Property| Description| 
|---|---|
|ItemId (Text): Mandatory|DropdownServerSide item identifier. | 
|IsSelected (Boolean): Optional| Set to True to allow users to select more than one option.  | 
|ExtendedClass (Text): Optional  | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet).|

## Events

### Dropdown Server Side

|Event| Description  | 
|---|---|
|Initialized: Optional| Event triggered after the DropdownServerSide instance is ready. | 
|OnToggle: Optional| Event triggered each time the DropdownServerSide opens or closes.| 

### Dropdown Server Side Item

|Event| Description  | 
|---|---|
|OnSelected: Mandatory| Event triggered each time the item is clicked. | 


## API - Dropdown Server Side

If you are an advanced user, you might want to use the Accordion API (OutSystems.OSUI.Patterns.DropdownAPI) for more advanced use cases.

### Methods

|Function| Description|Parameters|
|---|---|---|
|ChangeProperty| Changes the property of the Dropdown.|<li>dropdownId: string </li><li>propertyName: string</li><li> propertyValue: any</li>  |
|Clear|Clears any selected values from the Dropdown.| <li>dropdownId: string</li> |
|Create|Creates the new DropdownItem instance and adds it to the dropdownItemsMap.|<li>dropdownId: string </li><li> mode: string </li><li> provider: string </li><li> configs: string</li> |
|Disable|Sets the Dropdown as disabled.|<li> dropdownId: string</li>|
|Dispose|Destroys the instance of the Dropdown.|<li> dropdownId: string</li>|
|Enable|Function that will set Dropdown with given ID as enabled|<li>dropdownId: string</li>|
|GetAllDropDownItemsInScreen|Returns the map with all the Dropdown instances on the page.|<li>Returns array of Ids</li>|
|GetDropdownById|Gets the instance of Dropdown.|<li>dropdownId: string</li>|
|GetSelectedValues|Returns all the selected values from a specific Dropdown Id.|<li>dropdownId: string</li>|
|Initialize|Initializes the pattern instance.|<li>dropdownId: string</li>|
|RegisterCallback|Registers a provider callback.|<li>dropdownId: string</li><li>eventName: string</li><li>callback: OSUIFramework.Callbacks.OSGeneric</li>|
|SetValidation|Sets the validation status to a specific Dropdown Id.|<li>dropdownId: string</li><li>isValid: boolean</li><li>validationMessage: string</li>|


## API - Dropdown Server Side Item

If you are an advanced user, you might want to use the Accordion API (OutSystems.OSUI.Patterns.DropdownServerSideItemAPI) for more advanced use cases.

### Methods

|Function| Description|Parameters|
|---|---|---|
|ChangeProperty| Changes the property of a specific DropdownServerSideItem Id.|<li>dropdownServerSideItemId: string</li><li>propertyName: string</li><li>propertyValue: any</li>  |
|Create|Creates the new DropdownServerSideItemItem instance and adds it to the dropdownServerSideItemItemsMap.|<li>dropdownServerSideItemId: string</li><li>configs: string</li> |
|Clear|Creates the new DropdownItem instance and adds it to the dropdownItemsMap.|<li>dropdownId: string </li><li> mode: string </li><li> provider: string </li><li> configs: string</li> |
|Disable|Sets a Dropdown with a specific ID as disabled.|<li> dropdownServerSideItemId: string</li>|
|Dispose|Disposes the instance of a specific DropdownServerSideItemItem Id.|<li> dropdownServerSideItemId: string</li>|
|GetAllDropdownServerSideItemItemsMap|Sets a Dropdown with a specific ID as enabled.|<li>dropdownId: string</li>|
|GetAllDropDownItemsInScreen|Returns the map with all the DropdownServerSideItem instances on the page.|<li>Returns array of Ids</li>|
|GetDropdownServerSideItemItemById|Gets the instance of DropdownServerSideItem by a specific ID.|<li>dropdownServerSideItemId: string</li>|
|Initialize|Initializes the pattern instance.|<li>dropdownId: string</li>|
|Initialize|Initializes the pattern instance.|<li>dropdownServerSideId: string</li><li>eventName: string</li><li>callback: OSUIFramework.Callbacks.OSGeneric</li>|
