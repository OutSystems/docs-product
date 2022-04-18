---
kinds: ServiceStudio.Model.ProcessNodes+ExecuteProcess+Kind
helpids: 0
locale: en-us
guid: c895ee72-9869-47c1-a51d-5189df376351
app_type: traditional web apps, mobile apps, reactive web apps
---

# Execute Process

When designing the process flow of your process, you can execute another process. Your process flow waits for the executed process to end its execution before following on into the next process activity in the path. This behavior is implemented through the **Execute** process activity which you can drag onto your canvas from the [Process Flow Toolbox](<../../../develop/processes/process-flow/process-flow-toolbox.md>).

The use of the Execute Process allows you to improve the reusability of processes and help you to maintain consistency in the implementation of processes.

An Execute Process has the input parameters and output parameters of the executed process.

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
<td>Text displayed in the back-office when an instance of this Execute Process activity is executed.</td>
<td></td>
<td></td>
<td>If not defined, the displayed text will be the Execute Process activity name.</td>
</tr>
<tr>
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Process">Process</td>
<td>Process that is executed by the process activity.</td>
<td>Yes</td>
<td></td>
<td>Read-only.</td>
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

