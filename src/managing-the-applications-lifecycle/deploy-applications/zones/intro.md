---
summary: Deployment zones allow you to define the distribution of modules (or eSpaces) by servers on a farm environment. 
tags: support-Application_Lifecycle; support-Application_Troubleshooting; support-webapps
---

# Selective Deployment Using Deployment Zones 

<div class="info" markdown="1">

Only available in OutSystems on-premises installations.

</div>

Deployment zones allow you to define the distribution of modules, or eSpaces, by front-end servers on a farm environment.

Use deployment zones when you have servers with different purposes — e.g. when some of the servers are in a DMZ network — and want to choose which servers your modules (or full applications) will be deployed to.

Deployment zones provide isolation to modules by ensuring they are only deployed to the servers configured for a given deployment zone. When the deployment zone defined for a module is changed or when the module changes to a different deployment zone, that module is deployed on the servers configured for the new deployment zone and is removed from the servers that don't belong to that deployment zone.

Each deployment zone has one or more servers. Servers can belong to several zones at the same time. However, a application (or an application module) can only be associated with a single deployment zone. All these configurations are defined in Service Center.

A deployment zone can be set to automatically include all front-end servers available in the environment by activating the "Includes all Servers" configuration option. This will avoid the manual task of adding a new server to the deployment zone each time you add a new front-end server to the environment.

<div class="info" markdown="1">

When a deployment zone is configured with a [container-based hosting technology](<../../containers/intro.md>) you will only be able to configure it for an **entire application** and not for its individual modules, since the deployment unit for containers is the application.

Additionally, when you change the deployment zone of an application to a deployment zone using a container-based hosting technology, you need to republish your application for the changes to take effect.

</div>

## Default Deployment Zone

The **default deployment zone** configuration controls where your new modules and applications will be deployed to. OutSystems will create a deployment zone named "Global" on a first install that is set as the default deployment zone. 

As a rule, when you create a new application and publish it for the first time, its modules will be deployed in the default deployment zone. Once a module or application has been published for the first time, you can select any other deployment zone as its deployment target.

There's one exception to this rule: when **all** the modules of an application are configured to the same deployment zone, creating a new module &#8212; either via Service Studio or by including the new application module (i.e. an application module never deployed to the environment) in a solution file &#8212; will associate it automatically with the **same deployment zone** as the other modules in that application.

You can make any other deployment zone the default one as long as its hosting technology is "Classic Virtual Machines".

## Example

In the following example, we define three zones:

* The "Internal Apps" deployment zone has two associated servers: Server 1 and Server 2
* The "B2E" deployment zone has one associated server: Server 2
* The "Public" deployment zone has one associated server: Server 3

![](<images/intro-front-ends-diag.png>)

Then, we configure three modules associating them with a given deployment zone:

* Module 1 is associated with the "Internal Apps" deployment zone
* Module 2 is associated with the "B2E" deployment zone
* Module 3 is associated with the "Public" deployment zone

The modules will be deployed to the three servers according to the following diagram:

![](<images/intro-modules-diag.png>)

Deployment zones can be configured to perform one of two different kinds of deployments: deploying to a regular Internet Information Services (IIS) web server &#8212; a hosted technology named "Classic Virtual Machines" &#8212;, or deploying to a [container-based infrastructure](<../../containers/app-run.md>), supporting different hosting technologies.

## Communication Between Applications in Different Deployment Zones

Sometimes applications need to communicate with other applications outside of their deployment zone. To achieve this they use the deployment zone address of the second application. 

This is required for features like [Services](<../../../develop/reuse-and-refactor/services.md>), [Processes](<../../../develop/processes/intro.md>), [Timers](<../../../develop/timers/intro.md>), [Emails](<../../../develop/logic/emails.md>), and for management operations performed by Service Center.

###  Example 

In the following scenario, we have an application named "Front-end App" exposing the web interface for Internet users. This application reuses existing logic in the form of [Services](<../../../develop/reuse-and-refactor/services.md>) for its back-end. The "Back-end Service" was deployed in the "Internal Apps" deployment zone while the "Front-end App" was deployed to the "Public" deployment zone. This allows the "Back-end Service" to be isolated from the Internet users while also allowing its functionality to be accessed via the "Front-end App".

The "Back-end Service" is discovered by the "Front-end App" through the deployment zone address of the "Back-end Service". This address might vary according to your network architecture and is defined by you in the "[Deployment Zone Address](<reference.md>)" parameter when creating the deployment zone.

![](<images/intro-ex-interzonecommunication-single-diag.png>)

## Example Use Cases

In following examples we have an environment with multiple servers, one targeted at internal end users ("Internal Server") and one (or more) targeted at public end users ("Public-facing Servers").

### Explicitly Segmented Servers

Consider a scenario with two servers configured in the environment, in which the default deployment zone only includes the Internal Server: 

* One server on a DMZ network, serving _public only_ web applications to be accessed by external end users connected to the Internet;
* One internal server, serving _internal only_ web applications to be accessed by internal end users.

You wish to deploy some web applications that are only available to internal end users and some other web application that are exclusively available to external end users. By default, a web application is deployed to the default deployment zone; however, this would make it available only in the internal server in the Intranet network.

To change the configuration of a web application so that it is only deployed to the public-facing server, do the following:

* Create a new deployment zone (e.g. "Public") containing only the public-facing server;
* Configure the web application to use the new deployment zone.

![](<images/intro-ex-segmented-server-diag.png>)

After these steps, the application you just configured will only be deployed to the public-facing server, and it will be removed from any other servers belonging to the previously configured deployment zone. Internet users will access the application through the public server address. 

If at a later stage you add a new module to the web application, it will be deployed to the same deployment zone ("Public"), as long as all the application modules are still associated with this deployment zone.

### Internal Web Application

Consider a scenario with two servers configured in the environment, in which both are part of the default deployment zone: 

* One server on a DMZ network, to be accessed by external end users connected to the Internet
* One internal server, to be accessed by internal end users

You wish to deploy a web application and make it available to internal end users only. By default, your web application is deployed to the default deployment zone; however, this would make it available in all servers, both the internal and the public-facing one in the DMZ network.

To change the configuration of the web application so that it is only deployed to the internal server, do the following:

1. Create a new deployment zone (e.g. "Intranet") containing only the internal server.
1. Configure the web application to use the new deployment zone.

![](<images/intro-ex-internal-app-diag.png>)

After these steps, the application you just configured will only be deployed to the internal server, and it will be removed from any other servers belonging to the previously configured deployment zone. Internal end users will access the application through the internal server address. 

If at a later stage you add a new module to the web application, it will be deployed to the same deployment zone ("Intranet"), as long as all the application modules are still associated with this deployment zone.


### Load Distribution for a Public Web Application

Consider a scenario with two public servers, accessible from the Internet, with all servers being part of the default deployment zone. You wish to deploy a web application for public access and distribute the load between the two available public servers. This will require you to set up a load balancer, a 3rd-party component, to split the load between the two.

To correctly deploy a web application to these two public-facing servers and do a load distribution between them, do the following:

1. Set up a deployment zone (e.g. "Public") containing the two public-facing servers that will handle requests made to the web application.
1. Configure the web application to use the new deployment zone.
1. Set up a load balancer that will route the requests to the application module URLs in one of the public-facing servers that you configured in the deployment zone.

![](<images/intro-ex-load-distribution-diag.png>)

After doing these configurations, the web application will be deployed in the two public-facing servers. Users will access the modules using the address of the load balancer, which will hand over the requests to the configured servers in the "Public" deployment zone.

## Limitations

Take the following limitations into account when deploying **modules** to different deployment zones:

* System Components are deployed to the default deployment zone. Use the internal network configuration to limit the access to Service Center and LifeTime (available in Service Center in Administration > Security > Network Security).

* Processes, Timers and Emails require that there is at least one server in the zone of the module configured to execute them.
