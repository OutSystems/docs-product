---
summary: OutSystems 11 (O11) features the Block Widget, enabling customizable blocks with input parameters on screens.
locale: en-us
guid: 2a9589d1-4484-4a62-aa11-9574fa5e2b17
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: low-code development, user interface components, widget implementation, application development
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Block Widget


Allows you to use a Block in your screen. If the Block is designed with input parameters, you must specify the value for those parameters.

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
<td>Identifies an element in the scope where it's defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Source Block">Source Block</td>
<td>Block to display.</td>
<td>Yes</td>
<td></td>
<td>It might be necessary to specify additional input arguments.</td>
</tr>
</tbody>
</table>

## Runtime properties

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
<td>Id</td>
<td>Identifies the widget instance at runtime (HTML 'id' attribute). You can use it in JavaScript and Extended Properties.</td>
<td>Yes</td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

