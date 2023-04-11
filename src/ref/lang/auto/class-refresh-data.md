---
kinds: ServiceStudio.Model.Nodes+RefreshQuery+Kind
helpids: 0
locale: en-us
guid: 6cabc6e6-e10d-4777-96ef-894020476cd1
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Refresh Data

Use it to get updated data from the existing data source.

**Note**: This operation is synchronous. This means the execution flow is blocked while the data is being refreshed.

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
<td title="Data Source">Data Source</td>
<td>Specifies the data source to be fetched.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Max. Records">Max. Records</td>
<td>Maximum number of records read from the database.</td>
<td></td>
<td></td>
<td>If undefined, the default value is:<br/>
        – In widgets: StartIndex + LineCount + 1;<br/>
        – Exporting to Excel: No limit.</td>
</tr>
<tr>
<td title="Start Index">Start Index</td>
<td>Index of the first List item to iterate. Can be an expression.</td>
<td></td>
<td></td>
<td>The expression used in this property (if present) is evaluated before the web screen preparation.</td>
</tr>
</tbody>
</table>

