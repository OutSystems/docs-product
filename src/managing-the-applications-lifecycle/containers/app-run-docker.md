---
summary: Detailed instructions on how to deploy an application to a Docker Container.
tags: support-Application_Lifecycle
---

# Deploying an Application to a Docker Container

<div class="warning" markdown="1">

Container deployment is available as an [Early Access Program](<https://www.outsystems.com/goto/technical-preview>).

</div>

<div class="info" markdown="1">

**Before you start**, make sure that:

* You meet the [system requirements](<https://success.outsystems.com/Support/Archive/11/OutSystems_Platform_system_requirements#Containers_considerations>) and [network requirements](<https://success.outsystems.com/Support/Archive/11/OutSystems_network_requirements#Containers_considerations>) for deploying to containers, and the specific requirements for Docker Containers;
* You follow the [recommended network architecture](<architecture.md>);
* You have read and followed the [general instructions required for deploying to containers](<app-run.md>), namely having a properly configured deployment zone.

</div>

The following sections contain specific information on using Docker Containers hosting technology and detailed instructions on publishing an application to a Docker container.

## Sharing Data with a Docker Container

OutSystems applications running in Docker containers make use of **volumes** to read information from outside the container, namely configurations and the environment key. This allows the application running inside the container to change its runtime behavior without having to build a new Docker image. 

![](<images/docker-volumes-mapping.png>)

As such, we will need two folders, one for the configurations (`<host_configs_folder>`) and another for the environment key (`<host_secrets_folder>`). These folders can be located anywhere in the machine which will run Docker or in another machine, as long as Docker Engine has access to them. These folders will be mapped to folders inside the containers. The folder `<host_configs_folder>` will be mapped to the folder `c:\configs` of the container and the folder `<host_secrets_folder>` will be mapped to the folder `c:\secrets` of the container.

 The process of deploying an application to a Docker container explained below assumes, for a matter of simplicity, that these folders were placed in the container host machine.

### Configurations Folder

Specifying a mounted volume for the configurations folder allows you to change the settings of OutSystems applications without having to build a new Docker image. 

To change OutSystems application settings, place the [updated configuration file](<./app-run.md#update-configurations>) belonging to the application in the folder `<host_configs_folder>` being mapped and the application will automatically fetch the new settings.

### Secrets Folder

Some of the platform capabilities use encryption and need an environment key, but this key is **not distributed** with the container code. This key file is named `private.key` and can be found in the OutSystems platform installation folder (usually `C:\Program Files\OutSystems\Platform Server`). The procedure described below will show how you can share this key with the container.

## SSL Offloading

Make sure you have followed the instructions in [End-to-end SSL and SSL Offloading](<https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Using_OutSystems_in_Reverse_Proxy_Scenarios/03_OutSystems_configurations_in_reverse_proxy_scenarios#C_-_End-to-end_SSL_and_SSL_Offloading>). You **do not** need to follow the step instructing you to add a new record to the `OSSYS_PARAMETER` database, since the platform already does this step for you when deploying to containers.  
If these instructions are not followed before publishing the application, you will need to update the configuration of the deployed application.

## Publish an Application to a Docker Container 

These instructions build upon the general steps outlined in [Publish an Application to a Container](<app-run.md#publish-an-application-to-a-container>). Make sure you have read them before proceeding.

### 1. Compile application and generate bundle

To start the publish process and generate an application bundle, do the following:

1. In Service Center, navigate to Factory > Applications and click on your application name;

1. Click the "Publish" button.

Service Center shows the progress of this stage, which includes compiling the application, generating the binaries and providing the application bundle later used to build a container image.

After creating the bundle, Service Center shows two important pieces of information in the last log messages:

Generated bundle filename and full path (ZIP file)
:   This file is used in the second stage of deploying an application to a container. The filename is defined according to the following template: `<ApplicationKey>_<OperationId>.zip` 

    Example:  
    `\\twoflower\luggage\bundles\07897a77-3f58-4e5b-b926-a48605c0b6d0_dab321f9-72e8-44e8-ae5c-2c8212314cf6.zip`

Expected result filename and full path for deployment preparation step
:   The name and path of the result file for the "Preparing Deploy" step that you must provide (either manually or through some automation tool). For now ignore this message, as this will be tackled in step 3.

### 2. Build container image

In this second stage the operator (either a human person or an automated deployment tool) must perform a set of operations outside the scope of the OutSystems platform.

Do the following:

1. Extract the contents of the application bundle ZIP file into a folder.

2. Using PowerShell, navigate to the target folder and build a container image by running the following command:

    `docker image build -t <image_name> .`

    This command builds an image ready to be launched and registers it in the local Docker registry. The `-t` tag flag and the argument following it is used to give the image a name.

    _Optional:_ At this point you can register the built image in your central Docker registry, if you are using one.

### 3. Create result file for the deployment preparation step

During the second step, Service Center is expecting the result file for the "Preparing Deploy" step after building the container image. Thus, you need to create the result file for the "Preparing Deploy" step with the expected name.

The contents of the result file will depend on the result of build container image step:

Successful deployment preparation
:   Create an empty file with the expected name (`.preparedone` extension) on the configured "Result" folder of the deployment zone.

Failed deployment preparation
:   Create a JSON file with the correct filename and with a `.preparedone` extension whose contents follows the template presented next — it contains a user-defined error message:

    ```
    {"Error":{"Message":"This user-defined error message will appear in the progress log messages in Service Center."}}
    ```

    Then copy the result file to the configured "Result" folder of the deployment zone.


This file must then be placed in the configured ["Result" folder](<../deploy-applications/zones/reference.md>) (the same information appears in the publication log messages). The filename must exactly match the expected name and have a `.preparedone` extension. This information appears in the publication messages.

Example:  
`\\twoflower\luggage\results\07897a77-3f58-4e5b-b926-a48605c0b6d0_dab321f9-72e8-44e8-ae5c-2c8212314cf6.preparedone`


### 4. Instantiate container image

In this fourth stage the operator (either a human person or an automated deployment tool) instantiates the previously created container image into a running container.

Before starting the container, you will need to configure the `<host_config_folder>` and `<host_secrets_folder>` folders.

#### 4.1 Configuration folder

<div class="info" markdown="1">

You can skip this step if you are using the same folder for both purposes (i.e. if the folder belonging to the application (with same name as the expected name of the result files) which is inside deployment zone's "Output Configs To" folder will be mounted as a Docker container volume in stage 3).

</div>

When deploying a container-bound application to Docker Containers, the OutSystems platform will create an `App.config` file in a folder inside the ["Output Config Files to" folder](<../deploy-applications/zones/reference.md>) specified in the configuration of the deployment zone set for the application.

To set up the configuration file, do the following:

* Copy the `App.config` configurations file from the folder belonging to the application (i.e. with same name as the expected name of the result files) which is inside the deployment zone's ["Output Configs To" folder](<../deploy-applications/zones/reference.md>) to the `<host_config_folder>`, i.e a folder of your choice.


#### 4.2 Secrets folder

<div class="info" markdown="1">

You can skip this step if you have already deployed an OutSystems application into containers, since you can use the same `host_secrets_folder` folder for multiple Docker containers with OutSystems applications.

</div>

OutSystems applications in containers require a key file named `private.key` which can be found in the OutSystems platform installation folder (by default `C:\Program Files\OutSystems\Platform Server`).

To share this file with the container, do the following:

* Copy the `private.key` file to the `<host_secrets_folder>` folder, i.e a folder of your choice.


#### 4.3 Running the container

To instantiate a container image do the following:

1. Run the following command in PowerShell:

    `docker run --name <container_name> -d -v <host_config_folder>:c:\configs:ro -v <host_secret_folder>:c:\secrets:ro <image_name>`
    
    The `<container_name>` argument can be any name of your choice, but `<image_name>` must be the name of the image you defined in step 2 (Build container image).    
    The two `-v` parameters will mount volumes for configuration settings and secrets. The local folder `<host_config_folder>` on the hosting machine is being mapped to the container folder `c:\configs` and `<host_secret_folder>` is being mapped to the container folder `c:\secrets`, both in read-only mode (`:ro`). Replace `<host_config_folder>` with the folder on the containers host machine that contains the configuration file generated when publishing the application in Service Center and `<host_secret_folder>` with the folder on the containers host machine that contains the environment private key (`private.key` file).

    If the operation succeeds, this will output the full container ID. The operation will fail if a container already exists with the name `<container_name>`; in this case, choose a different name for the container, e.g. `<container_name>_1`.

1. Check that the container is running by issuing the following command in PowerShell:
    
    `docker ps`

    This will output the status and ID of the container. The ID is the first set of 12 hexadecimal characters of the full ID shown in the output.


### 5. Define network routing rules for container

In this fifth stage the operator makes the application inside the container reachable using the deployment zone address.

Usually it’s necessary to define a network routing configuration so that requests coming from outside the container host machine can reach the application modules running inside the container. Note that when the container IP address changes, the routing rules might need to be changed also.

Check if your application modules are reachable using the deployment zone address configured for the application.  
For example, if you have an application with modules "Directory" and "Employees" then they must be reachable at addresses `<zone_address>/Directory` and `<zone_address>/Employees`.

You will need to configure several routing rules so that requests coming from outside the container host machine can reach the different application modules running inside the container.

<div class="info" markdown="1">

**Docker Containers Example: Configure Routing Rules in IIS**

Check the [Configure Routing Rules in IIS](<https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Docker_Containers%3A_Configure_Routing_Rules_in_IIS>) document to learn how you can use IIS to perform the network routing to your application running in a Docker container; the document describes how to define the minimum routing rules needed in this scenario.  
Be sure to validate your final routing configuration with your Network and DevOps teams.

</div>

### 6. Create result file for the deployment step

In this stage the operator creates a deployment result file for the "Deploying" step with the expected name. The contents of this file will depend whether you were capable of successfully instantiate the container image:

Successful deployment
:   Create an empty file with the expected name (`.deploydone` extension) on the configured "Result" folder of the deployment zone.

Failed deployment
:   Create a JSON file with the correct filename and with a `.deploydone` extension whose contents follows the template presented next — it contains a user-defined error message:

    ```
    {"Error":{"Message":"This user-defined error message will appear in the progress log messages in Service Center."}}
    ```

    Then copy the result file to the configured "Result" folder of the deployment zone.

This file must then be placed in the configured ["Result" folder](<../deploy-applications/zones/reference.md>), the one that also appears in the publication messages. The filename must exactly match the expected name and have a `.deploydone` extension. It must also match the one that appears in the publication messages.

Example:  
`\\twoflower\luggage\results\07897a77-3f58-4e5b-b926-a48605c0b6d0_dab321f9-72e8-44e8-ae5c-2c8212314cf6.deploydone`
