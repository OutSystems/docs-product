# The log tables and views

The log model is designed to have minimal interference in the application runtime. Because of this the log tables have limited indexes, making them inefficient for querying. Depending on the volume of logs and the intended use, we recommend that you copy data from the log database to a separate location where you can create a model optimized for querying.

For each log type, the database model consists of:

* A set of 10 tables, `oslog_<TYPE>_0` to `oslog_<TYPE>_9`
* Two views, `oslog_<TYPE>` mapped to the current week, and `oslog_<TYPE>_Previous` mapped to the previous week

For example: for the Error type, there are tables `oslog_Error_0` to `oslog_Error_9` and views `oslog_Error` and `oslog_Error_Previous`. The numbers `_0` to `_9` refer to a tables that are rotated.

<div class="info" markdown="1">

Also available: [The log tables and views in OutSystems 10](https://success.outsystems.com/Documentation/10/Managing_the_Applications_Lifecycle/Monitor_and_Troubleshoot/Logging_database_and_architecture/The_log_tables_and_views).

</div>

## The types of the platform logs in the database

Log information reflects the lifecycle of accesses to applications by end-users or external systems. Because of that, there are two log types.

### Top-level logs

These are logs directly mapped to individual accesses to the platform. They can be considered the "top-level objects" when interpreting logs: each of these logs will have zero or more logs, from other types, associated with this entry. Mapping is made via the `request_key` field.

The following logs are considered "top-level":  

* Screen – one entry in this log maps to an access to a web application or a responsive web application on a mobile device
* Integration (of sub-type: exposed) – one entry in this log maps to an access to a web service (SOAP or REST) exposed by the platform
* Mobile Request – one entry in this log maps to an access to server-side logic in a mobile web application
* Cyclic Job – one entry in this log maps to an execution of a batch job/Timer
  
### Drill logs

These logs drill down on the activity executed by the application as consequence of an access. They exist in the context of a request ("top-level object") and detail activity performed by the application.

The following logs are considered "drill":  

* Error
* General
* Integration (of sub-type: consumed)
* Extension

Note that in complex application architectures an "end-user request" may translate into more than one "top-level" object. For example, a web application Screen may call a local REST service in the platform. In that case, it is not possible to use `request_key` to map the request all the way through because the mapping stops at the integration call.  

Also, note that logs of type Error can occur associated with other drill logs, as indicated in the details of the model. So it is possible to interpret an error in a top-level object (for example, Mobile Request) because of an error in a drill object (for example, an Integration call).

## The rotation of the logs

Logs are stored in a different table every week. The rotation occurs every Friday at 11h45 PM (database time). In a given week, the same cycle number is used for all log types. The cycle number is determined from the current date: the math formula `<Number of weeks between Jan 1st 2000 and today> MOD 10` is used for this purpose.

Rotation means that:

* The definition of the views in the database, for each log type, is updated to point to the next cycle number.
* Log writing automatically begins to happen in the tables from the new cycle. This part is made algorithmically in the Deployment Controller Service — no changes to the database happen for this purpose.
* Old log tables are cleaned after their retention period passes, defined in OutSystems Configuration Tool, preparing them for later use. The retention period configured in OutSystems PaaS is 9 weeks.
