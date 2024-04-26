---
summary: Mobile apps updates distribution setting lets you control how the apps update on user devices. Select store-only updates or hybrid updates. The store-only updates go through Google Play or the Apple App Store, and always update the native shell. In hybrid updates, apps can update the logic inside the existing native shell automatically, or require an update of native shell.
tags: runtime-mobile; support-application_development; support-Mobile_Apps
locale: en-us
guid: c9f2e601-8b4c-4dc7-93d4-e456c058b6f4
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/RizSdkiVSDYFb97Vqvc7oj/Delivering%20Mobile%20Apps?node-id=310:36
---

# Technical Preview - Configure mobile apps updates distribution

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

With **mobile apps updates distribution settings**, you can choose how apps update on user devices. This technical preview introduces store-only updates, as an addition to the existing hybrid updates. Here is an overview of the two models for updating mobile apps:

**Store-only updates** require the download of the entire native build to the user devices. These are updates through Google Play or the Apple App Store, or a private store. The store updates always bring both the native shell of the app to user devices and the app logic. This a traditional store distribution model.

**Hybrid updates** are lightweight updates where the app itself downloads only the new app parts, without downloading and updating the native mobile shell. These updates are efficient when you slightly change the UI or logic, and when the app works with the already installed native shell. When the changes require an update of the entire app, you can still publish the app via the app store.

## Prerequisites

These are the prerequisites to manage how mobile apps update on user devices.

### Activating the feature

To manage how mobile apps update on user devices, you need to meet the following requirements:

* Platform Server 11.10 or later.
* LifeTime 11.6.0 or later.
* MABS 6.2 or later.
* You activated the [technical preview](https://success.outsystems.com/Support/Release_Notes/Technical_Preview_features) **Configure Mobile application updates distribution** in LifeTime in **all environments**. You need to activate this option for each new environment you add afterward. If the option is off for any of the environments in the Technical Preview settings screen, it's turned off in all deployment plans you create.
* You create and distribute the native mobile builds of your apps to submit them to the app stores. This means you created and app based on **Phone App** or **Tablet App** in Service Studio. 
* Ensure you can follow the steps in [How to develop an app that updates only through the app stores](#how-to-develop-an-app-that-updates-only-through-the-app-stores).

### Deactivating the feature

You can deactivate this technical preview only after you meet both of these conditions:

1. You turned off the store-only updates **for all apps**. You can do this with [a new deployment plan that activates the hybrid updates](#set-hybrid-updates).
1. You turned off the store-only updates **in all environments**. You can do this in the [Technical Preview settings](https://success.outsystems.com/Support/Release_Notes/Technical_Preview_features).

These steps ensure that the deployment in LifeTime works correctly and that the apps continue working for your users.


## How LifeTime manages the configuration of mobile apps updates { #about }

Deployment plans in LifeTime let you configure how apps update on the user devices. LifeTime keeps the settings local to the app and the environment, so you need to change the setting **per app and per target environment**:

* **Per app**. LifeTime stores the updates deployment setting of each app in the deployment plan. When you create a deployment plan, LifeTime by default configures all apps in the plan to receive hybrid updates until you change the plan setting to store-only updates **for one or more apps**.
* **Per target environment**. LifeTime stores the deployment setting of an app for the target environment. LifeTime applies the default hybrid update setting for all environments until you change the deployment setting for the app and **for the target environment**.

Here is an example. There are three environments in LifeTime: DEV, TEST, and PROD. The team is developing MyApp in DEV. Your goal is to create a native app build in PROD, so you can submit the app to the app stores. You also want to test the native build in TEST.

You need to run the following deployment plans **when your first deploy** MyApp across all environments:

1. Plan A, from DEV to TEST. Configure MyApp for store-only updates in Plan A and deploy to TEST. With this, MyApp still receives hybrid updates in DEV.
1. Plan B, from TEST1 to PROD. Configure MyApp for store-only updates in Plan B and deploy to PROD.

![Diagram illustrating a sample deployment plan with store-only updates configuration across DEV, TEST, and PROD environments](images/deployment-sample-diag.png "Sample Deployment Plan")

### Mobile app update preferences

When you create a new deployment plan in LifeTime, you can change the update preferences in the **Configure applications settings** step. In the **DISTRIBUTION** tab, there are the following options under **Mobile application update preferences** section:

* **Updates are automatically pushed through your servers, and optionally through the app stores. (recommended).** When you select this option, the native mobile apps in the deployment plan receive the **hybrid updates**. This is the **default setting** for both apps and environments.
* **Updates are distributed only through the app stores.** This is an optional setting that you need to activate per app and per environment, by adding apps to the deployment plan with this option on. When you select this option, the native mobile apps receive the **store-only updates**. The option applies to native mobile apps only, as progressive web apps (PWAs) always get the latest updates you deploy.

![Screenshot of the Distribution tab in a LifeTime deployment plan showing mobile application update preferences](images/distribution-tab-deployment-plan-lt.png "Distribution Tab in Deployment Plan")


## Configure a mobile app to update through the stores only { #set-store-only-updates}

Edit the distribution settings in the deployment plan. In LifeTime, locate **Configure application settings** screen of the deployment configuration, and then click the **DISTRIBUTION** tab. Here are the instructions with more details.

<div class="info" markdown="1">

To configure all environments for store-only updates, you need to configure the app in each environment through separate deployment plans. See the [introduction of this document](#about) for more information.

</div>

1. Go to the **Applications** screen in LifeTime.

1. Decide what's your source environment and what's your target environment. For example, your source environment is the development environment (DEV) and the target is the testing environment (TST).

    ![Screenshot of the Applications screen in LifeTime displaying a list of apps and environments](images/applications-screen-lt.png "Applications Screen in LifeTime")

    <div class="warning" markdown="1">

    To ensure the users receive automatic updates after you submit a new version to an app store, tag your app with a valid native build version number. See [Tag a version](<../../tag-a-version.md>) for more information on how to properly increment the app version. 

    </div>

1. Click the **DEPLOY** button on the left side of your target environment.

    ![Screenshot highlighting the Deploy button on the Applications screen in LifeTime](images/applications-deploy-button-lt.png "Deploy Command in LifeTime")
 
1. If the deployment plan contains no apps, the **Choose one or more Applications** dialog opens. Select your app, click **Add to Deployment Plan** and close the dialog.

    ![Dialog window for adding an application to a deployment plan in LifeTime](images/add-app-to-deployment-plan-lt.png "Add App to Deployment Plan")

1. In the deployment plan screen, click **VALIDATE NOW**. The deployment validation starts.

    ![Screenshot showing the Validate Now button for a pending deployment plan in LifeTime](images/validate-deployment-plan-lt.png "Validate Deployment Plan")

1. Click **CONTINUE** after the validation succeeds. The deployment settings screen opens.

1. Click the **Configure applications settings** tab to open the settings.

    ![Screenshot of the screen to edit the deployment plan in LifeTime](images/edit-deployment-plan-lt.png "Edit Deployment Plan in LifeTime")

1. Click the **DISTRIBUTION** tab and locate the **Mobile application update preferences** section. Select **Updates are distributed only through the app stores**, and then click **Continue** to return to the deployment settings screen.

    ![Screenshot of the Distribution tab where 'Updates are distributed only through the app stores' is selected](images/configure-updates-distribution-app-store-only-lt.png "Configure Updates Distribution for App Store Only")

    If you have several apps in your deployment plan, click each of the app names in the **All remaining applications** section and then configure each app. Click **Continue** after you configure all apps.

    ![Screenshot showing the configuration of multiple apps for updates through the app stores only](images/configure-updates-distribution-app-store-only-multiple-lt.png "Configure Multiple Apps for Updates Through App Stores Only")


1. Click **Deploy Now**, and then confirm the deployment plan. The deployment overview screen opens, showing the deployment running in the background. Once LifeTime finishes deploying your app to the target environment, a confirmation message shows.

If your app is ready for distribution, generate the native build and submit the app to the app stores. See the **See Also** section in this document for further instructions.

## Configure a mobile app to receive hybrid updates { #set-hybrid-updates }

Read this section for instructions on how to turn off the store-only updates and switch back to the default hybrid updates in the deployment plans.

<div class="info" markdown="1">

For more details about the steps, see the section about configuring the [store-only updates](#set-store-only-updates). 

</div>

1. Create a new deployment plan and add one or more apps to it.
1. Turn on the hybrid updates. Select **Updates are automatically pushed through your servers, and optionally through the app stores** in the **Configure applications settings** step. If you have more than one app in the deployment plan, do this for each app.
1. Run the deployment plan and deploy your app to the target environment.
1. Check the update setting of the app to confirm you successfully configured the app to receive hybrid apps. See [Check how users get updates for a mobile app](#check-how-users-get-updates-for-a-mobile-app).
1. Repeat the steps for all environments where you previously deployed the apps with the store-only deployment setting.

## Check how users get updates for a mobile app

Follow these steps to check if an app receives store-only updates or hybrid updates.

1. In LifeTime, go to the **Applications** screen.

1. Find the app and then select the name in the results list. The app details screen opens.

1. Click **Settings** to open the app settings screen.

    ![Screenshot of the app details screen in LifeTime with the Settings button highlighted](images/app-details-lt.png "App Details Screen in LifeTime")

1. At the top of the screen, click the name of the environment in **Settings in (ENVIRONMENT)**, and then select the environment from the list.

    ![Screenshot of the environment selection list in LifeTime app settings](images/app-settings-select-environment-lt.png "Environment Selection in LifeTime App Settings")


1. Scroll down to the **Advanced** section and check the text next to **Native Mobile Application Updates**:

    * **Automatically pushed through your servers.** The app receives hybrid updates.
    * **Distributed only through the app stores.** The app receives updates only through the app stores.

    ![Screenshot of the Advanced settings section showing the mobile updates configuration status](images/app-settings-advanced-updates.png "Advanced Settings and Mobile Updates Configuration Status")

## How to develop an app that updates only through the app stores

If you're a Service Studio developer or LifeTime administrator, keep in mind the following workflow for managing apps with store-only updates distribution.

1. Before you change the app updates setting, define a minimum app version and generate the new version with Platform Server 11.10. You need to ensure that the **users have the version of the app that recognizes the new distribution configuration**. Check out the community-contributed plugins [App BuildInfo Plugin](https://www.outsystems.com/forge/component-overview/5580/app-buildinfo-plugin) and [Mobile Force Install Manager](https://www.outsystems.com/forge/Component_Documentation.aspx?ProjectId=3493) to assist you in meeting this requirement.

1. Create logic that's resistant to breaking changes. Here are the two key guidelines. 
    
    * If you're changing the logic on the server side, **change the server logic without breaking the resulting API hash signatures**. Avoid changing elements like Server Action or Aggregates by adding or removing new parameters. Instead, create a new API version, and leave the old logic to work on the old app versions.

    * **Avoid removing the logic on the client side**; instead, add If nodes to prevent the new version from using the old logic. This makes the app logic more resilient to breaking changes.

    <div class="warning" markdown="1">

    It's of a paramount importance that you edit the logic so the app works correctly for all users that decide to update the app.

    </div>

1. Activate store-only updates in the testing and deployment environments (option **Updates are distributed only through the app stores**).

1. Create a tag with a higher version number of the app in LifeTime **before the app reaches the production environment**. This ensures that the app updates automatically for users who activated the updates in Google Play or the Apple App Store, as the new build has a higher version number and triggers an update once you upload the app to the stores. See [Tag a version](<../../tag-a-version.md>).

1. Consider reviewing and editing the upgrade messages that users see in the app. In Service Studio, go to the module properties and locate the **Upgrade Messages** section. Those messages are about hybrid updates, and don't fit cases where users need to update the app through the store. For example, following the instruction "tap here to update" works for an app with hybrid updates, but not for app with the store-only update setting.  

    ![Screenshot of the default upgrade messages in Service Studio module properties](images/upgrade-messages-properties-ss.png "Upgrade Messages in Service Studio Module Properties")

1. Test your app extensively. With the store-only updates, your users may update the apps less frequently, and you need to ensure that the native shell, the client side, and the server side of your app work correctly for all existing and new users.

1. Manually start the generation of a native mobile build in the target environment. In the current version of this technical preview, you need to start the build process manually. 

1. Submit the build to the app stores.

<div class="info" markdown="1">

Check out the instructions about [publishing and distributing Android apps](../generate-distribute-mobile-app/publish-google-play-store.md) and about [publishing and distributing iOS apps](../generate-distribute-mobile-app/publish-apple-app-store.md).

</div>
