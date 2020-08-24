---
summary: How to configure an application in Service Center to use a specific deployment zone.
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

1. If the new deployment zone uses a **container-based hosting technology**, you need to republish your application for the configuration changes to take effect.

    On the other hand, if the selected deployment zone uses the **Classic Virtual Machines** hosting technology, the application is automatically deployed to the front-end servers included in the deployment zone. The application is also removed from all front-end servers that don't belong to the deployment zone.
