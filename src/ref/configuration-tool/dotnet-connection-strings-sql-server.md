---
summary: Fine-tune the connection strings of OutSystems Platform Server to it's database.
locale: en-us
guid: 40be4abc-c505-4c98-a897-40a87c1cd2a0
---

# Using custom .NET connection string parameters with the OutSystems Platform on SQL Server

## Overview

OutSystems Platform uses .NET connection pooling to connect to SQL Server databases. This is done using System.Data.SqlClient.

By default, OutSystems only uses the parameters explicitly needed to connect and the clauses needed for authentication (either Integrated Security=true or a combination of User ID and Password). For everything else, OutSystems relies on defaults - and these work for most use cases. However, in certain scenarios, tuning may be needed in the form of customizing the connection string.

This article guides towards that customization. It explains where such customization can be made, and brings some alerts on what customization to avoid.

This article isn't aimed at teaching how to fine-tune the connection strings. Unless advised for it by an expert on the matter, customers should leave the defaults provided by the platform.

## Where and how to customize the connection string

The connection string is customized in the [Configuration Tool](tabs/platform-sqlserver.md).

Customization applies to all connection strings created by the platform (ADMIN, RUNTIME, LOG, SESSION and external database connections). You can choose, however, to customize between:

* **Runtime Applications**: connection created by the platform in the context of an application. If you wish to customize the way your applications connect to the database, this is where to do it;

* **OutSystems Services**: connections created by the services used by the platform (Deployment Controller, Deployment Service, Log Service, Scheduler Service, SMS Connector).

All connections use the same parameters in the connection string (except for the division above). It's not possible to specify different parameters for connection strings based on any other difference.

Specifically, different parameters by module / Application or by front-end aren't possible to configure.

## What customization can I use and what should I steer away from?

As a rule of thumb, any customization that is applied should be for the effect of performance tuning or changing the way the platform starts connections to the database.

Don't change the connection string in a way that affects the behavior of the connection - as it can break Platform Server behavior. For example, if you add a connection string parameters so that the connection becomes read-only, the platform will break as all connections of that type will become read-only, and the platform needs to write to the database.

## Final notes

As with any tuning or reconfiguration of a software system, changes to the connection string parameters should be correctly tested to ensure they produce the expected improvements without any unforeseen side effects. If in doubt, go back to the defaults.


