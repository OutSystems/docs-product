---
summary: OutSystems 11 (O11) defines structured attributes for REST API methods, detailing properties like Name, Type, and Is Mandatory.
helpids: 30058
locale: en-us
guid: 1d89067b-946a-4832-99ec-81c78cb5ca3f
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: rest api, data modeling, attribute configuration, api documentation, web services
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - backend developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Structure Attribute - REST API Method

Attribute of structure used in input and output arguments of REST API Methods.  

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
<tr>
<td title="IsMandatory">Is Mandatory</td>
<td>Set to Yes to require for a value to be set.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr >
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
<td title="NameInJSON">Name in JSON</td>
<td>Name to use when sending this attribute in the payload of the request.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

