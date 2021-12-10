---
kinds: ServiceStudio.Model.Nodes+JSONDeserialize+Kind
helpids: 30004
---

# JSON Deserialize

Deserializes a JSON string to an OutSystems object.  

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
<td title="JSON String">JSON String</td>
<td>JSON string with the data to be deserialized to a Record or List.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Data Type">Data Type</td>
<td>List or Structure of the data in the JSON string. If you want to add a Record composed of Attributes of several Entities, you'll have to first create a Structure. </td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Date Format">Date Format</td>
<td>Date format used in the JSON string.</td>
<td>Yes</td>
<td>2014-01-01T00:00:00Z (ISO)</td>
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
<td>Data</td>
<td>The Record or List with the JSON data.</td>
<td></td>
<td>Record, Record List</td>
<td></td>
</tr>
</tbody>
</table>

