---
kinds: ServiceStudio.Plugin.NRWidgets.InputDescriptor
helpids: 30034
summary: Reference information on the Input widget for allowing users to input data on a screen.
tags: outsystems-designing-screens; reference; designing-screens; input-widget; input-data
locale: en-us
guid: d3d73598-1309-489b-a15a-2b9d518a8226
---

# Input


Field that holds the data typed by the user.

At runtime, the value typed by the user is validated against the variable data type.

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
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Prompt">Prompt</td>
<td>Text hint that describes the expected value for the input. Hides when the field has focus or is no longer empty.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="InputType">Input Type</td>
<td>Input element type. Allows a better input control and extra functionality.</td>
<td>Yes</td>
<td>Text</td>
<td>Available types: Text, Password, Number, Time, Date, Date Time, Phone, Email, Search.</td>
</tr>
<tr>
<td title="MaxLength">Max. Length</td>
<td>Maximum number of characters allowed.</td>
<td></td>
<td>50</td>
<td></td>
</tr>
<tr>
<td title="Mandatory">Mandatory</td>
<td>Boolean literal or expression that defines if the widget is required.</td>
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
<td title="Style">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"form-control"</td>
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
<td title="OnChange">On Change</td>
<td>Screen action to be executed or a screen to navigate to when the value of the element changes.</td>
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
<tr>
<td>Valid</td>
<td>False when required inputs are not present or the input value does not comply with the defined data type. You can override this property value when performing custom validations.</td>
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

## Additional Notes

### Rendering Empty Values

If a variable associated with an Input widget doesn't have a defined value, the widget will be rendered by default with no content. 

If you would like to show the default value for the associated variable type (e.g. show "0" in the widget for a variable of type Integer) when there's no defined value for the variable, add the following custom attribute to the widget in the properties editor:

* Property: **show-default-value**  
    Value: **true**

