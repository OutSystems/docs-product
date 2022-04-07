---
summary: How to configure an application to be deployed to a specific deployment zone.
tags: support-Application_Lifecycle; support-Infrastuture_Architecture
locale: en-us
guid: eed19a98-c672-43ac-90c9-70b9f33d921a
---

# Configure an Application to Use a Deployment Zone

<div class="info" markdown="1">

Only available in OutSystems on-premises installations.

</div>

After creating a new Deployment Zone in your OutSystems environment, you can configure the settings of your OutSystems applications so that the platform deploys them to this Deployment Zone.

For the applications already deployed in that environment, you can configure the Deployment Zone setting in the LifeTime console or in the environment's Service Center console, as described below.

For applications being deployed to that environment for the first time, you can [configure the Deployment Zone during the deployment](zone-configure-during-deploy.md).

## Configure an application in LifeTime

In your LifeTime console (`https://<your_lifetime_server>/lifetime`), do the following to configure an application to be deployed to a specific deployment zone in an environment:

1. In the **Applications** list, search for the application you want to configure.

1. Click the application's name to go to the application details page.

1. Click the **Settings** menu.

1. Select the environment where the deployment zone was created.

1. Choose the **Deployment Zone** where you want the application to be deployed.

1. Click **Save**.

1. Republish your application for the configuration changes to take effect.

## Configure an application in Service Center

In the environment's Service Center console (`https://<environment>/ServiceCenter`), do the following to configure an application to be deployed to specific deployment zone:

1. Go to the **Factory** section and select the **Applications** tab.

1. In the **Applications** list, search for the application you want to configure.

1. Click the application's name to go to the application details page.

1. In the **Operation** tab, choose the **Deployment Zone** where you want the application to be deployed.

1. Click **Save**.

1. Republish your application for the configuration changes to take effect.
