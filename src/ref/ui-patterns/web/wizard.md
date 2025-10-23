---
tags: ui patterns, css customization, web development, outsystems ui, user interface design
summary: Explore the implementation and customization of the Wizard UI Pattern in OutSystems 11 (O11) for enhancing Traditional Web Apps.
locale: en-us
guid: 40d6949b-644d-4bc3-8ed9-83bdbe79fba2
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:633
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Wizard Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout and classes of the Wizard UI Pattern](images/wizard-3-diag.png "Wizard Layout Diagram")

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|--- |
| .wizard |  .wizard.wizard-vertical|  When the wizard orientation is vertical  |
| .wizard-item |  .wizard-item.active|  Defines the current active step  |
| .wizard-item |  .wizard-item.past|  Defines the previous step  |
| .wizard-item |  .wizard-item.next|  Defines the next step  |

## Advanced use case

### Use the Wizard Pattern with ListRecords

1. Drag the Wizard Pattern into the screen.

1. In the Content placeholder, drag a ListRecords widget.

1. Set the Line Separator parameter of the ListRecords to None.

1. In the ListRecords widget, drag a WizardItem Pattern.

1. In the WizardItem Pattern, use expressions to display the database content you need.

1. Publish and test.

### Create a wizard navigation

Use this example to create a three steps Wizard with continue and back buttons.

1. Drag the Wizard Pattern into the page. By default, it comes with three WizardItems.

1. Create a Local Integer Variable, named WizardStepIndex, to hold the current Wizard step.

1. Drag two Button widgets and set their names to Continue and Back.

1. Create a new Screen Action named WizardNavigation.

    ![Screenshot of the Wizard Navigation screen action setup in the development environment](images/wizard-4-ss.png "Wizard Navigation Screen Action")

1. Create a mandatory boolean Input Parameter on this action named IsNext.

1. Drag an Assign and set WizardStepIndex, to `If(IsNext, WizardStepIndex + 1, WizardStepIndex - 1)`.

    ![Screenshot showing the assignment of the WizardStepIndex variable in the Wizard Navigation action](images/wizard-5-ss.png "Wizard Step Index Assignment")

1. Drag an AjaxRefresh to refresh your content container on the screen.

1. Set the OnClick of the Continue Button to the action WizardNavigation with Ajax Submit as the Method. Set the IsNext parameter to True.

1. Do the same for the Back button, but set the parameter to False.

    ![Screenshot of the Wizard UI with Continue and Back buttons configured for navigation](images/wizard-6-ss.png "Wizard Continue and Back Buttons")

1. In each WizardItem, add this If condition: `If(WizardStepIndex = 1, Entities.Step.Active, If(WizardStepIndex = 0, Entities.Step.Next, Entities.Step.Past))` to the Step parameter.

1. Wrap the content containers in Ifs and set the condition to the respective step.

    ![Screenshot demonstrating the custom style applied to the active step in the Wizard UI Pattern](images/wizard-7-ss.png "Wizard Active Step Custom Style")  
    ![Screenshot showing the content containers wrapped in conditional statements for each Wizard step](images/wizard-8-ss.png "Wizard Step Content Containers")

### Custom style for active step

To implement this, you can use either method described below.

* Write the following CSS in the CSS editor and change the `yourcolor`.

        .wizard-item.active .wizard-item-icon {
            border: 2px solid #fff;
            background-color: yourcolor;
            color: #fff;
        }

        .wizard-item.active .wizard-item-icon::after {
            background-color: transparent;
            border-radius: 50%;
            border: 2px solid #fff;
            box-shadow: 0 0 0 1px yourcolor;
            content: '';
            height: 100%;
            position: absolute;
            width: 100%;
        }

* Use CSS variables like `var(--color-yourcolor)`.

        .wizard-item.active .wizard-item-icon {
            border: 2px solid var(--color-neutral-0);
            background-color: var(--color-yourcolor);
            color: var(--color-neutral-0);
        }

        .wizard-item.active .wizard-item-icon::after {
            background-color: transparent;
            border-radius: 50%;
            border: 2px solid var(--color-neutral-0);
            box-shadow: 0 0 0 1px var(--color-yourcolor);
            content: '';
            height: 100%;
            position: absolute;
            width: 100%;
        }

    ![Screenshot of the CSS code for custom styling the active step in the Wizard UI Pattern](images/wizard-9-ss.png "Wizard Custom Style CSS Code")
