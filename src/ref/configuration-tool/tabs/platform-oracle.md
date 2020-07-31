---
summary: Platform tab showing specific configuration settings for the Oracle database provider.
---

# Platform Tab in Oracle

In the **Platform** tab, once you set the **Database Provider** property to
`Oracle`, the following configurations become available.

## Database section

This area contains general configurations for the Oracle database.

Configuration | Description | Default value  
--------------|-------------|--------------  
Naming Method | The method to connect to the Oracle database server. | `Service Name`  
Host | The hostname or IP address to the database server.<br/>This option is only available when the 'Naming Method' is set to 'Service Name'. | `localhost`
Port | The port on which the database service listens.<br/>This option is only available when the 'Naming Method' is set to 'Service Name'. | `1521`
Service Name | The Oracle database service name.<br/>This option is only available when the 'Naming Method' is set to 'Service Name'. |
TNS Name | An address name defined in the `tnsnames.ora` configuration file.<br/>This option is only available when the 'Naming Method' is set to 'TNS Name'. |

For advanced settings, click on the **Advanced Settings** link.

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
<td>Allows you to configure the behavior of database connections when used by OutSystems applications at runtime.</td>
<td></td>
</tr>
<tr>
<td>OutSystems Services</td>
<td>Allows you to configure the behavior of database connections when used by OutSystems services.</td>
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
<td>`BINARY_AI`</td>
</tr>
<tr>
<td>Default Query Timeout</td>
<td>Defines the default maximum time (in seconds) the platform waits for query execution (since establishing the database connection).</td>
<td>`30`</td>
</tr>
<tr>
<td colspan="3">
**1-Click Publish**
</td>
</tr>
<tr>
<td>Database Update Query Timeout</td>
<td>Defines the default maximum time (in seconds) the platform waits for query execution in a 1-Click Publish operation (since establishing the database connection).</td>
<td>`600`</td>
</tr>
</tbody>
</table>

OutSystems supports Unicode for Oracle databases. To start developing with support for Unicode you need to ensure that your Oracle database is using the `AL32UTF8` database character set.

## Administrator section

The Administrator section allows you to configure the database user that manages the platform. This user owns the OutSystems metamodel tables, views, and indexes.

Configuration | Description | Default value  
--------------|-------------|--------------  
User | Name of the user that's the owner of OutSystems metamodel tables. | `OSADMIN`  
Password | Password for the user. |  
Tablespace | Table space holding system tables. | `OSSYS`  
Index Tablespace | Table space holding all indexes of the platform. | `OSIDX`  
  
## Runtime section

In this section you specify the login for the user that owns user tables.

Configuration | Description | Default value  
--------------|-------------|--------------  
User | Name of the user that's the owner of tables created in the development environment. | `OSRUNTIME`  
Password | Password for the user. |
Tablespace | Table space holding the tables created in the development environment. | `OSUSR`

## Create/Upgrade Database button

To create all the database objects (tables, indexes, views, etc) the platform requires, click **Create/Upgrade Database**.

This button creates all necessary database objects (tables, indexes, views, stored procedures, etc) to run the Platform Server version you're installing.

To install or upgrade OutSystems, follow the installation checklist.
