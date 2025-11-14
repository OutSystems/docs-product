---
locale: en-us
guid: bec0793d-a9f6-429b-b6dc-a86e4fdb60d3
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=612:324
summary: Implement the "On Application Resume" event in OutSystems 11 (O11) to manage app state upon resuming.
tags: mobile development, application state management, event handling, network availability, outsystems platform
audience:
  - mobile developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
topic:
  - system-events
---

# On Application Resume

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

Action to be executed when the application is returning from background to foreground (in the home module only). Can be used for validating application state when resuming (e.g. checking for network availability).  

To add this action to a Mobile app do the following:

1. In the home module of your app, open the **Logic** tab.

1. Right-click the "Client Actions" node in the tree and select **Add System Event** > **On Application Resume**.

    ![Screenshot showing how to add On Application Resume system event in Service Studio](images/ss-add-system-event-reactive.png "Adding On Application Resume System Event")

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
</tbody>
</table>
