---
kinds: ServiceStudio.Plugin.RESTService.RestServiceActionDescriptor
helpids: 17226
locale: en-us
guid: 259604df-5c74-4e48-b673-cf10be6f3e07
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# REST API Method

Method of an exposed REST API.  

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
<td title="URL">URL</td>
<td>Relative URL where the method is made available.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="URL Path">URL Path</td>
<td>Customized URL for the method. Use it in order to follow RESTful principles identified by your organization.</td>
<td></td>
<td></td>
<td>Due to a limitation in .NET stack, the last part of the URL (i.e. the part after the last '/' character) cannot contain a '.' character, otherwise method calls will not work.</td>
</tr>
<tr>
<td title="HTTPMethod">HTTP Method</td>
<td>HTTP verb to access this method.</td>
<td>Yes</td>
<td>GET</td>
<td>The possible values are: GET, PUT, POST, DELETE.</td>
</tr>
</tbody>
</table>

