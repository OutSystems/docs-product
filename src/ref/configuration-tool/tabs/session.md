---
summary: The Session tab allows you to configure the database used by OutSystems to store the end user persistent sessions.
---

# Session Tab

The **Session** tab allows you to configure the database used by OutSystems to store the end user persistent sessions.

## Database Section (for SQL Server / Azure SQL)

Configuration | Description | Default value  
---|---|---  
Server | The hostname or IP address to the database server to store the end user persistent sessions. | `localhost`  
Database | Name of the catalog/schema created in the database; it contains the session tables. | `osSession`  
  
## Database section (for Oracle)

Configuration | Description | Default value  
---|---|---  
Naming Method | The method to connect to the Oracle database server. | `Service Name`  
Host | The hostname or IP address to the database server.<br/>This option is only available when the 'Naming Method' is set to 'Service Name'. | `localhost`  
Port | The port on which the database service listens.<br/>This option is only available when the 'Naming Method' is set to 'Service Name'. | `1521`  
Service Name | The Oracle database service name.<br/>This option is only available when the 'Naming Method' is set to 'Service Name'. |
TNS Name | An address name defined in the `tnsnames.ora` configuration file.<br/>This option is only available when the 'Naming Method' is set to 'TNS Name'. |

For advanced settings, click on the **Advanced Settings** link.

Configuration | Description | Default value  
---|---|---  
Extra Parameters | Extra parameters to add to the database connection string. |
Error Messages Language | Allows you to set the NLS_LANGUAGE setting when connecting to your database.<br/>This field is only available for the Oracle database provider. Check the [Oracle documentation](<http://docs.oracle.com/cd/B28359_01/server.111/b28298/applocaledata.htm>) to learn what are the supported values. |

## Session section

Configuration | Description | Default value
---|---|---
User | Name of the user that's the owner of OutSystems session tables. | `OSSTATE`
Password | Password for the specified user. |  
Tablespace | Table space holding the session tables.<br/>This field is only available for the Oracle database provider. | `OSSTATE`
