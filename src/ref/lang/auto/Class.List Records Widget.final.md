---
kinds: ServiceStudio.Model.WebWidgets+ListRecords+Kind, ServiceStudio.Model.WebWidgets+ReferenceListRecords+Kind
helpids: 4023
tags: runtime-traditionalweb
locale: en-us
guid: bd15fc86-95cb-4875-a4e6-dd2e4e0e0faf
app_type: traditional web apps
---

# List Records Widget

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

List Records widget displays the records in a list layout. After you drag this widget to the Screen, you need to supply data to it and set up how records show. 

![List Records Widget overview](<images/list-records.png?width=600>)

Here are some additional notes.

1. Find List Records in the widget toolbox and drag it to the main editor, just like other widgets.
2. Use the **Line Separator** property to set up how the list shows in the Screen. You can separate the records by a new line, bullets, or not separate them at all.
3. The **Preparation** Action is often used to supply data to the widgets in Traditional Web App.
4. In our example, we dragged the FirstName and LastName Attributes from the related Entity to the List Widget to get a full name in one line. We set the **Line Separator** to **New Line**. The main editor shows a preview of the list, but make sure you try it out by publishing your app as well. 

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
<td title="Source Record List">Source Record List</td>
<td>Current list of records displayed by the widget.</td>
<td>Yes</td>
<td></td>
<td>The expression used in this property (if present) is evaluated when a widget runtime property is first used (e.g. an expression using the list Length runtime property) or when the widget is rendered.</td>
</tr>
<tr>
<td title="Empty Message">Empty Message</td>
<td>Text displayed in the first row of the widget when there are no records to show.</td>
<td></td>
<td>"No items to show..."</td>
<td></td>
</tr>
<tr>
<td title="Line Separator">Line Separator</td>
<td>Type of separator to display between records.</td>
<td>Yes</td>
<td>New Line</td>
<td>Possible values are: None, New Line and Bullets.</td>
</tr>
<tr>
<td title="Line Count">Line Count</td>
<td>Maximum number of rows to display in this widget.</td>
<td>Yes</td>
<td>50</td>
<td></td>
</tr>
<tr>
<td title="Start Index">Start Index</td>
<td>Index of the first List item to iterate. Can be an expression.</td>
<td>Yes</td>
<td>0</td>
<td>The expression used in this property (if present) is evaluated before the web screen preparation.</td>
</tr>
<tr>
<td title="Style Classes">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"ListRecords"</td>
<td></td>
</tr>
<tr>
<td title="Empty Message Style">Empty Message Style</td>
<td>Style applied to the text defined in the Empty Message property.</td>
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
<tr>
<td>List</td>
<td>Collection of records returned by the performed query.</td>
<td></td>
<td>Record List</td>
<td></td>
</tr>
<tr>
<td>LineCount</td>
<td>Maximum number of rows displayed in the widget as defined in the Line Count property.</td>
<td>Yes</td>
<td>Integer</td>
<td></td>
</tr>
<tr>
<td>StartIndex</td>
<td>Index of the first record displayed in the widget as defined in the Start Index property.</td>
<td>Yes</td>
<td>Integer</td>
<td></td>
</tr>
</tbody>
</table>

