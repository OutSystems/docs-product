---
summary: Understand how automatic updates to mobile apps work when you click on "1-Click Publish".
tags: runtime-mobile; support-application_development; support-Mobile_Apps
---

# Mobile App Update Scenarios

After you click on “1-Click Publish” the changes made to the mobile app automatically become available to the users with no need to install a new app version. The mobile apps running on the user devices automatically detect the updates when the apps establish a connection to the server. Only mobile app packages generated from an environment receive the new developments and changes published in that same environment.

## Detecting a new app version

To be up to date with the version on the server, there are several instances when the app checks for a new version. These instances are:

* Opening of the app.
* Navigation between screens.
* Call to the server, for example, to execute a Server Action or a Server Aggregate.

When there's a new version on the server, the app updates itself and notifies the user with a feedback message.

## Seamless upgrades and attention-requiring upgrades

**Seamless upgrade.** After detecting that a new version is available, the app starts caching all the new resources in the background. Once the app caches the resources, the next navigation event triggers the update. This can be, for example, a screen transition. Once the app is fully updated and the destination screen loads, the app notifies the user about the update with a feedback message. If the update takes time, the app shows the splash screen before navigating to the destination screen. This is a seamless upgrade.

**Attention-requiring upgrade.** An attention-requiring upgrade may happen when the user is on a screen that's changed in the new app version. If the user does something in the app that requires interaction with the server, that interaction may fail due to the upgrade requirements. For example, tapping a button to save data calls a Server Action, but because that action now has a different signature, the action fails. The user then sees a message that a new version is available and required to proceed. Clicking that message updates the app. After the update, the app loads the updated screen and shows the message that the app is up to date.

When there's a Form widget on the screen, the message about the required update also informs the user that the information they entered in the Form will be lost, because the app needs to reload. The data saved in local storage and Client Variables isn't affected.

<div class="info" markdown="1">

The technical preview [Configure mobile apps updates distribution](manage-distribution-options/intro.md) lets you select between **hybrid updates**, described in this document, and **store-only updates**. 

</div>

## Situations when the update isn't possible in the device

There may be situations when the automatic update of the app isn't possible in the user device, even when there are no issues during the publishing step. Possible causes:

* Poor network connection to download the resources needed for the update.
* Local data model upgrade that the app can't update automatically.
  
In situations where the app can't update itself on the device of the user, the app rolls back to the most recent fully working version. There's also a message that the update wasn't possible and that the user should restart the app and then try updating the app again.

When the error happens while updating the local storage data model, possibly because the existing data is incompatible with the new data model, the message informs the user that they may need to reinstall the app if the problem persists. The reinstallation clears the current app data.

You can find the issue and the cause in the Service Center logs by looking for "Upgrade failed - rolling back to previous application version". The information in the log should help you discover the cause of the upgrade failure and implement a fix in a new version of the app.

## Situations when the user must install a new build

Even though every time you publish the app the platform makes the changes automatically available to the app, some changes require installation of an updated app package on the user device. This happens when you **change** one of the following:

* App name.
* App icon.
* Main color of the app. 
* An external resource of a plugin.
* Configurations for a mobile platform.
* Entry module or the name of the entry module name. 
* Extensibility Configurations property (for example: modification, addition or removal of mobile plugins, changes to status bar transparency, custom icons or splash screens, and similar) 

These changes may negatively affect the user experience in the outdated apps, but the issues are automatically fixed when the user upgrades to the latest app package. In the case of plugins, it's a good practice to include fallbacks in the apps to avoid crashing until the latest app version is on the device. 

<div class="warning" markdown="1">

When installing a new version of an Android app already installed on the device and generated using the build type "Debug", uninstall the previous version from the device before installing the new one. This guarantees the new features work correctly.

</div>

After the first mobile app generation, every time you click “1-Click Publish”, OutSystems generates a new app package in the situations listed above. You can then download those app packages via Service Studio, Service Center, and LifeTime. This guarantees that the latest app package available to download from the environment is synchronized with the development of the app.
