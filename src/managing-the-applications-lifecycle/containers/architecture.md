---
summary: Check the recommended network architecture of container-based solutions for OutSystems applications.
tags: support-Application_Lifecycle; support-Infrastuture_Architecture
---

# Recommended Network Architecture

To take full advantage of containers with OutSystems you should adopt a network topology where there's a load balancer and a reverse proxy at the address defined for the container-based deployment zone. This functionality can be provided either by the container cluster itself, in a limited way, or by a standalone software component.

Deployment zones for containers usually have its deployment zone address set to the container cluster manager address, or to the load balancer in front of that cluster.

## Connectivity Requirements

The container infrastructure needs to be able to connect to the platform database, logging database, and session database, as well as the OutSystems Deployment Controller Service. This means that the server names configured through [Configuration Tool](../../ref/configuration-tool/intro.md) **must be valid and reachable from inside a container**. 

**Do not use "localhost"** as a database server name since it will not work when your application is running inside a container (i.e. the databases will not be accessible in the local host).

To check your configuration, do the following:

1. Open the Configuration Tool.

1. In the Platform tab, validate that the Database > "Server" field is correctly configured.
    
    ![](<images/configuration-tool-platform.png>)

1. In the Log tab, validate that the Database > "Server" field is correctly configured.
    
    ![](<images/configuration-tool-log.png>)

1. In the Session tab, validate that the Database > "Server" field is correctly configured.

    ![](<images/configuration-tool-session.png>)

1. In the Controller tab, validate that the Deployment Controller Service > "Deployment Controller Server" field is correctly configured.

    ![](<images/configuration-tool-controller.png>)

1. In the Cache tab, validate that the Cache Invalidation Service > "Host" field is correctly configured.

    ![](<images/configuration-tool-cache.png>)

    **Note:** The Platform Server Deployment Controller port (12000) must allow connections from the Container Runtime. Check [OutSystems network requirements](https://success.outsystems.com/Support/Archive/11/OutSystems_network_requirements#Containers_considerations) for the full requirements list.


## Configuring the Address of Deployment Zones 

The **"Deployment Zone Address" attribute** of deployment zones allows a given module to refer to any other module, either in the same zone or in a different one (e.g. SOAP or REST calls, references to processes, references to resources from other modules). OutSystems will generate all server-side calls/redirects using the deployment zone address where the producer module is deployed. 

You have to make sure that the addresses configured for all your deployment zones fit your network layout and topology.

In a **single-server scenario**, you can set the "Deployment Zone Address" field to the address of the environment according to its "Hostname" parameter, which is configured in Service Center > Administration > Environment Configuration > Hostname.

![](<images/architecture-single-server.png>)

Element | Description
:------:|------------
![](<images/user-pc.png>) | User devices (mobile or desktop) accessing OutSystems applications.
![](<images/db.png>) | Database (on-premise or on the cloud) used by the platform to store application metadata and by applications to store business data.
![](<images/server-platform-apps.png>) | OutSystems platform, installed on a virtual machine or on the cloud, along with applications living in the same IIS server (possibly using different application pools).

In a **farm scenario**, i.e. when using multiple servers, the deployment zone address should be the address of the load balancer configured to distribute load across servers in that deployment zone.

![](<images/architecture-zones.png>)

Element | Description
:------:|------------
![](<images/load-balancer.png>) | **Main Load Balancer and Reverse Proxy** - Exposes `www.mydomain.net` address and knows how to map `/AppX` and `/AppY` to the servers where those applications are available.%%**Deployment Zone Load Balancer** - Distributes load among the servers configured in the deployment zone.
![](<images/server-apps.png>) | A second (or third) server on which OutSystems applications can be reached. Installed on a virtual machine or on the cloud and reachable by the platform.
**"Intranet" Deployment Zone** | A customer-defined zone, including only some of the servers configured in the environment (2 out of 3 in the diagram).

When deploying to **containers**, the deployment zone address is usually the same as your container cluster manager/orchestrator address (or the load balancer in front of the cluster), i.e. all applications inside and outside the container deployment zone will access applications in that deployment zone using the address of the cluster.

![](<images/architecture-containers.png>)

Element | Description
:------:|------------
![](<images/load-balancer.png>) | **Container Load Balancer and Reverse Proxy** - Exposes the address of the container cluster and knows how to map `/AppZ` and `/AppW` to the containers where those applications are available. Distributes requests among available containers in the cluster. Can be provided by the cluster directly, or installed as a standalone appliance.
![](<images/server-containers.png>) | A node in the container cluster, on which containers with applications are deployed. Installed on a virtual machine or on the cloud and reachable by the platform.
**"Containers" Deployment Zone** | A customer-defined zone that represents a container cluster, in which all applications will be deployed into containers. 

Client-side calls, i.e. any code running on the browser or on a mobile device, will rely on the environment URL, so be sure to configure your network topology so that your public-facing applications are reachable through the environment URL.

## Using Multiple Deployment Zones for Containers

We strongly recommend that you start experimenting with containers using a **single deployment zone** configured to use containers. This will allow you to validate the benefits of using containers in your factory, without the added overhead of having to deal with multiple container zones.

As you become more proficient with containers technology used together with OutSystems, you might want to explore more complex scenarios and consider adding more deployment zones to be used with containers.

The following are examples of more advanced scenarios, where multiple deployment zones for containers can be useful:

Advanced Scenario #1
:   Some of the container-bound applications should have a different base image, because you want to bundle extra libraries that are only required by some applications (and you don't want those libraries available in the images for other applications).

    Proposal: create a deployment zone with a different "From Image" configuration.

Advanced Scenario #2
:   Some of the container-bound applications should be accessible to the outside world, i.e. over the environment URL, while others should only be accessible from applications in your back-office.

    Proposal: create a deployment zone with a different address.
