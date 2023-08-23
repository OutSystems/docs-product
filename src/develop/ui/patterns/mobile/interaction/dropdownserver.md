---
tags: runtime-mobileandreactiveweb;
summary: The Dropdown Server Side UI Pattern offers a choice of available options that the user can search. This version of the dropdown block has no logic functionality, leaving the logic to be fully implemented by the developers.
locale: en-us
guid: 8B9A073C-74E8-4019-84DE-C686AAFAC59A
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=3562%3A27976&mode=design&t=bjGuZjSEF5sQNURT-1
---

# Dropdown Server Side

The Dropdown Server Side is an advanced OutSystems UI pattern. It has a highly customizable structure for creating tailor-made dropdowns. This pattern is intended to achieve complex use cases. For a further look at how the Dropdown Server Side pattern works, see the [OutSystems Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/PatternDetail?MenuCategoryId=8&MenuSubCategorId=90).

## When to use it?

This block is recommended when you want to:

* **Display long lists of options.** In this case, it is recommended to fetch data when needed instead of having all data in memory and the component is prepared for this case. With this component, you will have total control over when data is loaded. 

* **Customize the look and feel of dropdown options.** The structure of the component can be changed in the canvas of Service Studio. For each of the dropdown items, you can drag and drop additional elements such as images, checkboxes, or text. Additionally, you can apply all the logic you need to customize the behavior of the dropdown. 


## How to use the Dropdown Server Side UI Pattern

In this example, we create a Dropdown Server Side for a list of employees with a corresponding image. 

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

1. To fetch the data to your screen, select and right-click your screen name, and select **Fetch Data from Database**.

    ![Fetch database](<images/dropdownserver-db-ss.png>)

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant database entity and click **Select**.

    In this example, we select the **Sample_Employee** entity.

    ![Add database entity](<images/dropdownserver-aggregate-ss.png>)

    The **GetEmployees** aggregate is automatically created.

    ![Get Employee Aggregate](<images/dropdownserver-getemployee-ss.png>)

1. Return to your screen by double-clicking the screen name. Select the **Dropdown Server Side** widget, and inside the **BallonContent** placeholder, set the list **Source** to **GetEmployees List**.  This populates the dropdown options with a list of employees.

    ![Navigate to List](<images/dropdownserver-list-ss.png>)

1. To display the employee name in the dropdown, expand the **DropdownServerSideItem**, and inside the **DropdownItemContent**, set the expression value as **GetEmployees.List.Current.FirstName + GetEmployees.List.Current.LastName**.

    ![Enter logic for Dropdown Item ](<images/dropdownserver-itemcontent-ss.png>)

1. To add images to each dropdown item, drag and drop an **Image** widget from the Toolbox to the **DropdownItemContent** placeholder, next to the **Expression** widget.

    ![Add Image widget](<images/dropdownserver-image-ss.png>)

1. Set the image **Type** parameter to **Binary Data** and set the **Image Content** parameter to **GetEmployees.List.Current.Picture** (the employees picture).

    ![Set image properties](<images/dropdownserver-imageprop-ss.png>)

1. To change the image shape to a circle, set the **Style Classes** parameter to **"img-circle"**.

After following these steps and publishing the module, you can test the pattern in your app. 

**Note**: Because this pattern is so customizable, not all features of the widget are used in this example and show up as errors. You can delete all unused elements/parameters of the widget. In this example, we don't use the search feature. For that reason, the elements inside **BalloonSearchInput** and **BalloonSearchInputIcon** are removed to avoid errors.

The results from this example should look something like the following:

![Result](<images/dropdownserver-result.png>)

### Save the selected option in a local variable

The following steps demonstrate how you can save the selected dropdown option and display it in a message on screen. 

1. Return to your main screen, add a local variable called **SelectedValue** and set the **Data Type** to **DropdownItem**. 

    ![Create a local variable](<images/dropdownserver-selectedvalue-ss.png>)

    This variable is used to save the **DropdownServerSide** selected value. 

1. On the **Widget Tree** tab,  expand the **List**, and select the **DropdownServerSideItem**. In the **ItemId** field, enter **GetEmployees.List.Current.Sample_Employee.Id**.

    ![Set the Item Id](<images/dropdownserver-itemid-ss.png>)

1. Select the **DropdownServerSideItem** and staying on the **Properties** tab, on the **OnSelected** event, from the **Handler** dropdown, select **New Client Action**.

    ![Add client action](<images/dropdownserver-clientaction-ss.png>)

1. Add an **Assign** node to the client action and assign the following values:
    * ``SelectedValue.Text`` to ``GetEmployees.List.Current.Sample_Employee.FirstName + GetEmployees.List.Current.Sample_Employee.LastName``
    * ``SelectedValue.Value`` to ``GetEmployees.List.Current.Sample_Employee.Id``

    ![Add logic to Assign](<images/dropdownserver-assign-ss.png>)

1. Add a **Message** to the client action and add the following logic to the expression editor:

    ``SelectedValue.Text + "(Employee ID: " + SelectedValue.Value + ")"``

    ![Add logic to Message](<images/dropdownserver-message-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. The results from this example should look something like the following:

![Add logic to Message](<images/dropdownserver-selectedval-result.png>)

## Properties

### Dropdown Server Side

| Property  | Description  | 
|---|---|
|AllowMultipleSelection (Boolean): Optional|If True, users can select multiple options. If False, users can only select one option. This is the default. <br/>If AllowMultipleSelection is False, the dropdown automatically closes after the user picks an option, otherwise it remains open.| 
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
