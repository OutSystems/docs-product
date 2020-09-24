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
|SysOps|Server|22/3389|TCP|Access the server through SSH or Remote Desktop|
|End Users|Front-End|80|TCP|Applications HTTP access|
|End Users|Front-End|443|TCP|Applications HTTPS access (always required for Mobile and Reactive Web apps)|
|Development Tools|Front-End|80|TCP|Deploy applications to the environment|
|Development Tools|Front-End|443|TCP|Deploy applications to the environment|
|Front-End|nativebuilder.api.outsystems.com|443|TCP|Generate Mobile apps ([more info](https://success.outsystems.com/Support/Enterprise_Customers/Installation/Mobile_App_Builder_Service_connectivity_requirements))|
|Front-End|Controller (by default)<br/>— Depends on where the Cache Invalidation Service/RabbitMQ is installed.|5672|TCP|Cache Invalidation Service connection|
|Front-End|Controller|12000|TCP|OutSystems Deployment Controller Service connection|
|Front-End|SQL Server / Oracle|1433 / 1521|TCP|Database connection|
|Controller|Front-End|12001|TCP|OutSystems Deployment Service connection|
|Controller|SQL Server / Oracle|1433 / 1521|TCP|Database connection|

The following table lists the ports that should be open to correctly **monitor** OutSystems. A failure on opening these ports may result in warnings and error messages.

|Source|Destination|Port|Protocol|Notes|
|------|-----------|----|--------|-----|
|Front-End|Front-End|80|TCP|IIS Monitoring|
|Front-End|Controller|12000|TCP|OutSystems Deployment Controller Service Monitoring|
|Front-End|Front-End|12001|TCP|OutSystems Deployment Service Monitoring|
|Front-End|Front-End|12002|TCP|OutSystems Scheduler Service Monitoring|
|Controller|Front-End|80|TCP|IIS Monitoring|
|Controller|Front-End|12001|TCP|OutSystems Deployment Service Monitoring|
|Controller|Front-End|12002|TCP|OutSystems Scheduler Service Monitoring|

In case you are using a hybrid infrastructure where some part is in OutSystems Cloud and another is managed by yourself, it's possible to create a VPN connection between the environments (hybrid configuration is only supported in OutSystems licenses purchased before January 2020). Learn more in the [Amazon documentation](http://aws.amazon.com/vpc/faqs/#C1).

### Containers considerations

If you are using a container-based hosting technology for deploying OutSystems applications, your network topology and firewall configuration should fulfill these requirements:

* The Container Runtime network endpoint must accept connections on port 80.

* The platform database and logging database addresses (and ports) must allow connections from the Container Runtime.

* The Platform Server Deployment Controller port (12000) must allow connections from the Container Runtime.

* The Cache Invalidation Service (RabbitMQ) port (default is 5672) must allow connections from the Container Runtime.

SSL offloading **is required** to run applications in containers. Follow the instructions presented in [End-to-end SSL and SSL Offloading](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Using_OutSystems_in_Reverse_Proxy_Scenarios/03_OutSystems_configurations_in_reverse_proxy_scenarios#C_-_End-to-end_SSL_and_SSL_Offloading). Note that you **do not** need to follow the step instructing you to add a new record to the `OSSYS_PARAMETER` table, since the platform already does this step for you when deploying to containers.

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

## Network infrastructure requirements

### LifeTime

To use LifeTime to manage your application lifecycle, you need to have bidirectional communication between the front-end of the LifeTime environment, and all other servers (front-ends and deployment controllers) of your OutSystems Infrastructure. 

In case HTTPS isn't supported, LifeTime communicates with the environments it manages by HTTP.

Applications must be deployed as follows:

|Source|Destination|Port|Protocol|
|------|-----------|----|--------|
|LifeTime Front-End|Environment Front-End|80|TCP|
|LifeTime Front-End|Environment Front-End|443|TCP|
|Environment Front-End|LifeTime Front-End|80|TCP|
|Environment Front-End|LifeTime Front-End|443|TCP|

### Architecture Dashboard

To use [Architecture Dashboard](https://architecture.outsystems.com), the Architecture Dashboard LifeTime plugin must be able to communicate with the Architecture Dashboard SaaS. Ensure that the following port is open:

Source|Destination|Port|Protocol|Notes
---|---|---|---|---
LifeTime Front-End|architecture.outsystems.com/Broker_API/ArchitectureDashboard.asmx|443|TCP| Architecture Dashboard LifeTime plugin. Check out [how Architecture Dashboard works](https://success.outsystems.com/Documentation/Architecture_Dashboard/How_does_Architecture_Dashboard_work).
 
