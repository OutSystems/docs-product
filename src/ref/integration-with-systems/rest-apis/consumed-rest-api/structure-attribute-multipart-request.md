---
summary: OutSystems 11 (O11) includes a structure attribute for handling REST API multipart requests, detailing properties like Name, Description, and Data Type.
tags: rest api, api development, data structuring, api integration, json
locale: en-us
guid: DE3E8594-E1DF-416D-969A-91C522B637B8
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
helpids: 30452
figma:
audience:
  - backend developers
  - full stack developers
  - mobile developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Structure Attribute - REST API Multipart Request

Attribute belonging to a structure used in input arguments of REST API Multipart Requests. For more information on Multipart Requests, see [Consuming a REST API with a multipart/form data method](../../../../integration-with-systems/rest/consume-rest-apis/consume-multipart-form-data.md).  

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
<td>Text literal or expression used as a tooltip when hovering the image or displayed when the image cannot be displayed.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Type">Data Type</td>
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
</tbody>
</table>

