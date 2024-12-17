---
summary: Learn to develop a Reactive Web App using OutSystems 11 (O11) by importing data, creating screens, and implementing logic.
tags: ide usage, reactive web apps, tutorials for beginners, database integration, ui development, lifecycle management
locale: en-us
guid: 795332a5-e1f3-40c0-886d-75b7bddf48af
app_type: reactive web apps
platform-version: o11
figma: https://www.figma.com/file/mDMvfanpcaW6fqmEKxjvMQ/Getting%20Started?node-id=67:2
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - platform server
  - lifetime
coverage-type:
  - apply
  - understand
---

# Create Your First Reactive Web App

<div class="info" markdown="1">

Check our training [Becoming a Reactive Web Developer](https://www.outsystems.com/learn/paths/18/becoming-a-reactive-web-developer/) for a guided introduction into Reactive Web App. 

</div>

Developing Reactive Web Apps with OutSystems is fast. In this example, we will use a spreadsheet to create some database entries and then add user interface and logic to connect everything - into a ToDo app.

This is the overview of what we are about to do:

1. Create a Reactive Web App, name it, and choose the primary color.
1. Automatically create a database model by importing data from Excel.
1. Create a Screen that lists the data from the database.
1. Create a Screen to add and update records.
1. Implement functionality to delete records.
1. Test the application in a browser.

## Pre-requisites

You should satisfy the following requirements to develop, run, and deploy a Reactive App.

* Service Studio 11.53.7 or later
* Platform Server 11 - Release Oct.2019.CP1 or later
* LifeTime Management Console - Release Sep.2019 version 11.0.321.0 or later 

We also recommend that you update the following components:

* OutSystems UI
* OutSystems UI Templates Reactive

## Create a Reactive Web App { #new-app }

Let's create a sample "ToDo" app.

1. In Service Studio, select **New Application**.

    ![Screenshot showing the option to select 'New Application' in Service Studio for creating a Reactive Web App](images/select-new-application-ss.png "Select New Application in Service Studio")

1. In the **New Application** window, choose **From scratch**, then click **Next**.

    ![Screenshot of the 'New Application' window with the 'From scratch' option highlighted](images/start-from-scracth-ss.png "Start From Scratch Option")

1. Choose **Reactive Web App**, then click **Next**.

    ![Screenshot displaying the selection of 'Reactive Web App' option during the new application setup](images/select-reactive-web-app-ss.png "Select Reactive Web App Option")

1. In the properties for your new app, set up the following: 
    
    1. Name your app "ToDo".  
    
    1. Add a description.
    
    1. Change the primary color of your app by picking one of the suggested colors, or using the color picker.
    
    1. Upload an icon by clicking **Upload icon**.
    
    1. Click **Create App** to advance to the next step.

    ![Screenshot showing the application properties setup with fields for name, description, primary color, and icon upload](images/app-info-ss.png "Application Information Setup")

1. In the application properties screen, make sure **Reactive Web App** is selected in the **Choose module type** dropdown. Click **Create Module** to create the first module and open it for editing.

    ![Screenshot of the application properties screen with 'Reactive Web App' selected in the 'Choose module type' dropdown](images/module-type-ss.png "Module Type Selection")


## Create a database table from an Excel file { #create-entity-from-excel }

In OutSystems, application data can be stored in a relational database. This means that the first step in creating an app is defining the data model.

To do this, we are going to use an Excel file that already contains the following task information:

* Description
* Due Date
* Is Active

Download the [tutorial Excel file](resources/TutorialResource.xlsx) to your computer.

In the **ToDo** module, open the **Data** tab on the top right-hand corner, right-click the **Database** folder, choose **Import New Entities from Excel**, and select the `TutorialResource.xlsx` Excel file. Click **Import** in the dialog to confirm.

![Screenshot illustrating how to import new entities from an Excel file into the OutSystems database](images/import-entities-excel-ss.png "Import Entities from Excel")

When importing an Excel file, OutSystems creates a database table (called an Entity in OutSystems) with the necessary columns (called Attributes in OutSystems) to store the data in the database.

Behind the scenes, OutSystems also creates logic to import each row in the Excel file into a corresponding database record. After publishing your application, the background logic populates (bootstraps) your database with the data from the Excel file. In this tutorial, we're only storing the data in the server database.

## Create a Screen to show tasks

Now we can create a Screen that shows all of the tasks.

1. Switch to the **Interface** tab on the top right-hand corner, and double-click **MainFlow** under **UI Flows**. 

    ![Screenshot showing the action of double-clicking 'MainFlow' under 'UI Flows' in Service Studio](images/click-mainflow-ss.png "Accessing MainFlow in Service Studio")

1. Drag a **Screen** from the Toolbox to an empty area in the Main Editor window. 

    ![Screenshot of dragging a 'Screen' widget from the Toolbox to the main editor window in Service Studio](images/drag-screen-widget-ss.png "Drag Screen Widget to Main Editor")

1. Choose the **Empty** template (1), name your screen `Task` (2) and click **Create Screen** (3).

    ![Screenshot showing the selection of the 'Empty' template for a new screen named 'Task'](images/select-empty-screen-ss.png "Select Empty Screen Template")

1. Drag the **Task** Entity from the **Data** tab to the Content placeholder of the screen.

    ![Screenshot depicting the action of dragging the 'Task' entity to the content placeholder of a screen](images/drag-task-entity-ss.png "Drag Task Entity to Screen")

    This automatically creates a Table with pagination support.

    ![Screenshot of a table with pagination support automatically created after dragging the 'Task' entity to the screen](images/table-ss.png "Table with Pagination")

## Create a Screen to edit tasks

Creating a Screen to edit the records is as fast as creating a Table. Follow these steps:

1. Right-click the title of the first task in the row and select **Link to** > **(New Screen)**.

    ![Screenshot showing the context menu option to link the title of a task to a new screen for editing](images/create-link-new-screen-ss.png "Create Link to New Screen")

1. Choose the **Empty** template, name your screen `TaskDetail` and click **Create Screen**.

    This links the title of the tasks to a newly created screen. We will use this new screen to edit the tasks. For that, we will need a form.

1. Drag a **Form** widget from the Toolbox to the Content placeholder in the **TaskDetail** screen.

    ![Screenshot of dragging a 'Form' widget from the Toolbox to the content placeholder in the 'TaskDetail' screen](images/drag-form-widget-ss.png "Drag Form Widget to Screen")

1. Drag the **Task** entity from the **Data** tab to the previously created Form.

    ![Screenshot showing the action of dragging the 'Task' entity into a form widget to create a form](images/drag-task-entity-into-form-ss.png "Drag Task Entity into Form")

    Now we will define the logic that runs when the end users press the **Save** button:

1. Double-click an empty area of the **Save** button to define the logic associated with the button. This will create a new screen action named **SaveOnClick**.

    ![Screenshot of double-clicking the 'Save' button to define the logic associated with the button](images/double-click-save-button-ss.png "Define Save Button Logic")

1. In the **Logic** tab, right-click **Server Actions** and select **Add Server Action**. Set its name to **TaskCreateOrUpdate**. 

    ![Screenshot showing the creation of a new server action named 'TaskCreateOrUpdate' in Service Studio](images/create-server-action-ss.png "Create Server Action")
    
1. Right-click the newly created action and select **Add Input Parameter**. Set its name to **Task**.

    ![Screenshot illustrating the addition of an input parameter named 'Task' to a server action](images/add-input-parameter-ss.png "Add Input Parameter to Action")

1. In the Input Parameter properties, set the Data Type to **Task**.

    ![Screenshot showing the properties of an input parameter with the data type set to 'Task'](images/input-data-type-ss.png "Set Input Parameter Data Type")

1. Right-click the **TaskCreateOrUpdate** action and select **Add Output Parameter**. Set its name to **TaskId**.


1. In the Output Parameter properties, set the Data Type to **Task Identifier**. 

    ![Screenshot displaying the properties of an output parameter with the data type set to 'Task Identifier'](images/output-data-type-ss.png "Set Output Parameter Data Type")

1. In the **Data** tab, expand the **Task** entity and drag the **CreateOrUpdateTask** entity action to the flow of the **TaskCreateOrUpdate** server action. 

    ![Screenshot of dragging the 'CreateOrUpdateTask' entity action to the flow of the 'TaskCreateOrUpdate' server action](images/drag-entity-action-ss.png "Drag Entity Action to Server Action Flow")

1. Set the **Source** to the Input Parameter **Task**.

    ![Screenshot showing the setting of the 'Source' parameter to the input parameter 'Task' in an action](images/action-source-ss.png "Set Action Source Parameter")

1. Next, we'll need to assign the value of the Output Parameter **TaskId** to the **CreateOrUpdateTask**. Drag an **Assign** node from the toolbox to the flow (1) and set the **Variable** to **TaskId**, and the **Value** to `CreateOrUpdateTask.Id` (2).

    ![Screenshot of an 'Assign' node in a flow with the 'Variable' set to 'TaskId' and the 'Value' to 'CreateOrUpdateTask.Id'](images/drag-assign-set-variable-ss.png "Assign Output Parameter Value")

1. In the **Interface** tab, double-click the **SaveOnClick** action.

     ![Screenshot of the 'SaveOnClick' action in the interface tab of Service Studio](images/save-on-click-ss.png "SaveOnClick Action")

1. Navigate to the **Logic** tab and drag the **TaskCreateOrUpdate** server action to the **True** branch of the **If** (1). Set the **Task** property to `GetTaskById.List.Current.task` (2).

    ![Screenshot showing the dragging of the 'TaskCreateOrUpdate' server action to the 'True' branch of an 'If' condition](images/drag-server-action-ss.png "Drag Server Action to Logic Flow")

1. Drag the **Task** Screen from the **Interface** tab to the **End** node so that the user is redirected back to the main screen after saving a task. 

    ![Screenshot of dragging the 'Task' screen to the 'End' node in a logic flow to redirect the user after saving](images/drag-task-screen-to-end-node-ss.png "Redirect to Task Screen After Save")

## Allow completing tasks

Now let's add the functionality to mark tasks as complete. We can implement that by adding a feature to delete the completed task:

1. In the **Interface** tab, double-click the **Task** Screen. 

1. Right-click the Checkbox in the **Is Active** column and select **Delete**.

    ![Screenshot showing the deletion of a checkbox from the 'Is Active' column in a task list](images/delete-checkbox-icon-ss.png "Delete Checkbox from Task List")

1. Drag a **Button** widget to the same Container where the Checkbox was, and enter `Done` in the Text property of the button.

    ![Screenshot of dragging a 'Button' widget to replace a deleted checkbox in the task list](images/drag-button-widget-ss.png "Add Done Button to Task List")

1. Double-click an empty area of the button to define the logic associated with the click.

    ![Screenshot showing the definition of logic for a 'Done' button when clicked](images/define-button-logic-ss.png "Define Done Button Logic")

1. In the **Logic** tab, right-click the **Server Actions** and select **Add Server Action**. Name it **TaskDelete**. 

1. Add an Input Parameter to the **TaskDelete** to receive the Task identifier. Set its name to **TaskId** and the Data Type to **Task Identifier**.

    ![Screenshot illustrating the addition of an input parameter named 'TaskId' to the 'TaskDelete' server action](images/add-an-input-parameter-ss.png "Add Input Parameter to TaskDelete Action")

1. In the **Data** tab, expand the **Task** Entity. Drag the **DeleteTask** Entity Action to the flow. 

    ![Screenshot of dragging the 'DeleteTask' entity action to the flow of the 'TaskDelete' server action](images/drag-entity-action-to-flow-ss.png "Drag DeleteTask Action to Flow")

1. Set the **Id** property to the Input Parameter **TaskId**.

    ![Screenshot showing the setting of the 'Id' property to the input parameter 'TaskId' in the delete action](images/set-id-property-ss.png "Set Id Property for Delete Action")

1. Go back to the **Interface** tab and double-click the **DoneOnClick** action under the **Task** screen. 

    ![Screenshot of the 'DoneOnClick' action under the 'Task' screen in the interface tab](images/click-button-on-click-ss.png "DoneOnClick Action Definition")

1. Select the **Logic** tab and drag the **TaskDelete** server action to the flow of the **DoneOnClick** action. Set the **TaskId** property to `GetTasks.List.Current.Task.Id`.

    ![Screenshot showing the dragging of the 'TaskDelete' server action to the flow and setting the 'TaskId' property](images/drag-server-action-set-property-ss.png "Set TaskId Property for TaskDelete Action")

1. Drag **Refresh Data** from the Toolbox to the action flow, after the **TaskDelete** action, and select the aggregate **GetTasks** to refresh the available tasks on the screen.

    ![Screenshot of dragging a 'Refresh Data' widget to the action flow after the 'TaskDelete' action](images/drag-refresh-data-widget-ss.png "Refresh Data After Task Deletion")

## Allow adding tasks

We also want to enable the end users to add new tasks from the screen with all tasks by linking to the screen that is already used to edit tasks:

1. Go to the **Interface** tab > **UI Flows** > **MainFlow**, and double-click the "Task" Screen to open the screen with all tasks in the main editor.  

1. Drag a **Button** widget from the toolbox to the Actions placeholder in the top right-hand corner of the screen. Change the label of the button to **Add Task**.

    ![Screenshot of dragging a 'Button' widget to the actions placeholder with the label 'Add Task'](images/drag-button-widget-from-toolbox-ss.png "Add Add Task Button to Task Screen")

1. Right-click an empty area of the button and choose **Link** > **MainFlow\TaskDetail**.

    ![Screenshot showing the linking of the 'Add Task' button to the 'TaskDetail' screen](images/link-to-screen-ss.png "Link Add Task Button to TaskDetail Screen")

## Test your Reactive Web App

At this stage, you can test your Reactive Web App. Click the **1-Click Publish** button to publish the application to your environment. When the application is deployed, click the **Open in Browser** button to test your application in a browser.

![Screenshot of the published Reactive Web App ready to be tested in a browser](images/your-reactive-web-app-ss.png "Test Your Reactive Web App")
