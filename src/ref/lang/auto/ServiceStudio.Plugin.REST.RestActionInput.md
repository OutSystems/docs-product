---
kinds: ServiceStudio.Plugin.REST.RestActionInputDescriptor
helpids: 30080
---

# Input Parameter (REST API Method)

Input parameter of a consumed REST API Method.  

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
<td>Set to Yes to require for a value to be set.</td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="separator">
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="InputPlacement">Send In</td>
<td>Name to use for the parameter in the request. Only available when parameter is sent in the header of the request.</td>
<td>Yes</td>
<td>URL</td>
<td></td>
</tr>
<tr>
<td title="Original Name">Name in Request</td>
<td>Original name of the input parameter that is used in the HTTP request.
If not specified, it has the same value as the Name.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="DefaultValue">Default Value</td>
<td>Initial value of this element. If undefined, the default value of the data type is used.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

