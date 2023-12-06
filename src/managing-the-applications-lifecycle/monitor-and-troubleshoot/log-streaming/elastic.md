---
summary: Streaming log data to Elastic
tags: 
locale: en-us
guid: 1b3c1db5-f89c-4ec8-a921-d91cbff3a4ea
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Stream logs to Elastic 

This article explains how you can set up log streaming from OutSystems applications to the **Elastic** APM tool. 

To set up the log streaming to Elastic, you need the **Elastic URL** and **Secret token** values. Once you have these, go to LifeTime and [configure the log streaming service](lifetime-streaming.md). 

## Prerequisites

* Enabled [Log separation](../../../setup-maintain/setup/logging-db/logs-separation-cloud/intro.md).

* Native Elastic APM OpenTelemetry log ingestion is only available in version 8.0 onwards.

* The Elastic Observability services and Kibana plugins must be deployed alongside the Elasticsearch cluster to complete the following steps.

* Installed Platform Server version 11.23.1 or higher.

* Installed LifeTime version 11.19.0 or higher.

## Additional resources

* [Elastic Observability](https://www.elastic.co/observability)

* [OpenTelemetry integration in Elastic](https://www.elastic.co/guide/en/apm/guide/8.6/open-telemetry.html) 

* [OpenTelemetry Collector configuration](https://opentelemetry.io/docs/collector/configuration/)

