---
kinds: ServiceStudio.Plugin.SAP.SapClientDescriptor
helpids: 17252
---

# SAP Connection

Defines a connection to a SAP system.  

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
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
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
<td title="Image">Icon</td>
<td>Picture to be displayed to help identify this element.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr class="separator">
<th colspan="5">Default Connection Settings</th>
</tr>
<tr>
<td title="AppServerHost">Application Server</td>
<td>Hostname of the SAP application server where the remote function calls are executed.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="SystemId">System ID</td>
<td>Three-letter identifier of the SAP installation to which to connect.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="InstanceNumber">Instance Number</td>
<td>Two-digit identifier of the SAP instance to which to connect.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="SAPRouter">SAP Router String</td>
<td>Router string to connect to the SAP application server, e.g.: /H/sap.acme.com/S/3299/H/</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Client">Client</td>
<td>Three-digit client number that identifies which tenant's data to use in the remote function calls.</td>
<td></td>
<td>800</td>
<td></td>
</tr>
<tr>
<td title="Language">Language</td>
<td>Two-letter language key used for translating language-specific data when retrieving data from SAP.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="User">Username</td>
<td>Username to authenticate in SAP.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="separator">
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="DefaultValueBehavior">Send Default Value</td>
<td>Set to Yes to send the default value for an optional atribute or parameter in the payload of the request.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="OnBeforeConnection">On Before Connection</td>
<td>The action that allows you to customize the connection and its parameters. Executed before every SAP remote function call.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="OnBeforeInvoke">On Before Call</td>
<td>The action that allows you to customize values passed to a SAP remote function. Executed before every remote function call.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="OnAfterInvoke">On After Call</td>
<td>The action that allows you to customize the values received from a SAP remote function. Executed after every remote function call.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

