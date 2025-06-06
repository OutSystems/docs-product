---
summary: Explore the properties and configurations of input parameters in REST API methods in OutSystems 11 (O11).
helpids: 30059
locale: en-us
guid: b9efcc46-e86d-4ca7-b9f2-73d1f9a361db
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: rest api, api development, api management, web services, data types
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - backend developers
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Input Parameter - REST API Method

Input parameter of an exposed REST API Method.  

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
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="ReceiveIn">Receive In</td>
<td>Specifies if the value of the input parameter is to be received in the URL, the Header or Body of the HTTP request.</td>
<td>Yes</td>
<td>URL</td>
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
<td title="ReceiveAs">Name in Request</td>
<td>The parameter name received in the request, for example: Content-Language.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

