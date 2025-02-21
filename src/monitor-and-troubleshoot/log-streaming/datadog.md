---
summary: Learn how to stream logs from OutSystems 11 (O11) to Datadog by setting up the OpenTelemetry Collector and configuring the log streaming service.
tags: log management, application performance monitoring, opentelemetry, api integration, cloud infrastructure
locale: en-us
guid: 2812b9bc-ca11-436f-ac4e-2fc596b9dd61
app_type: traditional web apps, mobile apps, reactive web apps
figma:
platform-version: o11
audience:
  - platform administrators
  - full stack developers
  - backend developers
  - tech leads
outsystems-tools:
  - platform server
  - lifetime
coverage-type:
  - apply
---

# Stream logs to Datadog

This article explains how you can set up log streaming from OutSystems applications to the Datadog APM tool.

## Prerequisites

Before streaming logs to Datadog, ensure you have: 

* Enabled [Log separation](../../setup-infra-platform/setup/logging-db/logs-separation-cloud/intro.md). 

* Installed Platform Server version 11.23.1 or higher (recommended Platform Server version is 11.30.0 or higher).

* Installed LifeTime version 11.19.0 or higher (recommended LifeTime version is 11.25.0 or higher).

* Have subscription to log streaming. Contact your Account Manager for provisioning.

## Set up log streaming

To set up the OutSystems log streaming service, using Datadog as the destination tool, follow these steps:

1. Get the Datadog API key.

1. Set up the [OpenTelemetry Collector](configure-collector.md) with Datadog as the exporter.

1. Get the OpenTelemetry Collector endpoint and authentication credentials.

Once you've completed these steps, go to LifeTime and [configure the log streaming service](lifetime-streaming.md). 

## Additional resources

Here are some additional helpful documentation, links, and articles:

* [Datadog API and Application Keys](https://docs.datadoghq.com/account_management/api-app-keys/)

* [OpenTelemetry in Datadog](https://docs.datadoghq.com/opentelemetry/)

* [OpenTelemetry Collector configuration](https://opentelemetry.io/docs/collector/configuration/)
