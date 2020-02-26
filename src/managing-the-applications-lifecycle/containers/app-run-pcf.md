---
summary: Detailed instructions on how to deploy an application to Pivotal Cloud Foundry.
tags: support-Application_Lifecycle
---

# Deploying an Application to Pivotal Cloud Foundry

<div class="info" markdown="1">

**Before you start**, make sure that:

* You meet the [system requirements](<https://success.outsystems.com/Support/Archive/11/OutSystems_Platform_system_requirements#Containers_considerations>) and [network requirements](<https://success.outsystems.com/Support/Archive/11/OutSystems_network_requirements#Containers_considerations>) for deploying to containers, and the specific requirements for Pivotal Cloud Foundry;
* You follow the [recommended network architecture](<architecture.md>);
* You have read and followed the [general instructions required for deploying to containers](<app-run.md>), namely having a properly configured deployment zone.

</div>

The following sections contain specific information on using Pivotal Cloud Foundry (PCF) hosting technology and detailed instructions on publishing an application to PCF.

## SSL Offloading

Make sure you have followed the instructions in [End-to-end SSL and SSL Offloading](<https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Using_OutSystems_in_Reverse_Proxy_Scenarios/03_OutSystems_configurations_in_reverse_proxy_scenarios#C_-_End-to-end_SSL_and_SSL_Offloading>). You **do not** need to follow the step instructing you to add a new record to the `OSSYS_PARAMETER` database, since the platform already does this step for you when deploying to containers.  
If these instructions are not followed before publishing the application, you will need to republish the application and push it again to PCF.

## Publish an Application to PCF

<div class="info" markdown="1">

**Before publishing your application**, ensure that in Pivotal Apps Manager your "org" has the two recommended domain entries, according to the [System Requirements](<https://success.outsystems.com/Support/Archive/11/OutSystems_Platform_system_requirements#Containers_considerations>) for PCF deployments.

</div>

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

### 2. Push the application to PCF 

In this second stage the operator (either a human person or an automated deployment tool) must perform a set of operations outside the scope of the OutSystems platform.

Perform the following steps to push your application to PCF:

1. Extract the contents of the application bundle ZIP file into a given folder.

1. Copy the `private.key` file from the platform installation folder (usually `C:\Program Files\OutSystems\Platform Server`) to the `secrets` folder inside the application bundle.

1. Copy the `App.config` file from folder of the application (with the same name as the resulted file name) inside the ["Output Configs To" folder](<../deploy-applications/zones/reference.md>) configured for the deployment zone to the `configs` folder inside the application bundle.

1. Using PowerShell, navigate to the target folder and run the following command:

    `cf push --no-start`

    This will push the application to PCF and prepare it to be started. When the command runs successfully, its output will contain the **application name on PCF**, which is based on the OutSystems application name.

<div class="info" markdown="1">

**Important:** Always start the application via the command line, instead of the Pivotal Apps Manager. The command line is the only way to ensure that all pre-requisites are met when the application starts.

</div>

### 3. Create result file for the deployment preparation step

During the second step, Service Center is expecting the result file for the "Preparing Deploy" step after pushing the application. Thus, you need to create the result file for the "Preparing Deploy" step with the expected name. The contents of this file will depend on the result of push the application to PCF step:

Successful deployment preparation
:   Create an empty file with the expected name (`.preparedone` extension) on the configured "Result" folder of the deployment zone.

Failed deployment preparation
:   Create a JSON file with the correct filename and with a `.preparedone` extension whose contents follows the template presented next — it contains a user-defined error message:

    ```
    {"Error":{"Message":"This user-defined error message will appear in the progress log messages in Service Center."}}
    ```

    Then copy the result file to the configured "Result" folder of the deployment zone.

 This file must then be copied in the configured ["Result" folder](<../deploy-applications/zones/reference.md>) (the same folder mentioned in the publication messages). The filename must exactly match the expected name and have a `.preparedone` extension.

Example:  
`\\twoflower\luggage\results\07897a77-3f58-4e5b-b926-a48605c0b6d0_dab321f9-72e8-44e8-ae5c-2c8212314cf6.preparedone`

### 4. Start the container

In this fourth stage the operator (either a human person or an automated deployment tool) starts the previously pushed application.

Perform the following steps to start the container:

1. Run the following command in PowerShell:

    `cf start <app_name>`

    Replace the `<app_name>` with the application  name in PCF, as stated in the output of the previous `cf push` command.

    If the operation succeeds, this will output the status of the application.

1. Check that the application inside the container is running by issuing the following command in PowerShell:
    
    `cf app <app_name>`

    This will output the status of the application.

### 5. Define network routing rules for container

In this fifth stage the operator makes the application inside the container reachable using the deployment zone address.

First, you will need to add route mappings so that the PCF router knows how to handle requests to the applications modules:

1. Download the [`PCFUtils.psm1` PowerShell module](<https://github.com/OutSystems/ContainerAutomation/blob/master/misc/pcf/PCFUtils.psm1>) into a given folder.  
Note: This script requires that the PowerShell Execution Policy is set to `Unrestricted`. For more information check [Microsoft's documentation](<https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-6>).

1. In a PowerShell console, execute the following command to import the module:

        Import-Module <path>/PCFUtils.psm1
    
    Replace `<path>` with the parent folder you choose for the script.

1. In the same PowerShell console, execute the following command to add to PCF the routes for each module of your application

        Add-CFRoutes -Filepath <bundle_path> -AppName <app_name> -PublicAddress <public_address> -ZoneAddress <zone_address>

    Replace:

    * `<bundle_path>` with the path to the application bundle ZIP file
    * `<app_name>` with the application name in PCF, as stated in the output of the previous `cf push` command
    * `<public_address>` with your public address of your main load balancer and reverse proxy, as described in the [PCF requirements](<https://success.outsystems.com/Support/Archive/11/OutSystems_Platform_system_requirements#Pivotal_Cloud_Foundry>)
    * `<zone_address>` with your PCF zone address (also as described in the [PCF requirements](<https://success.outsystems.com/Support/Archive/11/OutSystems_Platform_system_requirements#Pivotal_Cloud_Foundry>))

    In summary, this function will obtain the module names (`<module_name_N>`) of your application from the ZIP file and execute the following commands for each of them:

        cf map-route <app_name> <public_address> --path <module_name_N>
        cf map-route <app_name> <zone_address> --path <module_name_N>

If the operation succeeds, the command will output the status of the application.

Additionally, you will likely need to configure several routing rules **on your main load balancer and reverse proxy** so that requests coming from outside your internal network can reach the different OutSystems application modules running inside the Pivotal Cloud Foundry containers. 

<div class="info" markdown="1">

**PCF Example: Define PCF Routes and Configure IIS Routing Rules**

Check [Define PCF Routes and Configure IIS Routing Rules](<https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Pivotal_Cloud_Foundry%3A_Define_PCF_Routes_and_Configure_IIS_Routing_Rules>) to learn how you can use IIS to perform the network routing to your application running in a container; the document describes how to define the minimum routing rules needed in this scenario.  
Be sure to validate your final routing configuration with your Network and DevOps teams.

</div>

Check if your application modules are reachable using the deployment zone address configured for the application and using your public address (if applicable).  
For example, if you have an application with modules "Directory" and "Employees" then they must be at least reachable at addresses `<zone_address>/Directory` and `<zone_address>/Employees`. If they are meant to be publicly accessible, they will also need to be accessible at addresses `<public_address>/Directory` and `<public_address>/Employees`.

### 6. Create result file for the deployment step

In this stage the operator creates a deployment result file for the "Deploying" step with the expected name. The contents of this file will depend whether you were capable of successfully starting the container:


Successful deployment
:   Create an empty file with the expected name (`.deploydone` extension) on the configured "Result" folder of the deployment zone.

Failed deployment
:   Create a JSON file with the correct filename and with a `.deploydone` extension whose contents follows the template presented next — it contains a user-defined error message:

    ```
    {"Error":{"Message":"This user-defined error message will appear in the progress log messages in Service Center."}}
    ```

    Then copy the result file to the configured "Result" folder of the deployment zone.


This file must then be placed in the configured in the ["Result" folder](<../deploy-applications/zones/reference.md>) configured for the application's deployment zone, the same folder that is mentioned in the publication messages. The filename must exactly match the expected name and have a `.deploydone` extension. The expected filename is also shown in the publication messages.

Example:  
`\\twoflower\luggage\results\07897a77-3f58-4e5b-b926-a48605c0b6d0_dab321f9-72e8-44e8-ae5c-2c8212314cf6.deploydone`
