---
locale: en-us
guid: b87b0a9b-ac31-4705-ae8e-87ae97505fb1
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
summary: OutSystems 11 (O11) provides three logging levels for REST APIs and SOAP Web Services - Default, Troubleshoot, and Full.
tags: api logging, error handling, performance monitoring, security, documentation best practices
audience:
  - backend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
coverage-type:
  - remember
  - evaluate
---

# Logging levels reference for integrations

The available logging levels for REST APIs and consumed SOAP Web Services are the following:

Default
:   Information is only logged for requests with errors.  
    Example for a consumed SOAP Web Service:

    ![Screenshot showing the Default log level for a consumed SOAP Web Service](images/log-level-default.png "Default Log Level")

Troubleshoot  
:   Information is only logged for requests with errors, along with additional HTTP trace information.  
    Example for a consumed SOAP Web Service:

    ![Screenshot showing the Troubleshoot log level with additional HTTP trace information for a consumed SOAP Web Service](images/log-level-troubleshoot.png "Troubleshoot Log Level")

Full
:   All requests/responses are logged, including additional HTTP trace information.  
    Example for a consumed SOAP Web Service:

    ![Screenshot showing the Full log level with all requests and responses logged for a consumed SOAP Web Service](images/log-level-full.png "Full Log Level")

Increasing the logging level implies that:

* More information gets logged, increasing the amount of information stored in the environment's database.

* The platform logs input and output parameter values along with the request, thus making any sensitive information present in these parameters available through the environment management console.  
**Note:** For consumed REST APIs, you can [redact input parameter values from the logs](rest/consume-rest-apis/redact-info-from-logs.md).
