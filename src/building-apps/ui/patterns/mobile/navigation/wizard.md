---
tags: ide usage, reactive web apps, tutorials for beginners, ui pattern implementation, step-by-step guides
summary: OutSystems 11 (O11) features a Wizard UI Pattern for simplifying complex tasks into manageable steps.
locale: en-us
guid: 133fb7c1-4365-4a44-85d0-a81abe22458e
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=218:5
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Wizard

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Wizard UI Pattern to split large complex tasks and processes into smaller manageable steps. A wizard presents a series of steps or conditions that the user needs to complete in order to accomplish a goal. Additionally, wizards usually include explicit button navigation to move a step forward or backward. Some wizard examples include software installation wizards and sign-up screens.

![Screenshot of the Wizard UI Pattern in OutSystems Service Studio](images/wizard-2-ss.png "Wizard UI Pattern in Service Studio")

**How to use the Wizard UI Pattern**

The following example demonstrates how you can create a four step Wizard with navigation buttons. The example is made up of the following steps:

* Creating a wizard
* Adding content to the wizard
* Creating the wizard navigation

**Create a wizard**

1. In Service Studio, in the Toolbox, search for `Wizard`.

    The Wizard and Wizard Item widgets are displayed (both of which are required to use this pattern).

    ![Screenshot of the Wizard UI Pattern in OutSystems Service Studio](images/wizard-2-ss.png "Wizard UI Pattern in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Wizard widget into the Main Content area of your application's screen.

    ![Default Wizard widget containing three Wizard Item widgets in Service Studio](images/wizard-3-ss.png "Default Wizard Widget with Three Steps")

    By default, the Wizard widget contains three Wizard Item widgets. Each Wizard Item represents a step. You can add or delete Wizard Items as required.

1. From the Toolbox, drag another Wizard Item into your Wizard Pattern.

    ![Dragging a new Wizard Item into the Wizard Pattern in Service Studio](images/wizard-4-ss.png "Adding a Wizard Item to the Wizard Pattern")

1. Drag the Text widget into the Icon placeholders, and enter the numbers 1-4 consecutively.

    ![Entering numbers 1 to 4 into the Icon placeholders of the Wizard Pattern](images/wizard-5-ss.png "Numbering Wizard Steps")

1. Enter the following text to each of the Label placeholders:

    * Shopping Details
    * Payment Details
    * Review Order
    * Confirm Order

    ![Labels for Wizard steps: Shopping Details, Payment Details, Review Order, Confirm Order](images/wizard-6-ss.png "Labeling Wizard Steps")

1. From the Element tree, create an Input Parameter by right-clicking on your screen, and from the drop-down, select **Add Input Parameter**.

    The input parameter controls which Wizard step is shown to the user.

    ![Creating an Input Parameter for controlling Wizard steps in Service Studio](images/wizard-7-ss.png "Creating an Input Parameter in Service Studio")

1. On the **Properties** tab, set the Input Parameter properties as follows:

    * Name: CurrentStep
    * Data Type: Integer
    * Is Mandatory: No
    * Default Value: 1

    ![Configuring properties of the CurrentStep Input Parameter with a default value of 1](images/wizard-8-ss.png "Setting Input Parameter Properties")

    By setting the **Default Value** to 1, you ensure that the  Wizard always starts on step 1.

1. To create the logic that defines the status of each Wizard Item (as an active step, a past step, or a next step), select the first Wizard Item (step 1), and on the **Properties** tab, from the **Status** drop-down, select **Expression Editor**.

    ![Selecting the status of the first Wizard Item in the Properties tab](images/wizard-9-ss.png "Selecting Wizard Item Status")

1. In the expression editor, enter the following expression and click **Close**:

    `If(CurrentStep = 1, Entities.Steps.Active,If(CurrentStep > 1, Entities.Steps.Past, Entities.Steps.Next))`

    ![Expression editor with logic to define the status of Wizard steps based on CurrentStep](images/wizard-10-ss.png "Defining Wizard Step Status Logic")

    This logic has the following meaning:

    * If the user is on step 1, the step is displayed as the active step in the wizard.
    * If the user is on a step greater than step 1, step 1 is displayed as a step that is in the past (completed).
    * If the user is on a step less than 1, the step is displayed as an upcoming (next) step.

1. Repeat steps 8 and 9 for all of the Wizard Items. Replace the number 1 in the expression with 2, 3, and 4 respectively.

**Add content to the wizard**

1. From the Toolbox, drag the If widget onto the main content area of your application's screen, just below the Wizard Pattern.

    ![Dragging an If widget onto the main content area below the Wizard Pattern](images/wizard-11-ss.png "Adding an If Widget Below the Wizard Pattern")

1. On the **Properties** tab, from the **Condition** dropdown, select Expression Editor, enter the following logic and click **Close**:

    `CurrentStep = 1`

    ![Setting a condition in the Properties tab to control the display of Wizard steps](images/wizard-12-ss.png "Setting Condition for Wizard Step Display")

    You have now created a condition that controls what's displayed on screen when the step is active.

1. Repeat steps 1 and 2 for all of the Wizard Items. Replace the **Condition** logic with 2, 3, and 4 respectively.

1. In the top section (True) of the If widget, create the relevant content for each of the steps.

    The following example shows a Shipping Details step that contains labels and input boxes.

    ![Example of Shipping Details step with labels and input boxes in the Wizard Pattern](images/wizard-13-ss.png "Shipping Details Step Content")

**Create the wizard navigation**

1. From the Toolbox, drag two Button widgets onto your screen.

1. On the **Properties** tab, in the **Name** property, enter a name for each of the buttons (in this example, Previous and Next).

1. To ensure that all of the information the user enters is passed from step to step, create a [action](../../../../logic/actions.md) by selecting the **Next** button, and on the **Properties** tab, from the **OnClick** drop-down, select **New Client Action**.

    ![Setting up a new client action for the Next button in the Wizard navigation](images/wizard-14-ss.png "Creating a New Client Action for Next Button")

1. From the Toolbox, drag the Assign block onto your screen and set the **Variable** property to `CurrentStep` and the **Value** property to `CurrentStep + 1`. This ensures that user inputs are passed from step to step.

    ![Assign block to pass user inputs from one Wizard step to the next](images/wizard-15-ss.png "Passing User Inputs Between Wizard Steps")

1. Repeat steps 3 and 4 for the **Previous** button, setting the **Variable** property to `CurrentStep` and the **Value** property to `CurrentStep - 1`.

1. To display the **Next** button when applicable, select the **Next** button, right-click, and select **Enclose in If**.

    ![Enclosing the Next button in an If widget to control its display based on the current step](images/wizard-16-ss.png "Enclosing Next Button in If Widget")

1. On the **Properties** tab, in the **Condition** property, enter the following:

    `CurrentStep < 4`

    ![Setting a condition to ensure the Next button is displayed only for steps 1 to 3](images/wizard-17-ss.png "Condition for Displaying Next Button")

    You have now created a condition that ensures that the user can never go above the number of steps in the wizard.

1. Repeat steps 6 and 7 for the **Previous** button. Enter `CurrentStep > 1` as the **Condition** logic. This ensures the **Previous** button is only displayed when applicable, and the user can never go below the number of steps in the wizard.

After following all of the steps in each of the sections, you can publish the module, and test the Wizard in your app.

## Properties

### Wizard

| Property| Description|
|---|---|
| IsVertical (Boolean): Optional | If True the wizard is displayed vertically. If False, the wizard is displayed horizontally. This is the default.|
| ExtendedClass (Text): Optional | <p>Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added. This is the default.</li><li>_"myclass"_ - adds the _myclass_ style to the UI styles being applied</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |

### Wizard Item

| Property| Description|
|---|---|
| Status (Step Identifier): Mandatory | <p>Set the status of the Wizard Item relative to the current step of the Wizard. You can customize an expression to set the status of the Wizard Item or you can use the predefined values Active, Next, and Past. </p><p>Examples <ul><li>_Entities.Step.Active_ - Sets the Wizard Item to active, that is, the current step the user is on.</li><li>_Entities.Step.Next_ - Sets the Wizard Item to incomplete, that is, a step that is yet to be completed by the user.</li><li>_Entities.Step.Past_ - Sets the step to inactive, that is, a step that has already been completed by the user.</li></ul></p> |
| UseTopLabel (Boolean): Optional     | If True, the label (text describing the step) is placed above the icon. If False, the label is placed below the icon. This is the default.|
| ExtendedClass (Text): Optional      | <p>Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.</p> <p>Examples <ul><li>Blank - No custom styles are added. This is the default.</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet).|

<div class="info" markdown="1">

To ensure that all elements in the list are correctly fetched, for any List used inside a Wizard with WizardItems you must deactivate the [virtualization](../../../../../ref/lang/auto/servicestudio-plugin-nrwidgets-list.md). To do this, set the List attribute value to ``disable-virtualization=True``.

</div>

## Accessibility – WCAG 2.2 AA compliance

By default, the Wizard UI pattern requires a small update to fully comply with WCAG 2.2 AA standards. You must manually update it to fix the following issues:

* Incorrect use of `aria-label` on Wizard items, and missing `aria-hidden` on icon wrappers.  

* Wizard steps don’t have the correct roles when navigating panels. Each step should be associated with a container that has the `tabpanel` role.  

* Wizard steps used as a progress tracker don’t expose the active state properly. The current step should use `aria-current="step"` to inform assistive technologies.  

Updating the Wizard ensures accessible names and roles are correctly exposed, improving support for screen readers and voice commands.

### Fix redundant labels and icon exposure

1. In Service Studio, go to the **Interface** tab.  

1. Select the Screen or Block where the Wizard is used.  

1. In the **Screen** or **Block** properties, select the **OnReady** event. A Client Action is created.

    ![Screenshot showing how to create an OnReady action](images/wizard-onready-ss.png "Selecting OnReady Event")

1. In the **OnReady** Client Action, drag a **JavaScript** node to the flow, from the left panel.  

    ![Screenshot showing how to add a Javascript nodean OnReady action](images/wizard-addemptyjsnode-ss.png "Selecting OnReady Event")

1. Add the following script to remove `aria-label` from Wizard items and hide the icon wrapper from screen readers:  

    ```
    const wizardItems = document.querySelectorAll(".wizard-wrapper-item");

    wizardItems.forEach(item => {
        item.removeAttribute("aria-label");

        const wizardItemIcon = item.querySelector(".wizard-item-icon-wrapper");
        if (wizardItemIcon) {
            wizardItemIcon.setAttribute("aria-hidden", "true");
        }
    });

    ```

1. Click **Done**, then publish the module, and test it.

### Fix Wizard roles and states

There are two ways to fix the Wizard, depending on how it’s used.

### Option 1 Wizard steps navigate between panels

1. In Service Studio, go to the **Interface** tab.  

1. Select the Screen or Block where the Wizard is used.  

1. In the **Screen** or **Block** properties, select the **OnReady** event. A Client Action is created.  

1. In the **OnReady** Client Action, drag a **JavaScript** node to the flow, from the left panel.

1. Add the following script to assign the `tabpanel` role to each Wizard item:  

    ```
    const wizardItems = document.querySelectorAll(".wizard-wrapper-item");

    wizardItems.forEach(item => {
        item.setAttribute("role", "tabpanel");
    });
    ```

    ![Screenshot showing how to add code in JS node](images/wizard-addroletabpanel-ss.png "Adding code to JS node")

1. Click **Done**, then publish the module, and test it.

### Option 2 Wizard steps act as a progress tracker

If the Wizard is only a progress tracker, it should be implemented as a non-interactive list.

1. In Service Studio, go to the **Interface** tab.  

1. Select the Screen or Block where the Wizard is used.  

1. In the **Screen** or **Block** properties, select the **OnReady** event. A Client Action is created.

1. In the **OnReady** Client Action, drag a **JavaScript** node to the flow, from the left panel.

1. Add the following script to assign `aria-current="step"` to the active Wizard item:  

    ```javascript
    const wizardItems = document.querySelectorAll(".wizard-wrapper-item");
    wizardItems.forEach(item => item.removeAttribute("aria-current"));
    const activeItem = document.querySelector(".wizard-wrapper-item.active");
    if (activeItem) {
        activeItem.setAttribute("aria-current", "step");
    }
    ```

1. Click **Done**, publish the module, and test the Wizard.

<div class="info" markdown="1">

This example uses the OnReady action for simplicity.  
If the step changes dynamically, for example, when clicking a button and the page doesn’t reload, extend this logic to run both OnReady and on the OnClick or Event that triggers the change.

</div>

### Result

After you apply these updates, the Wizard becomes more accessible and works correctly with screen readers:

* Screen readers no longer announce redundant or incorrect labels, since `aria-label` is removed from Wizard items and the icon wrapper is hidden.

* For navigational Wizards, each panel is announced correctly with the **tabpanel** role.

* For progress-only Wizards, the current step is announced correctly using **aria-current="step"**.

Test the Wizard in your app to confirm the update.
