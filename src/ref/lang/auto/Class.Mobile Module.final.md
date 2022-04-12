---
kinds: ServiceStudio.Model.ESpace+Kind
helpids: 1011
locale: en-us
guid: d3a9dc9a-5e49-43c2-9d77-fc4e9f1778a8
---

# Mobile Module


<div class="info" markdown="1">

Applies to Mobile and Reactive Web Apps.

</div>

An OutSystems App consists of one or more Modules joined by an Application Template. Click the module name (1) in any of the main Service Studio tabs (**Process**, **Interface**, **Logic**, or **Data**) to see the module properties pane (2).

![Module properties](images/servicestudio-module-properties.png?width=800)

## Create a new module

To create a new in an app, follow these steps in Service Studio:

1. Go to the application list, search your app, and click on it. The application details screen opens.

     ![App details screen](images/servicestudio-applications-screen.png?width=700)

1. In the application details screen enter **Module name** and select module type from the **Choose module type** list.

    ![App details screen](images/servicestudio-new-module.png?width=700)
  
2. Click **Create module**. Your new module opens for editing.

## Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Mandatory</th>
<th>Default value</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="Name">Name</td>
<td>Identifies the module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="DBMS">DBMS</td>
<td>Defines the DataBase Management System type considered by developers when writing SQL. The development environment executes some validations regarding your queries regarding compliance with the selected DBMS.</td>
<td>Yes</td>
<td>(All)</td>
<td>The possible values are: Oracle, SqlServer, (All).<br/>
        This property allows the development environment to execute some validations on SQL queries to check if the SQL is compliant with the DBMS type specified in this property.<br/>
        It must be set according to the OutSystems Platform Server Database, otherwise a warning message is presented and you should either specify the exact database type or select (All).<br/>
        Though this property is merely informative, it is important for communication and knowledge transfer between developers.</td>
</tr>
<tr>
<td title="Is User Provider">Is User Provider</td>
<td>Set to Yes to make this a module which provides users.</td>
<td>Yes</td>
<td>No</td>
<td>When this property is set to Yes, the Users entity (System) is set as public and the module becomes available as an option as a user source in modules User Provider Module property.</td>
</tr>
<tr>
<td title="User Provider module">User Provider module</td>
<td>Specifies a source for the user records to be used by this module.</td>
<td></td>
<td>Users</td>
<td>By default it shows the following possible values: (Current eSpace), ServiceCenter, Users.</td>
</tr>
<tr>
<td title="Icon">Icon</td>
<td>Identifies the module in the element tree of the development environment.</td>
<td>Yes</td>
<td>Default Icon</td>
<td>Identifies the module in the element tree of the development environment.<br/>
            <strong>Note:</strong> This icon will <em>not</em> be used as the mobile app icon; 
            to change the app icon check <a href="http://www.outsystems.com/DocRouter/Router.aspx?PlatformToolName=ServiceStudio&amp;PlatformVersionNumber=10.0&amp;HelpId=30112">Modify the App Icon</a>.</td>
</tr>
<tr >
<th colspan="5">Defaults</th>
</tr>
<tr>
<td title="Default Theme">Default Theme</td>
<td>Main theme defining the look and feel to apply to the screens and blocks of the module.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Default Screen">Default Screen</td>
<td>Start screen of the application.</td>
<td></td>
<td>MainFlow\HomeScreen</td>
<td></td>
</tr>
<tr>
<td title="Splash Screen">Splash Screen</td>
<td>Splash screen of the application.</td>
<td></td>
<td>Common\Splash</td>
<td></td>
</tr>
<tr>
<td title="Global Exception Handler">Global Exception Handler</td>
<td>Specifies the 'OnException' handler to be used by all the flows of this module.</td>
<td></td>
<td>Common\OnException</td>
<td></td>
</tr>
<tr>
<td title="Default Transition">Default Transition</td>
<td>Transition effect applied when navigating to another screen.</td>
<td>Yes</td>
<td>Slide from Right</td>
<td></td>
</tr>
<tr>
<td title="Server Request Timeout">Server Request Timeout</td>
<td>Maximum time in seconds to wait for server requests to complete before triggering a Communication Exception. The default is 10 seconds. You can override this value for specific Run Server Actions, Aggregates and Data actions.</td>
<td></td>
<td>10</td>
<td></td>
</tr>
<tr >
<th colspan="5">Validation Messages</th>
</tr>
<tr>
<td title="Mandatory Input">Mandatory Input</td>
<td>Default message displayed whenever a mandatory input field is left empty.</td>
<td></td>
<td>"Required field!"</td>
<td></td>
</tr>
<tr>
<td title="Invalid Integer">Invalid Integer</td>
<td>Default message displayed whenever a provided value is not of Integer type as expected by an input field.</td>
<td></td>
<td>"Integer expected!"</td>
<td></td>
</tr>
<tr>
<td title="Invalid Decimal">Invalid Decimal</td>
<td>Default message displayed whenever a provided value is not of Decimal type as expected by an input field.</td>
<td></td>
<td>"Decimal expected!"</td>
<td></td>
</tr>
<tr>
<td title="Invalid Currency">Invalid Currency</td>
<td>Default message displayed whenever a provided value is not of Currency type as expected by an input field.</td>
<td></td>
<td>"Currency expected!"</td>
<td></td>
</tr>
<tr>
<td title="Invalid Date">Invalid Date</td>
<td>Default message displayed whenever a provided value is not of Date type as expected by an input field.</td>
<td></td>
<td>"Date expected!"</td>
<td></td>
</tr>
<tr>
<td title="Invalid Time">Invalid Time</td>
<td>Default message displayed whenever a provided value is not of Time type as expected by an input field.</td>
<td></td>
<td>"Time expected!"</td>
<td></td>
</tr>
<tr>
<td title="Invalid DateTime">Invalid DateTime</td>
<td>Default message displayed whenever a provided value is not of DateTime type as expected by an input field.</td>
<td></td>
<td>"DateTime expected!"</td>
<td></td>
</tr>
<tr>
<td title="Invalid Text">Invalid Text</td>
<td>Default message displayed whenever a provided value is not of Text type as expected by an input field.</td>
<td></td>
<td>"Text expected!"</td>
<td></td>
</tr>
<tr>
<td title="Invalid Phone">Invalid Phone</td>
<td>Default message displayed whenever a provided value is not of Phone type as expected by an input field.</td>
<td></td>
<td>"Phone Number expected!"</td>
<td></td>
</tr>
<tr>
<td title="Invalid Email">Invalid Email</td>
<td>Default message displayed whenever a provided value is not of Email type as expected by an input field.</td>
<td></td>
<td>"Email expected!"</td>
<td></td>
</tr>
<tr >
<th colspan="5">Upgrade Messages</th>
</tr>
<tr>
<td title="Upgrade Complete">Upgrade Complete</td>
<td></td>
<td></td>
<td>"Your application has been updated to the latest version."</td>
<td></td>
</tr>
<tr>
<td title="Upgrade Failed">Upgrade Failed</td>
<td></td>
<td></td>
<td>"An error occurred while trying to update the app. If you want to retry the update, restart the app."</td>
<td></td>
</tr>
<tr>
<td title="Upgrade Failed on Resources">Upgrade Failed on Resources</td>
<td></td>
<td></td>
<td>"An error occurred while trying to update the app. If you want to retry the update, restart the app."</td>
<td></td>
</tr>
<tr>
<td title="Upgrade Failed on Data Model">Upgrade Failed on Data Model</td>
<td></td>
<td></td>
<td>"An error occurred while trying to update the app. If you want to retry the update, restart the app. If the problem persists you can reinstall, but all local data will be lost."</td>
<td></td>
</tr>
<tr>
<td title="Upgrade Required">Upgrade Required</td>
<td></td>
<td></td>
<td>"Your application needs to be updated. Tap here to update."</td>
<td></td>
</tr>
<tr>
<td title="Upgrade Required with Data Loss">Upgrade Required with Data Loss</td>
<td></td>
<td></td>
<td>"Your application needs to be updated. Unsaved data will be lost. Tap here to update."</td>
<td></td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Is Multi-tenant">Is Multi-tenant</td>
<td>Set to Yes to enable multi-tenancy for this module.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Web Services Namespace">Web Services Namespace</td>
<td>Namespace of the WSDL generated by this module.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Extensibility Configurations">Extensibility Configurations</td>
<td>JSON configuration data used for integrating functionality such as Cordova plug-ins.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Required Scripts</th>
</tr>
<tr>
<td title="Required Script">Required Script</td>
<td>Script(s) required by the element.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

