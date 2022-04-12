---
kinds: ServiceStudio.Plugin.RESTService.RestServiceDescriptor
helpids: 17225
locale: en-us
guid: 57616b45-1a96-4752-aa4a-dff3dd159a86
---

# REST API

API exposing methods to allow other systems to retrieve or manipulate information through REST.  

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
<td title="Image">Icon</td>
<td>Picture to be displayed to help identify this element.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="URL">URL</td>
<td>Base URL of all REST API methods.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Security</th>
</tr>
<tr>
<td title="HttpSecurity">HTTP Security</td>
<td>Security level required for HTTP requests. Can be overridden by the security level set in the environment or infrastructure.</td>
<td>Yes</td>
<td>SSL/TLS</td>
<td></td>
</tr>
<tr>
<td title="Authentication">Authentication</td>
<td>Required authentication in HTTP requests. The callback action OnAuthentication is made available to implement Basic or Custom authentication.</td>
<td>Yes</td>
<td>None</td>
<td></td>
</tr>
<tr>
<td title="InternalAccess">Internal Access Only</td>
<td>Only users with access to the internal network can access the Web Service.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="ShowDocumentation">Documentation</td>
<td>Set to Yes to automatically generate a documentation page at the REST API base URL.</td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td title="DefaultValueBehavior">Send Default Values</td>
<td>Send the input parameter value in the response payload if it is holding its default value.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="OnRequestCallback">On Request</td>
<td>The action to customize the request before it reaches the REST API methods.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="OnResponseCallback">On Response</td>
<td>The action to customize the response before sending it.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

