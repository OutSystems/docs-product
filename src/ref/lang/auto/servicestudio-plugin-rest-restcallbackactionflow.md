---
summary: OutSystems 11 (O11) supports REST API callback customization through specific action flows, enhancing API integration capabilities.
locale: en-us
guid: 75d5ed76-ed3d-405c-a3a5-e497af70434c
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: rest apis, api integration, callback handling, api customization, action flows
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# REST API Callback

Action used to customize the request/response of a consumed REST API method call. There are four available action flows for implementing these customizations: OnBeforeRequest, OnAfterResponse, OnBeforeRequestAdvanced or OnAfterResponseAdvanced (defined in the consumed REST API element).  

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
