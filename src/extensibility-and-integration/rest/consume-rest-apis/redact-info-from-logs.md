---
locale: en-us
guid: 966c33e2-bdc0-4847-91b3-9fbda9b29d9f
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility-and-Integration?type=design&node-id=410%3A99&mode=design&t=187UAgmZTPxcY0ZG-1
summary: The article explains how to redact sensitive information from REST API logs by setting the Log Redaction property to Yes for specific input parameters in Service Studio
---
# Redacting information from REST API logs

You can redact sensitive input parameter values from the logs of a consumed
REST API, containing information like an employee's salary or health data.

To redact the values of a given Input Parameter from the logs, do the
following:

1. In Service Studio, open the module containing the consumed REST API element.

1. In the element tree, expand the consumed REST element, and then expand the
   element for REST Method with the input parameter you want to redact from the
   logs.

1. Select the input parameter you wish to redact, and set its **Log Redaction**
   property to **Yes**.

    ![Screenshot showing how to set the Log Redaction property to Yes for an input parameter in Service Studio](images/redact-logs-property-ss.png "Setting Log Redaction Property in Service Studio")
