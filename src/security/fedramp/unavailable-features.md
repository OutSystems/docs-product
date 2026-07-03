---
summary: A reference list of OutSystems 11 features that aren't available in OutSystems FedRAMP, with links to documentation for each feature.
tags:
  - Forge
  - Infrastructure
  - Logging
  - Mentor Studio
  - Mobile app
  - Native App
  - Security
locale: en-us
guid: 9bf5e518-7e13-4b2b-85af-cd3a11adf09c
app_type: traditional web apps, reactive web apps
platform-version: o11
figma:
audience:
  - Developer
  - Architect
  - Platform administrator
outsystems-tools:
  - none
coverage-type:
  - remember
  - evaluate
isautopublish: true
---

# Unavailable features in OutSystems FedRAMP

To meet FedRAMP data residency and flow controls, some features available in the standard OutSystems 11 Cloud offering aren't available in OutSystems FedRAMP.

Review this list before designing or planning projects on OutSystems FedRAMP.

The services in the [OutSystems Cloud services catalog](https://www.outsystems.com/legal/success/cloud-services-catalog/) are available in OutSystems FedRAMP, except where this article notes otherwise. You request these services by opening a support case, because in OutSystems FedRAMP you can't configure them yourself.

For alternative approaches to work around these limitations, refer to [Alternatives to unavailable features in OutSystems FedRAMP](alternatives.md).

## Mobile app builds

[Mobile Apps Build Service (MABS)](../../deploying-apps/mobile-app-packaging-delivery/mobile-apps-build-service/intro.md) isn't available. Native mobile application builds aren't supported in OutSystems FedRAMP.

Build Reactive Web Apps and Progressive Web Apps (PWAs) instead.

## OutSystems tools

The following OutSystems tools aren't available in OutSystems FedRAMP:

* **[AI Mentor Studio](../../monitor-and-troubleshoot/manage-tech-debt/intro.md)**: The AI-powered architecture analysis tool isn't available.
* **[Integration Builder](../../integration-with-systems/integration-builder/intro.md)**: The visual integration builder tool isn't available.
* **[Workflow Builder](../../building-apps/case-management-workflow/workflow-builder/intro.md)**: The workflow builder tool isn't available.

## Connectivity

The following connectivity features aren't available in OutSystems FedRAMP:

* **O11/ODC Connector**: Connections between OutSystems FedRAMP and ODC environments aren't supported. The FedRAMP platform can't link to non-FedRAMP systems.

External database and service connections from your applications are supported at your discretion. These connections fall outside the platform's FedRAMP authorization boundary, so you're responsible for assessing and validating their FedRAMP compliance.

## Infrastructure

**[Cross-Region Disaster Recovery](../../setup-infra-platform/setup/possible-setups/ha-scalability/xrdr.md)** isn't available. High availability across multiple [AWS Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) within the US East region is included for every customer.

## Log streaming

[Log streaming](../../monitor-and-troubleshoot/log-streaming/intro.md) to external Application Performance Monitoring (APM) tools isn't available in OutSystems FedRAMP.

## Forge components

[Forge components](https://www.outsystems.com/forge/) aren't reviewed or certified as FedRAMP-compliant by OutSystems. If you use Forge components, you're responsible for assessing and validating their FedRAMP compliance for your specific use case.

## Service Studio features

Some Service Studio features that aren't compliant with the Federal Information Processing Standards (FIPS), such as feedback submission and AI assistants, are disabled in OutSystems FedRAMP. To disable them, [configure Service Studio for FIPS compliance](getting-started.md#configure-service-studio-for-fips-compliance) on each developer's workstation.

You're responsible for applying this configuration to each Service Studio installation.
