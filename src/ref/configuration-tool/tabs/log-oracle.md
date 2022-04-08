---
summary: Log tab showing specific settings for the 'Oracle' database provider.
locale: en-us
guid: 4730ef3b-0979-41fb-95dc-b177a430f9e7
---

# Log Tab in Oracle

The following configurations are available in the **Log** tab when the **Database Provider** property is set to `Oracle`.

## Database section

This area contains general configurations for the Oracle database.

Configuration | Description | Default value  
--------------|-------------|--------------  
Naming Method | The method to connect to the Oracle database server. | `Service Name`
Host | The hostname or IP address to the database server.<br/>This option is only available when the 'Naming Method' is set to 'Service Name'. | `localhost`
Port | The port on which the database service listens.<br/>This option is only available when the 'Naming Method' is set to 'Service Name'. | `1521`
Service Name | The Oracle database service name.<br/>This option is only available when the 'Naming Method' is set to 'Service Name'. |
TNS Name | An address name defined in the `tnsnames.ora` configuration file.<br/>This option is only available when the 'Naming Method' is set to 'TNS Name'. |

For advanced settings, click the **Advanced Settings** link.

<table>
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
<strong>Advanced Connection Settings</strong>
</td>
</tr>
<tr>
<td>Runtime Applications</td>
<td>Allows you to configure the behavior of database connections when used by OutSystems applications at runtime.</td>
<td></td>
</tr>
<tr>
<td>Error Messages Language</td>
<td>Allows you to set the NLS_LANGUAGE setting when connecting to your database.<br/>
<a target="_blank" href="http://docs.oracle.com/cd/B28359_01/server.111/b28298/applocaledata.htm" rel="external nofollow" class="external">Check the Oracle documentation</a> to learn what are the supported values.</td>
<td></td>
</tr>
<tr>
<td>Linguistic Sorting</td>
<td>Allows you to set the NLS_SORT parameter. Choose one of the following values:<br/>
BINARY_AI – Collation-sensitive SQL operations use a binary sort that is accent-insensitive and case-insensitive.<br/>
BINARY_CI – Collation-sensitive SQL operations use a binary sort that is case-insensitive, but accent-sensitive. Using this value can help prevent issues in languages where accents are relevant for SQL operations. For example, in Japanese "Seto" (セト) and "Zeto" (ゼト) would both be valid query results for the "セト" search when using the BINARY_AI linguistic sort.</td>
<td><code>BINARY_AI</code></td>
</tr>
<tr>
<td>Log Service Port</td>
<td>The port the log service listens to.<br/>Note: This setting is not available in fresh installs.</td>
<td><code>12003</code></td>
</tr>
<tr>
<td>Log Cycle Period</td>
<td>Indicates for how long (in weeks) the log files are kept. After this time, the log tables are rotated and information is lost.</td>
<td><code>4</code></td>
</tr>
</tbody>
</table>

OutSystems supports Unicode for Oracle databases. To start developing with support for Unicode you just need to ensure that your Oracle database is set to use `AL32UTF8` as the database character set.

## Administrator section

The Administrator section allows you to configure the database user that manages the logging database. This user owns the log tables, views, and indexes.

Configuration | Description | Default value  
--------------|-------------|--------------  
User | Name of the user that's the owner of log tables and associated objects. | `OSADMIN_LOG`  
Password | Password for the user. |  
Tablespace | Table space holding system tables. | `OSSYS_LOG`
Index Tablespace | Table space holding all indexes of the platform. | `OSIDX_LOG`
  
## Runtime section

In this section you specify the login for the user that owns user tables in the logging database.

Configuration | Description | Default value  
--------------|-------------|--------------  
User | Name of the user that's the owner of user tables created in the logging database. | `OSRUNTIME_LOG`
Password | Password for the specified user. |
Tablespace | Table space holding user tables created in the logging database. | `OSUSR_LOG`

## Create/Upgrade Database button

To create all the database objects (tables, indexes, views, etc) required for logging purposes, click **Create/Upgrade Database**.
