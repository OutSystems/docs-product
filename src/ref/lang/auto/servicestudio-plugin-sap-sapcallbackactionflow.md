---
summary: Explore SAP Callback customization in OutSystems 11 (O11) for SAP remote function calls with properties like Name and Description.
helpids: 30068
locale: en-us
guid: 447f9880-e68f-4858-94ca-8d0b24de4c15
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: sap integration, callback customization, function calls, outsystems platform, outsystems sap
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# SAP Callback

Action that allows the customization of the calls to SAP remote functions. Once defined, they are executed on every call to any SAP remote functions under the connection. There are three available action flows for implementing these customizations: OnBeforeConnection, OnBeforeCall, OnAfterCall (defined in the SAP Connection element).  

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
</tbody>
</table>
