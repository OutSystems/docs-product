---
kinds: ServiceStudio.Model.WebWidgets+ListBox+Kind, ServiceStudio.Model.WebWidgets+ReferenceListBox+Kind
helpids: 4041
---

# List Box Widget

Allows the selection of one or more values from a dropdown list of possible values.  

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
<td title="Validation Parent">Validation Parent</td>
<td>Specifies an Edit Record widget. Widgets with the same Validation Parent are validated as a group.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Source Record List">Source Record List</td>
<td>Current list of records displayed by the widget.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Source Attribute">Source Attribute</td>
<td>Specifies the attribute of the records in the list to populate the widget.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Selection Mode">Selection Mode</td>
<td>Specifies if the user can select only a single item or multiple items from the list.</td>
<td>Yes</td>
<td>Multiple</td>
<td>The possible values are: Multiple and Single.</td>
</tr>
<tr>
<td title="Selection Attribute">Selection Attribute</td>
<td>Boolean attribute of the records in the list that holds if a value is selected or not. If using a list from an Aggregate, you can add a new Boolean attribute in the Aggregate.</td>
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
<td title="Visible">Visible</td>
<td>Boolean literal or expression that defines if the widget is displayed.</td>
<td></td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td title="Enabled">Enabled</td>
<td>Boolean literal or expression that defines if the widget is editable.</td>
<td></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="separator">
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
<tr class="separator">
<th colspan="5">On Change</th>
</tr>
<tr>
<td title="Destination">Destination</td>
<td>Screen action to be executed or a screen to navigate to when the value of the element changes.</td>
<td></td>
<td></td>
<td>It might be necessary to specify additional input arguments.</td>
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
<td>List</td>
<td>Collection of records returned by the performed query.</td>
<td></td>
<td>Record List</td>
<td></td>
</tr>
<tr>
<td>Valid</td>
<td>Always True for List Boxes. You can override this property value when performing custom validation.</td>
<td></td>
<td>Boolean</td>
<td></td>
</tr>
<tr>
<td>ValidationMessage</td>
<td>Message describing the built-in validation constraints not satisfied when 'Valid' is False. You can override this property value when performing custom validations.</td>
<td></td>
<td>Text</td>
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

