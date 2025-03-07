---
summary: Explore the Scheduler tab configurations for OutSystems 11 (O11), including maximum concurrent timers and service port settings.
locale: en-us
guid: 311b549c-496e-40b8-9d2b-4cf8bfe87d1e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: scheduler service, timer configuration, performance optimization, infrastructure configuration, port settings
audience:
  - platform administrators
  - full stack developers
  - frontend developers
  - backend developers
  - infrastructure managers
outsystems-tools:
  - service center
coverage-type:
  - remember
---

# Scheduler tab

The **Scheduler** tab allows you to configure the OutSystems Scheduler Service.

![Screenshot of the Scheduler tab in the Configuration Tool](images/scheduler-tab-ct.png "Scheduler tab")

Configuration | Description | Default value  
---|---|---  
Max. Concurrent Timers | Maximum number of Timers (asynchronous jobs) that can be executed at the same time in each Front-end Server. | `3`  
Scheduler Service Primary Port | The primary port the scheduler service listens to. | `12102`
Scheduler Service Secondary Port | The secondary port the scheduler service listens to. | `12002`
