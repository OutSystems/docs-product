---
kinds: ServiceStudio.Plugin.RESTService.RestServiceActionOutputDescriptor
helpids: 30060
locale: en-us
guid: 887a371e-106f-46cc-b419-92d929de0dd1
app_type: traditional web apps, mobile apps, reactive web apps
---

# Output Parameter (REST API Method)

Output parameter of an exposed REST API Method.  

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
<td>The data type of the output parameter.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="SendIn">Send In</td>
<td>Indicates whether the output parameter is sent in the HTTP Header or Body.</td>
<td>Yes</td>
<td>Body</td>
<td></td>
</tr>
<tr>
<td title="DefaultValue">Default Value</td>
<td>Initial value of this element. If undefined, the default value of the data type is used.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="SendAs">Name in Response</td>
<td>The parameter name sent in the response, for example: Content-Language.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

