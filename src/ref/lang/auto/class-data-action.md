---
locale: en-us
guid: c1518786-3c7a-4b70-8e10-60eb048fd357
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
summary: OutSystems 11 (O11) enables efficient server-side data fetching with Data Actions after screen loads.
---

# Data Action

Data Actions are server-side processes that fetch complex data from databases or external systems. They execute after the [Screen](../../../building-apps/ui/screens/intro.md) loads, running concurrently with client-side [Aggregates](class-aggregate.md).

<div class="info" markdown="1">

Avoid doing any login operations in Data Actions. Data Actions coincide with other server requests, making it unclear which will ultimately override the cookies.

</div>

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
<td>Useful for documentation purposes.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Server Request Timeout">Server Request Timeout</td>
<td>Maximum time in seconds to wait for the Data Action to return data before triggering a Communication Exception. Overrides the default timeout defined on the module.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Fetch">Fetch</td>
<td></td>
<td>Yes</td>
<td>At start</td>
<td></td>
</tr>
<tr >
<th colspan="5">Events</th>
</tr>
<tr>
<td title="On After Fetch">On After Fetch</td>
<td>Action executed after the aggregate fetches data from the data source.</td>
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
<td>IsDataFetched</td>
<td>True when data has been fetched from the database and is ready to be used.</td>
<td>Yes</td>
<td>Boolean</td>
<td></td>
</tr>
<tr>
<td>HasFetchError</td>
<td>True when there is an error during data fetch due to a server error or communication timeout.</td>
<td>Yes</td>
<td>Boolean</td>
<td></td>
</tr>
</tbody>
</table>
