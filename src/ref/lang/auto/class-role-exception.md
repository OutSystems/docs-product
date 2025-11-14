---
summary: Learn how OutSystems 11 (O11) automatically creates Role Exceptions for user role management in modules.
locale: en-us
guid: eba380ac-388a-493d-b166-f806e40a09f1
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: role-based access control, user authentication, security, exception handling, permission management
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Role Exception

Role Exception is a custom exception created automatically by OutSystems from each role available in your module.

The name of a Role Exception takes the following form:

`Not <role_name>`

For example, if you create a role named `BackofficeUser` in a module, OutSystems automatically creates a Role Exception named `Not BackofficeUser` in the same module.

Role Exceptions are child nodes of the "Not Registered" System Exception.

## Using a Role Exception

Raise a Role Exception in your logic when a user without the appropriate role tries to perform an action that should only be performed by users with that role.

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
<td title="Role">Role</td>
<td></td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
