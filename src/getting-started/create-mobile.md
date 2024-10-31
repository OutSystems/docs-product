---
summary: Learn to build and test a mobile app with OutSystems 11 (O11) by importing Excel data into a database.
tags: runtime-mobile; support-Mobile_Apps; support-Mobile_Apps-overview
locale: en-us
guid: 0ee5a8f6-0c94-4316-818f-49cc25f92283
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/mDMvfanpcaW6fqmEKxjvMQ/Getting%20Started?node-id=67:19
---

# Create Your First Mobile App

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

Developing mobile apps with OutSystems is fast. If you have an Excel file containing your data, you can import it into a database and quickly create a mobile app that enables you to check and manage your data on the go.

To create a mobile app with data that's imported from an Excel file, you need to:

1. Create a database model, and import the data from the Excel file into the database
2. Create a screen that lists the data from the database
3. Create a screen that enables you to create new records, and update existing ones
4. Implement functionality to delete records from the database
5. Test the application on your mobile device.

Let's do this! In this example we'll use a sample Excel file with to-do task information, and we'll create a simple task management mobile app.

## Create a Mobile App

Let's create a new task management mobile app. Do the following in Service Studio:

1. Select **New Application**.

    ![Screenshot showing the selection of 'New Application' in Service Studio](images/new-app-ss.png "New Application Selection")

1. Select **From scratch** and click **Next**.

    ![Screenshot of the 'From scratch' option selected when creating a new app](images/from-scratch-ss.png "Creating App From Scratch")

1. Choose the **Phone App** template and click **Next**.

    ![Screenshot displaying the selection of the 'Phone App' template in the app creation process](images/phone-app-template-ss.png "Phone App Template Selection")

1. Name the app **To Do** and click **Create App**. Service Studio opens app details for you to add your first module.

    ![Screenshot where the name 'To Do' is entered for the new mobile app](images/name-of-app-ss.png "Naming the Mobile App")

1. In the app detail screen, confirm the following and click **Create Module**:
    
    * The name of the module is `ToDo`
    * The module type is **Phone App**.

    ![Screenshot showing the creation of a new module with the name 'ToDo' and type 'Phone App'](images/new-module-ss.png "Creating a New Module")

    An application contains one or more modules, different parts of the application can be encapsulated in a module. A module is where you design the data model, implement the logic, and design the UI of your application.

## Create a database table from an Excel file

OutSystems stores your application data in a relational database. This means that the first step in creating an application is defining the data model.

To do this, we're going to use an Excel file that already contains the following task information:

* Description
* Due Date
* Is Active

Download the [tutorial Excel file](https://www.outsystems.com/home/TutorialResource.aspx) to your computer.

In the **ToDo** module, open the **Data** tab on the top right-hand corner, right-click the **Entities** folder, choose **Import New Entities from Excel**, and select the tutorial Excel file `TutorialResource.xlsx`. Click **Import** in the dialog to confirm.

![Screenshot illustrating the import of an Excel file into the OutSystems database](images/create-mobile-03.png "Importing Excel Data")

When importing an Excel file, OutSystems creates a database table (called an Entity in OutSystems) with the necessary columns (called Attributes in OutSystems) to store the data in the database.

Behind the scenes, OutSystems also creates logic to import each row in the Excel file into a corresponding database record. After publishing your application, the background logic populates your database with the data from the Excel file.

In this tutorial we're only storing the data in the server database, but for offline usage, it's also possible to store the data locally in mobile devices using Local Storage.

## Create a screen to list tasks

Now we can create a screen that lists all of the tasks.

Open the **Interface** tab on the top right-hand corner, and double-click **MainFlow** under **UI Flows**. Then, drag a **Screen** from the Toolbox to an empty area in the Main Editor window. Choose the **Empty** template, name your screen `Tasks` and click **Create Screen**.

![Screenshot of the process to create a new screen for listing tasks in the mobile app](images/create-mobile-04.png "Creating a List Screen")

Drag the **Task** entity from the **Data** tab to the Content placeholder of the mobile screen that is displayed in the Main Editor window.

![Screenshot showing the Task entity being dragged to the content placeholder of the mobile screen](images/create-mobile-05.png "Adding Task Entity to Screen")

This updates the **Tasks** to include a list that initially displays 20 tasks and automatically loads more tasks when the user scrolls to the end of the list.

![Screenshot of the Tasks list screen with a list that loads more tasks on scroll](images/create-mobile-06.png "Tasks List Screen")

## Create a screen to edit tasks

Creating a screen to edit the records is as fast as creating a list screen.

Right-click the title of the first task in the list, click **Link to** > **(New Screen)**, choose the **Empty** template, name your screen `TaskDetail` and click **Create Screen**.

![Screenshot showing the linking of the task title to a new screen for editing tasks](images/create-mobile-07.png "Linking Task Title to Edit Screen")

This links the title of the tasks to a newly created screen. We will use this new screen to edit the tasks, but for that we will need a form:

1. Drag a **Form** widget from the Toolbox to the Content placeholder in the **TaskDetail** mobile screen.

    ![Screenshot of a Form widget being added to the TaskDetail screen for editing tasks](images/create-mobile-08.png "Adding Form Widget to TaskDetail Screen")

1. Drag the **Task** entity from the **Data** tab to the previously created Form.

    ![Screenshot where the Task entity is dragged onto the previously created form on the TaskDetail screen](images/create-mobile-10.png "Dragging Task Entity to Form")

Now we will define the logic that runs when the end users press the Save button:

1. Double-click the **Save** button, ensure you click outside of the button text area, to define the logic associated with the button. This creates a new screen action named **SaveOnClick**.

1. In the Logic tab create a server action named **TaskCreateOrUpdate**.

1. Add an input parameter and set its name to **Task**. Set the data type to **Task**.

1. Add an output parameter and set its name to **TaskId**. Set the data type to **Task Identifier**. This will be the task id returned by the CreateOrUpdateTask that we'll need to pass on to the **SaveOnClick** action.

1. In the **Data** tab, expand the **Task** entity and drag the **CreateOrUpdateTask** entity action to the flow of the **TaskCreateOrUpdate** server action. Set the **Source** to the input parameter **Task**.

1. Next, we'll need to assign value of the output parameter **TaskId** to the **CreateOrUpdateTask**. Drag an **Assign** node to the flow and set the **Variable** to **TaskId**, and the **Value** to `CreateOrUpdateTask.Id`.
    
    ![Screenshot of the logic flow for creating or updating a task in the OutSystems Service Studio](images/wrapper-create-ss.png "Task Create or Update Logic")

<!---1. In the **Data** tab, expand the **Task** entity and drag the **CreateOrUpdateTask** entity action to the **True** branch of the **If**. Set the **Source** property to `GetTaskById.List.Current`.

1. Drag the screen **Tasks** from the **Interface** tab to the End node so that the user is redirected back to the main screen after saving a task.-->

1. Navigate to the **Interface** tab and double-click the **SaveOnClick** action.

1. In the **Logic** tab, drag the **TaskCreateOrUpdate** server action to the **True** branch of the **If**. Set the **Task** property to `GetTaskById.List.Current.task`.

1. Drag the screen **Tasks** from the **Interface** tab to the End node so that the user is redirected back to the main screen after saving a task. 

   ![Screenshot showing the Save button logic in the TaskDetail screen for saving task changes](images/create-mobile-11.png "Save Button Logic")

## Allow completing tasks

Now let's add the functionality to mark tasks as complete. Let's implement that by deleting the completed tasks:

1. Click the item of the list and then, on the Toolbar, click **Swipe Left Action**.

1. In the newly created List Action, replace the text "Action" with "Done".

    ![Screenshot of the Swipe Left Action being configured to mark tasks as done](images/create-mobile-14.png "Swipe Left Action for Task Completion")

1. Double-click an empty area of the List Action to define the logic associated with the Swipe Left Action.

1. Click the **Logic** tab and add a a Server Action. Name it *TaskDelete*. 

1. Add an input parameter to the *TaskDelete* to receive the Task identifier. Set its name to *TaskId* and the Data Type to *Task Identifier*.

1. Go to the **Data** tab and expand the **Task** Entity and drag the **DeleteTask** entity action to the flow. Set the property *Id* to the input parameter *TaskId*.

    ![Screenshot depicting the logic for deleting a task in the OutSystems Service Studio](images/wrapper-delete-ss.png "Task Delete Logic")

1. Go back to the **Interface** tab and double click the action **DeleteTask**. Drag the **TaskDelete** server action to the flow. and set the TaskId to the input parameter *TaskId*.

1. Drag **Refresh Data** from the Toolbox to the action Flow, after the **TaskDelete** action, and select the aggregate **GetTasks** to refresh the available tasks in the screen.

    ![Screenshot showing the Refresh Data action after deleting a task to update the task list](images/reactive-new-app-delete-refresh.png "Refresh Data After Task Deletion")


## Allow adding tasks

We want to enable the end users to add new tasks from the list screen by linking to the screen that is already used to edit tasks:

1. In the **Interface** tab, double-click the **Tasks** to open the list screen.  
Drag an **Icon** widget from the Toolbox to the Actions placeholder in the top right-hand corner of the screen and select the **plus** icon.

    ![Screenshot of adding a plus icon to the Actions placeholder for creating new tasks](images/create-mobile-12.png "Adding New Task Icon")

1. Right-click the **plus** icon and choose **Link** > **MainFlow\TaskDetail**.

    ![Screenshot showing the plus icon linked to the TaskDetail screen for adding new tasks](images/create-mobile-13.png "Linking Plus Icon to TaskDetail Screen")


## Test your Mobile App

At this stage we test the mobile app. Click the **1-Click Publish** button to publish the application to your environment.

![Screenshot of the 1-Click Publish button to deploy the mobile app to the environment](images/create-mobile-17.png "Publishing the Mobile App")

When the application is deployed, click the **Open in Browser** button to test your application in a browser (Chrome and Safari are supported).


To try out the app on your mobile device see [Distribute as a progressive web app (PWA)](../deploying-apps/mobile-app-packaging-delivery/distribute-pwa/intro.md).
