---
summary: OutSystems 11 (O11) details the properties of output parameters for SAP remote functions, including data types and documentation features.
helpids: 30067
locale: en-us
guid: 4ce0e5f5-6bad-48f9-9685-88693679ab22
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: sap integration, data mapping, data types, api documentation, system integration
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Output Parameter - SAP Remote Function

Output parameter of an imported SAP remote function.  

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
<tr>
<td title="DefaultValue">Default Value</td>
<td>Initial value of this element. If undefined, the default value of the data type is used.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="OriginalDescription">OriginalDescription</td>
<td>Original description of the parameter.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="OriginalType">Original Type</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="OriginalABAPType">Original ABAP DataType</td>
<td></td>
<td>Yes</td>
<td>Integer</td>
<td></td>
</tr>
</tbody>
</table>

