---
summary: Learn how to set the preferences for your mobile application.
tags: runtime-mobile
locale: en-us
guid: 36e4b86b-db80-4a29-9c79-86cc1c4f7f66
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/RizSdkiVSDYFb97Vqvc7oj/Delivering%20Mobile%20Apps?node-id=307:214
---

# Set the Preferences for Your Mobile App

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

You may want your mobile application to have some configurations and preferences that allow you to better guarantee behavior requirements and improve the user experience. For example, define mobile app preferences when the app should only work in a specific orientation (portrait or landscape), or when it should only be available on devices holding, at least, a specific minimum mobile platform version to ensure a great experience to your users.

To specify the preferences for your mobile app:

1. Select the application module, go to its properties and open the Extensibility Configurations property. 

    ![Screenshot of the Extensibility Configurations property in a mobile application module](images/extensibility-configurations-ss.png "Extensibility Configurations Property")

2. In the Extensibility Configurations value window, you must create a JSON object (if not created) where you can specify the preferences. Add the “preferences” tag to the JSON to indicate that you will set preferences for the app.

    ![Screenshot showing the JSON editor within Extensibility Configurations for setting mobile app preferences](images/extensibility-preferences-ss.png "Extensibility Configurations JSON Editor")

3. Introduce the preferences you want from the [available preferences](https://cordova.apache.org/docs/en/latest/config_ref/#preference) in the JSON value: 

    1. Each preference you want to define is represented as a name/value pair, where the name is the preference name and the value is its parameter specified as a string (enclosed in double quotes), a boolean, or a number. The preference name is case-sensitive. Check the [preferences JSON template](#preferences-json-template) to avoid mistakes. 

        ![Screenshot of global preferences specified in JSON format for a mobile app](images/extensibility-preferences-global-ss.png "Global Preferences JSON Example")

    2. You can set a preference to work only for a target mobile platform or apply it to all. Be aware that some [preferences may not work on every mobile platform](https://cordova.apache.org/docs/en/latest/config_ref/#preference). 

        ![Screenshot illustrating how to set platform-specific preferences in JSON for Android and iOS](images/extensibility-preferences-global-android-ios-ss.png "Platform-Specific Preferences JSON Example")

4. To make this change available for the users, [publish and generate a new mobile application](<../generate-distribute-mobile-app/intro.md>) and distribute it. 

    ![Screenshot of the process to publish and generate a new version of a mobile application](images/generate-mobile-app-ss.png "Publish and Generate Mobile App")

## Preferences JSON Template { #preferences-json-template }

```javascript    
{
    "preferences": {
        "global": [{
            "name": "<preference_name>",
            "value": "<preference_value>"
        }],
        "android": [{
            "name": "<preference_name>",
            "value": "<preference_value>"
        }],
        "ios": [{
            "name": "<preference_name>",
            "value": "<preference_value>"
        }]
    }
}
```
