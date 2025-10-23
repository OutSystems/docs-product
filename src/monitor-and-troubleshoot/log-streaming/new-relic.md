---
summary: Learn how to stream logs from OutSystems 11 (O11) applications to New Relic by setting up the necessary configurations and API integrations.
tags: log management, application performance management (apm), api integration, cloud infrastructure, data ingestion
locale: en-us
guid: 3155fa32-225e-4925-bf8e-95a0816f62b3
app_type: traditional web apps, mobile apps, reactive web apps
figma:
platform-version: o11
audience:
  - platform administrators
  - full stack developers
  - backend developers
  - tech leads
  - infrastructure managers
outsystems-tools:
  - platform server
  - lifetime
coverage-type:
  - apply
---

# Stream logs to New Relic

This article explains how you can set up log streaming from OutSystems applications to the New Relic APM tool.

## Prerequisites

For a complete list of prerequisites, refer to [Introduction to log streaming](intro.md#prerequisites).

## Set up log streaming

To set up the OutSystems log streaming service, using **New Relic** as the destination tool, get the New Relic API key and the location for New relic account (U.S. or EU).

Once you have these values, go to LifeTime and [configure the log streaming service](lifetime-streaming.md).

<div class="info" markdown="1">

Large 'message and 'exception.stacktrace' attribute values are truncated to 4,000 characters before streaming in order to follow New Relic's ingestion API limits. For more information, refer to New Relic's documentation on [Send custom events with our Event API](https://docs.newrelic.com/docs/data-apis/ingest-apis/event-api/introduction-event-api/#limits).

</div>

## Additional resources

Here are some additional helpful documentation, links, and articles:

* [New Relic API keys](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/)

* [Getting started with OpenTelemetry](https://docs.newrelic.com/docs/more-integrations/open-source-telemetry-integrations/opentelemetry/get-started/opentelemetry-get-started-intro/)  

* [OpenTelemetry Collector configuration](https://opentelemetry.io/docs/collector/configuration/)
