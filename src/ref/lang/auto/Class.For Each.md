---
kinds: ServiceStudio.Model.Nodes+ForEach+Kind
helpids: 7004
---

# For Each

Executes the same logic over each item of a list.  

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
<td title="Label">Label</td>
<td>Identifies an element in the flow.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Record List">Record List</td>
<td>Holds the list of records to be iterated in the Cycle flow.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Start Index">Start Index</td>
<td>Index of the first List item to iterate. Can be an expression.</td>
<td></td>
<td>0</td>
<td></td>
</tr>
<tr>
<td title="Maximum Iterations">Maximum Iterations</td>
<td>Maximum number of list items to be iterated.</td>
<td></td>
<td><i>Record List.Length</i></td>
<td></td>
</tr>
</tbody>
</table>

