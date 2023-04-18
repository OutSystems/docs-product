---
summary: Follow this tutorial to quickly create and test a Traditional Web App example to manage contacts.
tags: runtime-traditionalweb; support-webapps
locale: en-us
guid: f84888af-0987-4ec7-98f7-195f6e493292
app_type: traditional web apps
platform-version: o11
---

# Create Your First Traditional Web App

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

Developing Traditional Web Apps with OutSystems is straightforward. If you have an Excel file containing your data, you can import it into a database and quickly create an enterprise-grade application to manage your data. Don't worry if you don't have an Excel file ready, we provide a sample file for you.

To create an application with data that's imported from an Excel file, you need to:

1. Create a database model, and import the data from the Excel file into the database
2. Create a screen that lists the data from the database
3. Create a screen that allows creating new records, and updating existing ones
4. Implement functionality to delete records from the database
5. Publish your application

Let's do this! In this example we'll use a provided Excel file with contact information, and we'll create a simple contact management application.

## Create a Traditional Web App

Let's create a new contact information management app. An application contains one or more modules, different parts of the application can be encapsulated in a module. A module is where you design the data model, implement the logic, and design the UI of your applications.

In Service Studio, click **New Application**, choose **Traditional Web**, and name it `Contact Portal`.

![Create a Traditional Web App](images/create-web-01.png)

In the new **Contact Portal** application, create a **Traditional Web** module, named `ContactPortal`.

![Create a Module](images/create-web-02.png)

Click **Create Module** to create the module and open it for editing.

## Create a database table from an Excel File

OutSystems stores your application data in a relational database. This means that the first step in creating an application is defining the data model.

To do this, we are going to use an Excel file that already contains the following contact information:

* Name
* Address
* Birth date
* Email

In the `ContactPortal` module, open the **Data** tab on the top right-hand corner, right-click the **Entities** folder, choose **Import New Entities from Excel...**, and select the sample file `Contacts.xlsx` (available [here](resources/Contacts.xlsx)).

![Create a Database Table from an Excel File](images/create-web-03.png)

When importing an Excel file, OutSystems creates a database table (called an Entity in OutSystems) with the necessary columns (called Attributes in OutSystems) to store the data in the database.

Behind the scenes, OutSystems also creates logic to import each row from the Excel file into a database record. After publishing your application the logic runs automatically, and populates your database with the data that is in the Excel file.

## Create a screen to list contacts

Now we can create a screen that lists all of the contacts.

Open the **Interface** tab on the top right-hand corner, and double-click **MainFlow** under **UI Flows**. Then, drag and drop the entity **Contact** from the **Data** tab to an empty area in the Main Editor window.

![Create a Screen to List Contacts](images/create-web-04.png)

This creates a screen that includes a list that displays 50 contacts at a time, along with pagination and search functionality.

![Contacts Screen](images/create-web-05.png)

## Create a screen to create and edit contacts

Creating a screen to create and edit records is as fast as creating a list screen. In fact you just have to repeat the previous step.

With the **MainFlow** open, drag and drop the entity Contact from the **Data** tab to an empty area in the Main Editor window.

![Create a Screen to Create and Edit Contacts](images/create-web-06.png)

This creates a new screen with a form to create new records or edit existing ones. OutSystems also adds the server-side logic to create and edit records automatically.

![ContactDetail Screen](images/create-web-07.png)

## Allow deleting contacts

To implement an application to manage contacts we are just missing the delete functionality. Let's implement that!

Double-click the screen **ContactDetail** to open it. Drag and drop a **Button** widget from the toolbox to the right of the Cancel button of the screen, right-click the new button and choose **Link to New 'DeleteContact' Screen Action**.

![](images/create-web-09.png)

OutSystems adds server-side logic to delete the contact record and associates the button to that logic.

## Publish your Traditional Web App

Now we just need to make the application go live. Click the **1-Click Publish** button to publish the application to your environment.

![Publish Your Application](images/create-web-10.png)

When the application is deployed, click the **Open in Browser** button to test your application in a browser.

![Open Your Application](images/create-web-11.png)
