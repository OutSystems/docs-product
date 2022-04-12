---
kinds: ServiceStudio.Model.Resource+Kind, ServiceStudio.Model.ReferenceResource+Kind
helpids: 17020
locale: en-us
guid: e2cc47cf-825c-475d-b989-952f2dbf90d3
---

# Resource


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
<td title="Public">Public</td>
<td>Set to Yes to allow the element to be added as dependency by other modules.</td>
<td>Yes</td>
<td>No</td>
<td>Available in Mobile modules only.</td>
</tr>
<tr>
<td title="Deploy Action">Deploy Action</td>
<td>Specifies the action to be executed when the module is deployed.</td>
<td>Yes</td>
<td>Do Nothing</td>
<td>The possible values are: Do Nothing, Deploy to Target Directory.</td>
</tr>
<tr>
<td title="Target Directory">Target Directory</td>
<td>Target directory where the resource is to be deployed. Use / to separate multiple names. Only available when the selected Deploy Action is Deploy to Target Directory.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Runtime Path">Runtime Path</td>
<td>Path where the resource is to be deployed.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Resource Content">Resource Content</td>
<td>Image content.</td>
<td>Yes</td>
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
</tbody>
</table>

## Runtime Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Read Only</th>
<th>Type</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td>URL</td>
<td>The runtime URL of the resource.</td>
<td>Yes</td>
<td>Text</td>
<td>Only available in mobile apps.</td>
</tr>
<tr>
<td>Content</td>
<td>Binary content of the file specified in the widget.</td>
<td>Yes</td>
<td>Binary Data</td>
<td></td>
</tr>
</tbody>
</table>

