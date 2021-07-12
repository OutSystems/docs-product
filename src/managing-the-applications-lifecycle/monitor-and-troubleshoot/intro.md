---
summary: Understand the current state of an environment and monitor problems impacting end users.
tags: support-devOps; support-monitoring
---

# Monitor and Troubleshoot

To understand the current state of an environment and monitor problems impacting end users, OutSystems allows you to:

* [See the logs](monitoring-an-environment.md) of your OutSystems applications and the environment status.
* [Manage the feedback](../app-feedback/intro.md) submitted by end users.
* [Audit the tasks](monitor-usage-with-audit-logs.md) performed by IT users.

## Built-in Tools

OutSystems provides built-in tools that collect and present data about the platform and the applications running on it.

Service Center Console
:   [Service Center](monitoring-an-environment.md) provides a set of metrics regarding a specific environment. It provides access to application logs and errors, web and mobile requests, integration calls, business processes, and security audits. Additionally, it displays the current status of environment servers and services and allows the creation of aggregation reports over the available data.

 ![Monitoring tools](images/intro-tools-sc.png?width=800)

App Feedback
:   [App Feedback](../app-feedback/intro.md) application lets you manage the feedback from your business users. It allows you to streamline the feedback gathering process and defect tracking.

![Monitoring tools](images/app-feedback-af.png?width=800)

## Extending OutSystems Monitoring Capabilities

OutSystems allows you to extend the built-in monitoring capabilities, as you can:

* Instrument your OutSystems applications for more advanced monitoring using the [Asynchronous Logging API](../../ref/apis/auto/asynchronous-logging-api.final.md) to collect custom logs.

* Create your own OutSystems applications to extend the built-in monitoring capabilities, or reuse the existing components developed by the OutSystems community, available at [OutSystems Forge](https://www.outsystems.com/forge/). For example, [MonitorProbe](https://www.outsystems.com/forge/component-overview/4559/monitorprobe) enables you to expose the platform monitoring data as an API, while [New Relic RUM](https://www.outsystems.com/forge/component-overview/6848/new-relic-rum-for-react) or [Dynatrace RUM](https://www.outsystems.com/forge/component-overview/6850/dynatrace-rum-for-react) enable you to monitor your OutSystems Reactive Web and Mobile applications .

Also, OutSystems exposes the collected data and shares monitoring points that enable you to:

* Use the [PerformanceMonitoring API](../../ref/apis/performancemonitoring-api.md) to integrate with custom or third-party monitoring tools that you may already be using.

* Use your custom-built APIs in your integrations.

## Monitoring Responsibilities

The scope of your monitoring responsibility depends on the [setup of your OutSystems infrastructure](../../setup/possible-setups/intro.md) **on the cloud**.

OutSystems Cloud
:   OutSystems guarantees the monitoring of the infrastructure layer components (servers and networking) and the platform main services in the middleware layer (web servers, deployment controllers, database). The customer is responsible for monitoring application usage (errors and performance), external integrations, end user experience, and business outcomes.

![Monitoring scope](images/intro-cloud-scope-diag.png?width=600)
