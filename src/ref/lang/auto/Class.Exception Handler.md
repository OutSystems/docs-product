---
kinds: ServiceStudio.Model.Nodes+ErrorHandler+Kind
helpids: 0
---

# Exception Handler

Logic to catch an exception or set of exceptions.  

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
<td title="Exception">Exception</td>
<td>Type of exception to handle.</td>
<td>Yes</td>
<td></td>
<td>There is a call hierarchy for exceptions that determines the error handler behavior. For more info see Exception Handling Mechanism</td>
</tr>
<tr>
<td title="Abort Transaction">Abort Transaction</td>
<td>Set to Yes to abort the transaction and rollback changes.</td>
<td>Yes</td>
<td>Yes</td>
<td>This property is only available in web apps.</td>
</tr>
<tr>
<td title="Log Error">Log Error</td>
<td>Set to Yes to log an error when the exception occurs.</td>
<td>Yes</td>
<td>Yes</td>
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
<td>ExceptionMessage</td>
<td>Text that explains the reason for the last error.</td>
<td>Yes</td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

