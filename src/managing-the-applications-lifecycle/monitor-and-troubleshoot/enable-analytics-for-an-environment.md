---
summary: Learn how to turn on monitoring in an environment.
tags: support-Integrations_Extensions; support-monitoring; support-monitoring-overview
---

# Enable Analytics for an Environment

OutSystems collects analytics about the end user experience of all applications running in the Production environment. However, you can turn on monitoring in other environments too. This article describes how.

## Example

You want to detect performance issues of the FieldServices application, before deploying it to Production. For this, you want the key users of the application to test it in the Quality Assurance environment. To monitor the end user experience, you want to enable analytics in QA.

To do so, follow these steps:

1. In the infrastructure management console, navigate to the 'Analytics' tab;
1. Then, click the 'Configuration' link below the name of the current environment;
1. In the 'Analytics Configuration' page, use the toggle to enable analytics for the 'Quality Assurance' environment.

![](images/enable-analytics-for-an-environment.png)



After these steps, the platform starts collecting analytics about all applications in the 'Quality Assurance' environment.   
You can view the collected data in the 'Analytics' area.
