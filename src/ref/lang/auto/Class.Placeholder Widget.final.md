---
kinds: ServiceStudio.Model.NRWebWidgets+Placeholder+Kind, ServiceStudio.Model.WebWidgets+Placeholder+Kind, ServiceStudio.Model.NRWebWidgets+ReferencePlaceholder+Kind, ServiceStudio.Model.WebWidgets+ReferencePlaceholder+Kind
helpids: 17142
summary: Reference information on the Placeholder widget for reserving space in your block for filling when the block is used.
tags: outsystems-designing-screens; reference; designing-screens; placeholder-widget
locale: en-us
guid: 5d21e0a3-fe0a-40cd-827b-a2a1ea1aa5ac
app_type: traditional web apps, mobile apps, reactive web apps
---

# Placeholder Widget


Reserves space in your block for filling when the block is used.

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
<td>Text documenting the widget.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Align">Align</td>
<td>Specifies the horizontal alignment of the widgets inside this widget.</td>
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
<td title="Is Ajax Refreshed">Is Ajax Refreshed</td>
<td>Read-only property informing if the placeholder, or one of its containers, is refreshed by an Ajax Refresh.</td>
<td>Yes</td>
<td>No</td>
<td>This is useful to understand the placeholders design in the web block regarding refreshing their content.</td>
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

