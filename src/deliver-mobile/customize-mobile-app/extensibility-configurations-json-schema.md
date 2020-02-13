---
summary: JSON Schema and values expected for the Extensibility Configurations property.
tags: runtime-mobile
---

# Extensibility Configurations JSON Schema

The value of the Extensibility Configurations property of a mobile app module is a JSON schema. In order that the mobile app package is correctly generated and there are no unexpected behaviours in runtime, the defined JSON schema must follow a set of constraints.

## Constraints

1. The JSON schema and key/value pairs must follow the official structure described in this topic. 
1. The first-level key/value pairs are optional and the order isn't relevant. 
1. The developer must write the name of each name/value pair using lower case letters (the JSON is case sensitive). 
1. Must only be specified one resource key in the JSON. All content used in the app (icons, splashscreens, and plugins) must be inside that file. 
1. When specifying the resource file for the app, the resource name must end with ".zip". 
1. The resource file name must be equal to the resource name of the file submitted by the developer. 
1. The specified path for an asset (e.g. the icon or splash screen) in the JSON must be the same as the path inside the resources ZIP file. 

In case some constraint is not respected, OutSystems might not be able to generate the mobile app package or the application behavior could be unstable.

## Property Schema

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
