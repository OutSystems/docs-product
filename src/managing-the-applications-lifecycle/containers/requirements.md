# Requirements

<div class="warning" markdown="1">

**This page is not published on Mindtouch.** 

It's temporarily used as a repository of both Network Requirements and Systems Requirements for containers.

It will be discontinued (i.e. deleted) in the short term.

</div>

## General Network Requirements

If you are using a container-based hosting technology for deploying OutSystems applications, your network topology and firewall configuration should fulfill these requirements:

* The Container Runtime network endpoint must accept connections on port 80;
* The Database address (and port) must allow connections from the Container Runtime;
* The Platform Server Deployment Controller port must allow connections from the Container Runtime.

<div class="info" markdown="1">
**Note:** From version 11.0.128.0 and onward, it is no longer required to insert the `OSSYS_Parameter` in the database when deploying to containers. This step is now done by the platform.
</div>

SSL offloading is **required** to run applications in containers. Follow the instructions presented in [End-to-end SSL and SSL Offloading](<https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Using_OutSystems_in_Reverse_Proxy_Scenarios/03_OutSystems_configurations_in_reverse_proxy_scenarios#C_-_End-to-end_SSL_and_SSL_Offloading>). You **do not** need to follow the step instructing you to add a new record to the `OSSYS_PARAMETER` database, since the platform already does this step for you when deploying to containers.

---

## System Requirements

Containers only expose HTTP port 80; HTTPS connections must be ensured by the load balancer, following an SSL offload scenario.
Follow the instructions in [End-to-end SSL and SSL Offloading](<https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Using_OutSystems_in_Reverse_Proxy_Scenarios/03_OutSystems_configurations_in_reverse_proxy_scenarios#C_-_End-to-end_SSL_and_SSL_Offloading>). You **do not** need to follow the step instructing you to add a new record to the `OSSYS_PARAMETER` database, since the platform already does this step for you when deploying to containers.

## Docker Containers

To deploy your OutSystems applications to Docker containers you will need to have access to a Docker infrastructure. This infrastructure must be able to run standard Docker Windows Server containers, i.e. Windows Server containers that only use the functionality provided by default in a Docker installation and do not require extra tools or mechanisms to work.

### Infrastructure

The minimum required Docker infrastructure consists of a Docker Engine installation, i.e. the client-server technology that builds and runs containers using Docker's components and services. The engine must support and be able to run Windows Server containers.

The minimum recommended Docker version is the following:

* Docker client/server version 17.10

The machine running Docker must fulfill the following OS/software requirements:

* Windows Server 2016 (version 1709 or later);
* .NET Core Windows Server Hosting bundle installed.

OutSystems also supports the following Docker-based hosting technologies:

* Amazon ECS (Elastic Container Service);
* Azure Container Service (ACS).

If you are using Amazon please read the [Amazon Elastic Container Service documentation](<https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_GetStarted.html>). If you are using Azure please read the documentation on [Azure for Containers documentation](<https://docs.microsoft.com/en-us/azure/containers/>).

The Docker Secrets functionality is not supported, since its support on Windows containers is not yet ready for production use.

### Docker Registries

While having a Docker registry is not mandatory, it is highly recommended. You can use any Docker registry as long as it supports storing and retrieving images for Windows Server containers.

For example, you can use one of the following docker registries (either on-premises or in the cloud):

* Docker Hub;
* Docker Trusted Registry.

### Container Cluster Orchestrators

When deploying an OutSystems application in a Docker container it's necessary to map the port 80 exposed by the container to an available port in the container host (usually a high-numbered port selected by the container runtime).
Since this port in the container host may change and each container needs at least port 80 mapped in the container host machine, the recommended approach is to set up a **container cluster**, together with a container cluster manager/orchestrator, that seamlessly handles all the routing to the right container and port.

You can use OutSystems with the following container cluster orchestrators:

* Docker Swarm;
* Google Kubernetes;
* Amazon Elastic Container Service.

If you are using Docker Swarm, please read the official [Docker Swarm documentation](<https://docs.docker.com/engine/swarm/>). If you are using Kubernetes, please read the official Kubernetes documentation that includes detailed instructions on [using Kubernetes with a cluster](<https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/>).

The container cluster manager/orchestrator can be installed anywhere as long as it allows you to manage the Docker engine on which you will be running the containers with OutSystems applications.

### Base Image Availability

Ensure that all machines that will build/run the application images have the [`microsoft/iis`](<https://hub.docker.com/r/microsoft/iis/>) base image present in the machine. If the base image is not in the machine, the first build/run may timeout while the base image is downloaded.

## Pivotal Cloud Foundry

To deploy your OutSystems applications to Pivotal Cloud Foundry (PCF) you will need to have access to a PCF infrastructure. It must be able to run Windows stemcells, i.e. you will need to install a Windows tile in your infrastructure.

### Infrastructure

The PCF infrastructure must have a Pivotal Application Service for Windows tile installed. To install a Windows tile, follow the [instructions provided by Pivotal](<https://docs.pivotal.io/pivotalcf/2-1/windows/installing.html>) for the Windows 2016 tile.

Note: The Windows 2012r2 tile is **not supported**.

### PCF Internal Routing

You will need to ensure that your PCF internal router can route requests to OutSystems applications both when these come from your internal network, as well as when coming from the outside. 

We recommend adding **two domains** to your Pivotal Apps Manager's "org" (organization):

* A subdomain on your main shared domain that will be used as the PCF's deployment zone address. All the modules of each OutSystems application deployed to this zone will be mapped here.  

    _Example:_  
    If your main shared domain is `apps.pcf.example.com`, add a new domain called `<subdomain>.apps.pcf.example.com`, where `<subdomain>` can be anything of your choice.
 
* A domain equal to the public address of your main load balancer and reverse proxy. This lets the PCF internally route requests coming from outside your internal network.  

    _Example:_  
    If your main load balancer and reverse proxy is publicly accessible using `site.example.com`, add exactly this value as a new domain.
 

### Command-line Tools (cf CLI)

The deployment instructions provided by OutSystems use the Cloud Foundry Command Line Interface ("cf CLI") tool provided by Pivotal.

You must [install "cf CLI"](<https://docs.cloudfoundry.org/cf-cli/install-go-cli.html>) on the machine executing the deployment to PCF to be able to run the `cf` command-line executable.

You will also need to [log in to Cloud Foundry using "cf CLI"](<https://docs.cloudfoundry.org/cf-cli/getting-started.html#login>), specifying an API endpoint and an org (organization), before you are able to run commands like `cf push` successfully.


