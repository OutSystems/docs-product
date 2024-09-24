---
summary: How to configure an application in Service Center to use a specific deployment zone.
tags: support-Application_Lifecycle; support-Infrastuture_Architecture
locale: en-us
guid: eed19a98-c672-43ac-90c9-70b9f33d921a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Configure an Application to Use a Deployment Zone

<div class="info" markdown="1">

Only available in OutSystems on-premises installations.

</div>

After creating a new deployment zone and associating one or more front-end servers to it, you can change the configuration of OutSystems applications so that the platform deploys them to this deployment zone.

## Configure an application

To configure an application to use a given deployment zone do the following:

1. Go to the Service Center management console of your OutSystems environment.

1. Go to the **Factory** section and select the **Applications** tab.

1. Click the name of the application that you are deploying to the new deployment zone.

1. In the **Operation** tab, select the desired deployment zone in the **Deployment Zone** field.

1. Click the **Save** button.

1. Republish your application for the configuration changes to take effect.
