---
summary: OutSystems 11 (O11) features a Comment Widget for development-time screen annotations and TrueChange™ reminders.
helpids: 30083
tags: development tools, screen design, ui components, application development, truechange
locale: en-us
guid: 59c80eef-8238-406b-b0a4-231ea54d5c4e
app_type: traditional web apps
platform-version: o11
figma:
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Comment Widget

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

Allows you to add a comment to the design of your screen, which is displayed only at development time.

If you set the comment as a reminder, it will be displayed in the TrueChange&#8482; tab.

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
<td title="Text">Text</td>
<td>Text to display.</td>
<td></td>
<td>"Write your comment here"</td>
<td></td>
</tr>
<tr>
<td title="Is Reminder">Is Reminder</td>
<td>Set to Yes to have the comment displayed as a reminder in the TrueChange tab.</td>
<td>Yes</td>
<td>No</td>
<td>The upper-cased keywords TODO, TBD, and REMINDER automatically set the comment as a reminder.</td>
</tr>
</tbody>
</table>
