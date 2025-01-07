---
tags: data synchronization, lifecycle management, scheduled tasks, queues, infrastructure management
summary: Explore how to request unscheduled data synchronizations in OutSystems 11 using AI Mentor Studio.
locale: en-us
guid: b67d9ffc-b28f-4e00-8ffc-6544f9d66812
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=929:744
audience:
  - platform administrators
outsystems-tools:
  - ai mentor studio
  - lifetime
coverage-type:
  - apply
---

# How to request a synchronization

<div class="info" markdown="1">

Architecture Dashboard is now AI Mentor Studio.

</div>

Synchronization of data between the AI Mentor Studio LifeTime probe and the AI Mentor Studio SaaS occurs every 12 hours, but you may also request unscheduled synchronizations. 

<div class="info" markdown="1">

There's a daily limit to the number of unscheduled synchronization requests that AI Mentor Studio can process for each infrastructure. You can request up to 5 unscheduled synchronizations after each scheduled synchronization.

</div>

To request an unscheduled synchronization, follow these steps:

1. Go to the AI Mentor Studio LifeTime plugin (`https://<lifetime_environment>/AIMentorStudioProbe/`) and select **Monitor**.

    ![Screenshot of AI Mentor Studio LifeTime plugin showing the Monitor option](images/sync-plugin-monitor-lt.png "AI Mentor Studio LifeTime Monitor")

1. Select **Request Synchronization**.

    ![Screenshot of AI Mentor Studio LifeTime plugin with the Request Synchronization option highlighted](images/sync-plugin-request-lt.png "Request Synchronization Option")

After these steps, the synchronization request enters the **Outbound Queue** as **SyncRequest**.

<div class="info" markdown="1">

Select **Refresh** to update the queues and check changes to the status of **SyncRequest**.

</div>
