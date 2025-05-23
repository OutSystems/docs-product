---
summary: Explore conditional branching in OutSystems 11 (O11) using the If Tool to manage action flows based on Boolean conditions.
locale: en-us
guid: cc607302-6a99-4463-9756-adab0f7e2ccd
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: conditional branching, action flows, boolean conditions, flow control, service studio features
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# If

The If Tool executes a branch of the action flow if the condition is evaluated as True and another branch if the condition is evaluated as False. To swap the True and False branches, right-click on the element and select **Swap Connectors**. Use the Properties Pane to edit the condition. Use the If Condition window to edit complex expressions. Open it by double-clicking **Condition** in properties pane or right-clicking on the element and selecting **Edit Condition**.

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
<td title="Label">Label</td>
<td>Identifies an element in the flow.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Condition">Condition</td>
<td>Boolean literal or expression to decide which path of the flow to execute.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

