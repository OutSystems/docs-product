---
tags: azure integration, infrastructure setup, error handling, deployment troubleshooting, configuration management
summary: This guide details how to retrieve setup logs and configuration files for OutSystems 11 (O11) on Microsoft Azure.
locale: en-us
guid: 1e5925fb-8700-4998-a2b4-7a149caeb17d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/ZDYZVg9kmMXl758XX7ytXc/Setup%20and%20maintain%20your%20OutSystems%20Infrastructure?node-id=352:1278
audience:
  - platform administrators
  - infrastructure managers
  - full stack developers
outsystems-tools:
  - none
coverage-type:
  - understand
  - apply
---

# How to Get the Setup Logs of OutSystems on Microsoft Azure

When setting up OutSystems on Microsoft Azure, the first step is to [run the solution template wizard](set-up-platform.md#run-the-solution-template-wizard "Set Up OutSystems on Microsoft Azure") to deploy OutSystems infrastructure.

If an error occurs during this deployment phase, you will need the following information to troubleshoot the problem:

* OutSystems configuration file.
* The log files generated by the deployment process.
* The Azure Portal error stack.

This article shows you how to get this information.

## Get OutSystems Configuration File

For each OutSystems environment, you have a configuration file named **server.hsconf**.

To get this configuration file, do the following:

1. On your [Azure Portal](https://portal.azure.com), go to the resource group of your OutSystems infrastructure and select [the storage account associated](quick-reference.md#storage-accounts "Quick Reference for OutSystems on Microsoft Azure") with your deployment.

    ![Azure Portal showing the resource group of OutSystems infrastructure](images/Logs-Azure-1.png "Azure Portal Resource Group")

1. On the **Storage account** details page, click **Files** to access the storage account file service.

    ![Storage account details page with Files option highlighted](images/Logs-Azure-2.png "Storage Account Details")  

1. Select **share** from the list of file shares.

    ![List of file shares in the Azure storage account](images/Logs-Azure-3.png "File Shares in Storage Account")  

1. Select the directory corresponding to the virtual machine of the environment.

    ![Directory corresponding to the virtual machine in the Azure file share](images/Logs-Azure-4.png "Virtual Machine Directory")  

1. You will find **server.hsconf** configuration file in this directory. To download the file, select the file name and click **Download**.

    ![server.hsconf configuration file selected for download in Azure file share](images/Logs-Azure-8.png "Download server.hsconf File")

## Get the Log Files Generated by the Deployment Process

For each OutSystems environment, the infrastructure deployment process generates the following log files:

* Log.txt
* ConfigurationTool.log
* DevelopmentEnvironmentInstall.log
* PlatformServerInstall.log

To get these log files, do the following:

1. Follow steps 1 to 4 from section  **Get OutSystems Configuration Files** to go to the Directory corresponding to the virtual machine of the environment, inside the storage account file service. Then, select the **logs** directory.

    ![Navigating to the logs directory inside the Azure file share](images/Logs-Azure-9.png "Logs Directory in Azure File Share")  

1. You will find the log files in this directory. To download each file, select the file name and click **Download**.

    ![List of OutSystems log files available for download in Azure file share](images/Logs-Azure-6.png "Download Log Files")

## Get the Azure Portal Error Stack

To get the stack of the deployment error thrown in the Azure Portal, do the following:

1. Go to the Resource group of your OutSystems infrastructure and choose **Deployments** from the menu to the left.

    ![Azure Portal showing the Deployments section of the OutSystems resource group](images/Logs-Azure-7.png "Azure Portal Deployments Section")

1. Click on the failed deployment to expand the error and see the error stack.

    ![Detailed view of a failed deployment error stack in the Azure Portal](images/Logs-Azure-10.png "Azure Portal Deployment Error Stack")
