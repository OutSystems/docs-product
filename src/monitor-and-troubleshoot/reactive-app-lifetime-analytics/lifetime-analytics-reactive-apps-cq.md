---
summary: Use runtime performance data from LifeTime Analytics in Code Quality to prioritize fixes and diagnose issues across Reactive and Mobile apps.
tags:
  - Mobile app
  - Monitoring
  - Performance
  - Technical Debt
  - Troubleshooting
locale: en-us
guid: c9f5e3d2-7a4b-4c8e-1d2f-4a6b9c3d5e7f
app_type: reactive web apps, mobile apps
platform-version: o11
figma:
audience:
  - Developer
  - Architect
  - Platform administrator
outsystems-tools:
  - lifetime
  - code quality
coverage-type:
  - understand
  - apply
  - unblock
isautopublish: true
---

# Using performance analytics in Code Quality

<div class="info" markdown="1">

**Beta feature.** Behavior and UI may change before general availability. For more information, refer to [Technical Preview Features](https://success.outsystems.com/support/release_notes/technical_preview_features/).

</div>

Once you enable performance analytics for Reactive and Mobile apps in Lifetime, Code Quality uses this data to enhance your findings report and help you prioritize findings that affect performance. Average runtime durations appear in findings and are linked to Lifetime analytics for detailed analysis. High values are highlighted in red, and affected apps, modules, and patterns display an icon for easy identification.

For more information on how to enable performance analytics for Reactive and Mobile apps, refer to [Performance analytics for Reactive and Mobile apps](lifetime-analytics-reactive-apps-overview.md).

## Prerequisites

Before you begin, verify the following requirements:

* Platform Server version 11.43.0 or higher on the environment where the apps you want to monitor are running

* LifeTime version 11.31.0 or higher

* Monitoring enabled for the target environment in Analytics Configuration

* Code Quality probes version 6.0.0 or higher published on the LifeTime and Code Analysis environments

* **LifeTime Administrator role** to enable Code Quality integration

* **Open and Debug Applications** permission (or higher) to access runtime performance data in your findings. For more information, refer to [Open findings report](../manage-tech-debt/how-works.md#open-findings-report).

## Set up the Code Quality integration

You can enable Code Quality to use runtime performance data by either registering your infrastructure for the first time or updating your existing registration.

### New registration

To register your infrastructure, follow the steps in [Register and setup your infrastructure in Code Quality](https://success.outsystems.com/documentation/11/monitoring_and_troubleshooting_apps/manage_technical_debt/how_to_set_up_code_quality/#register).

### Existing registration

If you've already registered your infrastructure, [update your Code Quality probes](https://success.outsystems.com/documentation/11/monitoring_and_troubleshooting_apps/manage_technical_debt/how_to_update_the_code_quality_probes) to the latest version, then follow these steps:

1. Go to **LifeTime** > **Plugins** > **Code Quality**.

1. Select **Configuration**.

1. Set the **Runtime Performance** probe environment to your production environment as the **Target environment**.  

    You can choose a different environment, however, OutSystems recommends using the Production environment as it contains metrics from user behavior which may surface issues that may not be visible in non-production environments.

1. Select **Save and update**.

After completing these steps it may take up to 12 hours for your runtime performance data to appear in Code Quality. This is because a synchronization needs to occur for data to be sent to the Code Quality SaaS.

## Understanding data differences

When using runtime performance data from LifeTime Analytics in Code Quality, you may notice differences between the two systems. These differences are expected and reflect their different purposes and synchronization cycles.

* **Using different environments.** If the **Runtime Performance** environment is set to an environment different than the one chosen for **Code Analysis**, fixing an issue in the Code Analysis environment won't immediately resolve it in the Runtime Performance environment. You won't see the issue in Code Quality anymore, even though it still exists in the Runtime Performance environment.

* **Values in Code Quality do not match LifeTime Analytics.** The average runtime duration shown on a finding might differ from LifeTime Analytics since LifeTime Analytics synchronizes application performance data every 15 minutes while Code Quality has its own synchronization cadence.

* **Some values on LifeTime Analytics do not show up in Code Quality.** Code Quality displays runtime performance data only when there is a relevant finding and runtime performance data from the past 7 days is available in LifeTime Analytics. For broader insights on runtime performance across your infrastructure, refer to [Performance Analytics for Reactive and Mobile apps](lifetime-analytics-reactive-apps-overview.md).

## Troubleshooting

### You cannot choose the same environment for the code analysis probe and runtime performance probe

This selection is not supported. Choose a different environment for the runtime performance probe.

### No environments are listed in the runtime performance probe dropdown

Ensure there is at least one environment other than the one you chose for code analysis where you've enabled LifeTime Analytics.

### You have chosen an environment and allowed synchronization, but no data appears in Code Quality

Code Quality needs a synchronization to occur before it can request runtime performance data. During this sync, Code Quality LifeTime notifies the Code Quality SaaS that you've configured the runtime performance probe. After this
notification, the Code Quality SaaS starts collecting runtime performance data
from your probes.

### No data appears after waiting and multiple synchronizations

If data isn't appearing, follow these troubleshooting steps to identify and resolve common issues:

1. **No data on LifeTime Analytics:** Check if LifeTime Analytics is enabled for the environment. If not, enable it.

1. **LifeTime Analytics is enabled but technical preview is not enabled:** Enable the technical preview and resume monitoring on the apps you want to monitor.

1. **Technical preview is enabled but monitoring has not been resumed:** Resume monitoring on the apps you want to monitor.

1. **Monitoring is resumed but the app has not been republished:** Deploy or republish the app in the environment to activate monitoring.

1. **App is republished:** Check if your apps have traffic. Apps without traffic don't generate data.

1. **No recent data on Analytics:** The runtime performance probe only collects data from the past 7 days.

1. **No findings to correlate on Code Quality:** Code Quality only shows runtime performance data when you have findings. For more information, refer to [Performance Analytics for Reactive and Mobile apps](lifetime-analytics-reactive-apps-overview.md).

### Data appears for Traditional Web apps only

Follow the troubleshooting steps in [No data appears after waiting and multiple synchronizations](#no-data-appears-after-waiting-and-multiple-synchronizations) (excluding steps 1 and 2).

### Data appears for some Reactive or Mobile apps only

Follow the troubleshooting steps in [No data appears after waiting and multiple synchronizations](#no-data-appears-after-waiting-and-multiple-synchronizations) (excluding steps 1 and 2).

### No filters are applied when you select **Analyze Technical Debt**

Code Quality doesn't apply the app or module filter if you haven't configured it or if you've excluded it from analysis.

* Make sure you're logged in to the correct infrastructure before selecting **Analyze Technical Debt**.
  
* Confirm you didn't exclude the app or module from analysis.

### The Code Quality probe does not seem to be synchronizing properly or has errors

Refer to [Code Quality troubleshooting](../manage-tech-debt/troubleshoot.md) for additional troubleshooting steps and [Code Quality FAQs](../manage-tech-debt/faq.md) for frequently asked questions.

## Related resources

For more information about Performance Analytics and Code Quality, refer to these resources:

* [Performance analytics for Reactive and Mobile apps](lifetime-analytics-reactive-apps-overview.md):
  Overview and key features.
  
* [How to enable performance analytics for Reactive and Mobile apps](lifetime-analytics-reactive-apps-enable.md):
  Setup and configuration guide.
