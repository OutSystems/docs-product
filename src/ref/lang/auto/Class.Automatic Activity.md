---
kinds: ServiceStudio.Model.ProcessNodes+Activity+Kind
helpids: 0
---

# Automatic Activity

Executes an action flow to do work without the intervention of the end-user.  

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
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Label">Label</td>
<td>Text displayed in the back-office when an instance of this Automatic Activity is executed.</td>
<td></td>
<td></td>
<td>If not defined, the displayed text will be the Automatic Activity name.</td>
</tr>
<tr>
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr class="separator">
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Start Date">Start Date</td>
<td>Optional date that defines when the activity is scheduled to become available to be handled. Can be an expression.</td>
<td></td>
<td></td>
<td>Not supported when using Light Process Execution.</td>
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
<td>ClosedInstant</td>
<td>Date and time when the process activity instance was closed.</td>
<td>Yes</td>
<td>Date Time</td>
<td></td>
</tr>
<tr>
<td>ActivityId</td>
<td>Identifier of the process activity instance at runtime.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

