---
kinds: ServiceStudio.Model.Flows+WebFlow+Kind, ServiceStudio.Model.NRFlows+WebFlow+Kind, ServiceStudio.Model.NewRuntime.ReferenceWebFlow+Kind, ServiceStudio.Model.ReferenceWebFlow+Kind
helpids: 4034, 0
locale: en-us
guid: c6a9d058-311b-4564-8685-cd992ed4563f
---

# UI Flow

UI Flows group screens into logical units with common settings.

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
<td title="Theme">Theme</td>
<td>Defines the look and feel to apply to the screens and blocks of the UI Flow.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>Name of the element as defined in the module which implements it (producer module). This property is read-only.</td>
<td>Yes</td>
<td></td>
<td>This property is only visible for referenced elements.</td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="HTTP Security">HTTP Security</td>
<td>Security level required for HTTP requests. Can be overridden by application security settings in Service Center or LifeTime.</td>
<td>Yes</td>
<td>None</td>
<td>The possible values are: None, SSL/TLS, SSL/TLS with client certificates.<br/>This property is only available in web apps.</td>
</tr>
<tr>
<td title="Integrated Authentication">Integrated Authentication</td>
<td>Set to Yes to use Integrated Authentication to validate user access.</td>
<td>Yes</td>
<td>No</td>
<td>This property is only available in web apps.</td>
</tr>
<tr>
<td title="Internal Access Only">Internal Access Only</td>
<td>Only users with access to the internal network can access the UI Flow elements.</td>
<td>Yes</td>
<td>No</td>
<td>This property is only available in web apps.</td>
</tr>
</tbody>
</table>

