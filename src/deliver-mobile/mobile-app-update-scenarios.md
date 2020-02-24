---
summary: Understand how automatic updates to mobile apps work when you click on "1-Click Publish".
tags: runtime-mobile; support-application_development; support-Mobile_Apps
---

# Mobile App Update Scenarios

When developing a mobile app, after you click on “1-Click Publish” the new developments and changes made to the app automatically become available to the end users with no need to install a new application version. The mobile apps running on the end user devices automatically detect these updates when they establish a connection to the server of the updated environment. Only mobile application packages generated from an environment receive the new developments and changes published in that same environment.

## Situations When the Update Is Not Possible in the Device

There may be situations when the automatic update of the application is not possible in the end user device even if the publish happened without problems. Possible causes can be a poor network connection to download the resources needed from the last publish or a local data model upgrade that is not possible to update automatically. In situations where an update is not possible on the device of an end user, the mobile app notifies the end user with a message and rolls back to its previous fully working version.

The issue and the causes will be logged on the environment and the developer can check them on the Service Center of the environment. With these logs, the developer will be able to identify the cause and implement a fix in a new version of the application.

## Situations When the User Must Install a New Build

Even though every time a “1-Click Publish” runs the changes are automatically made available to the application, some changes require the end users to install an updated application package on the device. It happens when:

* the configurations for a mobile platform were changed 
* the Extensibility Configurations property was changed, for instance, modification, addition or removal of mobile plugins, changes to status bar transparency, custom icons or splashscreens, and so on 
* an external resource of a plugin was updated
* the application name was changed 
* the entry module or its name was changed 
* the application icon was replaced 
* the main color of the application was changed 

After these changes are published, the experience of the end users with outdated applications may suffer some impact. In the case of plugins, it is a good practice to include fallbacks in the apps to avoid crashing until the last version is installed on the device. These potential issues are automatically fixed when the end user upgrades to the latest application package.

<div class="warning" markdown="1">

When installing a new version of an Android app already installed on the device and generated using the build type "Debug", uninstall the previous version from the device before installing the new one. This guarantees the new features will be working correctly.

</div>

After the first mobile app generation, every time you click “1-Click Publish”, OutSystems will generate a new application package in the situations listed above. You can then download those application packages via Service Studio, Service Center and LifeTime. This guarantees that the latest application package available to download from the environment is synchronized with the development of the application.
