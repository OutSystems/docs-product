---
kinds: ServiceStudio.Model.StructureAttribute+Kind, ServiceStudio.Model.SystemActionStructureAttribute+Kind, ServiceStudio.Model.WebReferenceStructureAttribute+Kind, ServiceStudio.Model.ReferenceStructureAttribute+Kind
helpids: 0
---

# Structure Attribute

Stores part of the information that concerns a structure. Examples of attributes are: customer name, product id, product price.  

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
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Label">Label</td>
<td>Text of the label associated with the input field of this attribute when it is the source of a widget allowing record editing.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Data Type">Data Type</td>
<td>The attribute data type.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Length">Length</td>
<td>Maximum size of the attribute in characters.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Decimals">Decimals</td>
<td>Number of decimal places.</td>
<td></td>
<td></td>
<td>Only available when data type is Decimal (mandatory).</td>
</tr>
<tr>
<td title="Is Mandatory">Is Mandatory</td>
<td>Set to Yes to require for a value to be set.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Default Value">Default Value</td>
<td>Initial value of this element. If undefined, the default value of the data type is used.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="separator">
<th colspan="5">JSON Properties</th>
</tr>
<tr>
<td title="Name in JSON">Name in JSON</td>
<td>Name to use when sending this attribute in the payload of the request.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

