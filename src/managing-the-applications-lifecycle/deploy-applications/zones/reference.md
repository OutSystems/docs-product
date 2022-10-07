---
summary: Reference information on deployment zone parameters.
locale: en-us
guid: 73511ea5-c2d6-493a-9d84-bbc699e84fc5
app_type: traditional web apps, mobile apps, reactive web apps
---

# Deployment Zones Reference

<div class="info" markdown="1">

Only available in OutSystems on-premises installations.

</div>

Each deployment zone has the following parameters:

Name
:   The name that identifies the deployment zone. This name appears in several places in the UI, so it should be meaningful of what it represents.

    Examples: `Business backend`, `Services`, `Core factory`, `Intranet`

Description
:   The purpose of the deployment zone. You can use this field to store any relevant information to better understand how the zone is used and what kind of applications should be added to it.

Is Default for new modules
:   Boolean parameter that, when active, states that the current deployment zone is the [default deployment zone](<intro.md#default-deployment-zone>). You can set a deployment zone as the default one by clicking "Set as Default".

Deployment Zone Address
:   Address for all applications living in the deployment zone, intended for internal communications. When applications in other deployment zones need to refer applications living in this deployment zone and do not want to use the environment URL, they will use this address. If you enabled **Use HTTPS for internal communications** in a Deployment Zone, make sure that the address defined in the **Deployment Zone Address** field is covered by the certificate.

    <div class="info" markdown="1">

    You can only change the Deployment Zone Address if there are no modules deployed in that deployment zone.

    </div>

    This address may vary according to your network architecture. For example with only one front-end server, the "Deployment Zone Address" can be the machine's hostname. However, with multiple front-ends, the "Deployment Zone Address" should be the Fully Qualified Domain Name (FQDN) of the device responsible for the communication between these front-end servers, for example, a load balancer.

    Learn how this address must fit in your network architecture in [Recommended Network Architecture](<network-architecture.md#configuring-the-address-of-deployment-zones>).

    The platform installation must be able to access this address on ports 80 and 443. Anything living in this deployment zone must be able to reach the platform installation on the port defined for the Deployment Controller Service (by default, 12000).

    This address must be a valid machine domain name or IP address, and **it cannot have a port**.

    Valid examples: `192.168.42.23`, `intranet.mydomain.com`, `rincewind.lan`
  
    Invalid examples: `192.168.42.23/site`, `192.168.42.23:8080/site`, `rincewind.lan/university`

Use HTTPS for internal communications
:   Boolean parameter that, when active, causes all communication made by OutSystems applications in another deployment zones to applications in the current deployment zone to be made via HTTPS.

Includes all Servers
:   Boolean parameter that, when active, makes the platform automatically include all servers in the current deployment zone, including those added later. When this parameter is active you can't manually add or remove servers from the deployment zone.

Some changes to deployment zones settings require you to republish your applications to be effective. You may also have to republish the consumers of your applications.
