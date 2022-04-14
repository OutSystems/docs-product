---
kinds: ServiceStudio.Model.WebWidgets+Container+Kind, ServiceStudio.Model.WebWidgets+EmailContainer+Kind, ServiceStudio.Model.WebWidgets+ReferenceContainer+Kind, ServiceStudio.Model.WebWidgets+ReferenceEmailContainer+Kind
helpids: 4047
tags: runtime-traditionalweb
locale: en-us
guid: f018d411-b8b9-4c20-9744-4807528f9255
---

# Container Widget

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

Container "box" where you can drag and drop other widgets, including other containers, to organize the layout of the screen.

Containers allow you to:

* Group content with the same layout (style, position, etc.)
* Group content with the same behavior (for example, content that must be visible or hidden in the screen at the same time)
* Create a nested structure of content

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
<td title="Style Classes">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Display">Display</td>
<td>Boolean literal or expression that defines if the widget is displayed.</td>
<td></td>
<td>True</td>
<td>Be aware that this property does not have the same behavior as the "Visible" property of other widgets. When set to false, the HTML for the widget is still generated, and can be accessed and manipulated, for example, using JavaScript.</td>
</tr>
<tr >
<th colspan="5">Extended Properties</th>
</tr>
<tr>
<td title="Property">Property</td>
<td>Name of an attribute to add to the HTML translation for this element.</td>
<td></td>
<td></td>
<td>You can pick a property from the drop-down list or type a free text. The name of the property will not be validated by the platform.<br/><br/>Duplicated properties are not allowed. Spaces, " or ' are also not allowed.</td>
</tr>
<tr>
<td title="Value">Value</td>
<td>Value of the attribute.</td>
<td></td>
<td></td>
<td>You can type the value directly or write expressions using the Expression Editor.<br/><br/>If the Value is empty, the corresponding HTML tag is created as property="property". For example, the nowrap property does not require a value, therefore nowrap="nowrap" is added.</td>
</tr>
<tr >
<th colspan="5">On Click</th>
</tr>
<tr>
<td title="Destination">Destination</td>
<td>Screen to which to navigate.</td>
<td></td>
<td></td>
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

