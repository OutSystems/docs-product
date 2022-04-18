---
kinds: ServiceStudio.Plugin.Widgets.FormDescriptor
helpids: 17194
tags: runtime-traditionalweb
locale: en-us
guid: 0e4bedbe-6a83-44f4-8c55-969878cb2fc4
app_type: traditional web apps
---

# Form Widget

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

Groups a set of input widgets sharing the same validation context. A common usage for this widget is to group the several inputs of an Entity or Structure record in a screen to create or update that record.

The layout of this widget is flexible, allowing you to organize the widgets inside the way you need.

All enabled inputs inside the form will have the following behaviors:

* When the mouse hovers over the input, an icon appears inside the input indicating that the value is editable.
* After changing a value in one input, an undo action becomes available allowing the end user to revert the value to the original one.

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
<td title="SourceRecord">Source Record</td>
<td>Specifies a record to populate the widget.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Width">Width</td>
<td>Width of the widget in columns. Other accepted units are pixels(px), points(pt), or percentage(%). Overrides the style sheet definition.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="MarginLeft">Margin Left</td>
<td>Left margin of the widget in columns. Other accepted units are pixels(px), points(pt), or percentage(%). Overrides the style sheet definition.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="MarginTop">Margin Top</td>
<td>Top margin of the widget in pixels. Other accepted units are points(pt) or percentage(%). Overrides the style sheet definition.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="LabelsPosition">Label Position</td>
<td>Specifies the relative position of the labels in the form.</td>
<td>Yes</td>
<td>Above Input</td>
<td></td>
</tr>
<tr>
<td title="Style">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td>Form</td>
<td></td>
</tr>
<tr>
<td title="IsEditable">Enabled</td>
<td>Boolean literal or expression that defines if the widget is editable.</td>
<td>Yes</td>
<td>True</td>
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
<td>Id</td>
<td>Identifies the widget instance at runtime (HTML 'id' attribute). You can use it in JavaScript and Extended Properties.</td>
<td>Yes</td>
<td>Text</td>
<td></td>
</tr>
<tr>
<td>Record</td>
<td></td>
<td></td>
<td>Record</td>
<td></td>
</tr>
<tr>
<td>Valid</td>
<td>False when required inputs are not present or the input value does not comply with the defined data type. You can override this property value when performing custom validations.</td>
<td>Yes</td>
<td>Boolean</td>
<td></td>
</tr>
</tbody>
</table>

