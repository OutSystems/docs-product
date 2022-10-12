---
summary: How to create a new deployment zone in Service Center.
locale: en-us
guid: bcb24adb-f56c-4be3-afcc-6305fe0f0e4e
app_type: traditional web apps, mobile apps, reactive web apps
---

# Create a New Deployment Zone

<div class="info" markdown="1">

Only available in OutSystems on-premises installations.

</div>

To create a new deployment zone do the following:

1. Go to the Service Center management console of your OutSystems environment.

1. Go to the **Administration** section and select the **Deployment Zones** tab.

1. Click the **New Deployment Zone** link.

1. Fill in the [basic parameters](<reference.md>) for the deployment zone, namely its name and Deployment Zone Address.

1. Click the **Create** button.

After creating the zone, define which front-end servers belong to it. Do the following:

1. In the input box under "Associate Servers to this Deployment Zone", type the front-end server names you wish to associate with the zone.

    ![Associate front-end servers to deployment zone in Service Center](<images/zone-add-front-end.png>)

    _Tip:_ The full name of the front-end server appears as suggested text after you start typing it.

1. Click the **Add Server(s)** button to associate the entered front-end server names with the zone.

Note: Instead of defining the servers belonging to the deployment zone, you can check the "Includes all Servers" setting when creating the deployment zone. In this case, the platform automatically includes all servers in the deployment zone, including those added later.

<div class="info" markdown="1">

Configuring the deployment zone of individual modules is **deprecated** since Platform Server 11.8. Even though applications with modules in different deployment zones are still supported, OutSystems will stop supporting this option in the future.

For more information see [Modules and apps in deployments zones](modules-and-apps-in-deployment-zones.md).

</div>
