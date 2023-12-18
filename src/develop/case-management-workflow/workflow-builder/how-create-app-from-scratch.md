---
tags: workflow-builder; case-management; outsystems; business-users; citizen-developers; citizen-dev; workflow
summary: Learn how to create an app from scratch in Workflow Builder.
guid: 23eb1fab-8030-4857-ab70-2e96e1735bc6
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=4376:917
---

# Creating a Workflow Builder app from scratch

<div class="info" markdown="1">

The instructions that follow use the example of creating an expenses approval app.

</div>

To start creating your app from scratch, follow the steps below.

1. On the initial screen, select the **Blank Canvas** option. Workflow Builder then displays a preview about creating apps from scratch.

1. Click on the **Select** button to proceed.

1. Enter the app's basic information:

    * **App name** — the name of the app you are developing.

    * **Description** — a brief description of the outcome of the app.

    * **App icon** — upload an icon for the app that you are about to create.

    * **Main color** — Pick up the color to apply to the main actions (buttons) and menus background on the generated app. If you upload an icon for your app, Workflow Builder selects the main color based on it, for example, your company brand color.

        ![Screenshot showing the customization options for a new app including fields for app name, description, app icon, and main color in Workflow Builder.](images/wfb-blank-canvas.png "Customize your app from scratch")

## Workflow design

Once you fulfill the overall information about the app, you can start designing the workflow.

All applications created in the Workflow Builder start by creating a single request **form** used to gather the required information from your app end users. These forms are the trigger of every workflow, so the first thing to do in your new app is to create a form. For example, if you are building an app to manage expenses from your employees, you need to add the form that they're going to fulfill for the expense request, to trigger the approval process of that particular expense.

![Workflow Builder interface prompting to set up a new form for the app.](images/wfb-setup-form.png "Set up a new form")

## Set up form { #set-up-form }

To create the form to gather information from the end users, follow the steps below.

1. Start by clicking on the **Setup Form** button. In this screen, you can define the request form your end users are going to see. To publish your app, you need to define at least one form field.

    ![Screenshot of the Workflow Builder interface with an option to add a new field to a form.](images/wfb-setup-form-field.png "Adding new field in form")

1. Click on the **+Add a field** button. The **New field** window opens.

1. The **Type** of the field is automatically pre-filled based on the field name, but you can select another one that better fits. Each selected type shows different input parameters, for example, the Dropdown type allows you to add several options for your users to select from:

    * Number
    * Text
    * Currency
    * Date
    * Checkbox
    * Dropdown
    * Database Entity - Read more about using OutSystems database Entities  in the [Using the existing OutSystems database Entities](#use-outsystems-entities) section.
    * File upload

    ![Image showing the new field window in Workflow Builder with different field types like Number, Text, Currency, and others.](images/wfb-form-new-field.png "New form fields")

1. To make a field visible depending on the user inputs, click **Add visible rule** to set the conditions to make it visible. Learn about this feature in the [Adding conditional fields](#add-conditional-fields) section.

1. Click **Save**.

1. To add other fields to your form, repeat steps 2 to 4.

1. To preview your app's form, select the **Preview** button on top of the screen. The form preview opens in a new tab and you can test it by interacting with it.

### Adding conditional fields { #add-conditional-fields }

When building your form, you can choose to make fields visible depending on your user's inputs. To add conditions to a form field, follow these steps:

1. On the **New field** window, enter the field **Label** and **Type**.

1. Click **Add visibility rule**.

    ![Screenshot illustrating how to add a visibility rule to a form field in Workflow Builder.](images/wfb-form-visibility-rule.png "Add visibility rule")

1. From the first **If** dropdown (1), select the field name you want to add to the condition. You must have previously defined other fields in the form.

1. From the second dropdown of the **If** condition (2), select the relevant condition logic, for example, **greater than**.

    ![Image showing the process of setting a condition for a field's visibility in Workflow Builder.](images/wfb-visibility-rule-set-condition.png "Setting the field condition")

1. In the right-hand field (3), enter the value for the rule. In this example, **If** the `Expense [€]` value is **greater than** `50`, then show the `Attach receipt` form field.

    ![Screenshot displaying the final condition set for a field's visibility in Workflow Builder.](images/wfb-visibility-rule-condition.png "Final field condition")

1. Click **Save**.

1. Check if the new fields setting you set are correct. To edit the visibility rule again, click **Edit rule**. To close the field definitions, click **Save**. 

    ![Image of a defined conditional field in Workflow Builder with visibility rules applied.](images/wfb-form-visibility-rule-final.png "Conditional field defined")

1. To test the new conditional field, select the **Preview** button on top of the screen and then interact with the form preview.

    ![Screenshot showing the result of applying a visibility rule to a form field in Workflow Builder.](images/wfb-visibility-rule-applied.png "Visibility rule applied")

### Using the existing OutSystems database Entities { #use-outsystems-entities }

One of the available fields you can add to a form is the **Database entity** field. This field allows you to use public OutSystems Entities you have in your development environment. By reusing existing Entities, you don't need to add all the list items manually to the form.

<div class="info" markdown="1">

To use OutSystems Entities in Workflow Builder apps, your development environment must use Platform Server 11.9 or higher.

</div>

To learn about OutSystems Database Entities, read the [Entities](../../data/modeling/entity.md) document, and watch the [Database Entities](https://www.outsystems.com/learn/lesson/1774/database-entities) lesson from the OutSystems Training.

To use an Entity in a form field, follow these steps:

1. In the **New field** window, from the **Type** drop-down list, select **Database entity**.

1. To browse the existing public Entities in your development environment, click **Browse entity** .

    ![Image of the Workflow Builder interface with options to browse existing OutSystems database entities.](images/wfb-design-browse-entity.png "Browsing existing OutSystems Entities")

1. Select the Module that contains the Entity by clicking the **>** symbol. If you're not sure which module has the Entity you need, ask your IT administrator.

    ![Screenshot showing the selection process of an OutSystems module that contains the desired entity in Workflow Builder.](images/wfb-design-find-entity.png "Finding existing OutSystems Entity Modules")

1. Select the Entity by clicking on the radio button, and then click **Save**.

    ![Image depicting the choice of an OutSystems Entity from a list in Workflow Builder.](images/wfb-design-choose-entity.png "Choosing the OutSystems Entity")

1. From the **Choose attribute** drop-down menu, select the relevant attribute.

    ![Screenshot highlighting the selection of a specific attribute from an OutSystems Entity in Workflow Builder.](images/wfb-design-choose-entity-field.png "Choosing the OutSystems Entity field")

1. Click **Save** to add the new form field.

## Setting the form status { #set-form-status }

The default status of a form when you complete designing it in the workflow is **Submitted**. If you want change the form status, perform the following steps:

1. Click on the **Status** workflow block below the form. 

    The Change status window is displayed.

    ![Image showing the interface for setting the status of a form in Workflow Builder.](images/wfb-set-form-status.png "Setting the form status")

1. From the **Change status to** drop-down, select one of the following options:

    * **Submitted** - default status.
    * **Create new status** — add a new status to the list, for example, **Pending**.
    * **Manage status** — create and manage all the statuses your request has. 

    ![Screenshot of the drop-down menu for selecting the status of a form in Workflow Builder.](images/wfb-design-select-form-status.png "Select the form status")

1. To notify the users (Requesters) who submitted the form about the request status, select the **Send email to requester?** checkbox. You can preview the email by clicking the preview icon.

    ![Image of an email preview in Workflow Builder that is sent to the requester upon form status change.](images/wfb-design-email-preview.png "Email preview")

1. To edit the email, click **Edit email**. 

    You can edit the email by directly typing in the **Subject** and **Message** fields. You can also edit the dynamic fields by choosing a value from the **Dynamic field** drop-down. 

    ![Screenshot showing the email editing interface in Workflow Builder with options to customize the subject and message.](images/wfb-design-edit-email.png "Email edit")

    The dynamic fields are placeholders that allow you to customize the email by automatically inserting the recipients data into these placeholders. In this example, we change the email message and add the **{{Request number}}** dynamic field.

    ![Image of the email editing interface in Workflow Builder with an option to add a new dynamic field to the message.](images/wfb-design-email-edit-dynamic-field-add-dynamic.png "Add new dynamic field")

    ![Screenshot displaying a new email message in Workflow Builder with a dynamic field added to the content.](images/wfb-design-email-edit-dynamic-new-email.png "New email message")

1. Click **Save**.

## Adding steps

Once you have your form created, start adding steps to your workflow.
To add a step, click on the **+ Add step** button.
There are two kinds of steps: Manual task and Condition.
![Workflow Builder showing two types of steps available for adding to the workflow: manual task and condition.](images/wfb-design-step-types.png "Two kinds of steps: manual task and condition")


## Manual tasks { #manual-tasks }

A specific group of people perform tasks manually. Using the example of the employee expenses approval app, a manual task could be the approval step of a manager.

<div class="info" markdown="1">

The Workflow Builder targets simple applications with two to three steps of approval and simple business rules. It supports applications with up to 20 manual tasks with at least one task field per manual task. Workflow Builder can support an unlimited number of manual tasks without task fields.

If your workflow application has more than 20 manual tasks, with at least 1 task field per manual task, we advise building your application in Service Studio using the Case Management framework and Business Process Technology (BPT).

</div>

To define a manual task, perform the following steps:

1. In the **Name** field, enter the task name.

    ![Screenshot of the manual task naming interface in Workflow Builder.](images/wfb-design-manual-task-name.png "Manual task - name")

1. From the **Assign to a group** drop-down menu, select one of the following options:

    ![Image showing the assignment options for a manual task in Workflow Builder, including requester, requester's manager, and specific groups.](images/wfb-design-manual-task-assignment.png "Manual task - assigning to a group")

    * **Requester** - automatically assigns the request to the requester

    * **Requester's manager** — automatically assigns the request to the requester's manager.

    * **&lt;group-name&gt;** — assigns the request to one of the groups already created, where &lt;group-name&gt; is the name of a group.

    * **Create a new group** — defines the group to whom you want to assign the approval of the request, for example, **Managers**.

    * **Manage groups** — creates or deletes groups of users.

    * **Create assignment rule** — sets the assigned user or group dependent on a condition. Check how to [create assignment rules](#create-assignment-rule).

    <div class="info" markdown="1">

    **User groups** are groups of end users with different roles in the hierarchy and may not correspond to groups or teams within your organization. To learn more about user groups refer to [How to set up a Governance Model](how-setup-governance.md) and [How to set up the end users hierarchy](how-setup-end-users-hierarchy.md).

    </div>

1. On the **Send email to assigned group?** menu activate the checkbox if you want to notify all the users of your group about the new request waiting for their action. To preview how the email looks like, click on the preview icon.

1. To notify the users of your group about the new request, select the **Send email assigned group?** checkbox. You can preview the email by clicking the preview icon.

    ![Screenshot of an email preview in Workflow Builder that notifies a group about a new request assigned to them.](images/wfb-design-email-preview-new-request.png "Manual task - email preview")

1. To edit the email, click **Edit email**. 

    You can edit the email by directly typing in the **Subject** and **Message** fields. You can also edit the dynamic fields by choosing a value from the **Dynamic field** drop-down.  

    ![Image of the email editing interface in Workflow Builder for customizing the notification sent to a group about a new request.](images/wfb-design-email-edit-new-request.png "Email edit")
   
### Create assignment rule

While assigning manual tasks to user groups you can set an assignment rule to assign groups at runtime based on form and case fields.

An assignment rule exists only in the context of the manual task for which you created the rule.

1. On the assign group, on the drop down select **Create assignment rule**.

1. Choose the attribute of the **If** rule in the first drop-down list. This is the first logical operand.

1. Choose the logical operator from the second drop-down list. These conditions vary according to the data type of the field you chose in the previous step.

1. Write or choose the value in the third drop-down list. The available options change according to the previous field. This is the second logical operand.

1. If needed you can add another logical expression to the **If** rule by selecting **And** and repeating steps 2 to 4.

1. In the drop-down following **assign to**, choose the user or group of users to assign to the task if the rule is true.

    **Note**: You cannot assign the task to the Requester.

    ![Screenshot showing an example of an assignment rule in Workflow Builder where a task is assigned based on a condition.](images/wfb-design-assign-rule.png "Example of an assignment rule")

1. If needed add another **If** rule, by selecting **+If**, and then following steps 2 to 6 to define the rule and assignment.

1. In the drop-down following **Else assign to**, choose the user or group of users to assign to the task if the rules are all false.

From this point on, the manual task is automatically assigned to the group that fulfills the condition you defined.
You can edit existing rules at any time.

### Adding fields to tasks

While configuring a **Manual task**, you can add fields to the task. These fields apply to that specific manual task only. Once you generate your app, these fields are shown in the task's detail screen.

Manual tasks are only executable by specific groups of users, meaning that only the users belonging to these groups can deal with the request, and consequently have access to these fields.

To add fields to a manual task, perform the following steps.

1. In the **Manual task**, click **+Add field**.

1. In the **Manual task form** screen, click **+Add a field**.

1. In the **New field** window, set the **Label** of the field.

1. The **Type** of the field is automatically pre-filled based on the **Label** set in the previous step. You can change the field type to one of the following types:

    * Number
    * Text
    * Currency
    * Date
    * Checkbox
    * Dropdown
    * Database entity - Read more about using OutSystems database Entities  in the [Using the existing OutSystems database Entities](#use-outsystems-entities) section.
    * File upload

    Each type you select shows different input parameters. For example, choosing the **Dropdown** type allows you to add several options for your users to select from.

1. If the field is mandatory, turn on the **Required** field switch.

1. Click **Save**.

1. To add other fields to your form, repeat steps 3 to 6 .

1. To preview the fields you added to the manual task, select **Preview**. The task's details screen preview opens in a new tab and you can test it by interacting with it.

Using the example of the employee expense approval, this field could be a **Required** field for managers to validate the expense submitted by the employees.

## Conditions { #conditions }

Conditions allow you to automate decisions based on attributes. You can set a condition based on an input field and create a decision (rule) based on that. Conditions lead to two different branches:

* One branch that defines what happens if you meet the condition.
* The **Else** branch that defines what happens if you don't meet the condition.

Using the example of the employee expense, you can use a **Condition** to automatically approve expenses lower than a defined value, or require approval from a manager, if exceeding that value.

To define the **Condition**, perform the steps below. You can add more than one rule.

1. Enter the name of the condition.

1. Choose the attribute of the rule in the first drop-down list. This contains the **Status** field by default, and also the [form fields you defined](#setup-form) for each task.

1. Choose the rule from the second drop-down list. These conditions vary according to what you chose in the previous field.

    ![Image of the interface for adding conditions to a workflow in Workflow Builder.](images/wfb-design-add-condition.png "Adding conditions")

1. Write or choose the value in the third drop-down list. The available options change according to the previous field. Some examples:

    * If **Expense** is **greater** than **100...**
    * If **Status** is **equal** to **submitted...**
    * If **Description** contains **hotel...**

1. You can add another rule, selecting the **+If** button below, and defining the new rule as described in the previous steps. The **Else** button isn't clickable. It refers to the workflow branch to run if you don't meet the condition.

1. Click on the **Save** button to save the condition.

After creating a condition the workflow automatically splits into two branches: the true and the false branches.

![Workflow Builder showing the split into two branches after creating a condition: the true and the false branches.](images/wfb-design-condition-branches.png "Condition branches")

For each branch, you need to define the following steps in the workflow. You can add the following tasks:

* **Manual task** — to insert a new manual task
* **Condition** — to add a new condition to the branch
* **Status** — to set a new status
* **Go to...** — to proceed to another destination in your workflow, for example, to one of the existing manual tasks, conditions, or to the form submission.

![Workflow Builder interface showing options for adding manual tasks to the middle of the workflow.](images/wfb-design-add-manual-task-workflow.png "Adding manual tasks to the middle of the workflow")

All branches of a workflow finish with an **End** green icon.

Once you finish your app workflow, you can **Publish** and test it.

To learn how to publish and test your Workflow Builder app, go to [Publishing and testing your app](publish-test.md).

## Parallel flows { #parallel-flow }

A parallel flow is a process modeling capability that allows multiple paths with activities to be executed in parallel, but always within the same case instance.

A sequential flow ends when all tasks in the process are complete.

![Diagram illustrating the concept of sequential and parallel flows in Workflow Builder.](images/sequential-parallel-flow-wb.png "Sequential parallel flow diagram")

When a parallel flow is executed, the sequence of activities in each parallel path is executed independently. 

![Diagram showing a parallel flow with independent paths being executed simultaneously in Workflow Builder.](images/parallel-flow-wb.png "Parallel flow diagram")  

You can define when a parallel flow ends, for example, when all branches are complete or when a specific branch finishes before the rest. This option means when that specific branch completes, the main flow continues.

![Workflow Builder interface with options to select when a parallel flow ends.](images/branch-ends-wb.png "Select when parallel flow ends")

Workflow Builder allows you to create parallel flows. The following diagram shows parallel branches being used for an employee onboarding request where the IT manager and the facilities manager have parallel tasks to complete at the same time. 

![Workflow Builder diagram showing parallel branches used for an employee onboarding request.](images/parallel-branches-employee-onboarding-wb.png "Example employee onboarding example")

## Creating a parallel flow

1. From the main canvas, click **+Add Step**, and select **Parallel branches**.

    ![Image showing the option to add a parallel branch to a workflow in Workflow Builder.](images/parallel-branch-wb.png "Add parallel branch")

1. In the **Parallel branches** popup, click **Add branch**.

    ![Screenshot of the 'Add branch' button in Workflow Builder for creating new branches in a parallel flow.](images/add-branch-wb.png "Add branch")

    **Note**: You can add a maximum of 4 branches to a branch flow. Adding  a new branch allows you to delete an existing branch. For each branch, you can add a manual task, a condition, a status, or a go to action. Adding a go to action allows you to proceed to another destination within the parallel flow. If you add a go to action after a condition or a parallel flow, you can only proceed to a manual task.  If you add a go to action after a manual task, you can proceed to another manual task, form submission, a condition, or another parallel flow.

    ![Image of the 'Go To' action in Workflow Builder that allows proceeding to another destination within the workflow.](images/go-to-wb.png "Go To action")

1. Enter a name for the branch flow and a name for each branch, then click **Save**.

1. Click the **Go back to main workflow** button.

    The new parallel flow is displayed on the main canvas.

    ![Screenshot showing a new parallel flow added to the main workflow canvas in Workflow Builder.](images/new-parallel-flow-wb.png "New parallel flow")

### Deleting a parallel flow

1. From the main canvas, select the parallel flow you want to delete.

    ![Image highlighting the selection of a parallel flow in Workflow Builder for deletion.](images/select-parallel-flow-delete-wb.png "Select parallel to delete")

1. Click the Delete icon.

    ![Screenshot showing the delete icon being clicked to remove a parallel flow from a workflow in Workflow Builder.](images/delete-parallel-flow-wb.png "Click delete icon")

1. Click the **Yes, delete** button.

    ![Image of the confirmation dialog with the 'Yes, delete' button to confirm the deletion of a parallel flow in Workflow Builder.](images/confirm-delete-wb.png "Click delete button")
