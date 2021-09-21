---
summary: Reference information on deployment zone parameters.
---

# Deployment Zones Reference

<div class="info" markdown="1">

Only available in OutSystems on-premises installations.

</div>

Each deployment zone has the following parameters:

Name
:   The name that identifies the deployment zone. This name will appear in several places in the UI, so it should be meaningful of what it represents.

    Examples: `Business backend`, `Services`, `Core factory`, `Intranet`

Description
:   The purpose of the deployment zone. You can use this field to store any relevant information to better understand how the zone is used and what kind of applications should be added to it.

Is Default for new modules
:   Boolean parameter that, when active, states that the current deployment zone is the [default deployment zone](<intro.md#default-deployment-zone>). You can set a deployment zone as the default one by clicking "Set as Default".

Deployment Zone Address
:   Address for all applications living in the deployment zone, intended for internal communications. When applications in other deployment zones need to refer applications living in this deployment zone and do not want to use the environment URL, they will use this address.

    <div class="info" markdown="1">

    You can only change the Deployment Zone Address if there are no modules deployed in that deployment zone.

    </div>

    This address may vary according to your network architecture. For example with only one front-end server, the "Deployment Zone Address" can be the machine's hostname. However, with multiple front-ends, the "Deployment Zone Address" should be the Fully Qualified Domain Name (FQDN) of the device responsible for the communication between these front-end servers, for example, a load balancer.

    This parameter value might also vary according to the "Hosting Technology" of the deployment zone. On container-based hosting technologies, the "Deployment Zone Address" can be the Fully Qualified Domain Name (FQDN) of your orchestrator, in cooperation with your container engine's ingress feature or some 3rd-party tool that knows how to forward requests to the appropriate containers.

    Learn how this address must fit in your network architecture in [Recommended Network Architecture](<../../containers/architecture.md#configuring-the-address-of-deployment-zones>).

    The platform installation must be able to access this address on ports 80 and 443. Anything living in this deployment zone must be able to reach the platform installation on the port defined for the Deployment Controller Service (by default, 12000).

    This address must be a valid machine domain name or IP address, and **it cannot have a port**.

    Valid examples: `192.168.42.23`, `intranet.mydomain.com`, `rincewind.lan`
  
    Invalid examples: `192.168.42.23/site`, `192.168.42.23:8080/site`, `rincewind.lan/university`

Use HTTPS for internal communications
:   Boolean parameter that, when active, will cause all communication made by OutSystems applications in another deployment zones to applications in the current deployment zone to be made via HTTPS.

Hosting Technology
:   Refers to the type of technology on which all applications in this zone will run on. Available options are: `Classic Virtual Machines`, `Docker Containers`, `Amazon ECS`, `Azure Container Service` and `Pivotal Cloud Foundry`.

    The following options are **container-based hosting technologies**: `Docker Containers`, `Amazon ECS`, `Azure Container Service` and `Pivotal Cloud Foundry`.
    
    The following options are **Docker-based container technologies**: `Docker Containers`, `Amazon ECS` and `Azure Container Service`.

Includes all Servers
:   Boolean parameter that, when active, will make the platform automatically include all servers in the current deployment zone, including those added at a later date. When this parameter is active you will not be able to manually add or remove servers from the deployment zone.

The following fields are only applicable to some of the hosting technologies available:

Deployment Mode
:   _Applies to: All container-based hosting technologies._

    Refers to the type of deployment that will be performed in this deployment zone: `Automatic` or `Manual`.

    In automatic deployments, in addition to all the required manual deployment parameters you must also define trigger URLs to connect the different OutSystems deployment steps with specific tasks on your automated deployment tool of choice. 

Output Files To
:   _Applies to: All container-based hosting technologies._
    
    A file-system location where the platform will put all the artifacts (a set of files) required to create the application container.

    The provided location can be a path on the same machine where the platform is installed or a network share.

    The user account used by OutSystems services (usually Local Service) must have **read/write** permissions on this location.

    Examples: `C:\users\eskerina\container-bundles`, `\\twoflower\luggage`

    NOTE: A `C:\` path (or similar) refers to a location in the same machine where the platform is installed. If the specified directory does not exist, it will be created when the application is published in this zone.

Result
:   _Applies to: All container-based hosting technologies._

    A file-system location where the platform expects you to put a [result file](<../../containers/app-run.md#publish-an-application-to-a-container>)  with a well-known structure to signal that either the container with the application is running and can be accessed, or the deployment has failed.

    The provided location can be a path on the same machine where the platform is installed or a network share. It can be the same folder that was configured in the previous parameter.

    The user account used by the OutSystems services (usually Local Service) must have **read** permissions on this location.

    Examples: `C:\users\eskerina\container-results`, `\\twoflower\luggage`

    NOTE: Any `C:\` path (or similar) refers to a location in the same machine where the platform is installed.

Output Config Files to
:   _Applies to: All container-based hosting technologies_.

    A file-system location where the platform will place the configuration file required for both the application and the [Application Scheduler Service](<../../containers/intro.md#asynchronous-tasks-in-containers>) living inside the container. Each application will have its own sub-folder inside the provided path.

    The provided location can be a path on the same machine where the platform is installed or a network share. The user account used by the OutSystems services (usually Local Service), must have **read/write** permissions on this location.

    Examples: `C:\users\eskerina\container-configs`, `\\twoflower\luggage`

    Note: Any `C:\` path (or similar) refers to a location in the same machine where the platform is installed. If the specified directory does not exist, it will be created when the application is published in this deployment zone.

From Image
:   _Applies to: All Docker-based hosting technologies_.
    
    The base image on which the containers for this deployment zone will be built upon. This parameter provides an extensibility point to use your own base images instead of the default (and recommended) one. This parameter matches the `FROM` directive used in Dockerfiles.

    The default (and recommended) image is `microsoft/dotnet-framework:4.7.1-runtime`. 

    If you want to use your own image, you can do so as long as the base image continues to be `microsoft/dotnet-framework:4.7.1-runtime` and the prerequisites added by OutSystems are not altered.

    While having a central registry is not a requirement, it is highly recommended that you set up your infrastructure so that the base image specified for the containers of a deployment zone is available for use by the container runtime before you start a deployment. This will significantly decrease the amount of time required to build container images for OutSystems applications.

    Check the [Docker registry requirements](<https://success.outsystems.com/Support/Archive/11/OutSystems_Platform_system_requirements#Docker_Containers>).

## Manual Deployment Fields

The following fields are only applicable when using ["Manual" deployment mode](<../../containers/app-run.md>) with container-based hosting technologies:

Operator Timeout
:   _Applies to: All Docker-based hosting technologies_.

    Timeout applied by the Deployment Controller Service to each operator action performed during the "Preparing Deploy", "Deploying", "Update Configs" and "Undeploy" steps.

    The deployment will fail if the operator does not execute the requested operations within "Operator Timeout" minutes.

## Automatic Deployment Fields

The following fields are only applicable when using ["Automatic" deployment mode](<../../containers/app-run-automate.md>) with container-based hosting technologies:

Container Build Trigger URL
:   URL called during application deployment in the "Preparing Deploy" step. The platform will make an HTTP "GET" request to the configured URL expecting a `2xx OK` response.

    The trigger URL handler must be synchronous and should respond as soon as possible stating that the task has started. The deployment will not proceed until a `.preparedone` result file is created in the "Result" folder, stating that the "Preparing Deploy" step was completed.

    During this stage you can automate operations like `docker image build` (for Docker-based hosting technologies) or `cf push --nostart` (for Pivotal Cloud Foundry) since all container artifacts will be available and ready for use.

    The following parameters will be appended to the URL query string:

    * **Address**: Configured deployment zone address.
    * **ApplicationName**: Name of the application being deployed.
    * **ApplicationKey**: Application key identifier used to identify the generated ZIP bundle, along with OperationId.
    * **OperationId**: A GUID representing the publish operation. Different deployments will have different Ids.
    * **TargetPath**: Path where the bundle is available.
    * **ResultPath**: Path where the result files should be placed.
    * **ConfigPath**: Path where the application configurations file exists.
    * **ModuleNames**: Names of the modules that belong to the application.

    All the values of these query string parameters will be **serialized in Base64 encoding**.

    The filename of the application bundle ZIP file created by the platform in "TargetPath" is defined in the following manner:

    `<ApplicationKey>_<OperationId>.zip`
    
    The filename of the result file for this stage, expected at "ResultPath", is the following:

    `<ApplicationKey>_<OperationId>.preparedone`

Container Run Trigger URL
:   URL called during application deployment in the "Deploying" step. The platform will make an HTTP "GET" request to the configured URL expecting a `2xx OK` response.

    The trigger URL handler must be synchronous and should respond as soon as possible stating that the task has started. The deployment will not proceed until a `.deploydone` result file is created in the "Result" folder, stating that the "Deploying" step was completed.

    During this stage you can automate operations like `docker run` (for Docker-based hosting technologies) or `cf start` (for Pivotal Cloud Foundry). The database metamodel will already be upgraded, so it’s the ideal stage to spin up the new version of the application, stop the old version and change any routing rules.

    The same set of query string parameters presented in the previous field will be appended to this trigger URL.

    The filename of the result file for this stage, expected at "ResultPath", is the following:
    
    `<ApplicationKey>_<OperationId>.deploydone`

Update Configurations Trigger URL
:   URL called whenever the application configuration file changes. The platform will make a an HTTP "GET" request to the configured URL expecting a `2xx OK` response.

    The trigger URL handler must be synchronous and should respond as soon as possible stating that the task has started. The deployment will not proceed until a `.configsdone` result file is created in the "Result" folder stating that the "Update Configs" step was completed.

    During this stage you can automate operations like:
    
    * _For Docker-based hosting technologies:_ Copying the configuration file generated in the "Output Config Files to" folder to the folder that was mounted in the Docker container. If the mounted folder is the same and no copy is needed, the trigger URL handler can simply create the `.configsdone` file in the "Result" folder.

    * _For PCF hosting technology:_ Copying the configuration file generated in the "Output Config Files to" to the bundle `config` folder and do a `cf push` to update the application with the new configurations. 

    The same set of query string parameters presented in the "Container Build Trigger URL" field will be appended to this trigger URL.

    The filename of the result file for this stage, expected at "ResultPath", is the following:

    `<ApplicationKey>_<OperationId>.configsdone`

Container Remove Trigger URL 
:   URL called whenever a container-deployed application can be removed. This will happen in the following situations:

    * The original application name changed;
    * The application was removed;
    * The application changed to a different deployment zone.

    The platform will make an HTTP "GET" request to the configured URL expecting a `2xx OK` response. The trigger URL handler must be synchronous and should respond as soon as possible stating that the task has started. The removal process will not proceed until a `.undeploydone` result file is created in the "Result" folder stating that the "Undeploy" step was completed.

    During this stage you can automate operations like `docker rm` (for Docker-based hosting technologies) or `cf delete` (for Pivotal Cloud Foundry).

    The same set of query string parameters presented in the "Container Build Trigger URL" field will be appended to this trigger URL.

    The filename of the result file for this stage, expected at “ResultPath”, is the following:

    `<ApplicationKey>_<OperationId>.undeploydone`

External Deployment Tool Timeout
:   Timeout applied by the Deployment Controller Service to each external deployment tool action performed during the "Preparing Deploy", "Deploying", "Update Configs" and "Undeploy" steps.

    The deployment will fail if the external deployment tool does not execute the requested operations within "External Deployment Tool" minutes.

You can change almost all parameters about a deployment zone, except for the "Hosting Technology" when the zone has modules/applications associated with it. Some changes to deployment zones settings will require you to republish your applications to be effective. You may also have to republish the consumers of your applications.

