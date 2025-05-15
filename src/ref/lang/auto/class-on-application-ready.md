---
summary: OutSystems 11 (O11) includes an "On Application Ready" action that initializes settings and blocks screen rendering until complete.
locale: en-us
guid: b89718c6-8e22-4481-a4ea-6481e349e206
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=612:322
tags: application initialization, screen rendering, system events, client actions, ide usage
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
topic:
  - system-events
---

# On Application Ready

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

The **On Application Ready** action runs when navigating to a module. Use **On Application Ready** to set up the app, for example, to initialize variables and mobile plugins.

**On Application Ready** action runs synchronously and blocks the screen render. This means that when navigating to a module for the first time, the accessed screen will render only after **On Application Ready** completes.

After the first execution, navigations between screens from the same module don't trigger **On Application Ready**. This includes navigating to other screens using 
[External Site](class-external-site.md) or [Destination](class-destination.md), navigating back to a previous screen, etc. However, if you navigate to a screen of a different module, the **On Application Ready** of that module is executed.

Note that **On Application Ready** is executed if the user types or refreshes the url of a screen directly in the browser address bar. This causes the corresponding module to reload.

To add the **On Application Ready** action to a Mobile or Reactive Web App do the following in Service Studio:

1. In the home module of your app, open the **Logic** tab.

1. Right-click the **Client Actions** node in the tree and select **Add System Event** > **On Application Ready**.

    ![Screenshot showing how to add the On Application Ready system event in Service Studio by right-clicking the Client Actions node and selecting Add System Event > On Application Ready](images/ss-add-system-event-reactive.png "Adding On Application Ready System Event in Service Studio")

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
