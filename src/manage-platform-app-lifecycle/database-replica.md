---
summary: Explore real-time business analytics with minimal performance impact using Database Replica in OutSystems 11 (O11).
tags:
locale: en-us
guid: 706c08f9-df6b-4bac-bb20-0e683262cadd
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Using Database Replica for reporting

Database Replica provides direct access to your OutSystems 11 live application data without affecting performance or stability. It's an exact replica of your production database, with changes reflected in seconds. This allows you to perform real-time business analytics on your data without limitations on the volume of data you can access or extract.

Database Replica can be deployed in any OutSystems 11 cloud environment. Upon deployment, you receive two read-only database access credentials, which can be used for your ETL processes or directly with business analytics and reporting tools. Additionally, you can connect Database Replica to your OutSystems applications as an [external data source](../integration-with-systems/external-database/intro.md) to build reporting dashboards within OutSystems.

With your read-only credentials, you gain access to:

* Database tables created by the entities you define in Service Studio.

* System tables that list users and their roles.

See [Granted permissions](#granted-permissions).

![Diagram showing the data flow from the primary database to the database replica with read/write access for the application server and read-only access for the BI/reporting application.](images/database-replica-diag.png "Database Replica Diagram")

## Requirements

Consider the following requirements for Database Replica:

* You must have an existing OutSystems 11 Cloud infrastructure.

* A subscription to Database Replica is required. Contact your Account Manager for provisioning.

* You must have the OutSystems Cloud high-availability option enabled. Users interested in obtaining the high-availability option should contact their account team for further assistance.

* Your primary database server must meet a minimum scalability requirement of Class 3.

## Before you begin

To request a **Database Replica user**:

* You must be a **company administrator** or an **infrastructure administrator** for your company's account.

### Request a Database Replica user

To request a Database Replica user, open a support case. Make sure you include the following information in the support case description:

* Identify the **environments** where you require database access by providing their name or address.

* Indicate **how you want to connect** to the database:

  * Via VPN - You can request a new VPN or use one that's already active.

  * Via AWS Transit Gateway - If you already connect to your OutSystems Cloud using this service.

* Provide a contact number that can receive the SMS to retrieve the password.

Following up on your support case, OutSystems does the following:

* Establishes the connectivity according to your chosen preference - via VPN or AWS Transit Gateway.

* Provides you a file with the database address and credentials.

### Granted permissions

Check below the permissions granted for **read-only**  credentials.

#### Read-only credentials

For SQL Server:

* SELECT over all database tables and views
* SHOWPLAN
* VIEW DATABASE STATE
* VIEW SERVER STATE

All database tables and views include all OutSystems tables (both metamodel tables and application tables), and the database management system tables.

Tables created by the Platform Server when you create entities in Service Studio. These tables use the prefix OSUSR.
