---
summary: OutSystems 11 (O11) provides a feature to monitor and log Timer activities, accessible through the Service Center with appropriate permissions.
locale: en-us
guid: caf9e5cf-7145-41f9-b6e7-af2f0f7f0652
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=280:3
---

# Monitor Timers

OutSystems logs Timers information so that you can see their past executions, and when they are scheduled to run. These operations are available at Service Center.

You can only view the logs and information of Timers if you have permissions over the corresponding modules. In LifeTime, you must have at least the **List** security level for the app.

To check the Timer's past activity, for example if there was any error during its execution, proceed as follows:

1. Go to **Service Center**.
1. In the **Monitoring** tab, click **Timers**.
1. Use the filters to find the Timer you want.

![Screenshot of the Service Center interface showing the Timers monitoring tab with filters](images/timer-monitor-sc.png "Service Center Timer Monitoring")

To better understand how Timers are handled in OutSystems, check [Use Timers](intro.md).
