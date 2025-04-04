---
summary: Explore the technical properties and behaviors of exposed roles in OutSystems 11 (O11), including transaction exceptions and persistence settings.
helpids: 15004
locale: en-us
guid: 9fc0da79-a220-4620-bcd5-b69331ec3b0c
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: outsystems, user roles, security, role-based access control, exceptions handling
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Role


## Exposed Role

When an exposed Role is checked, it raises an exception under the **transaction** of the Consumer module. 

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
<td title="Public">Public</td>
<td>Set to Yes to allow the element to be added as dependency by other modules.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>Name of the element as defined in the module which implements it (producer module). This property is read-only.</td>
<td>Yes</td>
<td></td>
<td>This property is only visible for referenced elements.</td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Is Persistent">Is Persistent</td>
<td>If set to Yes, the association between the user and the role is stored in the database and is persistent across multiple sessions. If set to No, the role is only associated with the user for a single session. In Reactive Web and Mobile modules, this property is read-only and set to Yes by default.</td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

