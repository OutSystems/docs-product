---
kinds: ServiceStudio.Plugin.NRWidgets.TableRecordsDescriptor
helpids: 30198
summary: Reference information on the Table widget for displaying data in cells distributed in rows and columns. The tables created with Table Widget support automatic pagination, sorting, and dragging Attributes to add columns.
tags: outsystems-designing-screens; reference; designing-screens; table-widget
---

# Table


Use the Table Widget to display data in cells distributed in rows and columns. The tables created with Table Widget support automatic pagination, sorting, and dragging Attributes to add columns.

This widget is available in Reactive Web Apps.

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
<td title="Source">Source</td>
<td>Specifies a list with records to populate the widget.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="ShowHeader">Show Header</td>
<td>Set as Yes to display the header row of the table.</td>
<td></td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td title="Style">Style Classes</td>
<td>Specifies one or more style classes to apply to the table. Separate multiple values with spaces.</td>
<td></td>
<td>"table"</td>
<td></td>
</tr>
<tr>
<td title="StyleHeader">Style Header</td>
<td>Specifies one or more style classes to apply to the table header. Separate multiple values with spaces.</td>
<td></td>
<td>"table-header"</td>
<td></td>
</tr>
<tr>
<td title="StyleRow">Style Row</td>
<td>Specifies one or more style classes to apply to the table row. Separate multiple values with spaces.</td>
<td></td>
<td>"table-row"</td>
<td></td>
</tr>
<tr >
<th colspan="5">Attributes</th>
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

## Events

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Mandatory</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="OnSort">On Sort</td>
<td>Screen action to be executed to sort the table.</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Transition">Transition</td>
<td>Transition effect applied when navigating to another screen.</td>
<td></td>
<td>By default defined at module level.</td>
</tr>
<tr>
<td title="EventName">Event</td>
<td>JavaScript or custom event to be handled.</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Handler">Handler</td>
<td>JavaScript event handler.</td>
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

