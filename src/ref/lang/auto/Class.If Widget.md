---
summary: Reference information on the If widget for displaying content on the screen based on a condition.
tags: outsystems-designing-screens; reference; designing-screens; if-widget
kinds: ServiceStudio.Model.NRWebWidgets+If+Kind, ServiceStudio.Model.WebWidgets+If+Kind, ServiceStudio.Model.NRWebWidgets+ReferenceIf+Kind, ServiceStudio.Model.WebWidgets+ReferenceIf+Kind
helpids: 4029
---

# If Widget

Displays content based on a condition.  

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
<td title="Condition">Condition</td>
<td>Boolean literal or expression to decide which content is displayed.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Animate">Animate</td>
<td>Performs an animation on the content when the condition changes its value.</td>
<td>Yes</td>
<td>No</td>
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
<td>Id</td>
<td>Identifies the widget instance at runtime (HTML 'id' attribute). You can use it in JavaScript and Extended Properties.</td>
<td>Yes</td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

