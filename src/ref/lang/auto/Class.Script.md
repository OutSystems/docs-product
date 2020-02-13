---
kinds: ServiceStudio.Model.Script+Kind, ServiceStudio.Model.ReferenceScript+Kind
helpids: 0
---

# Script

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
<td></td>
</tr>
<tr>
<td title="Runtime Path">Runtime Path</td>
<td>Path to the image.</td>
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
<tr>
<td title="JavaScript">JavaScript</td>
<td>JavaScript associated with this element.</td>
<td></td>
<td></td>
<td>Click on "..." to edit the property value.</td>
</tr>
<tr class="separator">
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
<td>The runtime URL of the script.</td>
<td>Yes</td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

