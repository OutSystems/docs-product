---
summary: Use these options to import and export the configuration, and export the SQL/PowerShell scripts.
locale: en-us
guid: c87ade70-83ff-4ba0-b333-9ce56da5c8f1
app_type: traditional web apps, mobile apps, reactive web apps
---

# File Menu

The **File menu** contains entires for import/export of the settings and configuration scripts.

## Import and export of configuration

* **Import Configuration...**: Imports a configuration file that was created by the **Export Configuration...** option.
* **Export Configuration...**: Exports your current configuration to a file.

You can store the exported configuration file in a shared folder, so it can be accessed by all front-end servers.

The **Import/Export Configuration...** options are very useful in environments with a Deployment Controller server and several front-end servers, as it is required that all front-end servers have the same configuration. 

1. Configure your Deployment Controller server.
1. Export the configuration of the Deployment Controller server using the **Export Configuration...** option.
1. In each Front-end server, open the Configuration Tool and use the **Import Configuration...** option to import the configuration file.

## Export and inspection of scripts

Use the following to generate the scripts, save them to a destination, and then inspect them:

* **Generate Platform SQL Script...**: Creates and exports the SQL script for Platform database server setup.
* **Generate Logging SQL Script...**: Creates and exports the SQL script for setting up the database used for logging.
* **Generate Session SQL Script...**: Creates and exports the SQL script for setting up the database used for information about sessions.
* **Generate Cache Invalidation Install Script...**: Creates and exports the PowerShell script for downloading, installing, and setting up the RabbitMQ Windows service.

## Applying the settings and exiting

* **Apply and Exit**: Applies the current configuration and exits the Configuration Tool.
* **Exit**: Exits the Configuration Tool.
