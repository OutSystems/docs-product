---
summary: The article provides a guide on how to set up log streaming from OutSystems to Dynatrace, including prerequisites and configuration steps
tags:
locale: en-us
guid: 7e46389e-dc1f-42cc-9225-929bed3b82a1
app_type: traditional web apps, mobile apps, reactive web apps
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing-the-Applications-Lifecycle?type=design&node-id=3139%3A322&mode=design&t=IIMVc2WTi7UxHv00-1
---
# Stream logs to Dynatrace

This article explains how you can set up log streaming from OutSystems applications to the **Dynatrace** APM tool.

## Prerequisites

* Enabled [Log separation](../../../setup-maintain/setup/logging-db/logs-separation-cloud/intro.md).

* Installed Platform Server version 11.23.1 or higher.

* Installed LifeTime version 11.19.0 or higher.

## Set up log streaming

To configure the OutSystems log streaming service, using **Dynatrace** as the destination tool, follow these steps:

1. Get the Dynatrace SaaS endpoint. 

1. Get the Dynatrace API token (must have the ingest logs permissions).

Once you've completed these steps, go to LifeTime and [configure the log streaming service](lifetime-streaming.md) and enter the following parameters:

* **Destination**: ``Other`` 
* **Protocol**: ``OTLP/HTTP`` (**Note**: gRPC is not supported)
* **Endpoint**: Dynatrace SaaS Endpoint  ``https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs``
* **API key header name**: ``Authorization``
* **API key**: ``Api-Token <access token>``

    ![Screenshot of the OutSystems LifeTime interface showing the log streaming configuration fields for Dynatrace](images/log-streaming-dynatrace-lt.png "Log Streaming Configuration in LifeTime")

## Additional resources

[Export with OLTP.](https://www.dynatrace.com/support/help/extend-dynatrace/opentelemetry/getting-started/otlp-export)
