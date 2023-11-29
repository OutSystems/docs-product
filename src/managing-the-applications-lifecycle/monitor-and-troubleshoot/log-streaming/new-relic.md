---
summary: This articles guides how you can stream log data to New Relic APM tool.
tags: 
locale: en-us
guid: 3155fa32-225e-4925-bf8e-95a0816f62b3
app_type: traditional web apps, mobile apps, reactive web apps
---

# Stream logs to New Relic

This article explains how you can set up log streaming from OutSystems applications to the New Relic APM tool.

## Prerequisites

* Enabled [Log separation](../../../setup-maintain/setup/logging-db/intro.md).

* Installed Platform Server version 11.23.1 or higher.

* Installed LifeTime version 11.18.1 or higher.

## Set up log streaming

To set up the OutSystems log streaming service, using **New Relic** as the destination tool, get the New Relic API key and the location for New relic account (U.S. or EU).

Once you have these values, go to LifeTime and [configure the log streaming service](lifetime-streaming.md). 

## Additional resources

Here are some additional helpful documentation, links, and articles:

* [New Relic API keys](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/)

* [Getting started with OpenTelemetry ](https://docs.newrelic.com/docs/more-integrations/open-source-telemetry-integrations/opentelemetry/get-started/opentelemetry-get-started-intro/)  

* [OpenTelemetry Collector configuration](https://opentelemetry.io/docs/collector/configuration/)
