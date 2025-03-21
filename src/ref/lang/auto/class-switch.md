---
summary: Learn how the Switch Tool in OutSystems 11 (O11) manages action flow paths based on evaluated conditions, including an "Otherwise" fallback.
locale: en-us
guid: bbcf3fc3-e6c7-4d65-b941-2a77b0b885d6
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: action flows, conditional logic, workflow design, visual programming, outsystems development
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Switch

The Switch Tool splits the action flow into two or more paths. The first action path whose connector evaluated as true will run. If none of the connectors is evaluated as True, the **Otherwise** path will execute. Double-click the connector label in the properties pane to open the Expression Editor and set the condition for that connector.

Use the label numbers to arrange the evaluation order (right-click on a connector and select **Move priority up** or **Move priority down**).

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
<tr >
<th colspan="5">Conditions</th>
</tr>
<tr>
<td title="Condition">Condition</td>
<td>Determines the condition that triggers the execution of the current switch link.</td>
<td>Yes</td>
<td></td>
<td>A condition has to be specified for each switch link, except for the Otherwise path.</td>
</tr>
</tbody>
</table>

