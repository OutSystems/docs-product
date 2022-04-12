---
kinds: ServiceStudio.Model.SystemActions+OnSessionStart+Kind
helpids: 0
tags: runtime-traditionalweb
locale: en-us
guid: 6b2deaab-c532-4326-9934-c042c42271de
---

# On Session Start


The OnSessionStart action is triggered by the On Session Start system event when the Session is created or cleared. This occurs in the following situations:

* On the first request to the server
* After the [User_Login](../../apis/auto/users-api.final.md#User_Login) action runs
* After the [User_Logout](../../apis/auto/users-api.final.md#User_Logout) action runs
* After the [TenantSwitch](../../apis/auto/system-actions.final.md#TenantSwitch) action runs

If an action from a [producer module](../../../develop/reuse-and-refactor/expose-and-reuse.md) runs after one of the situations listed above, the OnSessionStart action of that producer module is also executed.

To define the logic of the OnSessionStart action in your module, click **Logic** tab > **Server Actions** > **Add System Event** > **On Session Start**.

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

