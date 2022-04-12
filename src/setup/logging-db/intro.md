---
summary: OutSystems 11 allows you to store log data in a log database separate from the application database, reducing the impact that logging can have on running applications.
tags: article-page; support-Installation_Configuration; version-11
locale: en-us
guid: 1e5deb19-1e3e-4f3d-8036-ec5f4ade1a5c
---

# Keep OutSystems log data in a separate database

Up to version 10, OutSystems used a single database to store two types of data: **application data** and **log data**. Since these types of data have different requirements, you might need to handle each type of data differently.

OutSystems 11 allows you to store log data in a separate database, reducing the impact that log-writing operations could have on running applications while application data is being accessed. This also allows database maintenance tasks to address the business concerns in terms of data criticality and security for the two types of data in an appropriate manner.

## Architecture

Logs are a vital piece of information to help identify errors that may not have much visibility, as well as to troubleshoot problems that are ultimately affecting users and are having an impact on the business. 

Despite their importance, collecting those logs must be done in a way that does not impact the users experience while interacting with the application. Therefore, ensuring that applications are properly isolated in terms of producing logs is critical; log intensive applications must not compromise the behavior and user experience of other applications running in the same infrastructure.

Each OutSystems 11 application now writes its own log entries using an internal logging API, making sure that user requests are not blocked while these logs are being written. This logging API collects log information produced by the application and sends it to the log database.

![](<images/new-log-model.png>)

## Accessing log data

To read logging information, application developers can reference entities exposed by the **new PlatformLogs extension**, obtaining log data directly from the log database.

However, due to the underlying changes in the OutSystems log model, applications that consume these entities may need to be updated, depending on how they are using these entities.

### Impact on existing applications

Since log entities are now persisted in tables that may be stored in a different physical database from the application database, **it is no longer possible to join log data with application data**, regardless of log data being in a separate database or not. 

This will have an impact on applications that currently use joins between log and application data, making them invalid and requiring developers to perform some changes. OutSystems provides guidance on [how to update these invalid applications](<update-applications.md>).

To decrease the level of impact, log entities were [denormalized](<https://en.wikipedia.org/wiki/Denormalization>) and now contain most of the data needed to make log records self-explanatory, avoiding the need to join with other tables. Attributes like 'Application Name' no longer require a join with the 'Application' entity to obtain the application name. 

The attributes added to log entities were the following:

Attribute | Added to...
----|----
`Espace_Name`      | All log entities
`Application_Name` | All log entities
`Application_Key`  | All log entities
`Username`         | `Log_Error`, `Log_Error_Previous`, `Log_Extension`, `Log_Extension_Previous`, `Log_General`, `Log_General_Previous`, `Log_Mobile_Request`, `Log_Mobile_Request_Previous`, `Log_Screen`, `Log_Screen_Previous`, `Log_Sms`, `Log_Sms_Previous`
`Extension_Name`   | `Log_Extension`, `Log_Extension_Previous`

These new attributes in log entities will only be filled in for applications already upgraded to OutSystems 11 and the information saved in the log records will refer to the moment the log was generated, i.e. if an application changes its name from 'X' to 'Y' after a log record is created, the application name in that log record will still be 'X'. Note that this will not affect any filters using the key attribute rather than the name.

## "Should I use a separate database for log data?"

It's still possible to keep using the same database both for log data and application data. If you have no special requirements associated with the log data produced by OutSystems applications, then this kind of data can live side-by-side with application data in the same database. This is the default upgrade path if you are upgrading to OutSystems 11.

However, if you need to comply with more strict rules or procedures, it is advisable to store log data in a separate database. If you are upgrading to OutSystems 11, follow the steps in the following topics to take advantage of log data separation.

[Configure a separate database for log data](configure-separate-db.md)

[Update applications that access OutSystems log data](update-applications.md)
