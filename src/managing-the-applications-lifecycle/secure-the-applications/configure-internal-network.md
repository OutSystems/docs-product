---
summary: Configure the range of IP addresses that are considered part of your internal network.
tags: support-Security-overview
locale: en-us
guid: 2326f357-2f2a-4a5c-a05d-fb20edd7be5f
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=267:93
---

# Network Security - Service Center

Sub-header here: Configure an Internal Network

OutSystems applications can set the access to specific elements (Web UI Flows (**traditional web apps only**), exposed SOAP services, and exposed REST APIs) to be available only within an internal network, while other parts of the application are kept available to the general public.

<div class="info" markdown="1">

This procedure applies only to **self-managed environments**. For OutSystems Cloud installations, contact [OutSystems Support](https://www.outsystems.com/SupportPortal/CaseOpen/) and provide the desired internal network addresses.

</div>

To configure an internal network for your OutSystems environment, do the following:

1. Go to the Service Center management console of your OutSystems environment.

1. Go to the **Administration** section and select the **Security** tab.

1. Select the **Network Security** area.

    ![Screenshot of the Network Security area in the OutSystems Service Center where the Internal network addresses field is highlighted](images/configure-internal-network-1.png "Internal Network Configuration")

1. Fill in the **Internal network addresses** field with the list of IP addresses or ranges from which you want to allow the access to the management consoles and the endpoints of your applications defined as Internal Access Only. Assure you include also the IP addresses/ranges of the controller, all front-end servers and monitoring tools.

1. Click the **Save** button.

Clicking Save will invalidate the Service Center cache. After checking the cache was invalidated, all the running applications in the environment will load the new settings.

When you define an internal network for a specific OutSystems environment, it will affect the access to the following tools:

* The Service Center console of the environment
* The LifeTime console of the environment, if the environment where the configuration was applied is a LifeTime environment
* Connections from Service Studio, Integration Studio and OSP Tool to the environment

In the case you inadvertently define an internal network configuration that blocks you from accessing Service Center, you can:

* [use the Configuration Tool to clear the internal network settings](../../ref/configuration-tool/tabs/network.md) currently defined, if it's a self-managed environment;
* contact [OutSystems Support](https://www.outsystems.com/SupportPortal/CaseOpen/) to revert or adjust the internal network addresses if it's an OutSystems Cloud environment.


Sub header here: Configure a Trusted Proxy

On the same page, you can find a configuration called Trusted proxy addresses: where you can add a Load Balancer or proxy address that will be always trusted by the platform.

This will be a list of IP addresses or ranges of addresses for proxies that inject X-Forwarded-For headers and must be respected by the platform (as load balancers). This also helps for scenarios where multiple IT users will be accessing the platform or a specific application through a load balancer, and if there is an issue for a user that tries to log in consecutively, it will not block the load balancer IP address, this way not blocking all IT users that use the load balancer/proxy to access that application. , such as our brute force mechanism would work. (provide brute force mechanism article here: https://success.outsystems.com/documentation/11/managing_the_applications_lifecycle/secure_the_applications/protection_against_brute_force_attacks/ ). This can also be helpful when trying to run debug sessions when your infrastructure has multiple Front-end servers behind a proxy scenario, as Service Studio will need to match the origin IP address with the developer IP address (Only for Traditional Web applications, Reactive and Mobile applications don't fall into this scenario)

Leaving the field empty means the platform will not look at the header.

To add load balancer or proxy addresses, you simply need to:
1 - Add the address to the configuration box.
2 - Save the change made.
3 - Apply settings to the whole factory.


Same warning as the one at the start of the page:

This procedure applies only to self-managed environments. For OutSystems Cloud installations, this is currently not supported.
