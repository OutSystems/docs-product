---
summary: Check how you can troubleshoot REST APIs by temporarily setting higher logging levels.
tags: 
locale: en-us
guid: 60a9bcc9-9841-40ba-b6be-95dc14831c47
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility-and-Integration?type=design&node-id=3518%3A268&mode=design&t=RWYtMZdGkE4SlpO3-1
---

# Troubleshoot a REST API

OutSystems keeps track of all requests and responses of your REST API, namely, a time log of all request/response activity and content.

You can configure the detail level of the logs that OutSystems keeps for each REST API, for example,increasing the logging level of a given REST API while troubleshooting an issue. Check [Set the logging level of REST and SOAP integrations](../log-levels-set.md) for more information.

## View consumed and exposed REST API Logs

To access the logs of your REST API, do the following:

1. Go to the Service Center management console of your OutSystems environment.

1. Go to the **Monitoring** section and select **Integrations**.

1. In **Type**, filter the logging you want to see: `REST (Consume)` or `REST (Expose)`.

    ![Screenshot of error details](images/type-filter-options-sc.png "Error details")

1. Click **Filter**.

1. To access the details of a log entry, click on the **Detail** link (or, if there is an error, on the **Error** link).

    ![Screenshot of Integrations Log](images/integrations-log-sc.png "Integrations Log")

1. Under the error details, you will also find the stack trace.

    ![Screenshot of error details](images/error-detail-sc.png "Error details")

## View REST API Logs directly from the database

Customers with access to the database cab also query related to an action and see all related details by doing the following:

1. Access the database on the selected environment.

1. Run the following query:

     ```
     select * from OSLOG_INT_DETAIL where id IN (select id from OSLOG_INTEGRATION where action like '%<APIaction>%')
     ```

1. Details similar to the example.

    ![Screenshot of query log](images/sql-query-usr.png "Query log")
