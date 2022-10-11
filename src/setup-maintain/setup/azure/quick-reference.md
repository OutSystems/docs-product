---
tags: support-Installation_Configuration; support-installation;
summary: More information about Azure Resources such as VMs, SQL databases, storage, virtual machine scale sets.
locale: en-us
guid: 88d66b58-baee-4c61-9d03-b21e5b4aeac9
app_type: traditional web apps, mobile apps, reactive web apps
---

# Quick Reference for OutSystems on Microsoft Azure

This article describes the Azure resources deployed by [OutSystems on Microsoft Azure](intro.md "OutSystems on Microsoft Azure Overview") solution template, which contains the OutSystems Development, Test, Production, and [LifeTime deployment management console](../../../managing-the-applications-lifecycle/intro.md) environments.

## Azure Resources

The Azure resources that the OutSystems on Microsoft Azure solution template deploys follow naming conventions based on the general [Azure naming conventions](https://docs.microsoft.com/en-us/azure/architecture/best-practices/naming-conventions). You can identify the deployed resources by the following:

* All resources are prefixed with the solution identifier (sol_id) that you chose and entered in the [solution template wizard](set-up-platform.md#run-the-solution-template-wizard "Set Up OutSystems on Microsoft Azure").
* Azure resources associated to a specific OutSystems environment will be named in a way that includes the environment short name: "dev" for Development, "test" for Test, "prod" for Production, and "life" for the LifeTime environment.

### Virtual Machines

Each environment contains a **virtual machine** as the OutSystems Platform Server, playing the role of deployment controller and front-end server.

![Deployment controller and front-end server](images/deployment_controller-and_front-end.png?width=400)

If you chose to deploy a farm production environment, your production environment will have a virtual machine and a scale set. The second one acts as the front-end server answering HTTP(S) requests.

![Additional front-end server](images/additional-front-end-server.png?width=300)

All virtual machines have Windows Server 2016 Datacenter installed.

You can choose the size of the virtual machines during the setup, in the solution template wizard. By default, "F4s_v2" size is selected for all environments.

The main features of the proposed sizes are:

 | |  **F4s_v2** (default)
---|---  
vCPUs  |  4  
Memory (GB)  |  8  
Temp Storage (GB)  |  32  
Max IOPS  |  8000
  
Check the [official Azure documentation](<https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes>) for detailed information on the different virtual machine sizes.

For security reasons, the deployed virtual machines have remote desktop access disabled. Check how to [enable remote desktop access for a virtual machine](additional-configurations.md#enable-remote-desktop-for-a-virtual-machine "OutSystems on Microsoft Azure - Additional Configurations").

### Azure SQL Database servers and databases

OutSystems on Microsoft Azure solution template uses Azure SQL Database service. Each environment contains one **SQL server** and three **SQL databases** \- the Platform/Applications database, the Logging database, and the Sessions database.

![Databases](images/databases.png?width=500)

The price tier of all created databases is "S3 Standard".

All database administration users are named "`VM_admin_user-sql`", where `VM_admin_user` is the user name you fill during the setup in the solution template wizard for the virtual machines administration user. The database administration user password is the same as for the virtual machine administration user.

### Storage Accounts

Each **solution template** deployment has an associated storage account. This storage account will hold the log files of the installation and configuration steps of each virtual machine **(one log folder for each VM)**, along with several configuration files used by the OutSystems environments.

### Application Gateways and Public IP Addresses

Each environment has an **application gateway** with an associated **public IP address**. This public IP Address is the entry point to the environment. Note that configurations involving private IP addresses, private-links and private endpoints are not part of the **OutSystems on Microsoft Azure Overview** solution template.

For example, if you have two front-end servers in your production environment, the entry point of the environment is the public IP address associated with the production application gateway.

Azure [application gateways](<https://azure.microsoft.com/en-us/blog/azure-web-application-firewall-waf-generally-available/>) provide baseline security against most of the [OWASP Top 10 vulnerabilities](<https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project>).

### Virtual Machine Scale Sets

In a Farm topology, the production environment is deployed with **virtual machine scale sets**, making these environments ready for horizontal scaling.

### Other Azure Resources

The following Azure resources are also deployed for each OutSystems environment to guarantee the infrastructure operation:

* Network interfaces
* Disk

## Resources Mapping

The table below shows examples of some of the Azure resources deployed for each environment, mapped into the main OutSystems components when applicable:

|OutSystems Component|Azure Resource Type|Azure Resource Name|Example|  
|:------------------:|:-----------------:|:-----------------:|:-----:|
|Non-production Platform Server|Virtual machine|`<sol_id>-<environment>-vm`|myid-dev-vm|
|Production Platform Server|Virtual machine|`<sol_id>-prod-vm`|myid-prod-vm|
|Production front-end server<br/>(Farm only)|Azure scale set|`<sol_id>-prod-vmss`|myid-prod-vmss|
|Database server|Azure SQL server|`<sol_id>-<environment>-srv<unique_suffix>` (*)|myid-dev-srvbqxs|
|Platform/Application database|Azure SQL database|`<sol_id>-<environment>-db`|myid-dev-db|
|Session database|Azure SQL database|`<sol_id>-<environment>session-db`|myid-devsession-db|
|Logging database|Azure SQL Database|`<sol_id>-<environment>log-db`|myid-prodlog-db|
|-|Application gateway|`<sol_id>-<environment>-appgw`|myid-dev-appgw|
|-|Storage account|`s<unique_suffix>` (*)|strbqxs|
|-|Public IP address|`<sol_id>-<environment>[appgw|VM]-PIP`|myid-dev-appgw-PIP|
|-|Virtual machine scale set|`<sol_id>-<environment>-VMSS`|myid-dev-VMSS|

(*) Storage accounts and SQL server resources include unique suffixes in their names because the resource name must be unique in the entire Azure infrastructure.
