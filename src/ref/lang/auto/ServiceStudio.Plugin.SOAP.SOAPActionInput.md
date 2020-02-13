---
kinds: ServiceStudio.Plugin.SOAP.SOAPActionInputDescriptor
helpids: -1
---

# Input Parameter (Consumed SOAP Method)

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
<td title="Type">Data Type</td>
<td>The data type of the input parameter.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="IsMandatory">Is Mandatory</td>
<td>Identifies if the parameter is mandatory or not.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr class="separator">
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="DefaultValue">Default Value</td>
<td>Initial value of this element. If undefined, the default value of the data type is used.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="DefaultValueBehavior">Send Default Value</td>
<td>Send the input parameter value in the response payload if it is holding its default value.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="OriginalNamespace">Original Namespace</td>
<td>Namespace as defined in the WSDL.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="OriginalName">Original Name</td>
<td>Name of the input parameter as defined in the WSDL.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="OriginalDescription">Original Description</td>
<td>Description of the input parameter as provided in the WSDL.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="OriginalType">Original Type</td>
<td>Type of the attribute as defined in the WSDL.</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="OriginalDefaultValue">Original Default Value</td>
<td>Default value of the attribute defined in the WSDL.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="MinOccurrencies">Min. Occurrences</td>
<td>Minimum number of times this element can appear as defined in the WSDL.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="MaxOccurrencies">Max. Occurrences</td>
<td>Maximum number of times this element can appear as defined in the WSDL.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Nillable">Nillable</td>
<td>Set to Yes to allow elements to accept nil values.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

