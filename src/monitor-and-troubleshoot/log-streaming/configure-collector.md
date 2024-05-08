---
summary: Learn how to set up the OpenTelemetry Collector for APM tools with OutSystems 11 (O11) for enhanced application performance monitoring.
tags:
locale: en-us
guid: ded295b9-7894-4192-a7df-9bf89f1eca25
app_type: traditional web apps, mobile apps, reactive web apps
figma: 
platform-version: o11
---
# Set up the OpenTelemetry Collector

This article explains how to set up the OpenTelemetry collector for Application Performance Monitoring (APM) tools that don't support native ingestion of OpenTelemetry data.

## Prerequisites

* Enabled [Logs separation](../../setup-infra-platform/setup/logging-db/logs-separation-cloud/intro.md). 

* Installed Platform Server version 11.23.1 or higher.

* Installed LifeTime version 11.19.0 or higher.

To receive logs in Datadog or Splunk, you must set up an OpenTelemetry Collector:

1. Download the latest release of the OpenTelemetry Collector Contrib distribution, from [OpenTelemetry’s GitHub repository](https://github.com/open-telemetry/opentelemetry-collector-releases/releases/tag/v0.87.0).

1. Install and deploy the OpenTelemetry Collector.

1. Set up the OpenTelemetry Collector.

    Add the APM tool exporter and security information to the collector config file. The configuration information varies depending on the type of the APM tool.   

1.  Run the OpenTelemetry Collector. 

<div class="info" markdown="1">

* If the OpenTelemetry Collector implementation is OLTP over HTTP, according to the [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otlp/#otlphttp-request) then, the default URL path for requests that carry log data is `v1/logs`. In this case, you must add this path to the URL endpoint in LifeTime, for example: `https://my-colletor.com/v1/logs`.

* To avoid unexpected connection failures, you should keep track and renew the SSL/TLS certificate used in the OpenTelemetry collector before the expiration date.

</div>

## Example file with a basic configuration

The following configuration provides a basic working example for **Datadog**. It secures the OpenTelemetry Collector with basic authentication. 

   ```
    extensions: 
       basicauth/server:
          htpasswd:
            inline:
              user:password

    receivers: 
       otlp:
          protocols:
            grpc:
              auth:
                 authenticator: basicauth/server
    
    exporters:
      datadog:
        api:
          site: <DD_SITE>
          key: <DD_API_KEY>

    service:
      extensions: [basicauth/server]
      pipelines:
        traces: 
          receivers: [otlp]
          exporters: [datadog]
        metrics:  
          receivers: [otlp]
          exporters: [datadog]
        logs:
          receivers: [otlp]
          exporters: [datadog]

   ```
* Replace **DD_SITE** with your **Datadog site**. The default is **datadoghq.com**.

* Replace **DD_API_KEY** with your **Datadog API key**.
