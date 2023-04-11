---
kinds: ServiceStudio.Model.StructureAttribute+Kind, ServiceStudio.Model.SystemActionStructureAttribute+Kind, ServiceStudio.Model.WebReferenceStructureAttribute+Kind, ServiceStudio.Model.ReferenceStructureAttribute+Kind
helpids: 0
locale: en-us
guid: fba19edd-e3b2-4689-a1d9-2d25e0f74852
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Structure Attribute - Deprecated SOAP

Attribute of structure used in input or output parameters of consumed SOAP Web Service Methods.  

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
<tr >
<th colspan="5">JSON Properties</th>
</tr>
<tr>
<td title="Name in JSON">Name in JSON</td>
<td>Attribute name used when serializing or deserializing JSON. If not specified, the value of the Name property will be used.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>Name of the attribute as defined in the WSDL.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Send Default Value">Send Default Value</td>
<td>Send the input parameter value in the response payload if it is holding its default value.</td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td title="Original Description">Original Description</td>
<td>Description of the Web Service as provided in the WSDL.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Original Default Value">Original Default Value</td>
<td>Default value of the attribute defined in the WSDL.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Min. Occurrences">Min. Occurrences</td>
<td>Minimum number of times this element can appear as defined in the WSDL.</td>
<td></td>
<td>1</td>
<td></td>
</tr>
<tr>
<td title="Max. Occurrences">Max. Occurrences</td>
<td>Maximum number of times this element can appear as defined in the WSDL.</td>
<td></td>
<td>1</td>
<td></td>
</tr>
<tr>
<td title="Nillable">Nillable</td>
<td>Set to Yes to allow elements to accept nil values.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
</tbody>
</table>

