---
summary: The On Application Ready action initializes app settings during the home module load in Mobile and Reactive Web Apps
kinds: ServiceStudio.Model.SystemClientActions+OnApplicationReady+Kind
tags:
locale: en-us
guid: b89718c6-8e22-4481-a4ea-6481e349e206
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=612:322
summary: The On Application Ready action initializes app settings during the home module load in Mobile and Reactive Web Apps
---
# On Application Ready

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

Your app runs the **On Application Ready** during the loading of the home module. Use **On Application Ready** to set up the app, for example, to initialize variables and mobile plugins.

Up to Platform Server version 11.16.0, the **On Application Ready** action runs asynchronously, and doesn't block the render of the screens.
On Platform Server version 11.16.1 and higher, the **On Application Ready** action runs synchronously and blocks screen render.

Note that **On Application Ready** by design runs only during the loading of the home module. This means that the app ignores this action in the non-home modules.

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

