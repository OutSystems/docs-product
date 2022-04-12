---
kinds: ServiceStudio.Model.WebWidgets+ComboBox+Kind, ServiceStudio.Model.WebWidgets+ReferenceComboBox+Kind
helpids: 4027
tags: runtime-traditionalweb
locale: en-us
guid: 2ad09f6b-4508-4db2-b84a-3ce248492fc3
---

# Combo Box Widget


Allows the user to select a specific value within a list of possible values.

The list of possible values can be an Attribute of an Entity, an Attribute of a Structure or a list of special values. You can also add special values like "All" and "None" to the list fetched from an Entity or Structure.

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
<td title="Variable">Variable</td>
<td>Holds the value entered by the user.</td>
<td></td>
<td></td>
<td>Mandatory if Source Entity/Structure is specified.</td>
</tr>
<tr>
<td title="Validation Parent">Validation Parent</td>
<td>Specifies an Edit Record widget. Widgets with the same Validation Parent are validated as a group.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Mandatory">Mandatory</td>
<td>Boolean literal or expression that defines if the user input is required.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Source Record List">Source Record List</td>
<td>Current list of records displayed by the widget.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Source Entity">Source Entity</td>
<td>Data entity to populate the widget.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Source Attribute">Source Attribute</td>
<td>Specifies the attribute of the records in the list to populate the widget.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Source Identifier Attribute">Source Identifier Attribute</td>
<td>Attribute of the structure to be used as the identifier of the selected value.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Special Variable">Special Variable</td>
<td>Holds the value selected by the user if this value belongs to the defined Special List.</td>
<td></td>
<td></td>
<td>The variable must be of type Text, Phone Number, Email, Boolean, Integer, or Long Integer.<br/>At runtime, if the user selects a value among the Source Entity/Structure list of values, this property will have the value "".</td>
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
<th colspan="5">On Change</th>
</tr>
<tr>
<td title="Destination">Destination</td>
<td>Screen action to be executed or a screen to navigate to when the value of the element changes.</td>
<td></td>
<td></td>
<td>It might be necessary to specify additional input arguments.</td>
</tr>
<tr >
<th colspan="5">Special List</th>
</tr>
<tr>
<td title="Value">Value</td>
<td>Value assigned to the Special Variable.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Option">Option</td>
<td>Text displayed in the widget.</td>
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
<td>SpecialListValue</td>
<td>SpecialListValue runtime property is deprecated. Consider using the Special Variable property instead.</td>
<td></td>
<td>Text</td>
<td></td>
</tr>
<tr>
<td>Valid</td>
<td>Always True for Combo Boxes. You can override this property value when performing custom validation.</td>
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

