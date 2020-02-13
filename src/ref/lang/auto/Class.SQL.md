---
kinds: ServiceStudio.Model.Nodes+AdvancedQuery+Kind
helpids: 9002
---

# SQL

Fetches data from the database using your own SQL statement.  

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
<td title="Timeout">Timeout</td>
<td>Time in seconds after which, if the data request is not fulfilled, the request is aborted and an exception is raised.</td>
<td></td>
<td></td>
<td>If there is no value specified in this property, the timeout corresponds to the "Default query timeout" parameter specified in the Platform Server Configuration Tool.</td>
</tr>
<tr>
<td title="Cache in Minutes">Cache in Minutes</td>
<td>Maximum time content or results are stored in memory. When undefined, nothing is cached.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Max. Records">Max. Records</td>
<td>Maximum number of records read from the database. The SQL statement is not changed by this setting; the limit applies only to the results received from the database.</td>
<td></td>
<td></td>
<td>If undefined, the default value is:<br/>
        – In widgets: StartIndex + LineCount + 1;<br/>
        – Exporting to Excel: No limit.</td>
</tr>
<tr>
<td title="Statement">Statement</td>
<td>SQL statement to fetch data from the database.</td>
<td></td>
<td>SELECT </td>
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
<td>List</td>
<td>The records returned by the query.</td>
<td></td>
<td>Record List</td>
<td></td>
</tr>
<tr>
<td>Count</td>
<td>Number of records returned by the Count query.</td>
<td></td>
<td>Long Integer</td>
<td></td>
</tr>
</tbody>
</table>

