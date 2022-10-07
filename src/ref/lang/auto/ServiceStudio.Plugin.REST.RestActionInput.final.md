---
kinds: ServiceStudio.Plugin.REST.RestActionInputDescriptor
helpids: 30080
locale: en-us
guid: 32eb391b-601d-4332-9f9b-a6844fd5c034
app_type: traditional web apps, mobile apps, reactive web apps
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
<td>Identifies an element in the scope where it is defined, such as a screen, action, or module.</td>
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
<td>Set to Yes to require that a value be set.</td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="InputPlacement">Send In</td>
<td>Name to use for the parameter in the request. Only available when `parameter` is sent in the header of the request.</td>
<td>Yes</td>
<td>URL</td>
<td></td>
</tr>
<tr>
<td title="Original Name">Name in Request</td>
<td>Original name of the input parameter used in the HTTP request.
If not specified, it has the same value as the Name.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="DefaultValue">Default Value</td>
<td>Initial value of this element. If undefined, use the default value of the data type is used.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="LogRedaction">Log Redaction</td>
<td>Set to Yes to hide sensitive information (for example, salary information) in integration logs.</td>
<td>Yes</td>
<td>No</td>
<td>Check <a href="https://success.outsystems.com/Documentation/11/Extensibility_and_Integration/REST/Consume_REST_APIs/Redacting_information_from_REST_API_logs">Redacting information from REST API logs</a>.</td>
</tr>
</tbody>
</table>
