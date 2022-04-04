---
kinds: ServiceStudio.Model.WebWidgets+Button+Kind, ServiceStudio.Model.WebWidgets+ReferenceButton+Kind
helpids: 4009
tags: runtime-traditionalweb
---

# Button Widget


Provides a button that users can click or tap to trigger an action, submit data or navigate to another screen.

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
<td title="Label">Label</td>
<td>Text literal or expression to be displayed in this widget.</td>
<td></td>
<td>"Ok"</td>
<td></td>
</tr>
<tr>
<td title="Example">Example</td>
<td>Text to display in Preview and Design modes.</td>
<td></td>
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
<td title="Is Default">Is Default</td>
<td>Set to Yes to define this widget as the screen or block default target when the user presses Enter.</td>
<td>Yes</td>
<td>No</td>
<td>In your web screens or web blocks you can define one default button or link.<br/>When you define a Button or Link widget as default, it means that pressing the <code>ENTER</code> key in an Input, Input Password, Select or Check Box widget has the same effect as pressing the button or the link.</td>
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
<th colspan="5">On Click</th>
</tr>
<tr>
<td title="Destination">Destination</td>
<td>Screen to which to navigate.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Method">Method</td>
<td>Specifies how the inputs are to be submitted.</td>
<td>Yes</td>
<td>Submit</td>
<td>The possible values are:<br/>
        <strong>Submit</strong>: the inputs are submitted. Uses the <code>POST</code> HTTP method;<br/>
        <strong>Ajax Submit</strong>: all the inputs you use in the Destination logic are asynchronously submitted (using Ajax techniques) while keeping the state of the screen;<br/>
        <strong>Navigate</strong>: the inputs are ignored. Uses the <code>GET</code> HTTP method.</td>
</tr>
<tr>
<td title="Validation">Validation</td>
<td>Specifies input validation to be used.</td>
<td>Yes</td>
<td>Server</td>
<td>The possible values are:<br/>
        <strong>Client &amp; Server</strong>: built-in validations are performed before submitting to the server;<br/>
        <strong>Server</strong>: validation is performed server-side;<br/>
        <strong>None</strong>.</td>
</tr>
<tr>
<td title="Confirmation Message">Confirmation Message</td>
<td>Text literal or expression to define the confirmation message displayed after clicking the button.</td>
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
<td>Id</td>
<td>Identifies the widget instance at runtime (HTML 'id' attribute). You can use it in JavaScript and Extended Properties.</td>
<td>Yes</td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

