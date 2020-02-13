---
kinds: ServiceStudio.Model.Nodes+JSONSerialize+Kind
helpids: 30002
---

# JSON Serialize

Serializes an OutSystems object to a JSON string.  

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
<td title="Data">Data</td>
<td>Record or List with the data to be serialized to a JSON string.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Serialize Default Values">Serialize Default Values</td>
<td>Set to Yes to serialize non-mandatory JSON attributes with a default value set.</td>
<td>Yes</td>
<td>No</td>
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
<td>JSON</td>
<td>String in JSON format.</td>
<td></td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

