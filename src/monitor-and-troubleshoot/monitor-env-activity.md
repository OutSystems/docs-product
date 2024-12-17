---
summary: OutSystems 11 (O11) allows monitoring of daily environment activity through the Service Center console, providing detailed application metrics.
tags: environment monitoring, analytics, reporting, performance metrics, configuration
locale: en-us
guid: 5d4aa86a-ec57-46d7-b29f-81c2967bdb0c
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=3200:4027
audience:
  - platform administrators
  - full stack developers
  - frontend developers
outsystems-tools:
  - service center
coverage-type:
  - remember
---

# Monitor the Environment Daily Activity

In OutSystems, you can monitor the daily activity of your environment in the Service Center console (`https://<environment>/ServiceCenter`).

In **Analytics > Daily History** area, you will find the daily reports containing the activity metrics for the applications in the environment.

![Screenshot of the OutSystems Service Center showing the list of daily activity reports](images/monitor-daily-activity-list-sc.png "OutSystems Service Center Daily Activity List")

Selecting the Daily Activity report for a specific date, you will see the daily metrics taken on that day for each application in the environment, such as the number of visitors, distinct users, sessions or errors.

![Detailed view of a daily activity report in the OutSystems Service Center, displaying metrics for a specific date](images/monitor-daily-activity-sc.png "OutSystems Service Center Daily Activity Report")

The Daily Activity reports are generated only if the option **Enable Daily Activity Reports** is enabled in the [environment configuration](https://success.outsystems.com/Documentation/11/Setting_Up_OutSystems/Configure_your_OutSystems_environment). By default, OutSystems enables this option upon installation.
