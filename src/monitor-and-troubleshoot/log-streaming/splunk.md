---
summary: Explore how to stream logs from OutSystems 11 (O11) applications to Splunk using OpenTelemetry Collector setup and configuration.
tags: outsystems, splunk, opentelemetry, logging, application performance management
locale: en-us
guid: 55b2e20c-fcbb-41d0-b01b-af9f007132b8
app_type: traditional web apps, mobile apps, reactive web apps
figma:
platform-version: o11
audience:
  - platform administrators
  - full stack developers
  - tech leads
outsystems-tools:
  - platform server
  - lifetime
coverage-type:
  - apply
---

# Stream logs to Splunk

This article explains how you can set up log streaming from OutSystems applications to the **Splunk** APM tool.

## Prerequisites

* Installed Platform Server version 11.23.1 or higher.

* Installed LifeTime version 11.19.0 or higher.

* Enabled [Log separation](../../setup-infra-platform/setup/logging-db/logs-separation-cloud/intro.md). 

## Set up

To configure the OutSystems log streaming service, using **Splunk** as the destination tool, follow these steps:

1. Set up the HTTP Event Collector on Splunk (refer [here](https://docs.splunk.com/Documentation/Splunk/9.2.1/Data/UsetheHTTPEventCollector) for instructions).

1. Set up the [OpenTelemetry Collector](configure-collector.md).

1. Configure a receiver that accepts HTTP or gRPC connections (see an example at https://github.com/open-telemetry/opentelemetry-collector/blob/main/receiver/otlpreceiver/README.md) and that uses the Splunk Exporter (refer [here](https://github.com/signalfx/splunk-otel-collector/tree/main/examples/otel-logs-splunk) for example).

1. Change the collector version to the most recent release in the **docker-compose.yml** file, change the image parameter [http://quay.io/signalfx/splunk-otel-collector:0.67.0](https://quay.io/repository/signalfx/splunk-otel-collector?tab=tags&tag=0.67.0) to the latest numerated image found.

1. Get the OpenTelemetry Collector endpoint and authentication credentials.

Once you've completed these steps, go to LifeTime and [configure the log streaming service](lifetime-streaming.md). 

## Additional resources

[Get started with the Splunk Distribution of the OpenTelemetry Collector](https://docs.splunk.com/observability/en/gdi/opentelemetry/opentelemetry.html)  

