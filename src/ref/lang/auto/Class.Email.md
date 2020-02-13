---
kinds: ServiceStudio.Model.Nodes+EmailScreen+Kind
helpids: 0
---

# Email

Allows defining the content to send by email.  

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
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Subject">Subject</td>
<td>Subject of the email.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr class="separator">
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Style Sheet">Style Sheet</td>
<td>Specifies one or more style classes to apply to the email. Separate multiple values with spaces.</td>
<td></td>
<td></td>
<td>Click on "..." to edit the property value.</td>
</tr>
<tr class="separator">
<th colspan="5">Extended Properties</th>
</tr>
<tr>
<td title="Property">Property</td>
<td>One or more extended properties for enhanced control of email headers (also known as MIME headers).</td>
<td></td>
<td></td>
<td>You can pick a property from the drop-down list or type a free text. The name of the property will not be validated by the platform.<br/><br/>Duplicated properties are not allowed. Spaces, " or ' are also not allowed.</td>
</tr>
<tr>
<td title="Value">Value</td>
<td>Value of the extended property.</td>
<td></td>
<td></td>
<td>You can type the value directly or write expressions using the Expression Editor.<br/><br/>If the Value is empty, the corresponding HTML tag is created as property="property". For example, the nowrap property does not require a value, therefore nowrap="nowrap" is added.</td>
</tr>
</tbody>
</table>

