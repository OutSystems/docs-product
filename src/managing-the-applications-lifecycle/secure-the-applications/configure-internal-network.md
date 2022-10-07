---
summary: Configure the range of IP addresses that are considered part of your internal network.
tags: support-Security-overview
locale: en-us
guid: 2326f357-2f2a-4a5c-a05d-fb20edd7be5f
app_type: traditional web apps, mobile apps, reactive web apps
---

# Configure an Internal Network

OutSystems applications can set the access to specific elements (Web UI Flows (**traditional web apps only**), exposed SOAP services, and exposed REST APIs) to be available only within an internal network, while other parts of the application are kept available to the general public.

<div class="info" markdown="1">

This procedure applies only to **self-managed environments**. For OutSystems Cloud installations, contact [OutSystems Support](https://www.outsystems.com/SupportPortal/CaseOpen/) and provide the desired internal network addresses.

</div>

To configure an internal network for your OutSystems environment, do the following:

1. Go to the Service Center management console of your OutSystems environment.

1. Go to the **Administration** section and select the **Security** tab.

1. Select the **Network Security** area.

    ![](images/configure-internal-network-1.png?width=600)

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
