---
summary: Understand how automatic updates to mobile apps work when you click on "1-Click Publish".
tags: runtime-mobile; support-application_development; support-Mobile_Apps
---

# Mobile App Update Scenarios

When developing a mobile app, after you click on “1-Click Publish” the changes made to the app automatically become available to the users with no need to install a new app version. The mobile apps running on the user devices automatically detect the updates when the apps establish a connection to the server. Only mobile app packages generated from an environment receive the new developments and changes published in that same environment.

## Detecting a new app version is available

To be up to date with the version on the server, there are several instances when the app checks for a new version. These instances are:

* Opening of the app
* Navigation between screens
* Call to the server, for example, to execute a Server Action or a Server Aggregate

When there's a new version on the server, the app updates itself and notifies the user with a feedback message.

## Seamless upgrades and attention-requiring upgrades

**Seamless upgrade.** After detecting that a new version is available, the app starts caching all the new resources in the background. Once all resources are cached, the update is triggered on the next navigation event. This can be, for example, during the screen transition. Once the app is fully updated and the destination screen is loaded, the app notifies the user about the update with a feedback message. If the update takes time, the app shows the splash screen before navigating to the destination screen. This is considered a seamless upgrade.

**Attention-requiring upgrade.** An attention-requiring upgrade may happen when the user is on a screen that is modified in the new app version. If the user performs an action that requires interaction with the server, for example, by executing a Server Action, and that action has a different signature, the action fails and a feedback message shows saying that a new version is available and required to proceed. Clicking that message updates the app. After the update, the app loads the updated screen and a feedback message shows with the message that the app is up to date.

When there's a Form widget on the screen, the message about the required update also informs the user that the information they entered in the Form will be lost, because the app needs to reload. The data persisted on Local Storage and Client Variables is not affected.

## Situations when the update is not possible in the device

There may be situations when the automatic update of the app is not possible in the user device, even if there were no issues during the publishing step. Possible causes can be:

* Poor network connection to download the resources needed for the update
* Local data model upgrade that is not possible to update automatically
  
In situations where an update is not possible on the device of the user, the mobile app rolls back to its most recent fully working version. There is also a message saying to the user the update was not possible and that they may need to restart the app to retry the update.

When the error happens while updating the Local Storage data model, possibly because the existing data is incompatible with the new data model, the message informs the user that they may need to reinstall the app if the problem persists. The reinstallation clears the current app data.

The issue and the cause are logged in the environment and you can check them in Service Center. With these logs, you should be able to identify the cause and implement a fix in a new version of the app.

## Situations when the user must install a new build

Even though every time a “1-Click Publish” runs the changes are automatically made available to the app, some changes require from the users to install an updated app package on the device. It happens when:

* the configurations for a mobile platform were changed 
* the Extensibility Configurations property was changed, for instance, modification, addition or removal of mobile plugins, changes to status bar transparency, custom icons or splash screens, and so on 
* an external resource of a plugin was updated
* the app name was changed 
* the entry module or its name was changed 
* the app icon was replaced 
* the main color of the app was changed 

After these changes are published, the experience of the users with outdated apps may suffer some impact. In the case of plugins, it is a good practice to include fallbacks in the apps to avoid crashing until the last version is installed on the device. These potential issues are automatically fixed when the user upgrades to the latest app package.

<div class="warning" markdown="1">

When installing a new version of an Android app already installed on the device and generated using the build type "Debug", uninstall the previous version from the device before installing the new one. This guarantees the new features work correctly.

</div>

After the first mobile app generation, every time you click “1-Click Publish”, OutSystems generates a new app package in the situations listed above. You can then download those app packages via Service Studio, Service Center, and LifeTime. This guarantees that the latest app package available to download from the environment is synchronized with the development of the app.
