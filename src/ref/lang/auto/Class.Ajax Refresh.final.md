---
kinds: ServiceStudio.Model.Nodes+AjaxRefresh+Kind
helpids: 0
locale: en-us
guid: 7b8ee1bd-6f84-4af0-b6a4-ea2ff8aaa6e4
app_type: traditional web apps, mobile apps, reactive web apps
---

# Ajax Refresh

Use the **Ajax Refresh** element in your flow to refresh parts of the screen without reloading the entire page.

Keep the following key points in mind when using **Ajax Refresh**:

One element
:   You can only select one element to refresh in each **Ajax Refresh** node. To refresh more than one interface element at the same time wrap them inside a **Container** and then refresh that **Container**.

Ajax Submit
:   Set Ajax Submit as the `Navigation Method` of the Link/Button that triggers the **Ajax Refresh**.

Name
:   The element you want to refresh using **Ajax Refresh** must have a `Name`.

Web Block Preparation
:   If you use **Ajax Refresh** to refresh a **Web Block**, the **Preparation** of the **Web Block** will be re-executed.

Refresh order
:   Multiple **Ajax Refresh** nodes in the same action flow are executed in the order defined in the action flow.

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
<td title="Widget or Web Block">Widget or Web Block</td>
<td>Specifies a widget or block to refresh.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Row Number">Row Number</td>
<td>Number of the row to refresh. If undefined, refreshes all the rows in the widget. Can be an expression.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Animation Effect">Animation Effect</td>
<td>Type of animation applied to the widget when refreshed.</td>
<td>Yes</td>
<td>None</td>
<td>The possible values are: None, Highlight, Fade, Vertical Slide.</td>
</tr>
</tbody>
</table>

