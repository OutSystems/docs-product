---
summary: Alternative approaches and workarounds for OutSystems 11 features that aren't available in OutSystems FedRAMP, so you can keep building.
tags:
  - Forge
  - Logging
  - Mobile app
  - Native App
  - Security
  - Technical Debt
  - Workflows
locale: en-us
guid: eefbaa82-854f-480c-9bd1-60de0e955798
app_type: traditional web apps, reactive web apps
platform-version: o11
figma:
audience:
  - Developer
  - Tech lead
outsystems-tools:
  - service studio
coverage-type:
  - understand
  - unblock
isautopublish: true
---

# Alternatives to unavailable features in OutSystems FedRAMP

Some features available in the standard OutSystems 11 Cloud offering aren't available in OutSystems FedRAMP. For the complete list, refer to [Unavailable features in OutSystems FedRAMP](unavailable-features.md).

This article describes alternative approaches that let you keep building while staying within the FedRAMP authorization boundary.

## Native mobile apps

Native mobile application builds through the Mobile Apps Build Service (MABS) aren't available. Build Reactive Web Apps and Progressive Web Apps (PWAs) instead. A PWA runs in the device browser, installs to the home screen, and works offline, so it covers most mobile use cases without a native build.

## OutSystems tooling

The visual accelerator tools (AI Mentor Studio, Integration Builder, and Workflow Builder) aren't available. You build the same functionality directly in Service Studio:

* **Integrations**: Build connectors and consume REST or SOAP services directly in Service Studio, instead of generating them with Integration Builder. For more information, refer to [Integrating OutSystems with your ecosystem](../../integration-with-systems/integrate-ecosystem.md)
* **Workflow apps**: Model business processes and task flows with Processes in Service Studio, instead of generating them with Workflow Builder.
* **AI Mentor Studio**: Apply OutSystems architecture and code best practices during development, since AI Mentor Studio isn't available to analyze technical debt after the fact.

## External integrations and AI services

Your applications make external connections at your discretion. Use supported Forge components to connect to Azure, AWS, or other AI and external services. These connections fall outside the FedRAMP authorization boundary, so you're responsible for assessing and validating their FedRAMP compliance.

## Connections to non-FedRAMP systems

The O11/ODC Connector isn't available, and OutSystems FedRAMP can't link to non-FedRAMP systems. There's no workaround that bridges environments. Develop and keep your FedRAMP workloads within OutSystems FedRAMP.

## Cross-region disaster recovery

Cross-Region Disaster Recovery isn't available. High availability across multiple [AWS Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) within your assigned region is included for every customer, so your environment stays available if a single data center fails.

## Log streaming

Log streaming to external Application Performance Monitoring (APM) tools isn't available. Use the built-in monitoring and logs in Service Center and LifeTime to analyze your application and platform log data within OutSystems FedRAMP.

## Forge components

Forge components aren't reviewed or certified as FedRAMP-compliant by OutSystems. If a Forge component meets your needs, assess and validate its FedRAMP compliance for your use case before using it, or build the equivalent functionality yourself in Service Studio.

The following Forge components are mandatory and pre-installed by OutSystems during infrastructure provisioning. OutSystems ensures these components are FedRAMP-compliant:

* [OutSystems Charts](https://www.outsystems.com/forge/component-overview/4141/outsystems-charts-o11)
* [OutSystems UI](https://www.outsystems.com/forge/component-overview/1385/outsystems-ui-o11)
* [OutSystems Maps](https://www.outsystems.com/forge/component-overview/9909/outsystems-maps-o11)
* [OutSystems Sample Data](https://www.outsystems.com/forge/component-overview/4145/outsystems-sample-data-o11)
* [OutSystems Templates Mobile](https://www.outsystems.com/forge/component-overview/4148/outsystems-templates-mobile-o11)
* [OutSystems Templates Reactive](https://www.outsystems.com/forge/component-overview/6335/outsystems-templates-reactive-o11)

These components are installed once during provisioning. To get the latest compliant version, you must trigger updates manually.
