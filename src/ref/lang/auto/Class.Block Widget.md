---
summary: Reference information on the Block widget available for displaying a reusable screen element on a screen.
tags: outsystems-designing-screens; reference; designing-screens; block-widget
kinds: ServiceStudio.Model.NRWebWidgets+WebBlockInstance+Kind, ServiceStudio.Model.NRWebWidgets+ReferenceWebBlockInstance+Kind
helpids: 0
---

# Block Widget

Displays a reusable screen element.  

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

