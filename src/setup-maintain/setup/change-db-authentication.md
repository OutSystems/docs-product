---
summary: Changing SQL Server database authentication to Windows Authentication or Database Authentication.
tags:
locale: en-us
guid: 34EF8749-5F32-456F-965D-5FF41037B82C
app_type: traditional web apps, mobile apps, reactive web apps
---

# Change SQL Server database authentication mode 

<div class="info" markdown="1">

This article applies only to self-managed environments using SQL Server databases (not applicable to Azure SQL databases).

</div>

This article describes how to change the SQL Server database authentication to Windows Authentication or Database Authentication. If you want to update an existing OutSystems platform installation to start using a different authentication mode in the database, you need to complete these steps to avoid undesired behaviors.  

Find below the steps you need to follow for standalone or farm installations.

## Standalone installations

For standalone installations, follow these steps:

<div class="info" markdown="1">

To reduce downtime during the process, you can execute the steps of the Database Catalogs (under step 9) beforehand, although you can’t test the connections in Service Center.

</div>

1. Open the Configuration Tool in the OutSystems Server.

1. On the **Platform** tab, in the **Database** section, set the **Authentication** to the desired authentication mode.

1. Configure the usernames and passwords for all users.

1. Click **Grant Permissions**.

1. Check everything is ok with the connection for each user, by clicking **Test Connection**.

1. If you changed the authentication to Windows Authentication, and if your machine has Application Pools configured to run OutSystems apps besides the OutSystemsApplications pool:  
    1. Go to the **IIS Management Console**.
    1. For each pool running OutSystems apps, set the **Identity** in **Advanced Settings** to match the Runtime user, and click **Ok**.

    If you changed the authentication to Database Authentication, we recommend that you restore the Application Pools **Identity** to the NetworkService or ApplicationPoolIdentity.

1. On the **Session** tab, click **Create Session Database**. 

1. Click **Apply and Exit**.  
A message to publish the latest version of Service Center displays. Click **OK**.

1. If there are Database Catalogs configured:
    1. Open **Service Center**.
    1. Go to **Administration** > **Database Catalogs**.
    1. For each configured catalog (other than Main), enable users to access that catalog in the database by assigning these roles to:  
        * The Admin user: db_accessadmin, db_datareader, db_datawriter, db_ddladmin and db_securityadmin.
        * The Runtime user: db_datareader and db_datawriter.

        <div class="info" markdown="1">

        Notes:   
        <ul>
        <li> If the Catalog was configured before Platform Server 7.0 with a specific Runtime user, we recommend changing it to the same user configured in the Configuration Tool. </li>
        <li> Using specific users is only allowed for backward compatibility. </li>
        </ul>
        
        </div>

    1. Test the connection of each database catalog using a tool like SQL Server Management Studio.
    1. Republish all modules.

## Farm installations

For Farm installations, follow these steps:

<div class="info" markdown="1">

Notes:
<ul>
<li>In Farm Installations there can be a temporary problem contacting the Session database between the step to grant permissions in each front end (step 7.3), and the step to apply the configurations to the controller (step 10).</li>
<li>To reduce downtime during the process, you can execute the steps of the Database Catalogs (step 13) beforehand, although you can’t test the connections in Service Center.</li>
</ul>

</div>

1. Open the Configuration Tool in the controller machine.

1. On the **Platform** tab, in the **Database** section, set the **Authentication** to the desired authentication mode.

1. Configure the usernames and passwords for all users. Note that users may be required to have Run as a Service permissions on the front-end servers.

1. Click **Grant Permissions**.

1. Check everything is ok with the connection for each user, by clicking **Test Connection**.

1. Click **File** > **Export Configuration** and save the configuration file.

1. On each front-end, do the following in the Configuration Tool:
    1. Click **File** > **Import Configuration** and choose the configuration file exported previously.
    1. Go to the **Database** tab. With Windows Authentication, passwords are not saved; so, if needed, configure the usernames and passwords for all users.
    1. Click **Grant Permissions**.
    1. Check everything is ok with the connection for each user, by clicking **Test Connection**.
    1. If you changed the authentication to Windows Authentication, and if you have machines with Application Pools configured to run OutSystems apps besides the OutSystemsApplications pool:  
        1. Go to the **IIS Management Console**.
        1. For each pool running OutSystems apps, set the **Identity** in **Advanced Settings** to match the Runtime user, and click **Ok**.  
          
        If you changed the authentication to Database Authentication, we recommend that you restore the Application Pools **Identity** to the NetworkService or ApplicationPoolIdentity.

1. On the Configuration Tool in the controller machine, go to the **Session** tab.

1. Click **Create Session Database**. To avoid downtime, set the Session state to a different database than the one for which you changed the authentication mode.

1. Click **Apply and Exit**.  
A message to publish the latest version of Service Center displays. Click **Cancel**.

1. On each front end, click **Apply and Exit**.

    <div class="info" markdown="1">

    If you have multiple front-end servers, you can avoid downtime by performing this operation one front end at a time. Leave at least one front end untouched until you’re sure that all apps republish.

    </div>

1. On the Configuration Tool in the controller machine, click **Apply and Exit**.  
A message to publish the latest version of Service Center displays. Click **OK**.

1. If there are Database Catalogs configured:
    1. Open **Service Center**.
    1. Go to **Administration** > **Database Catalogs**.
    1. For each configured catalog (other than Main), enable users to access that catalog in the database by assigning these roles to:  
        * The Admin user: db_accessadmin, db_datareader, db_datawriter, db_ddladmin and db_securityadmin.
        * The Runtime user: db_datareader and db_datawriter.
        * The Log role: db_datareader and db_datawiter.

        <div class="info" markdown="1">

        Notes:   
        <ul>
        <li> If the catalog was configured before Platform Server 7.0 with a specific Runtime user, we recommend changing it to the same user configured in the Configuration Tool. </li>
        <li> Using specific users is only allowed for backward compatibility. </li>
        </ul>

        </div>

    1. Test the connection of each database catalog using a tool like SQL Server Management Studio.
    1. Republish all modules.


## Impact on OutSystems Services and Application Pools

Changing  the authentication to Windows Authentication causes some changes in Outsystems Services and Application Pools.  

Accounts used to run OutSystems Windows Services change as follows:

| Service                                  | Log on as*    |
|------------------------------------------|---------------|
| OutSystems Deployment Controller Service | Administrator |
| OutSystems Deployment Service            | Administrator |
| OutSystems Scheduler Service             | Runtime       |

Application Pool identities change as follows:

| Name                            | Identity*     |
|---------------------------------|---------------|
| OutSystemsServerApiAppPool      | Administrator |
| OutSystemsServerIdentityAppPool | Administrator |
| ServiceCenterAppPool            | Runtime       |
| OutSystemsApplications          | Runtime       |

(*) Administrator and Runtime are Windows users configured in the Configuration Tool.

<div class="info" markdown="1">

Reverting to Database Authentication doesn’t revert the changes done to Application Pools identities and OutSystems Windows services Log-On accounts.

</div>


