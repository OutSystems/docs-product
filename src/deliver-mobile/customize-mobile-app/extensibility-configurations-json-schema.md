---
summary: JSON Schema and values expected for the Extensibility Configurations property.
tags: runtime-mobile
locale: en-us
guid: 232410a7-d16f-4258-9742-d9b6f294c600
---

# Extensibility Configurations JSON Schema

The **Extensibility Configurations** field provides additional settings as a JSON string. A number of settings you can change in the user interface of the IDE (for example, the name of the app). Some advanced settings are available in the **Extensibility Configurations** only (for example, adding custom mobile plugins). You can edit **Extensibility Configurations** in the properties of your home module.

## Property schema

The value of the **Extensibility Configurations** property of a mobile app module is a JSON object. What follows is the JSON schema outlining the most common options. There may be other options applicable in your use case, if the feature you're using provides them. 

```javascript 
{
    "plugin": {
        // Use only one the following ways to reference a plugin
        "url": "<The url to a public git repository containing your plugin>",
        // or
        "identifier": "<The identifier for your plugin>",
        // or
        "resource": "<The path to the plugin folder inside the resources file ZIP>",
        // If the plugin requires additional settings
        "variables": [
            {
                "name": "<The attribute name for your plugin variable>",
                "value": "<The attribute value for your plugin variable>"
            },
            /* ...more variables, if needed... */
        ]
    },
    "preferences": {
        // Common preferences for iOS and Android, like status bar customization settings
        "global": [
            {
                "name": "<The preference name for your Android/iOS application>",
                "value": "<The preference value for your Android/iOS application>"
            },
            /* ...more global preferences... */
        ],
        // Just for Android
        "android": [
            {
                "name": "<The preference name for your Android application>",
                "value": "<The preference value for your Android application>"
            },
            /* ...more Android preferences... */
        ],
        // Just for iOS
        "ios": [
            {
                "name": "<The preference name for your iOS application>",
                "value": "<The preference value for your iOS application>"
            },
            /* ...more iOS preferences... */
        ]
    },
    "icons": {
        // Just for Android
        "android": [
            {
                "resource": "<The resource path to the icon file for your Android app>",
                "density": "<The density of your Android icon>"
            },
            /* ...(mandatory) entries for all Android icons... */
        ],
        // Just for iOS
        "ios": [
            {
                "resource": "<The resource path to the icon file for your iOS app>",
                "width": "<The icon width for your iOS app>",
                "height": "<The icon height for your iOS app>"
            },
            /* ...(mandatory) entries for all iOS icons... */
        ],
    },
    "splashscreens": {
        // Just for Android
        "android": [
            {
                "resource": "<The resource path to the splash screen file for your Android app>",
                "density": "<The density of your Android splashscreen>"
            },
            /* ...(mandatory) entries for all Android splash screens ...*/
        ],
        // Just for iOS
        "ios": [
            {
                "resource": "<The resource path to the splashscreen file for your iOS app>",
                "width": "<The splashscreen width for your iOS app>",
                "height": "<The splashscreen height for your iOS app>"
            },
            /* ...(mandatory) entries for all iOS splash screens ...*/
        ],
    },
    "resource": "<The name of the ZIP file that contains all the resources you're using>",
    "clientRuntime": {
        // Use the entries below to customize the unhandled errors screen
        "errorPage": {
            "messages": {
                "defaultMessage": "<The message that is displayed to the user when a generic error occurs>",
                "screenNotFound": "<The message displayed when the user navigates to an inexistent screen>",
                "noDefaultScreen": "<The message displayed when no default screen was configured in the application>",
                "appOffline": "<Error message shown when the server is offline>",
                "incompatibleProducer": "<Message shown when the application uses an incompatible producer module>"
            },
            "extraMessage": "<Extra message displayed when any of the errors above occur>",
            "reloadLabel": "<Text displayed by the button used to reload the application>",
            "css": "<CSS rules to be included in the error page>"
        }
    },
    "access": [
        // Use the entries below to define which domains your mobile app can connect to
        {
            "origin": "<Protocol and URL of accessible domain>",
            "minimum-tls-version": "<Minimum required TLS version>",
            "requires-forward-secrecy": "<true if Forward Secrecy is required for this origin>",
            "requires-certificate-transparency": "<true if Certificate Transparency is required for this origin>"
        },
        // use the following template to set these three iOS-only fields
        {
            "origin": "*",
            "allows-arbitrary-loads-for-media": "<true_or_false>",
            "allows-arbitrary-loads-in-web-content": "<true_or_false>",
            "allows-local-networking": "<true_or_false>"
        },
        /* ...more whitelisted domain entries... */
    ]
}
```

## Preferences

The following section provides more details about the options you can use in the `preferences` top-level property. For a comprehensive list of the available settings, see [preferences in Config.xml](https://cordova.apache.org/docs/en/dev/config_ref/index.html#preference) by Apache Cordova. 

| Property                          | Platform | Default | Description |
| --------------------------------- | -------- | ------- | ----------- |
| (iOS_FEATURE)UsageDescription    | iOS        | NA       | Adds preferences that match the pattern of UsageDescription to the Info.plist file. For full list, see [Cocoa Keys](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW1) and filter by UsageDescription. For an example, see information about [iOS usage descriptions](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service/MABS_Version_7.1#iOS_Usage_Descriptions) in the release notes. |
| AddUploadWidgetPermissions      | Android, iOS        | true       | Set as false to skip adding permissions required by the upload widget to AndroidManifest.xml and/or Info.plist. For an example, see information about [Upload widget permissions](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service/MABS_Version_7.1#Upload_Widget_Permissions) in the release notes. |
| EnableRefererHeaderCustomScheme | iOS        | false       | Set to true to inject the `Referer: URL` in the requests of the native app, where `URL` is the app domain.         |
| InitLoggerSyncDelay             | Android        | 0       | Seconds to delay the logger synchronization after the initialization.         |
| RemoveUserCertificates          | Android        | false       | Set to true to remove user certificates from the trust anchors in network_security_config.xml.         |
| FilterTouchesWhenObscured | Android | false | Defines the value of the filterTouchesWhenObscured property of WebView on Android. Set to true to prevent the app from handling touches while obscured by other apps. Learn more about filterTouchesWhenObscured [here](https://developer.android.com/reference/android/view/View#security).|

## Constraints

To ensure the platform can build your app successfully and that your app works correctly, keep in mind the following restraints for the **Extensibility Configurations** JSON.

### Generic

Generic constants, applicable to all parts of the **Extensibility Configurations** JSON.

* The JSON schema and key/value pairs must follow the structure as described in this topic. 
* The first-level key/value pairs are optional and the order isn't relevant. 
* Write the name of each name/value pair using lower case letters, as the JSON is case sensitive. 

### Resources

Constraints related to managing the app resources in the **Extensibility Configurations** JSON.

* You can specify only one resource key in the JSON. All content used in the app must be inside that file (icons, splash screens, and plugins). 
* When specifying the resource file for the app, the resource name must end with ".zip". 
* The resource file name must be equal to the resource name of the file you add. 
* The specified path for an asset (for example, the icon or splash screen) in the JSON must be the same as the path inside the resources ZIP file.

## Additional information

Additional information about the **Extensibility Configurations**.

* For information about **progressive web app (PWA) manifest**, see [Advanced PWA settings and customization](../distribute-pwa/advanced.md).
* You can **override** the JSON from Service Studio with a JSON in LifeTime. See [Override the default mobile Extensibility Configurations](../../managing-the-applications-lifecycle/deploy-applications/override-extensibility-configurations.md) for more information.
* If you're using AppShield to **harden your mobile app** and protect it from tampering, see the [AppShield plugin configuration](../app-shield/intro.md#configuration).
