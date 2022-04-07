---
kinds: ServiceStudio.Plugin.REST.RestActionDescriptor
helpids: 17201
locale: en-us
guid: 936d4e2d-d929-4586-bdf0-ba3cb5fd6cd7
---

# REST API Method

Method of a consumed REST API.  

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
<td title="URL Path">URL Path</td>
<td>URL of the method relative to the Base URL of the REST API. It supports using input parameters enclosed in braces, for example, `/drive/v1/files/{id}?convert={convert}`</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="HTTPMethod">HTTP Method</td>
<td>HTTP verb used in the request.</td>
<td>Yes</td>
<td>GET</td>
<td>The possible values are: GET, PUT, POST, DELETE, PATCH.</td>
</tr>
<tr>
<td title="RequestFormat">Request Format</td>
<td>Content format of the body request. Mandatory for POST, PUT and PATCH HTTP methods.</td>
<td>Yes</td>
<td></td>
<td>The possible values are:<br/>JSON: for JSON content;<br/>Form URL Encoded; for URL-encoded form data;<br/>Binary: for binary content;<br/>Plain Text: for other content like, for example, XML.</td>
</tr>
<tr>
<td title="ResponseFormat">Response Format</td>
<td>Content format of the body response.</td>
<td>Yes</td>
<td></td>
<td>The possible values are:<br/>JSON: for JSON content;<br/>Binary: for binary content;<br/>Plain Text: for other content like, for example, XML.</td>
</tr>
<tr>
<td title="Timeout in Seconds">Timeout in Seconds</td>
<td>Maximum waiting time to get a response from the Web Service. By default is 100 seconds.</td>
<td></td>
<td></td>
<td>The "Duration" field in integration logs can have higher values than the "Timeout in Seconds" value. For more information check [Log data reference](../../../managing-the-applications-lifecycle/monitor-and-troubleshoot/logging/reference.md#integration).</td>
</tr>
</tbody>
</table>

