---
kinds: ServiceStudio.Plugin.NRWidgets.DropdownDescriptor
helpids: 30036
summary: Reference information on the Dropdown widget for showing a dropdown list for the users to select a value on the screen.
tags: outsystems-designing-screens; reference; designing-screens; drop-down
locale: en-us
guid: 15a7a421-2257-46eb-b995-caff2bf6404f
---

# Dropdown


Use the Dropdown Widget to create drop-down lists in your Mobile and Reactive Web Apps.

With the Dropdown Widget you can implement two types of lists:

* Simple list with text only, when you set **Options Content** to **Text Only**. These is the most common type of lists, rendered with the `<select>` HTML tag. It provides native look and feel in the devices.
* Custom list with other Widgets, when you set **Options Content** to **Custom**. Use them to build a list from, for example, images or other widgets. These lists are rendered with the `<div>` HTML tag.




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
<td>Identifies an element in the scope where it's defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Variable">Variable</td>
<td>Holds the value entered by the user.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="List">List</td>
<td>Specifies the list of records to show in the dropdown.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="DropdownMode">Options Content</td>
<td>'Text (Default)' content provides a native experience for selecting textual values (uses the select HTML tag). 'Custom' provides richer content with non-textual widgets (for example, images) inside the dropdown (uses the div HTML tag).</td>
<td>Yes</td>
<td>Custom</td>
<td></td>
</tr>
<tr>
<td title="Labels">Options Text</td>
<td>Attribute of the records in the list to use as the label.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Values">Options Value</td>
<td>Attribute of the records in the list to use as the identifier of the selected value.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Mandatory">Mandatory</td>
<td>Boolean literal or expression that defines the obligatoriness of the widget.</td>
<td>Yes</td>
<td>False</td>
<td></td>
</tr>
<tr>
<td title="Enabled">Enabled</td>
<td>Boolean literal or expression that defines if the widget is editable.</td>
<td></td>
<td>True</td>
<td></td>
</tr>
<tr>
<td title="EmptyValue">Empty Text</td>
<td>Text literal or expression displayed in the Dropdown list that represents an empty selection. By selecting this option, the variable defined holds a default value.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Style">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"dropdown"</td>
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
<td>You can pick a property from the drop-down list or type a free text. The name of the property isn't validated by the platform.<br/><br/>Duplicated properties aren't allowed. Spaces, " or ' are also not allowed.</td>
</tr>
<tr>
<td title="Value">Value</td>
<td>Value of the attribute.</td>
<td></td>
<td></td>
<td>You can type the value directly or write expressions using the Expression Editor.<br/><br/>If the Value is empty, the corresponding HTML tag is property="property". For example, the nowrap property doesn't require a value, therefore its property is nowrap="nowrap".</td>
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
<td title="OnChange">On Change</td>
<td>Screen action to execute, or a screen to navigate to when the value of the element changes.</td>
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
<td>JavaScript or custom event to handle.</td>
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

## Runtime properties

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
<td>Valid</td>
<td>False when required inputs aren't present or the input value doesn't comply with the defined data type. You can override this property value when performing custom validations.</td>
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
</tbody>
</table>

