---
tags:
summary: Learn more about which users can access Experience Builder and how apps are generated and published.
locale: en-us
guid: 043fef18-091f-4d30-b347-29aeda65ed38
---

# How Experience Builder works

Experience Builder is a Software as a Service (SaaS) tool that lets you create mobile apps that are then published to one of your non-production environments.

You can use Experience Builder with environments that meet the [prerequisites](how-setup.md#your-environment) and that belong to infrastructures on OutSystems Cloud, on other public or private clouds, or on-premises.

Use a **non-production environment** with Experience Builder, preferably your **development environment** to ensure apps go through the same application development lifecycle as other OutSystems apps.

Since Experience Builder focuses on the creation of the front end of mobile apps, you'll probably need to expand and adapt these apps using Service Studio before you share them with your final end users.

## Users

Experience Builder authenticates IT users by contacting your environment to validate the user credentials.

To use Experience Builder you must have an [IT user](../../managing-the-applications-lifecycle/manage-it-teams/intro.md) that has the [correct permissions](how-setup.md#your-user) for the environment.  
All IT users in your infrastructure that have these permissions can use Experience Builder to create and publish apps.

Every Experience Builder user can access and edit all Experience Builder apps created in that environment.

## Apps

An Experience Builder app starts out as a draft that's only accessible and editable in Experience Builder. You can these use these drafts to generate mobile apps that are published in your environment.

Once you start publishing an app, Experience Builder goes through the following steps:

1. Connect to your environment and get information about the dependencies of the app.

2. Check if all the dependencies are installed and up to date, and if your app has any issues that may prevent publishing or using the app. Issues can be blockers or warnings, check the out the [list blockers and warnings](ref/error-ref.md).

3. Depending on the results of the validations performed in the previous step, one of the following occurs:

    * If issues are found, Experience Builder lists the issues so you can fix them. If the issues are warnings, you can still force the publishing of the app.

    * If no issues are found, Experience Builder generates and then publishes the app in the environment.

The first time you publish an app, Experience Builder may take up to 5 minutes to conclude the process. The next time you publish the same app, Experience Builder takes less time.

Once an app is published you can try it out in your browser or mobile device.

If you continue to edit your app in Experience Builder and then publish it, you create a new version of the app.

Once you are satisfied with the UI flows, you can start [adapting and extending the app in Service Studio](extend-app-in-ss.md), by adding your own data and business logic, integrating with other apps or external services, and adding more screens.

<div class="warning" markdown="1">

Make sure you are done editing your app in Experience Builder before editing it in Service Studio, since changes you make to the app in Service Studio aren't visible in Experience Builder.

Publishing a new version of the app using Experience Builder overwrites changes made to the app in Service Studio.

</div>
