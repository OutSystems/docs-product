---
kinds: ServiceStudio.Model.Nodes+WebEntry+Kind
helpids: 4001
---

# Entry

Defines the UI flow entry and represents a well-known URL public address.  

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
<td title="Is Default">Is Default</td>
<td>Set to Yes to make this entry the starting point of the module.</td>
<td>Yes</td>
<td>Yes</td>
<td>The entry will redirect to the screen it points to.</td>
</tr>
</tbody>
</table>

