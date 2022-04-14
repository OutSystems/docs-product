---
kinds: ServiceStudio.Model.WebWidgets+EmailWebBlockInstance+Kind, ServiceStudio.Model.WebWidgets+WebBlockInstance+Kind, ServiceStudio.Model.WebWidgets+ReferenceEmailWebBlockInstance+Kind, ServiceStudio.Model.WebWidgets+ReferenceWebBlockInstance+Kind
helpids: 0
tags: runtime-traditionalweb
locale: en-us
guid: 4160f6d7-1bcd-4299-80b7-5ccd8bbc42d2
---

# Web Block Widget

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

Allows you to use a Web Block in your screen. If the Web Block is designed with input parameters, you must specify the value for those parameters.

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
<td title="Source Web Block">Source Web Block</td>
<td>Web block to display.</td>
<td>Yes</td>
<td></td>
<td>It might be necessary to specify additional input arguments.</td>
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
<td>Id</td>
<td>Identifies the widget instance at runtime (HTML 'id' attribute). You can use it in JavaScript and Extended Properties.</td>
<td>Yes</td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

