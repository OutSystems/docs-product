---
summary: Learn how to stream logs from OutSystems 11 (O11) applications to New Relic by setting up the necessary configurations and API integrations.
tags: 
locale: en-us
guid: 3155fa32-225e-4925-bf8e-95a0816f62b3
app_type: traditional web apps, mobile apps, reactive web apps
figma: 
platform-version: o11
---

# Stream logs to New Relic

This article explains how you can set up log streaming from OutSystems applications to the New Relic APM tool.

## Prerequisites

* Enabled [Log separation](../../setup-infra-platform/setup/logging-db/logs-separation-cloud/intro.md).

* Installed Platform Server version 11.23.1 or higher.

* Installed LifeTime version 11.19.0 or higher.

## Set up log streaming

To set up the OutSystems log streaming service, using **New Relic** as the destination tool, get the New Relic API key and the location for New relic account (U.S. or EU).

Once you have these values, go to LifeTime and [configure the log streaming service](lifetime-streaming.md). 

<div class="info" markdown="1">
The streaming follows the limits of New Relic's ingestion API. For more information, refer to New Relic's documentation on [Send custom events with our Event API](https://docs.newrelic.com/docs/data-apis/ingest-apis/event-api/introduction-event-api/#limits).   
</div>

## Additional resources

Here are some additional helpful documentation, links, and articles:

* [New Relic API keys](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/)

* [Getting started with OpenTelemetry ](https://docs.newrelic.com/docs/more-integrations/open-source-telemetry-integrations/opentelemetry/get-started/opentelemetry-get-started-intro/)  

* [OpenTelemetry Collector configuration](https://opentelemetry.io/docs/collector/configuration/)
