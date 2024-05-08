---
summary: Explore how OutSystems 11 (O11) enhances client-side logic execution in reactive web and mobile apps through the Run Client Action feature.
helpids: 30110
locale: en-us
guid: 3be54d9f-15c8-4e78-8a14-350f5d1f2845
app_type: mobile apps, reactive web apps
platform-version: o11
figma:
---

# Run Client Action

Executes an action that runs logic on the client side. It's available in reactive web and mobile apps only. Dragging the tool on the action flow will open the Select Action dialogue, for selecting an existing action or creating a new action. The action will be listed in **Logic** tab, under **Client Actions**.

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
<td title="Action">Action</td>
<td>Action with logic to run on the client.</td>
<td>Yes</td>
<td></td>
<td>It might be necessary to specify additional action input arguments.</td>
</tr>
</tbody>
</table>

