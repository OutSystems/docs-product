---
summary: Specify a container-based deployment zone for an application when you are deploying it to a target environment for the first time in LifeTime.
---

# Deploy an Application to a Container

<div class="info" markdown="1">

Containers is a [Technical Preview](<https://www.outsystems.com/goto/technical-preview>).

</div>

You can specify the deployment zone of an application when you are deploying it to a target environment for the first time using LifeTime. This allows you to define the desired deployment zone, namely a containers deployment zone, for an application from the start, instead of having to deploy it to the default deployment zone first and then move it to a different deployment zone.

This option is only available when there is **more than one deployment zone** configured in the target environment and when the application is being deployed for the first time to the target environment.

To define the deployment zone for an application in LifeTime, do the following:

1. In LifeTime, follow the [usual procedure](<deploy-an-application.md>) to deploy an application to a target environment up to the final deployment screen containing the "Deploy Now" button.  
You will need to:  
a) Click the 'Deploy...' button between source and target environments;  
b) Select the application to deploy;  
c) Validate the deployment;  
d) Click "Continue".

1. In the final deployment screen (the one with the "Deploy Now" button), click the "Change Deployment Settings" link for the desired application to change its deployment zone.

    ![](<images/lifetime-change-deployment-zone.png>)

1. Select the desired deployment zone in the pop-up window.

    ![](<images/lifetime-deployment-settings.png>)

1. Click the "Deploy Now" button.

To complete the deployment, follow the same steps presented in [Publish an Application to a Container](<../containers/app-run.md#publish-an-application-to-a-container>) using Service Center from stage 2 onwards, taking into account the activity log messages presented in the LifeTime deployment progress screen.

![](<images/lifetime-deployment-log-messages.png>)


## Identifying applications deployed to containers

Applications that were deployed to a containers deployment zone will have a "Container" badge in LifeTime close to the version information, like in the following example:

![](<images/lifetime-containers-badge.png>)
