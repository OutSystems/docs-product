---
summary: Log tab showing specific settings for the 'SQL Server / Azure SQL' database provider.
---

# Log Tab in SQL Server / Azure SQL

The following configurations are available in the **Log** tab when the **Database Provider** property is set to `SQL Server / Azure SQL`.

## Database Section

This section contains general configurations for the SQL Server / Azure SQL database connection to the logging database.

Configuration | Description | Default value  
--------------|-------------|---------------  
Server | The hostname or IP address to the database server. | `localhost`
Database | The database catalog used for the logging database. | `outsystems_log`  

For advanced settings, click the **Advanced Settings** link.

<table markdown="1">
<thead>
<tr>
<th>Configuration</th>
<th>Description</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3">
**Advanced Connection Settings**
</td>
</tr>
<tr>
<td>Runtime Applications</td>
<td>Allows you to use a specific connection string for OutSystems applications.</td>
<td></td>
</tr>
<tr>
<td>Log Service Port</td>
<td>The port the log service listens to.</td>
<td>`12003`</td>
</tr>
<tr>
<td>Log Cycle Period</td>
<td>Indicates how long to keep the log files (in weeks). After this time, the log tables are rotated and information is lost.</td>
<td>`4`</td>
</tr>
</tbody>
</table>

## Administrator section

The Administrator section allows you to configure the database user that manages the logging database. This user owns the log tables, views, and indexes.

Configuration | Description | Default value  
--------------|-------------|--------------  
User | Name of the user that's the owner of log tables and associated objects. | `OSADMIN_LOG`  
Password | Password for the user. |

Note: these configurations are read-only when Authentication is set to `Windows Authentication` in the **Platform** tab.

## Runtime section

The Runtime section allows you to configure the database user used by the applications at runtime for logging purposes. This user owns the tables created by developers in the development environment.

Configuration | Description | Default value  
--------------|-------------|--------------  
User | Name of the user used by the applications at runtime for logging purposes. | `OSRUNTIME_LOG`
Password | Password of the specified user. |
  
Note: these configurations are read-only when Authentication is set to `Windows Authentication` in Platform tab.

## Create/Upgrade Database button

To create all the database objects (tables, indexes, views, etc) required for logging purposes, click **Create/Upgrade Database**.
