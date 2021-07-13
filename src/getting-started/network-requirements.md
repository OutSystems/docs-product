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

The table below details the ports that need to be accessible in each server of an OutSystems environment for **publication and runtime connectivity**. If a server has both roles (Controller and Front-End), then consider the ports for both profiles on that server.

|Source|Destination|Port|Protocol|Notes|
|------|-----------|----|--------|-----|
|End Users|Front-End|80|TCP|Applications HTTP access|
|End Users|Front-End|443|TCP|Applications HTTPS access (always required for Mobile and Reactive Web apps)|
|Development Tools (Service Studio and Integration Studio) |Front-End|80|TCP|Deploy applications to the environment|
|Development Tools (Service Studio and Integration Studio) |Front-End|443|TCP|Deploy applications to the environment|
|Front-End|SQL Server / Oracle|1433 / 1521|TCP|Database connection|
|Controller|SQL Server / Oracle|1433 / 1521|TCP|Database connection|


### Network latency

Even though OutSystems is built to scale horizontally, you need to consider the network latency between the database server, the Platform Server, and the front-end servers. For this reason, it’s advisable to have all servers that make up an environment, running under the same provider.
