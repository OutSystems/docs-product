---
kinds: ServiceStudio.Model.Nodes+ExecuteAction+Kind
helpids: 30107
---

# Run Server Action

Executes an action that runs logic on the server side.  

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
<td title="Action">Action</td>
<td>Action with logic to run on the server.</td>
<td>Yes</td>
<td></td>
<td>It might be necessary to specify additional action input arguments.</td>
</tr>
<tr>
<td title="Animation Effect">Animation Effect</td>
<td>Type of animation applied to the widget when refreshed.</td>
<td>Yes</td>
<td>None</td>
<td>The possible values are: None, Highlight, Fade, Vertical Slide.</td>
</tr>
<tr>
<td title="Server Request Timeout">Server Request Timeout</td>
<td>Maximum time in seconds to wait for the Execute Action to complete before triggering a Communication Exception. Overrides the default timeout defined on the module.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

