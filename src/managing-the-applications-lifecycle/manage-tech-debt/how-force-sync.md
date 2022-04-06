---
tags: 
summary: Learn how to request a synchonization between the probe and Architecture Dashboard.
---


# How to request a synchronization

Synchronization of data between the Architecture Dashboard LifeTime probe and the Architecture Dashboard SaaS occurs every 12 hours, but you may also request unscheduled synchronizations.

<div class="info" markdown="1">

There's a daily limit to the number of unscheduled synchronization requests that Architecture Dashboard can process for each infrastructure. You can request 5 synchronization requests per day. 

</div>

To force a synchronization, follow these steps:

1. Go to the Architecture Dashboard LifeTime plugin (`https://<lifetime_environment>/ArchitectureDashboardProbe/`) and select **Monitor**.

    ![](images/sync-plugin-monitor.png?width=575)

1. Select **Request Synchronization**.

    ![](images/sync-plugin-request.png?width=575)

After these steps, the synchronization request enters the **Outbound Queue** as **SyncRequest**.

<div class="info" markdown="1">

Select **Refresh** to update the queues and check changes to the status of **SyncRequest**.

</div>
