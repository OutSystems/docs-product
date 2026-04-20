---
summary: OutSystems 11 (O11) enables log redaction for sensitive information in REST API logs.
locale: en-us
guid: 3fcf9d96-a766-4578-9e76-3798201cca0e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility-and-Integration?type=design&node-id=2439%3A15059&mode=design&t=187UAgmZTPxcY0ZG-1
tags: security best practices, api integration, sensitive data handling, logging techniques, outsystems best practices
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
isautopublish: true
---

# Redacting information from REST API logs

When you set the [logging level](https://success.outsystems.com/documentation/11/extensibility_and_integration/set_the_logging_level_of_rest_and_soap_integrations/)
of a REST API to **Full**, OutSystems logs input and output parameter values. If
those values include sensitive data, use log redaction to hide them.

Log redaction prevents sensitive information from appearing in an exposed REST
API’s logs. You can redact input and output parameter values sent in the
header, body, or URL, and received in the header or body.

For example, if a request includes a username and password and the response
returns an access code, redact the **Password** input parameter and the
**Code** output parameter.

To redact the values of an input parameter, follow these steps:

1. In Service Studio, open the module that contains the exposed REST API.

1. In the element tree, expand the REST API, and then expand the REST API
   method that contains the input parameter you want to redact.

1. Select the input parameter, and set **Log Redaction** to **Yes**.

    ![Screenshot showing how to enable log redaction for an input parameter in Service Studio](images/redact-password-ss.png "Activating the Log Redaction property of an input parameter")

To redact the values of an output parameter, follow these steps:

1. In Service Studio, open the module that contains the exposed REST API.

1. In the element tree, expand the REST API, and then expand the REST API
   method that contains the output parameter you want to redact.

1. Select the output parameter (for example, **Code**), and set **Log
   Redaction** to **Yes**.

    ![Screenshot illustrating the activation of log redaction for an output parameter in Service Studio](images/redact-code-ss.png "Activating the Log Redaction property of an output parameter")

After you call the method, the integration logs show the redacted values.

![Sample logs displaying redacted values for sensitive information in a REST API call](images/redact-logs-sc.png "Example of redacted REST API logs")

In the logs, the **Password** and **Code** values appear as `[redacted]`.
