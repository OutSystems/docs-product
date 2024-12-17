---
tags: azure, configuration, deployment, remote access, ssl
summary: Explore advanced configurations for OutSystems 11 (O11) on Microsoft Azure, including remote access, SSL certificates, and scaling options.
locale: en-us
guid: 465ae50f-349c-4b1f-b082-565b3a653e7d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/ZDYZVg9kmMXl758XX7ytXc/Setup%20and%20maintain%20your%20OutSystems%20Infrastructure?node-id=352:1259
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

# Additional Configurations for OutSystems on Microsoft Azure

In this article you can find the instructions for some additional configurations you might want to apply to **OutSystems on Microsoft Azure**.

Check [OutSystems Documentation](https://success.outsystems.com/Documentation) and [Support Center](https://success.outsystems.com/Support) for further information.

## Enable Remote Desktop for a Virtual Machine

To access the machines remotely through RDF, you need to create a jump server - a dedicated VM with enabled RDP to reach and manage devices inside a network.

1. Create a VM with the RDP activated and connect to the VM. This is your jump server. Check [Quickstart: Create a Windows virtual machine in the Azure portal](<https://docs.microsoft.com/en-us/azure/virtual-machines/windows/quick-create-portal>) for detailed instructions. You can also use [Azure Bastion](https://azure.microsoft.com/services/azure-bastion).

1. Discover the IP of a machine you want to connect to. Access the machine in the Azure Portal and in the left blade choose **Networking**. The IP shows next to the label **Private IP**.

    ![Screenshot showing the Networking section in Azure Portal with the Private IP address highlighted](images/additconf-private-ip.png "Azure Portal Networking Section")  

1. After you connect remotely to the jump server, use it to connect to a machine inside the group by using the private IP of the machine.

## Add a Certificate Issued by a Certificate Authority to the Application Gateway of the Environment

SSL certificates enable secure connections between the web server and the web browser through HTTPS protocol. If you wish to build mobile applications with OutSystems, you will need a certificate from a public trusted authority to place on your application gateway.

SSL offloading is active by default on every environment. All access, both http and https, to the environments are made through the Application Gateway IP/DNS Address.

To add the trusted certificate to the application gateway of the environment, do the following:

1. Go to the details of the **application gateway** that was created for the environment and choose **Listeners** from the menu to the left.

    ![Screenshot of the Application Gateway details page with Listeners option highlighted in the Azure Portal](images/additconf-image12.png "Application Gateway Listeners")  

1. Select the **appGatewayHttpsListener**.

    ![Screenshot of the appGatewayHttpsListener selected in the Azure Portal](images/additconf-image20.png "appGatewayHttpsListener Selection")  

1. Add a new certificate by uploading the .pfx file and providing its password. Name it according to your preference.

    ![Screenshot showing the process of adding a new SSL certificate to the Application Gateway in Azure Portal](images/additconf-image11.png "Adding SSL Certificate to Application Gateway")

Note that you can set up the end-to-end encryption for traffic in Microsoft Azure, as described in the Microsoft document [Configure end to end SSL by using Application Gateway with PowerShell](https://docs.microsoft.com/en-us/azure/application-gateway/application-gateway-end-to-end-ssl-powershell).

## Scale Your Environments Using Azure Scale Sets

Your OutSystems environments are ready for horizontal scaling using **Azure virtual machine scale sets**. This is achieved scaling the number of front-ends of the environment with no need to manually install and register new servers into your infrastructure. To proceed with this operation, make sure your OutSystems license allows for multiple front-ends.

To scale the number of front-ends of an OutSystems environment on Microsoft Azure, do the following:

1. Go to your OutSystems resource group and list only the "Virtual machine scale sets" resources.

    ![Screenshot of the Azure Portal showing the Virtual Machine Scale Sets in the OutSystems resource group](images/additconf-image6.png "Azure Virtual Machine Scale Sets")  

1. Select the virtual machine scale set corresponding to your OutSystems Production environment.

    ![Screenshot of the Azure Portal with the Virtual Machine Scale Set for the OutSystems Production environment highlighted](images/additconf-image2.png "Selecting Virtual Machine Scale Set")

1. Choose **Scaling** from the menu to the left.

    ![Screenshot of the Scaling option in the menu for a Virtual Machine Scale Set in the Azure Portal](images/additconf-image5.png "Scaling Virtual Machine Scale Set")  

1. Drag the slide or input the number of servers you want to add to your environment and click **Save**.

    ![Screenshot showing the interface to adjust the number of instances in a Virtual Machine Scale Set in Azure Portal](images/additconf-image3.png "Adjusting Scale Set Instance Count")

Choosing **Instances** from the menu to the left, you can see the progress of the deployment.

![Screenshot of the Azure Portal showing the progress of deployment for new instances in a Virtual Machine Scale Set](images/additconf-image1.png "Deployment Progress of Scale Set Instances")

When the deployment finishes, you will see in the Service Center console for your environment that the new front-end servers are already running.

![Screenshot of the Service Center console in OutSystems showing the new front-end servers running after scaling](images/additconf-image25.png "New Front-end Servers Running")

## Update Azure Scale Sets to a Newer Platform Version

Follow these steps to update a Platform Server deployed on Microsoft Azure scale sets.

1. Go to **Service Center** > **Administration** > **Servers** and disable the servers that are part of the scale set. Deleting is optional, but advised, to ensure you stay within the limit of the front-ends your license permits.

    ![Screenshot of the Service Center in OutSystems with the option to disable servers in a scale set](images/azure-scale-sets-delete-env.png "Disabling Servers in Service Center")

1. Go to your Azure Portal and make sure **Scaling** > **Configure** > **Instance count** is 0.

    ![Screenshot of the Azure Portal showing the Instance count configuration set to 0 for a Virtual Machine Scale Set](images/azure-scale-sets-instance-count.png "Azure Scale Set Instance Count Configuration")

1. Update the Platform Server in your Deployment Controller, according to the checklist that opens in your browser when you run the update binary.

1. Go to the [Base Image Versioning table](<https://github.com/OutSystems/AzureARMTemplates/#base-image-versioning>) of the available image versions and note the version that matches the Platform Server you installed/updated in your Deployment Controller VM.

    ![Screenshot of the Base Image Versioning table on GitHub indicating available image versions for OutSystems](images/azure-image-versions.png "Base Image Versioning Table")

1. Update the Platform version by running the following command in your Azure Portal Powershell: `Update-AzVmss -ResourceGroupName "your_resource_group" -VMScaleSetName "your_scaleset_name" -ImageReferenceVersion your_desired_version`

    Here is an example:

    ![Screenshot of the Azure Portal Powershell interface with a command to update the Platform version of a Virtual Machine Scale Set](images/azure-powershell-image-update.png "Updating Platform Version in Azure Powershell")

    And here is the expected result. Notice that the version is updated to 1.6.0, which corresponds to the Platform Server 11.0.424.0:

    ![Screenshot showing the updated Platform version in a Virtual Machine Scale Set in the Azure Portal](images/azure-updated-image.png "Updated Platform Version in Azure")

1. Set the desired **Instance count** in the Azure Portal .

1. After a few minutes confirm that Service Center is reachable through the Application Gateway URL or the Public IP.
