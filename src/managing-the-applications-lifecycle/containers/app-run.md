---
summary: General steps for running an OutSystems application in a container.
tags: support-Application_Lifecycle
---

# Running Your Application in a Container

<div class="warning" markdown="1">

Container deployment is available as an [Early Access Program](<https://www.outsystems.com/goto/technical-preview>).

</div>

<div class="info" markdown="1">

**Before you start**, make sure that:

* You meet the [system requirements](<https://success.outsystems.com/Support/Archive/11/OutSystems_Platform_system_requirements#Containers_considerations>) and [network requirements](<https://success.outsystems.com/Support/Archive/11/OutSystems_network_requirements#Containers_considerations>) for deploying to containers;
* You know the [recommended network architecture](<architecture.md>) and the [limitations](<intro.md>) of running your applications in a container.

</div>

To run your application in a container your should follow the general steps outlined below:

1. Create and configure a **deployment zone for containers**, if you don't have one already;
1. **Configure the application** to be deployed to containers;
1. **Publish the application** to a container.

These steps are explained in greater detail in the following sections.

## Create and Configure a Containers Deployment Zone

To deploy an application to containers, you will need a [deployment zone](<../deploy-applications/zones/intro.md>) configured with a container-based hosting technology (`Docker Containers`, `Amazon ECS`, `Azure Container Service` or `Pivotal Cloud Foundry`).

You can create a new deployment zone for this purpose or change the hosting technology of an existing deployment zone, as long as there are no modules/applications associated with it. Since the minimum requirement is having one deployment zone for containers, you can perform the steps below only once to create this deployment zone and configure it in all the applications that you wish to deploy to containers.

To configure a new deployment zone for containers, do the following:

1. [Create a new deployment zone](<../deploy-applications/zones/zone-create.md>) filling in its basic parameters ("Name" and "Deployment Zone Address").

1. Before clicking the "Create" button, select one of the container-based hosting technologies: `Docker Containers`, `Amazon ECS`, `Azure Container Service` or `Pivotal Cloud Foundry`.

    You will have to provide values for specific parameters related with the selected hosting technology, or accept the default values.  
    Learn more about the different [deployment zone parameters](<../deploy-applications/zones/reference.md>).

After creating a deployment zone for containers, you will need to configure your application to use that deployment zone.

## Sharing Data with a Container

### Configurations Folder

Using a separate configurations folder allows you to change the settings of OutSystems applications without having to build a new application bundle. Though application configuration settings are not bundled with the application, when the application is deployed they must be available or else the application will not run properly.

When deploying an application to a deployment zone configured with a container-based hosting technology, the platform will write the `App.config` application configuration file to the "Output Config Files to" folder set in the deployment zone configuration. You will need to copy the `App.config` file to the correct configs folder for the application to be correctly deployed.

**Note:** The exact folder location depends on the hosting technology; for more details check the specific documentation for the desired hosting technology.

To change OutSystems application settings, place an updated configuration file in the proper folder that is being made available to your hosting technology and the application will automatically fetch the new settings.

### Secrets Folder

Some of the platform capabilities use encryption and need an environment key. That key is **not distributed** with the container code and must be provided before deploying your application to a given container-based hosting technology for your application to work properly, similarly to the configurations file. The key file is named `private.key` and can be found in the OutSystems platform installation folder (usually `C:\Program Files\OutSystems\Platform Server`).


## Configure an Application to be Deployed to Containers

To configure an OutSystems application to be deployed to containers, you must set its deployment zone to a containers deployment zone, as follows:

1. In Service Center, navigate to Factory > Applications and click on your application name;

1. In the Operations tab, set the "Deployment Zone" parameter to the deployment zone configured for containers;

1. Click the "Apply" button.

For this change to be effective, you would need to republish the application. The following section gives an overview how this operation is different when deploying to operations.  

## Publish an Application to a Container

<div class="info" markdown="1">

Note: This section is just an overview of the publishing process. For more information check the documentation on each hosting technology.

</div>

The "publish to a container" operation is divided in six stages further detailed below:

![](<images/containers-manual-deployment-steps.png?width=705>)

1\. Compile application and generate bundle (OutSystems)
:   The platform compiles the application, generates its binaries and creates the application bundle. The bundle (a ZIP file) is provided in the configured path for further action from the operator, either a human or an automated deployment tool.

2\. Build container image/push application (Operator)
:   The operator extracts the contents of the bundle and builds the container image or pushes the application to the container infrastructure, depending on the hosting technology being used.

3\. Create result file for deployment preparation step (Operator)
:   The operator creates a result file for the "Preparing Deploy" step with the expected filename in the configured "Result" folder, informing the platform that the application deployment to a container can proceed. This file may be empty in case of a successful deployment, or may have JSON content with the errors that occurred.

4\. Run container (Operator)
:   The operator starts the container, obtaining its identifier when the operation succeeds.

5\. Define network routing rules for container (Operator)
:   The operator checks if the application inside the container is reachable using the deployment zone address, defining a network routing configuration if necessary, or checking if the already defined configuration is  still valid (when the IP address of the container changes, the routing rules will probably need to be changed).

6\. Create result file for the deployment step (Operator)
:   The operator creates a result file for the "Deploying" step with the expected filename in the configured "Result" folder, stating the result of the application deployment operation. Similarly to the result file for deployment preparation step, this file may be empty in case of a successful deployment, or may have JSON content with the errors that occurred.

After the operator creates the result file, the platform detects it and proceeds with updating the state of the application modules according to the deployment operation result. 

<div class="info" markdown="1">

After the platform processes a result file, it will delete **all previous result files** related to the same application and operation, except for the most recent one created by the operator.

For example, consider a scenario of a deployment to a container which is in the deployment preparation step. After the operator places the `.preparedone` result file in the correct folder and the platform detects it, all previous `.preparedone` result files for that application will be deleted.

</div>

## Update Configurations

An update of the configurations of an application deployed to containers will require the operator to create a result file whose name must match the expected name and have a `.configsdone` extension; the expected filename appears in the publication messages. The contents of this file will depend on the result of the update configurations operation:

Successful
:   Create an empty file with the expected name (`.configsdone` extension) on the configured "Result" folder of the deployment zone.

Failed
:   Create a JSON file with the correct filename and with a `.configsdone` extension whose contents follows the template presented next — it contains a user-defined error message:

    ```
    {"Error":{"Message":"This user-defined error message will appear in the progress log messages in Service Center."}}
    ```

This file must then be placed in the ["Result" folder](<../deploy-applications/zones/reference.md>). This information also appears in the publication log messages.

Example:  
`\\twoflower\luggage\results\07897a77-3f58-4e5b-b926-a48605c0b6d0_dab321f9-72e8-44e8-ae5c-2c8212314cf6.configsdone`

## Undeploy an Application in Containers

<div class="info" markdown="1">

Note: This operation is only **required** in scenarios when the application is deployed in a container deployment zone and it will be deployed to a deployment zone with a different address or using a different hosting technology.

</div>

The undeploy or removal of an application in containers requires the operator to create a result file whose name must match the expected name and have an `.undeploydone` extension; the expected filename appears in the publication messages. The contents of this file will depend on the result of the undeploy operation:

Successful
:   Create an empty file with the expected name (`.undeploydone` extension) on the configured "Result" folder of the deployment zone.

Failed
:   Create a JSON file with the correct filename and with a `.undeploydone` extension whose contents follows the template presented next — it contains a user-defined error message:

    ```
    {"Error":{"Message":"This user-defined error message will appear in the progress log messages in Service Center."}}
    ```

This file must then be placed in the ["Result" folder](<../deploy-applications/zones/reference.md>). This information also appears in the publication log messages.

Example:
`\\twoflower\luggage\results\07897a77-3f58-4e5b-b926-a48605c0b6d0_dab321f9-72e8-44e8-ae5c-2c8212314cf6.undeploydone`

After the result file is processed by the platform, the operator can terminate the container and remove any configurations related to the application in the Reverse Proxy and Load Balancer.

<div class="info" markdown="1">

**Find detailed instructions according to your hosting technology in the other topics in this section:**

* [Deploying an Application to a Docker Container](<app-run-docker.md>)
* [Deploying an Application to Pivotal Cloud Foundry](<app-run-pcf.md>)

You can also check [how to automate the deployment process](<app-run-automate.md>) using an automated deployment tool.

</div>

## The two deployment stages

There are two stages in the publishing operation that involve **creating a result file**: 

* Stage 3 (Create result file for the deployment preparation step);
* Stage 6 (Create result file for the deployment step).

Having these two stages allows you to separate the deployment preparation from the actual deployment, on which any needed database changes will occur. This is important because these database changes might leave the currently running application (from a previous deployment in the same environment) in an inconsistent state.

By reducing the time between applying the database changes and having your container-bound application readily available to end users you will minimize the impact of the deployment process on applications that were already available in the environment you are deploying to.
