---
summary: Use the Firebase-based plugins Analytics, Crashlytics, and Performance to implement common development patterns in your mobile apps. 
tags: article-page; runtime-mobile; support-application_development; support-Mobile_Apps; support-Mobile_Apps-featured
---

# Firebase Plugins

Firebase is a Google mobile development platform. It speeds up development many of the common development patterns for mobile apps. You can use Firebase in the OutSystems mobile through the following Firebase-based plugins:

* [Analytics Plugin](https://www.outsystems.com/forge/component-overview/10704/firebase-analytics-plugin)
* [Crash Reporting](https://www.outsystems.com/forge/Component_Overview.aspx?ProjectId=10705)
* [Performance Monitoring](https://www.outsystems.com/forge/Component_Overview.aspx?ProjectId=10706)

## Prerequisites

To use the Firebase plugins you meet the following requirements:

* You set up a Firebase project in the [Google Firebase console](https://console.firebase.google.com/).
  
* You [added an Android and an iOS app in Firebase](https://support.google.com/firebase/answer/9326094?hl=en) and downloaded the configuration files:

    * **GoogleService-Info.plist** for iOS
    * **google-services.json** for Android

## Adding and using a Firebase plugin

To add a Firebase plugin to your module, follow these steps:

1. Install the plugin and reference it in your module. See [Adding plugins](../intro.md#adding-plugins) for detailed instructions.

2. Add the [Google services configuration file](#adding-google-services-configuration-file) to the module.

    <div class="info" markdown="1">

    You need to add Google services configuration file only for the first Firebase plugin in your module. The next Firebase plugin you add uses the same configuration files. 

    </div>

3. In Service Studio, go to **Logic** > **Client Action** > **your Firebase plugin** and use the actions in your logic.

    ![Firebase actions in the logic tab of Service Studio](images/plugin-logic-tab-ss.png?width=350)

## Adding Google services configuration file

An app with a Firebase Plugin requires the plugin configuration files in the app file resources. Follow the steps to add the Firebase configuration to your module:

1. In Service Studio, go to the **Data** tab.

2. Right-click the **Resources** folder and select **Import Resource**. The **Import Resource** dialog opens.

3. Select the [google-services.zip Firebase configuration file](#preparing-firebase-configuration-file) and confirm the selection. Service Studio adds the file under the **Resources** folder.

    ![Resources folder in Service Studio](images/resources-folder-ss.png?width=350)

4. Select the **google-services.zip** resource and configure the following:
   
    * In the **Deploy Action** list, select **Deploy to Target Directory**.
    * In the Target Directory, enter the [target directory for your environment](#generating-target-directories-for-configuration-files).

    ![Resource settings for Firebase](images/firebase-resource-properties-single-ss.png?width=350)

5. Repeat steps two and four for each environment, each time using a different configuration and [target directory](#generating-target-directories-for-configuration-files).

    ![Resource settings for Firebase](images/firebase-resource-properties-multiple-ss.png?width=350)

### Preparing Firebase configuration file

Add the files **GoogleService-Info.plist** and **google-services.json** in a zip file and name the zip file **google-services.zip**. 

![Configuration files in a zip archive](images/zipped-configs.png?width=500)

### Generating target directories for configuration files

A Firebase Plugin requires that you supply configuration files in the app file resources. The mobile apps commonly have different identifiers in different environments, so you need to generate target directories for each environment.

To get the target directory, concatenate the **app identifier** and **.firebase**. Here are examples for three environments with different app identifiers.

| Environment | App identifier | Target directory |
| - | - | - |
| DEV | com.sample.dev.MyApp | `com.sample.dev.MyApp.firebase` |
| QA | com.sample.qa.MyApp | `com.sample.qa.MyApp.firebase` |
| PROD | com.sample.prod.MyApp | `com.sample.prod.MyApp.firebase` |

Use the target directory value in the **Target Directory** property of the **Resource**.
