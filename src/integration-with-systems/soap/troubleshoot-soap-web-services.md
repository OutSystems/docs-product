---
summary: OutSystems 11 (O11) provides detailed logging for both exposed and consumed SOAP Web Services, accessible via the Service Center management console.
tags: support-application_development; support-Integrations_Extensions
locale: en-us
guid: ddb0cd62-4de7-48c2-9f44-3a9240a4ae66
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=418:40
---

# Troubleshoot a SOAP Web Service

OutSystems keeps track of all requests and responses of both exposed and consumed SOAP Web Services in your application. These log entries can be viewed in the OutSystems environment management console (Service Center).

You can configure the detail level of the logs that OutSystems keeps for each consumed SOAP Web Service, for example increasing the logging level of a given SOAP Web Service while troubleshooting an issue. Check [Set the logging level of REST and SOAP integrations](../log-levels-set.md) for more information.

## View SOAP Web Service Logs

To access the logs of your SOAP Web Service, do the following:

1. Go to the Service Center management console of your OutSystems environment.

1. Go to the **Monitoring** section and select **Integrations**.

1. In **Type**, filter the logging you want to see: `SOAP (Consume)` or `SOAP (Expose)`.

    ![Screenshot showing the selection of SOAP type in OutSystems Service Center for viewing logs](images/select-type-sc.png "Selecting SOAP Type in Service Center")

1. Click **Filter**.

1. To see the details of a log entry click on the **Detail** link (or, if there was an error, on the **Error** link) displayed on the right to get detailed information.

    ![Service Center screen displaying the details of SOAP Web Service logs with options to view specific entries](images/integrations-log-screen-sc.png "SOAP Web Service Log Details")
