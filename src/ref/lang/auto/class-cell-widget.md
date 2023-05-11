---
kinds: ServiceStudio.Model.WebWidgets+EditRecordCell+Kind, ServiceStudio.Model.WebWidgets+ShowRecordCell+Kind, ServiceStudio.Model.WebWidgets+TableCell+Kind, ServiceStudio.Model.WebWidgets+TableRecordsDataCell+Kind, ServiceStudio.Model.WebWidgets+TableRecordsHeaderCell+Kind, ServiceStudio.Model.WebWidgets+ReferenceEditRecordCell+Kind, ServiceStudio.Model.WebWidgets+ReferenceShowRecordCell+Kind, ServiceStudio.Model.WebWidgets+ReferenceTableCell+Kind, ServiceStudio.Model.WebWidgets+ReferenceTableRecordsDataCell+Kind, ServiceStudio.Model.WebWidgets+ReferenceTableRecordsHeaderCell+Kind
helpids: 0
locale: en-us
guid: c6a8d1ee-69f8-4864-b318-45e927008881
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Cell Widget

Cell of a table.  

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
<td title="Height">Height</td>
<td>Height of the widget in pixels. Other accepted units are points(pt) or percentage(%). Overrides the style sheet definition.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Vertical Alignment">Vertical Alignment</td>
<td>Specifies the relative vertical alignment of the widgets inside the cell.</td>
<td>Yes</td>
<td></td>
<td>The possible values are: "" (use default alignment), "Top", "Middle", "Bottom".</td>
</tr>
<tr>
<td title="Style Classes">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Column Span">Column Span</td>
<td>Indicates the number of columns that the cell spans across. Merge or split cells using the right-click contextual menu.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Row Span">Row Span</td>
<td>Indicates the number of rows that the cell spans across. Merge or split cells using the right-click contextual menu.</td>
<td></td>
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

