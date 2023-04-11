---
kinds: ServiceStudio.Model.Nodes+ForEach+Kind
helpids: 7004
locale: en-us
guid: 6a3422fb-fc3c-429b-9a52-cd0054520ac5
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# For Each

The For Each Tool repeats the execution of an action path for each entry in a Record List. By default the start index is at the beginning of the list, but you can define it in **Start Index**. **Maximum Iterations** will limit the number of cycles.  The Current variable inside the cycle represents the element of the current iteration. The loop action connector is labeled **Cycle**, while the exit connector has no label. You can swap the connectors by selecting **Swap Connectors** in the menu that shows after right-clicking on the connector.

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

