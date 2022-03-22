---
kinds: ServiceStudio.Model.UserException+Kind
helpids: 0
summary: User Exception is a custom exception that you can raise in your logic flows.
---

# User Exception


User Exception is a custom exception that you can raise in your logic flows. You can create your own User Exceptions as "children nodes" of the general User Exception. 

For example, you can create a User Exception named `UnavailableExternalSystem` and raise it in your logic when you detect that the external system you use to fetch data in your application is experiencing a downtime.

For more information, check [Handle Exceptions](../../../develop/logic/exceptions/intro.md).

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
</tbody>
</table>

