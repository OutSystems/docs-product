---
summary: Learn how to create a new zone in Service Center.
---

# Create a New Deployment Zone

<div class="info">

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

    ![](<images/zone-add-front-end.png>)

    _Tip:_ The full name of the front-end server will appear as suggested text after you start typing it.

1. Click the **Add Server(s)** button to associate the entered front-end server names with the zone.

Note: Instead of defining the servers belonging to the deployment zone, you can check the "Includes all Servers" setting when creating the deployment zone. In this case, the platform will automatically include all servers in the deployment zone, including those added at a later date.
