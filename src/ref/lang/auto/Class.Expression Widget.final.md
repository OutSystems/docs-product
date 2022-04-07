---
kinds: ServiceStudio.Model.WebWidgets+InlineExpression+Kind, ServiceStudio.Model.WebWidgets+ReferenceInlineExpression+Kind
helpids: 4020
tags: runtime-traditionalweb
locale: en-us
guid: bc4b0b1b-57cb-49ab-b9de-3d90a5f418c2
---

# Expression Widget


Displays a text literal or an expression evaluation at runtime. For example, the expression can be a combination of values and operators or the result of a function call.

<div class="info" markdown="1">

For more information see the [expression widget](../../lang/auto/ServiceStudio.Plugin.NRWidgets.Expression.final.md) for Mobile and Reactive Web Apps.

</div>

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
<td title="Value">Value</td>
<td>Combination of values, operands, operators and variables or the result of a function whose value is computed at runtime.</td>
<td>Yes</td>
<td></td>
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
<td title="Style Classes">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Escape Content">Escape Content</td>
<td>Set as No to display directly the results of your expression in the screen content or set to Yes to perform escaping.</td>
<td>Yes</td>
<td>Yes</td>
<td>Escaping an expression means that all accented and other special characters are replaced by a sequence that does not interfere with the protocols being used. In mobile apps expressions are escaped by default.</td>
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

