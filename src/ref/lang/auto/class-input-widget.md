---
kinds: ServiceStudio.Model.WebWidgets+Input+Kind, ServiceStudio.Model.WebWidgets+ReferenceInput+Kind
helpids: 4024
tags: runtime-traditionalweb
locale: en-us
guid: 194c0eca-3e99-4ee0-9ffd-d153e14b2225
app_type: traditional web apps
platform-version: o11
---

# Input Widget

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

Field that holds the data typed by the user.

At runtime, the value typed by the user will be validated against the variable data type.

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
<td title="Null Value">Null Value</td>
<td>Value assigned to the variable when no user input is provided.</td>
<td></td>
<td></td>
<td>If this property is not specified, the default value for the data type is used.</td>
</tr>
<tr>
<td title="Max. Length">Max. Length</td>
<td>Maximum number of characters allowed.</td>
<td></td>
<td>50</td>
<td></td>
</tr>
<tr>
<td title="Text Lines">Text Lines</td>
<td>Line-height of the widget.</td>
<td></td>
<td>1</td>
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
<tr>
<td title="Type">Type</td>
<td>HTML5 input element type. Allows a better input control and extra functionality.</td>
<td>Yes</td>
<td>Text</td>
<td>Available element types:<br/>Text: the input allows any text;<br/>Number: the input allows  numeric values;<br/>Email: the input allows email addresses;<br/>Search: the input is used to provide search field.<br/>
        The specific behavior defined by this property value varies from browser to browser.<br/><br/>
        The Date and DateTime types must follow the configurable format specified in the environment console for all the applications. When changing the format, re-publish the modules for the change to take effect.<br/>
        The default format is <code>yyyy-mm-dd</code> (e.g. 2006-03-15).</td>
</tr>
<tr>
<td title="Prompt">Prompt</td>
<td>Text hint that describes the expected value of the input. Hides when the field has focus or is no longer empty.</td>
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
<td>TypedValue</td>
<td>Value entered by the user at the time the input was submitted.</td>
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
<tr>
<td>Id</td>
<td>Identifies the widget instance at runtime (HTML 'id' attribute). You can use it in JavaScript and Extended Properties.</td>
<td>Yes</td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

