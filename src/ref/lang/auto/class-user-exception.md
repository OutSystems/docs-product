---
summary: User Exception is a custom exception that you can raise in your logic flows.
locale: en-us
guid: 86c93d94-6b0e-4e83-8797-8b0bebe9f170
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# User Exception


User Exception is a custom exception that you can raise in your logic flows. You can create your own User Exceptions as "children nodes" of the general User Exception. 

For example, you can create a User Exception named `UnavailableExternalSystem` and raise it in your logic when you detect that the external system you use to fetch data in your application is experiencing a downtime.

For more information, check [Handle Exceptions](../../../building-apps/handling-exceptions/intro.md).

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

