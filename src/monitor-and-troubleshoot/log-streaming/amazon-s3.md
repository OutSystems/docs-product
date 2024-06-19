---
summary: Learn how to stream logs from OutSystems 11 (O11) to Amazon S3 by setting up the OpenTelemetry Collector and configuring the log streaming service.
locale: en-us
guid: af2b3f29-6c76-45f1-9d77-9dc20f774f9f
app_type: traditional web apps, mobile apps, reactive web apps
figma: 
platform-version: o11
---

# Stream logs to Amazon S3

This article explains how you can set up log streaming from OutSystems applications to Amazon S3.

## Prerequisites

* Installed Platform Server version 11.23.1 or higher.

* Installed LifeTime version 11.19.0 or higher.

* Enabled [log separation](../../setup-infra-platform/setup/logging-db/logs-separation-cloud/intro.md).

<div class="info" markdown="1">

Stream to Amazon S3 requires an [OpenTelemetry Collector](configure-collector.md) with a specific [AWS S3 contrib exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awss3exporter#aws-s3-exporter-for-opentelemetry-collector/). 
As of June 2024, the [AWS S3 contrib exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awss3exporter#aws-s3-exporter-for-opentelemetry-collector/) is in [Alpha stability](https://github.com/open-telemetry/opentelemetry-collector#alpha/). 
Customers are advised to assess their use case and learn more before adopting it.

</div>

## Set up log streaming

To set up the OutSystems log streaming service, using Amazon S3 as the destination storage, follow these steps:

1. Set up the [OpenTelemetry Collector](configure-collector.md).

1. Configure a receiver that accepts HTTP or gRPC connections (refer [here](https://github.com/open-telemetry/opentelemetry-collector/blob/main/receiver/otlpreceiver/README.md) for example) and that uses the [AWS S3 contrib exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awss3exporter#aws-s3-exporter-for-opentelemetry-collector/).

1. Get the OpenTelemetry Collector endpoint and authentication credentials.

Once you've completed these steps, go to LifeTime and [configure the log streaming service](lifetime-streaming.md). 

## Additional resources

Here are some additional helpful documentation:

* [OpenTelemetry Collector contrib exporter for Amazon S3](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awss3exporter#aws-s3-exporter-for-opentelemetry-collector/)

* [OpenTelemetry Collector configuration](https://opentelemetry.io/docs/collector/configuration/)
