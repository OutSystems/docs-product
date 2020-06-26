---
summary: Platform tab showing specific configuration settings for the SQL Server / Azure SQL database provider.
---

# Platform Tab in SQL Server / Azure SQL

In the **Database** tab, once you set the **Database Provider** property to `SQL Server / Azure SQL`, the following configurations become available.

## Database section

This section contains general configurations for the SQL Server / Azure SQL database.

Configuration | Description | Default value  
--------------|-------------|---------------  
Server | The hostname or IP address to the database server. | `localhost`
Database | The database catalog used by OutSystems. | `outsystems`  
Authentication | Authentication protocol to use. | `Database Authentication`  

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
<td>Allows you to use a specific connection string for OutSystems applications.</td>
<td></td>
</tr>
<tr>
<td>OutSystems Services</td>
<td>Allows you to use a specific connection string for OutSystems services.</td>
<td></td>
</tr>
<tr>
<td>Default Query Timeout</td>
<td>Sets the default time (in seconds) for database queries to complete. The value can be overridden in the development environment, for each query.</td>
<td>30</td>
</tr>
<tr>
<td colspan="3">
**1-Click Publish**
</td>
</tr>
<tr>
<td>Database Update Query Timeout</td>
<td>Sets the default time (in seconds) for database updates to run when 1-Click publishing an application.</td>
<td>600</td>
</tr>
</tbody>
</table>
  
## Administrator section

The Administrator section allows you to configure the database user that manages the platform. This user owns the OutSystems metamodel tables, views, and indexes.

Configuration | Description | Default value  
--------------|-------------|--------------  
User | Name of the user that's the owner of OutSystems metamodel tables. | `OSADMIN`  
Password | Password for the user. |
  
## Runtime section

The Runtime section allows you to configure the database user used by the applications at runtime. This user owns the tables created by developers in the development environment.

Configuration | Description | Default value  
--------------|-------------|--------------  
User | Name of the user that's the owner of tables created in the development environment. | `OSRUNTIME`
Password | Password for the user. |

## Create/Upgrade Database button

To create all the database objects (tables, indexes, views, etc) the platform requires, click **Create/Upgrade Database**.

This button creates all necessary database objects (tables, indexes, views, stored procedures, etc) to run the Platform Server version you're installing.

To install or upgrade OutSystems, follow the installation checklist.
