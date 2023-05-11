---
summary: Log tab showing specific settings for the 'Azure SQL Database / SQL Server' database provider.
locale: en-us
guid: 09712708-bd45-4271-9005-9b19e43d29dc
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Log tab in SQL Server and Azure SQL Database

The following configurations are available in the **Log** tab when the **Database Provider** property is set to `SQL Server / Azure SQL`.

## Database Section

This section contains general configurations for the Azure SQL Database / SQL Server database connection to the logging database.

Configuration | Description | Default value  
--------------|-------------|---------------  
Server | The hostname or IP address to the database server. | `localhost`
Database | The database catalog used for the logging database. | `outsystems_log`  

For advanced settings, click the **Advanced Settings** link.

|Configuration | Description | Default value|
|---|---|---|
|Runtime Applications|Allows you to use a specific connection string for OutSystems applications.||
|Log Service Port|The port the log service listens to.|`12003`|
|Log Cycle Period|Indicates how long to keep the log files (in weeks). After this time, the log tables are rotated and information is lost.|`4`|

## Administrator section

The Administrator section allows you to configure the database user that manages the logging database. This user owns the log tables, views, and indexes.

<div class="info" markdown="1">

These configurations are read-only when Authentication is set to `Windows Authentication` in the **Platform** tab.

</div>

Configuration | Description | Default value  
--------------|-------------|--------------  
User | Name of the user that's the owner of log tables and associated objects. | `OSADMIN_LOG`  
Password | Password for the user. |

## Runtime section

The Runtime section allows you to configure the database user used by the applications at runtime for logging purposes. This user owns the tables created by developers in the development environment.

<div class="info" markdown="1">

These configurations are read-only when Authentication is set to `Windows Authentication` in the **Platform** tab.

</div>

Configuration | Description | Default value  
--------------|-------------|--------------  
User | Name of the user used by the applications at runtime for logging purposes. | `OSRUNTIME_LOG`
Password | Password of the specified user. |
  
## Create/Upgrade Database button

To create all the database objects (tables, indexes, views, etc) required for logging purposes, click **Create/Upgrade Database**.
