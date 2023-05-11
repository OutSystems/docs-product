---
summary: How to configure a separate database for log data and apply these configuration changes to existing OutSystems applications.
tags: support-Installation_Configuration; version-11
locale: en-us
guid: 5e138471-327c-410a-a2ea-104fdad2d68c
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Configure a separate database for log data

Follow the procedure below to configure a separate database for log data and apply these configuration changes to existing OutSystems applications.

## Before You Start

* This procedure is **optional**;
* Applications will only log data to the new log database after their configurations are re-applied;
* Existing log data will no longer be accessible unless it is explicitly copied to the new database tables (check the [Optional Tasks](<#optional-tasks>) section).

## SQL Server

When using SQL Server, you will need to create and configure the log database in Configuration Tool and apply the changes to all your factory modules in Service Center.

Do the following:

1. Open the Log tab in Configuration Tool and fill in the 'Server' and 'Database' fields.

    'Server' is the hostname/IP address of the database server, as well as the instance or TCP port, if applicable.  
    'Database' is the name of the database catalog to store the Logging Database model.

1. Fill in the 'User' and 'Password' fields in the Administrator section.

1. Fill in the 'User' and 'Password' fields in the Runtime section.  

1. Click 'Grant Permissions' to create the database catalog, users and permissions.

1. Create the log database schema by clicking 'Create/Upgrade Database'.

1. Click 'Apply and Exit' in the Configuration Tool. In the pop-up asking you to run the Service Center installation, click 'Yes'.

1. In Service Center, navigate to Factory > Solutions.

1. Select an existing solution containing all your factory modules or create a new solution and add all existing modules to it.

1. In the solution detail screen click 'Apply Settings' to apply the new log database settings to all modules.

## Oracle

When using Oracle, you will need to create the log database objects using an SQL script provided by OutSystems, configure the log database in Configuration Tool and apply the changes to all your factory modules in Service Center.

Do the following:

1. Run the SQL database creation script located in the Deployment Controller machine under the OutSystems Platform Server installation directory: `db\logging_creation_oracle.sql`.  
    Check with your Database Administrator how to execute this script according to your database environment. 

    This SQL script contains instructions to create users and tablespaces and to grant the necessary permissions for the log database. 

    By default, when executing this file, the following objects will be created:

    * Users: `OSADMIN_LOG`, `OSRUNTIME_LOG` (for the Administrator and Runtime roles, respectively)
    * Tablespaces: `OSSYS_LOG`, `OSIDX_LOG`, `OSUSR_LOG`
    * Grants for `OSADMIN_LOG` user: Create Session, Create View, Create Table, Alter Session, Create Sequence, Create Procedure, Create Trigger
    * Grants for `OSRUNTIME_LOG` user: Create Session

    Though this script can be customized, make sure that any file paths, tablespaces and users don't clash with existing objects in the database. If you change any of the default settings, remember to replace all occurrences throughout the file.

1. Open the Log tab in Configuration Tool and set the Oracle database to be used by configuring the Database section.  
For more information on these configurations, click the 'More info' link near the 'Naming Method' field.

1. Fill in the fields in the Administrator section using the database login, database password, logging tablespace, index tablespace previously defined for the logging **Administrator** role in step 1.

1. Fill in the fields in the Runtime section using the database login, database password and runtime tablespace previously created for the logging **Runtime** role in step 1.

1. Click 'Test Connection' for each configured user to make sure that all configurations were entered correctly.

1. Clicking 'Create/Upgrade Database' to create the log database schema.

1. Click 'Apply and Exit' in the Configuration Tool. In the pop-up asking you to run the Service Center installation, click 'Yes'.

1. In Service Center, navigate to Factory > Solutions.

1. Select an existing solution containing all your factory modules or create a new solution and add all existing modules to it.

1. In the solution detail screen click 'Apply Settings' to apply the new log database settings to all modules.

OutSystems applications will start using the new log database after following the steps outlined above. You should validate that new log records are correctly written to the newly configured database by testing all the different log types (e.g. screen logs, mobile requests, integrations).

## Optional Tasks

After validating that everything is working properly, you can perform the following tasks at the database level:

Copy old log data to the new database and tables
:   After configuring a separate log database, existing log data will not be accessible anymore. By copying old log information to the new database, applications will have visibility on the previously existing log data in the new location.

Remove old log tables from the platform database
:   Old log tables — those which name starts with `OSLOG_` — will not be the target of any of the maintenance mechanisms that the platform applies to log data, and therefore old log data (which can represent a substantial amount of disk space) will remain in the platform database. You can reclaim significant database space by removing these old log tables.

Keep in mind that these operations are recommended but optional.
