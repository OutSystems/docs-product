---
kinds: ServiceStudio.Model.WebWidgets+TableRecords+Kind, ServiceStudio.Model.WebWidgets+ReferenceTableRecords+Kind
helpids: 4042
---

# Table Records Widget

Displays a list in a tabular layout.  

## Properties

<table markdown="1">
<thead>
<tr>
<th>Property</th>
<th>Required Type</th>
<th>Description</th>
<th>Mandatory</th>
<th>Default value</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="Name">Name</td>
<td></td>
<td>Identifies an element in the scope where it is defined, such as a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
</tr>
<tr>
<td title="Source Record List">Source Record List</td>
<td>Record List</td>
<td>Current list of records displayed by the widget.</td>
<td>Yes</td>
<td></td>
<td>The expression used in this property (if present) is evaluated when a widget runtime property is first used (for example, an expression using the list Length runtime property) or when the widget is rendered.</td>
</tr>
<tr>
<td title="Empty Message">Empty Message</td>
<td>Text</td>
<td>Text displayed in the first row of the widget when there are no records to show.</td>
<td></td>
<td>"No items to show..."</td>
<td></td>
</tr>
<tr>
<td title="Line Count">Line Count</td>
<td>Integer</td>
<td>Maximum number of rows to display in the widget.</td>
<td>Yes</td>
<td>50</td>
<td></td>
</tr>
<tr>
<td title="Start Index">Start Index</td>
<td>Integer</td>
<td>Index of the first List item to iterate. Can be an expression.</td>
<td>Yes</td>
<td>0</td>
<td>The expression used in this property (if present) is evaluated before the web screen preparation.</td>
</tr>
<tr>
<td title="Cell Height">Cell Height</td>
<td>Pixels</td>
<td>Height of cells in the table in pixels. Other accepted units are points(pt) or percentage (%). Overrides the style sheet definition.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Cell Spacing">Cell Spacing</td>
<td>Pixels</td>
<td>Space between cells in pixels. Overrides the style sheet definition.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Show Header">Show Header</td>
<td>Boolean</td>
<td>Set as Yes to display the header row of the table.</td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td title="Style Classes">Style Classes</td>
<td></td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"TableRecords"</td>
<td></td>
</tr>
<tr>

<td title="Header Style">Header Style</td>
<td></td>
<td>Specifies one or more style classes to apply to the header of the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"TableRecords_Header"</td>
<td></td>
</tr>
<tr>
<td title="Odd Line Style">Odd Line Style</td>
<td></td>
<td>Specifies one or more style classes to apply to the odd lines of the widget (excluding the header). Separate multiple values with spaces.</td>
<td></td>
<td>"TableRecords_OddLine"</td>
<td></td>
</tr>
<tr>
<td title="Even Line Style">Even Line Style</td>
<td></td>
<td>Specifies one or more style classes to apply to the even lines of the widget (excluding the header). Separate multiple values with spaces.</td>
<td></td>
<td>"TableRecords_EvenLine"</td>
<td></td>
</tr>
<tr class="separator">
<th colspan="5">Extended Properties</th>
</tr>
<tr>
<td title="Property">Property</td>
<td></td>
<td>Name of an attribute to add to the HTML translation for this element.</td>
<td></td>
<td></td>
<td>You can pick a property from the drop-down list or enter free text. The name of the property is not validated by the platform.<br/><br/>Duplicated properties are not allowed. Spaces, " or ' are also not allowed.</td>
</tr>
<tr>
<td title="Value">Value</td>
<td></td>
<td>Value of the attribute.</td>
<td></td>
<td></td>
<td>You can enter the value directly or write expressions using the Expression Editor.<br/><br/>If the Value is empty, the corresponding HTML tag is created as property="property". For example, the nowrap property does not require a value, therefore nowrap="nowrap" is added.</td>
</tr>
</tbody>
</table>

## Runtime Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Read Only</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td>List</td>
<td>Record List</td>
<td>Collection of records returned by the performed query.</td>
<td></td>
<td></td>
</tr>
<tr>
<td>LineCount</td>
<td>Integer</td>
<td>Maximum number of rows displayed in the widget as defined in the Line Count property.</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td>StartIndex</td>
<td>Integer</td>
<td>Index of the first record displayed in the widget as defined in the Start Index property.</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td>Id</td>
<td>Text</td>
<td>Identifies the widget instance at runtime (HTML 'id' attribute). You can use it in JavaScript and Extended Properties.</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

