---
tags: support-Integrations_Extensions
locale: en-us
guid: 5d7d9c99-085a-4e8e-9bf3-8f73c6da6b16
---

# Troubleshoot SAP Remote Functions

Sometimes you encounter problems while integrating your application with SAP. OutSystems includes features and tools that help you to troubleshoot those problems.

You can troubleshoot your SAP Remote Functions calls by:

* checking the logs captured by OutSystems
* debugging your application

## Checking the Logs

If a call to a SAP Remote Function results in an exception, do the following to access the logs:

1. Go to the management console of your OutSystems environment (Service Center). 
2. Go to Monitoring section and select Integrations.
3. In Type, select `SAP`.
4. Click Filter. 

This logging shows all requests made to SAP.

## Set Logging Level

If you need more details on what is sent and received from SAP, change the logging level of the SAP connection:

1. Go to the management console of your OutSystems environment (Service Center).
1. Go to Factory section and open your application. 
1. Open the module containing your SAP integration. 
1. Select the Integrations tab and click on the SAP connection name to edit it. 
1. Set the Logging Level to `Full`. 
1. Click Apply. 

Requests and responses are now fully logged and new logs for calls to SAP always have a link:

* Details: gives access to full information of a successful call
* Errors: gives access to full information of a call with errors

Click on the link and press the Download Trace button located at the bottom of the page.
Notice that output parameter values may be not logged if the SAP execution fails, because they simply are not sent back.

## Debug Calls to SAP

When the logs for calls to SAP do not help you to understand the problem, such as when there is no error message returned from SAP, use the **Debugger** in your calls to SAP remote functions. The Debugger allows you to check the values sent and received from the SAP system.
