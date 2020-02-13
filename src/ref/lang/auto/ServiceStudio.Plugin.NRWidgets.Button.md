---
kinds: ServiceStudio.Plugin.NRWidgets.ButtonDescriptor
helpids: 30040
---

# Button

Widget which triggers an action.  

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
<td title="ConfirmationMessage">Confirmation Message</td>
<td>Text literal or expression to define the confirmation message displayed after clicking this widget.</td>
<td></td>
<td></td>
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
<td title="IsDefault">Is Form Default</td>
<td>Boolean to specify if the button should submit form that is enclosed in.</td>
<td></td>
<td>No</td>
<td>The entry will redirect to the screen it points to.</td>
</tr>
<tr>
<td title="Visible">Visible</td>
<td>Boolean literal or expression that defines if the widget is displayed.</td>
<td>Yes</td>
<td>True</td>
<td></td>
</tr>
<tr>
<td title="Style">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"btn"</td>
<td>The first button dragged to the screen or to the form will have an additional style class 'btn-primary'.</td>
</tr>
<tr class="separator">
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
<td title="OnClick">On Click</td>
<td>Screen action to be executed or a screen to navigate to when the widget is clicked.</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td title="Validation">Built-in Validations</td>
<td>Set to Yes to enable built-in validations for widgets that share the same form or screen with this widget.</td>
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

