---
kinds: ServiceStudio.Model.WebWidgets+ShowRecord+Kind, ServiceStudio.Model.WebWidgets+ReferenceShowRecord+Kind
helpids: 4022
tags: runtime-traditionalweb
locale: en-us
guid: d570d3e9-60ad-40d8-a87b-df968ff67d2a
app_type: traditional web apps
---

# Show Record Widget

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

Displays a single record of an Entity or a Structure.

<div class="info" markdown="1">

The layout of the Show Record widget is implemented in a tabular way, which limits the organization of the inputs and its captions. The [Form widget](<ServiceStudio.Plugin.Widgets.Form.final.md>) implements the same functionality with a more flexible layout.

Use the [Form widget](<ServiceStudio.Plugin.Widgets.Form.final.md>) instead of the Show Record widget to display a single record of an Entity or a Structure.

</div>

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
<td title="Source Record">Source Record</td>
<td>Current record being edited in the widget.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Display Columns">Display Columns</td>
<td>Specifies if the widget presents records in one or two columns.</td>
<td>Yes</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td title="Label Width">Label Width</td>
<td>Width of the label in columns. Other accepted units are pixels(px), points(pt), or percentage(%). Overrides the style sheet definition.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Cell Height">Cell Height</td>
<td>Height of cells in the table in pixels. Other accepted units are points(pt) or percentage(%). Overrides the style sheet definition.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Cell Spacing">Cell Spacing</td>
<td>Space between cells in pixels. Overrides the style sheet definition.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Style Classes">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"ShowRecord"</td>
<td></td>
</tr>
<tr>
<td title="Label Style">Label Style</td>
<td>Specifies one or more style classes to apply to labels. Separate multiple values with spaces.</td>
<td></td>
<td>"ShowRecord_Caption"</td>
<td></td>
</tr>
<tr>
<td title="Value Style">Value Style</td>
<td>Specifies one or more style classes to apply to values. Separate multiple values with spaces.</td>
<td></td>
<td>"ShowRecord_Value"</td>
<td></td>
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
<td>Record</td>
<td>Current record being displayed in the widget.</td>
<td>Yes</td>
<td>Record</td>
<td></td>
</tr>
<tr>
<td>Id</td>
<td>Identifies the widget instance at runtime (HTML 'id' attribute). You can use it in JavaScript and Extended Properties.</td>
<td>Yes</td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

