---
summary: Explore the structure and properties of REST API Callbacks in OutSystems 11 (O11) for effective integration and documentation.
helpids: 30055
locale: en-us
guid: 5fc67999-8f0f-455d-b611-9a4079cbcc0e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: rest api, api integration, software documentation, api documentation, outsystems api
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Structure - REST API Callback

Structure used in input and output arguments of REST API Callbacks.  

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
</tbody>
</table>

