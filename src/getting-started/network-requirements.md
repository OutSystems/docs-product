---
summary: Check OutSystems network requirements before installing it on an environment.
tags: requirements; support-installation
---

# OutSystems network requirements

<div class="info" markdown="1">

This article applies to: **OutSystems 11**&#8195;&#8195;Other versions available: [10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/OutSystems_network_requirements)&#8195;[9.1](https://success.outsystems.com/Support/Archive/9.1/OutSystems_Platform_network_requirements)&#8195;[9.0](https://success.outsystems.com/Support/Archive/9.0/OutSystems_Platform_network_requirements)

</div>

## Network environment requirements

### Open ports

The OutSystems services use the following ports:

* 12000 - OutSystems Deployment Controller Service

* 12001 - OutSystems Deployment Service

* 12002 - OutSystems Scheduler Service

For each server of an OutSystems environment, `localhost`:

* must resolve to 127.0.0.1 (IPv4)
* must be accessible by HTTP on 127.0.0.1

<div class="info" markdown="1">

It's possible to configure some of the ports used. Check the [Configuration Tool documentation](../ref/configuration-tool/intro.md) to learn more.

</div>

The table below details the ports that need to be accessible in each server of an OutSystems environment for **publication and runtime connectivity**. If a server has both roles (Controller and Front-End), then consider the ports for both profiles on that server.

|Source|Destination|Port|Protocol|Notes|
|------|-----------|----|--------|-----|
|End Users|Front-End|80|TCP|Applications HTTP access|
|End Users|Front-End|443|TCP|Applications HTTPS access (always required for Mobile and Reactive Web apps)|
|Development Tools (Service Studio and Integration Studio) |Front-End|80|TCP|Deploy applications to the environment|
|Development Tools (Service Studio and Integration Studio) |Front-End|443|TCP|Deploy applications to the environment|
|Front-End|SQL Server / Oracle|1433 / 1521|TCP|Database connection|
|Controller|SQL Server / Oracle|1433 / 1521|TCP|Database connection|

If you are using a hybrid infrastructure where some part is in OutSystems Cloud and another is managed by yourself, it's possible to create a VPN connection between the environments (hybrid configuration is only supported in OutSystems licenses purchased before January 2020). Learn more in the [Amazon documentation](http://aws.amazon.com/vpc/faqs/#C1).

### Network latency

Even though OutSystems is built to scale horizontally, you need to consider the network latency between the database server, the Platform Server, and the front-end servers. For this reason, it’s advisable to have all servers that make up an environment, running under the same provider.

As an example, if you are using Amazon RDS as your database server and running the Platform Server on your own infrastructure, the application’s performance will be degraded.

### Experience Builder

[Experience Builder](https://experiencebuilder.outsystems.com/) must be able to connect to the environment where you want Experience Builder to publish apps. Ensure that the front ends of that environment accept inbound connections from the **Source** address.

Alternatively, ensure that the front ends of the environment used with Experience Builder accepts connections from the IP addresses in the **Notes**. These IP addresses are subject to change.

Source|Destination|Port|Protocol|Notes
---|---|---|---|---
experiencebuilder.outsystems.com|Environment Front-End|443|TCP|52.51.203.1<br/>108.128.2.246<br/>54.228.47.100<br/>63.33.151.194<br/>34.241.56.16<br/>54.75.124.221

### Workflow Builder

[Workflow Builder](http://workflowbuilder.outsystems.com/) must be able to connect to the environment where you want Workflow Builder to publish apps. Ensure that the front ends of that environment accept inbound connections from the **Source** address.

Alternatively, ensure that the front ends of the environment used with Workflow Builder accepts connections from the IP addresses in the **Notes**. These IP addresses are subject to change.

Source|Destination|Port|Protocol|Notes
---|---|---|---|---
workflowbuilder.outsystems.com|Environment Front-End|443|TCP|52.51.203.1<br/>108.128.2.246<br/>54.228.47.100<br/>63.33.151.194<br/>34.241.56.16<br/>54.75.124.221

Workflow Builder needs to be able to connect directly to LifeTime via TCP using https, port 443.

### Architecture Dashboard

To use [Architecture Dashboard](https://architecture.outsystems.com), the Architecture Dashboard LifeTime plugin must be able to communicate with the Architecture Dashboard SaaS. Check out [how Architecture Dashboard works](https://success.outsystems.com/Documentation/Architecture_Dashboard/How_does_Architecture_Dashboard_work). 

Depending on the version of the Architecture Dashboard probe, ensure that one of the following destination endpoints is reachable:

Source|Destination|Port|Protocol|Notes
---|---|---|---|---
LifeTime Front-End|architecture.outsystems.com/Broker_API/rest/ArchitectureDashboard|443|TCP| **Version 4.0 or higher** of the Architecture Dashboard LifeTime probes.
LifeTime Front-End|architecture.outsystems.com/Broker_API/ArchitectureDashboard.asmx|443|TCP| **Version 3.0 or lower** of the Architecture Dashboard LifeTime probes.

 
