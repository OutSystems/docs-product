---
summary: Streaming log data to 3rd party monitoring platforms
tags: 
locale: en-us
guid: 55b2e20c-fcbb-41d0-b01b-af9f007132b8
app_type: traditional web apps, mobile apps, reactive web apps
---

# Stream logs to Splunk

This article explains how you can set up log streaming from OutSystems applications to the **Splunk** APM tool.

## Prerequisites

* Enabled [Log separation](../../../setup-maintain/setup/logging-db/logs-separation-cloud/intro.md). 

* Installed Platform Server version 11.23.1 or higher.

* Installed LifeTime version 11.19.0 or higher.

## Set up log streaming

To configure the OutSystems log streaming service, using **Splunk** as the destination tool, follow these steps:

To configure the OutSystems log streaming service, using Splunk as the destination tool, follow these steps:

1. [Configure Splunk to receive logs](#configure-splunk-to-receive-logs).

2. Set up the [OpenTelemetry Collector](configure-collector.md).

3. Get the OpenTelemetry Collector endpoint and authentication credentials.
Once you've completed these steps, go to LifeTime and configure the log streaming service. 

Once you've completed these steps, go to LifeTime and [configure the log streaming service](lifetime-streaming.md). 

## Configure Splunk to receive logs 

1. Set up the HTTP Event Collector on Splunk (see instructions [here](https://docs.splunk.com/Documentation/Splunk/9.0.1/Data/UsetheHTTPEventCollector)).

1. Set up an OpenTelemetry Collector with a receiver that accepts HTTP or gRPC connections (see example [here](https://github.com/open-telemetry/opentelemetry-collector/blob/main/receiver/otlpreceiver/README.md)) and that uses the Splunk Exporter (see example [here](https://github.com/signalfx/splunk-otel-collector/tree/main/examples/otel-logs-splunk)).

1. Change the collector version to the most recent release in the **docker-compose.yml** file, change the image parameter [http://quay.io/signalfx/splunk-otel-collector:0.67.0](https://quay.io/repository/signalfx/splunk-otel-collector?tab=tags&tag=0.67.0) to the latest numerated image found, for example, [quay.io/signalfx/splunk-otel-collector:0.79.0](https://quay.io/repository/signalfx/splunk-otel-collector?tab=tags&tag=0.77.0).

1. Add a transformation rule in the **otel-collector-config.yml** file by adding the following in the **processors** section.

    ```
    processors: 
    batch:
    transform:
    log_statements:
    - context: log
    statements: 
    - set(body, "Bodyfield is empty") where body == nil
    - set(body, "Bodyfield is empty") where body == ""

    ```

1. Activate the transformation rule in the **otel-collector-config.yml** file by adding transform in the **service/pipelines/logs/processors** section.

    ```
    processors: [batch,
    transform]
   
    ```

## Additional resources

[Get started with the Splunk Distribution of the OpenTelemetry Collector](https://docs.splunk.com/observability/en/gdi/opentelemetry/opentelemetry.html)  

