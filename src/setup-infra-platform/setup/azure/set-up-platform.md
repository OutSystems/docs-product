---
tags: azure, cloud deployment, licensing, security certificates, infrastructure management
summary: Learn how to deploy and configure OutSystems 11 (O11) on Microsoft Azure, including licensing, certificate installation, and environment registration.
locale: en-us
guid: 4a33c4a9-87b2-4ce0-9523-93c937f53fdd
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/ZDYZVg9kmMXl758XX7ytXc/Setup%20and%20maintain%20your%20OutSystems%20Infrastructure?node-id=352:1238
audience:
  - platform administrators
  - infrastructure managers
  - full stack developers
outsystems-tools:
  - lifetime
coverage-type:
  - understand
  - apply
---

# Set up OutSystems on Microsoft Azure

This article describes the steps to deploy and set up OutSystems on Microsoft Azure.

<div class="info" markdown="1">

Prerequisites: OutSystems on Microsoft Azure solution template is available on Microsoft Azure Marketplace under Bring-Your-Own-License (BYOL) pricing model. To deploy OutSystems on Microsoft Azure, start by [contacting OutSystems](https://www.outsystems.com/pricing-and-editions/#contact-us) and get your license.

</div>

To deploy and set up OutSystems on Microsoft Azure you must execute the following steps:

1. [Run the solution template wizard in Azure Portal to deploy your OutSystems infrastructure.](#run-the-solution-template-wizard)
1. [Apply your OutSystems license to the deployed environments.](#apply-your-outsystems-license)
1. [Add a valid certificate to the environments.](#add-a-valid-certificate-to-the-environments)
1. [Register the environments on your OutSystems deployment management console (LifeTime).](#register-the-environments-in-lifetime)
1. [Install the extended product components.](#install-the-extended-product-components)

## Run the solution template wizard

1. Go to [Azure Marketplace](https://azuremarketplace.microsoft.com "Azure Marketplace") or your [Azure Portal](https://portal.azure.com) and search for **OutSystems on Microsoft Azure** solution template.

1. On your [Azure Portal](https://portal.azure.com), in the OutSystems on Microsoft Azure solution template, click the **Create** button to proceed to the deployment wizard.

1. Fill in the information for the **Basics** blade and click OK to proceed to the next blade. The **Solution Identifier** you choose prefixes the name of all resources created during the deployment, such as virtual machines or databases. In the **Resource Group** section click **Create new** and enter a name.

    ![Screenshot of the Azure Setup Basics blade with fields for Solution Identifier and Resource Group](images/azure-setup-basics.png "Azure Setup Basics Blade")

1. In the **Virtual Machine Size** blade, choose between a Standalone (1 VM) or a Farm (1 VM and 1 scale set) production environment. Select the size of each virtual machine, using one of the recommended sizes. Click **OK** to proceed to the next blade.

    ![Screenshot showing the selection of virtual machine size in Azure with options for Standalone or Farm production environment](images/azure-vm-size.png "Azure Virtual Machine Size Selection")

1. In the **Virtual Network Size** blade, confirm the values for the **Virtual network** and **Subnets** sections, and click **OK** in the **Subnets** section. Click **OK** to proceed to the next blade.

    ![Screenshot of the Azure Virtual Network Size blade with Virtual network and Subnets configuration options](images/azure-subnets.png "Azure Virtual Network and Subnets Configuration")  

1. Click **OK** in the **Summary** blade.

    ![Screenshot of the Azure Summary blade displaying a summary of the deployment settings](images/azure-summary.png "Azure Deployment Summary")  

1. Click the **Create** button in the **Buy** blade to start the deployment.

The deployment process might take about 1 hour to complete. You can check the deployment status in the **Deployments** section of the resource group. OutSystems deployment is finished when all the listed deployments are successful.

![Screenshot showing the deployment status of OutSystems on Microsoft Azure in the Azure Portal](images/setup-image11.png "OutSystems Deployment Status in Azure")

In your Azure Portal, you now have a resource group with the name that you defined in the deployment wizard. This group contains all the newly created resources. All the [resources deployed](quick-reference.md#azure-resources "OutSystems on Microsoft Azure - Quick Reference") by OutSystems on Microsoft Azure solution template are prefixed with the solution identifier:

![Screenshot of the Azure Portal displaying the resource group with all resources created by the OutSystems solution template](images/setup-image15.png "OutSystems Azure Resources")

## Apply your OutSystems license

The next step is to apply your OutSystems license to each environment:

* Development
* Test
* Production
* LifeTime deployment management console

To set up OutSystems on Microsoft Azure you must have a valid [OutSystems license](https://www.outsystems.com/licensing).

To apply your OutSystems license to the **development** environment, do the following:

1. Go to the details of the **application gateway** created for the development environment to get the **DNS name** of its public IP address. For example, if your solution identifier is "myid", the application gateway of the development environment is "myid-dev-appgw". Click on the Frontend public IP address field to go to the details page of the public IP address.

    ![Screenshot of the Azure Portal showing the application gateway details for the OutSystems development environment](images/setup-image4.png "OutSystems Development Environment Application Gateway")  

1. Access the environment through the **DNS name** of the public IP address. In the Public IP address details page, use the "Click to copy" option to copy the DNS name.

    ![Screenshot of the Azure Portal with the DNS name of the public IP address for the OutSystems environment](images/setup-image7.png "OutSystems Public IP Address DNS Name")  

1. Using the DNS name from the previous step, access the Service Center management console of the environment with the following URL: `http://<DNS_name>/ServiceCenter`.

1. Log on using the following user credential:

    * Username = `admin`
    * Password =  password set in step 3. of the ["Run the Solution Template Wizard" section](#run-the-solution-template-wizard)

1. Go to the Administration section and select the Licensing tab.

1. Take note of the **Serial Number** of the environment. You need this to get the license file from the OutSystems customer portal.

    ![Screenshot of the Service Center management console displaying the Serial Number of the OutSystems environment](images/setup-image9.png "OutSystems Environment Serial Number")  

1. Follow the steps at [Get a license file for an environment](https://success.outsystems.com/Support/Enterprise_Customers/Licensing/Manage_and_Upgrade/03_Get_a_license_file_for_an_environment#Self-managed_environments) to register the Serial Number and download the license file.

1. Once you have the license file (`*.lic`), go back to the Licensing tab of Service Center and follow the steps to [install a license file](https://success.outsystems.com/Support/Enterprise_Customers/Licensing/Manage_and_Upgrade/04_How_to_install_a_license_file).

1. Repeat the same procedure to apply the license to the remaining environments - Test, Production, and LifeTime.

## Add a valid certificate to the environments

To register the Development, Test, and Production environments in LifeTime, you must first install valid certificates in the Application Gateways of all environments. Use certificates signed by a Certificate Authority.

To add the trusted certificate to the Application Gateway of each environment (including LifeTime) do the following:

1. Go to the details of the **Application Gateway** that was created for the environment.

1. From the Settings menu, select **Listeners**.

    ![Screenshot of the Azure Portal showing the Listeners settings in the Application Gateway](images/additconf-image12.png "Azure Application Gateway Listeners")  

1. Select **Add listener** to create an HTTPS listener with your certificate. Enter the settings in the **Add listener** screen as follows:

    | Setting                                | Value                              |
    | -------------------------------------- | ---------------------------------- |
    | Listener name                          | appGatewayHttpsListener            |
    | Frontend IP                            | Public                             |
    | Protocol                               | HTTPS                              |
    | Port                                   | 443                                |
    | Choose a certificate                   | Create new                         |
    | Choose a certificate (HTTPS Settings)  | Upload a certificate               |
    | Cert name                              | Enter a name of your choice        |
    | PFX certificate file                   | Select your .pfx certificate file  |
    | Password                               | Enter the certificate password     |
    | Enable SSL Profile                     | Leave unchecked                    |

### Add a routing rule for HTTPS traffic

After creating the HTTPS listener, you need to add a routing rule to direct incoming HTTPS traffic to the backend pool.

1. From the Settings menu, select **Rules** > **Routing rule**. The **Add a routing rule** screen opens.

1. In the **Listener** tab, enter the following settings:

    | Setting       | Value                   |
    | ------------- | ----------------------- |
    | Rule name     | httpsrule               |
    | Priority      | 2                       |
    | Listener      | appGatewayHttpsListener |

1. Select the **Backend targets** tab and enter the following settings:

    | Setting          | Value                         |
    | ---------------- | ----------------------------- |
    | Target type      | Backend pool                  |
    | Backend target   | appGatewayBackendPool         |
    | Backend settings | appGatewayBackendHttpSettings |

1. Select **Add** to create the routing rule.

1. Repeat the steps in this section for all remaining environments (Test, Production, and LifeTime).

## Register the environments in LifeTime

To register your environments in the LifeTime deployment management console, do the following:

1. Go to the details of the **application gateway** created for the LifeTime environment to get the **DNS name** of its public IP address. For example, if your solution identifier is "myid", the application gateway of the LifeTime environment is "myid-life-appgw". Click on the Frontend public IP address field to go to the details page of the public IP address.

    ![Screenshot of the Azure Portal showing the application gateway details for the OutSystems LifeTime environment](images/setup-image22.png "OutSystems LifeTime Environment Application Gateway")  

1. Access the environment through the **DNS name** of the public IP address. In the Public IP address details page, use the "Click to copy" option to copy the DNS name.

    ![Screenshot of the Azure Portal with the DNS name of the public IP address for the OutSystems LifeTime environment](images/setup-image18.png "OutSystems LifeTime Public IP Address DNS Name")  

1. Using the DNS name from the previous step, access the LifeTime console with the following URL: `http://<DNS_name>/LifeTime`.

1. To register the development environment, use the **DNS name** of the public IP address associated with its application gateway, for example "myid-devappgw-PIP". Go to the details of the **public IP address** and use the "Click to copy" option to copy the DNS name.

    ![Screenshot of the Azure Portal with the DNS name of the public IP address for the OutSystems environment](images/setup-image7.png "OutSystems Public IP Address DNS Name")  

1. Follow the instructions on [registering an environment in LifeTime](../lifetime-configure.md#register-an-environment), using the DNS name you copied in the step below as the Environment Address in the environment registration wizard.

1. The development environment is now registered in LifeTime. Repeat the process for the Test and Production environments.

At this point, we recommend that you change your password for the LifeTime administration user (admin). Choose **My Settings** on the top right side of the LifeTime header to go to your settings page where you can change your password. Changing the admin password on LifeTime automatically changes the admin password of the Service Center management console of each registered environment.

![Screenshot of the LifeTime console with the option to change the admin password highlighted](images/setup-image20.png "OutSystems LifeTime Admin Password Change")

## Install the extended product components

In this step you install the extended product components, a set of OutSystems modules that provide essential features for development. These components are available on the Forge repository. To install them, you need the OutSystems Community user name and password - which you can get from the [OutSystems sign up page](https://www.outsystems.com/home/signup.aspx).

There are eight components that you need to set up in your **development environment only**. What follows is an example on how to install the Charts Web component. Follow the steps for the remaining components.

1. Open Service Studio and click **Connect to environment**. In the **Environment** field enter the DNS name of the public IP address that belongs to your development environment. Enter your user name and password. Click **Connect**.

1. Click the **OutSystems** tab in the upper-left corner to open the Forge repository tab. If not logged in already, log in with your credentials for the OutSystems Community profile.

1. Go to the search field. Enter "Charts Web" and click **Search**. Click the result "Charts Web" to navigate to the details screen.

1. Click **Install**. After the system verifies the prerequisites the message "Application is ready to be installed" shows.

    ![Screenshot of the OutSystems Forge showing the message 'Application is ready to be installed'](images/forge-ready-to-install.png "OutSystems Forge Installation Confirmation")

1. Again, click **Install**. The application list in Service Studio opens, with a progress bar under the icon of the Charts Web component. The icon disappears after the installation finishes.

    ![Screenshot of the OutSystems Service Studio with a progress bar indicating the installation of an application](images/applinstall.png "OutSystems Service Studio Application Installation")

1. Follow the steps 2 to 5 to install the remaining extended product components.

### The list of the extended product components

Here is the list of all extended product components that you need to install, in the order as shown:

1. [OutSystems Charts Web](https://www.outsystems.com/forge/4142/) (we used it in the installation example)
1. [OutSystems Charts](https://www.outsystems.com/forge/4141/)
1. [OutSystems UI Web](https://www.outsystems.com/forge/4143/)
1. [OutSystems UI](https://www.outsystems.com/forge/component/1385/silk-ui-mobile/)
1. [OutSystems Sample Data](https://www.outsystems.com/forge/4145/)
1. [OutSystems UI Web Screen Templates](https://www.outsystems.com/forge/4146/)
1. [OutSystems UI Templates Mobile](https://www.outsystems.com/forge/4148/)
1. [OutSystems UI Templates Reactive](https://www.outsystems.com/forge/6335/)

And you are done! At this point, your OutSystems on Microsoft Azure is ready to use. Check [additional configurations](additional-configurations.md "OutSystems on Microsoft Azure - Additional Configurations") to learn more about configurations you might want to execute in your OutSystems infrastructure.
