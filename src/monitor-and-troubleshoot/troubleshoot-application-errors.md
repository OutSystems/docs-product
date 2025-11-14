---
summary: OutSystems 11 (O11) simplifies application error troubleshooting through detailed runtime error logging and management console insights.
tags: error logging, error management, runtime errors, application monitoring, sql troubleshooting
locale: en-us
guid: 6f940cff-b41b-4f7d-aef5-abdf4afd7ed7
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=3200:4024
audience:
  - full stack developers
  - platform administrators
outsystems-tools:
  - service center
coverage-type:
  - understand
  - apply
---

# Troubleshoot Application Errors

OutSystems logs runtime errors that happen in your application, making it easier to troubleshoot them.

You can check error logs in the environment management console (Service Center).

![Screenshot of the environment management console showing the error logs for application troubleshooting](images/troubleshoot-application-errors-1.png "Environment Management Console")

You can filter the error logs by application, module, error message, and more.

## Example - Troubleshoot the Directory App

Customers have been reporting an error in the Directory application, that is preventing them from updating their profile.

![Error report indicating an issue in the Directory application preventing profile updates](images/troubleshoot-application-errors-2.png "Error Report for Directory App")

Check if there are any errors logged for the Directory app.

1. In the Production environment, open the Service Center management console, and navigate to the **Monitoring** tab.
1. Filter by the 'Directory' application.

![Service Center management console with filters applied to show error logs for the Directory application](images/troubleshoot-application-errors-3.png "Filtering Error Logs")

It seems that there is a SQL query with errors. Click the **Detail** link to investigate.

![Detailed view of a SQL query error in the Service Center error log for the Directory module](images/troubleshoot-application-errors-4.png "SQL Query Error Details")

From the error log and stack trace, we can see the error is happening in the Directory module, more precisely in the Employee_MyProfile screen. Learn more about the [information logged by the platform.](<http://www.outsystems.com/forums/discussion/7856/anatomy-of-an-outsystems-error-stack/>)

Probably we found the problem.

We can now share this information with the development team, so that they can reproduce the error and fix it. An easy way of sharing this information is by going back to the 'Error Log' screen, and downloading an Excel file with the errors.
