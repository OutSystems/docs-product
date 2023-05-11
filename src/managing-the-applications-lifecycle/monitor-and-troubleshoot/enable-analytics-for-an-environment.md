---
summary: Learn how to turn on monitoring in an environment.
tags: support-Integrations_Extensions; support-monitoring; support-monitoring-overview; runtime-traditionalweb
locale: en-us
guid: 7257acb7-f5f1-46a9-a047-ff5a439ae49c
app_type: traditional web apps
platform-version: o11
---

# Enable Analytics for an Environment

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

OutSystems collects analytics about the end-user experience of all applications running in the Production environment. However, you can turn on monitoring in other environments too. This article describes how.

<div class="info" markdown="1">

LifeTime Analytics applies only to Traditional Web applications. For Mobile and Reactive apps, OutSystems enables you to integrate with industry-leading monitoring platforms. Check some of the components available in [OutSystems Forge](https://www.outsystems.com/forge/), such as [New Relic RUM](https://www.outsystems.com/forge/component-overview/6848/new-relic-rum) or [Elastic RUM](https://www.outsystems.com/forge/component-overview/7341/elastic-rum).

</div>

## Example

You want to detect performance issues of the FieldServices application before deploying it to Production. For this, you want the key users of the application to test it in the Quality Assurance environment. To monitor the end-user experience, you want to enable analytics in QA.

To do so, follow these steps:

1. In your LifeTime console (`https://<lifetime_env>/lifetime`), navigate to the **ANALYTICS** area.
1. Click the **Configuration** link below the name of the current environment.
1. On the **Analytics Configuration** page, use the toggle to enable analytics for the Quality Assurance environment.

![](images/enable-analytics-for-an-environment.png)

After these steps, the platform starts collecting analytics about all applications in the Quality Assurance environment.

You can view the collected data in the **ANALYTICS** area.

## Retention policy

LifeTime Analytics has the capability to hold data only for a specific period (for example, for one month or one year), instead of holding all the data. Data older than the defined period will be purged daily. If you have your own analysis tool, you can use the [Performance Monitoring API](../../ref/apis/performancemonitoring-api.md) to collect the data from LifeTime Analytics and keep in LifeTime Analytics only the most recent data.

By default, LifeTime Analytics will hold all data, but the data retention period can be adjusted in the "Platform Configurations" Tab of the [Factory Configuration](https://www.outsystems.com/forge/25/) Application. 

Once you define a value for the data retention period in Factory Configuration, you will lose all data older than the defined period.

If you want to keep this data archive it in another table in your database before changing the data retention period.
