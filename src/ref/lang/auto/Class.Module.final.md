---
kinds: ServiceStudio.Model.ESpace+Kind
helpids: 1011
locale: en-us
guid: 1189b6d2-baf6-4b9f-bfc7-e88033ba8e7b
---

# Module

<div class="info" markdown="1">

Applies to Traditional Web Apps only.

</div>

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
<td>The module icon is also displayed in the "Manage Dependencies" dialog box.</td>
</tr>
<tr >
<th colspan="5">Web</th>
</tr>
<tr>
<td title="Default Theme">Default Theme</td>
<td>Main theme defining the look and feel to apply to the screens and blocks of the module.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="jQuery Version">jQuery Version</td>
<td>jQuery version used in all screens and blocks of the module.</td>
<td>Yes</td>
<td>1.8.3</td>
<td>The possible values are: 1.8.3, 1.4.2 OS (Note: this older jQuery version is being deprecated).</td>
</tr>
<tr>
<td title="Global Exception Handler">Global Exception Handler</td>
<td>Specifies the 'OnException' handler to be used by all the flows of this module.</td>
<td></td>
<td>Common\OnException</td>
<td></td>
</tr>
<tr>
<td title="JavaScript">JavaScript</td>
<td>JavaScript associated with this element.</td>
<td></td>
<td></td>
<td>Click on "..." to edit the property value.</td>
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
<td title="Invalid Numeric Password">Invalid Numeric Password</td>
<td>Default message displayed whenever a provided value is not of Numberic Password type as expected by an input field.</td>
<td></td>
<td>"Numeric Password expected!"</td>
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
<td title="Use Cookies">Use Cookies</td>
<td>Set to Yes to use cookies to exchange the session identifier through the Web Browser cookies. If set to No, the session identifier is sent back and forth in the URL.</td>
<td>Yes</td>
<td>Yes</td>
<td>This feature is deprecated.</td>
</tr>
<tr>
<td title="Is Multi-tenant">Is Multi-tenant</td>
<td>Set to Yes to enable multi-tenancy for this module.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Web Screen Rendering Mode">Web Screen Rendering Mode</td>
<td>Defines the DOCTYPE declaration to put in generated HTML pages.</td>
<td>Yes</td>
<td>HTML 5</td>
<td>The possible values are: HTML 5, XHTML Transitional, Quirks.</td>
</tr>
<tr>
<td title="Web Services Namespace">Web Services Namespace</td>
<td>Namespace of the WSDL generated by this module.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

