---
summary: Overview of the log architecture.
---

# Logging database and architecture

The logs enable you to monitor the performance and availability of the platform and your applications. Use them to troubleshoot the issues and to make decisions about maintenance tasks.

The OutSystems logging mechanism is highly scalable. It separates logs by types into multiple database tables, rotates logic that enables retention while preventing indefinite growth. The tables are optimized for the quick logging and simple consultations.

Logs in the OutSystems platform flow from the applications to the database through an asynchronous mechanism. Bulk writing is used to optimize performance and minimize disruption of the application logic. This enables the platform to automatically generate detailed logging information and efficiently save it.

OutSystems 11 enables you to store the log data in a separate database, reducing the impact that log-writing operations could have on running applications while application data is being accessed. This also enables applicable database maintenance tasks to address the business concerns in terms of data criticality and security for the two types of data.

Each OutSystems 11 application writes its own log entries using an internal logging API, making sure that user requests are not blocked while these logs are being written. This logging API collects log information produced by the application and sends it to the log database.

![Logging architecture overview](images/logging-overview.png?width=700)

It's important to note that the Deployment Controller Service writes directly to the database tables, but Service Center consults only the database views.

This section of the documentation is an overview of the log architecture and provides the reference for the log database views. If you need information about the tables in the database, you should inspect the database manually.

<div class="info" markdown="1">

Also available: [Logging database and architecture in OutSystems 10](https://success.outsystems.com/Documentation/10/Managing_the_Applications_Lifecycle/Monitor_and_Troubleshoot/Logging_database_and_architecture).

</div>