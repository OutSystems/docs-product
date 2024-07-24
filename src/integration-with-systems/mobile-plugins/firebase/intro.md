---
summary: OutSystems 11 (O11) supports mobile app development with Firebase plugins for enhanced features like analytics and crash reporting.
locale: en-us
guid: 188c9757-ce29-4f78-9717-4e42226e0a4d
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility-and-Integration?type=design&node-id=1092%3A5184&mode=design&t=VFCa3RHG3vFTaPWn-1
---

# Firebase plugins

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

Firebase is a Google mobile development platform that speeds up the mobile app creation and design processes. You can use the Firebase services in the Mobile app through the following OutSystems Firebase-based plugins:

* [Analytics](https://www.outsystems.com/forge/component-overview/10704/firebase-analytics-plugin)
* [Crash Reporting](https://www.outsystems.com/forge/Component_Overview.aspx?ProjectId=10705)
* [Dynamic Links](https://www.outsystems.com/forge/component-overview/10988/dynamic-links-plugin-firebase)
* [Performance Monitoring](https://www.outsystems.com/forge/Component_Overview.aspx?ProjectId=10706)
* [Firebase Cloud Messaging](https://www.outsystems.com/forge/component-overview/12174/cloud-messaging-plugin-firebase)

<div class="info" markdown="1">

To migrate your app from the unsupported Firebase Mobile plugin, see [Migrating to the supported Firebase-based mobile plugins](https://www.outsystems.com/tk/redirect?g=0999bb9f-af58-4fc6-ba6d-9c411958eedc).

</div>

## Prerequisites

To use the Firebase plugins, you must complete the following prerequisites:

* Set up a Firebase project in the [Google Firebase console](https://console.firebase.google.com/).

* [Add an Android and an iOS app in Firebase](https://support.google.com/firebase/answer/9326094?hl=en) and download the configuration files:

    * **GoogleService-Info.plist** for iOS
    * **google-services.json** for Android

## Demo app

Install [Firebase Mobile Sample App](https://www.outsystems.com/forge/component_overview.aspx?projectid=10707&projectname=firebase-mobile-sample-app) from Forge. Then open the app in the Service Studio. The demo app contains logic for common use cases, which you can examine and recreate in your apps. If you want to build the app and run it, check the prerequisites on the Forge page.

## Adding and using a Firebase plugin

To add a Firebase plugin to your mobile app, complete the following steps:

1. Install the **Firebase** plugin and reference it in your mobile app. For detailed instruction, see [Adding plugins](../intro.md#adding-plugins) for detailed instructions.

1. Add the [Google services configuration files](#adding-google-services-configuration-files) to the mobile app.

    <div class="info" markdown="1">

    You only need to add Google services configuration file for the first Firebase plugin in your mobile app. The next Firebase plugin you add uses the same configuration files.

    </div>

1. In Service Studio, go to **Logic** > **Client Action**, then select your Firebase plugin and use the actions in your logic.

    ![Shows the Logic tab in Service Studio with the Firebase plugin actions.](images/plugin-logic-tab-ss.png "Firebase Plugin Logic Tab in Service Studio")

    <div class="info" markdown="1">

    To learn how to use the Firebase Cloud Messaging plugin, see [Firebase Cloud Messaging Plugin](../firebase/firebase-messaging.md) compatible with O11.

    </div>

## Adding Google services configuration files

You must provide the plugin configuration file as settings in the Service Studio for an app with a Firebase Plugin. To add the Firebase configuration to your app, complete the following steps:

1. In Service Studio, go to the **Data** tab.

1. Right-click the **Resources** folder and select **Import Resource**. The **Import Resource** dialog opens.

    ![Shows importing google-services.json file into the Resources folder in Service Studio](images/resources-folder-ss.png "Importing Resources in Service Studio")

1. Select the **google-services.json** file and confirm the selection. Service Studio adds the file under the **Resources** folder.

    Repeat this step for the **GoogleService-Info.plist** file.

    <div class="info" markdown="1">

    The iOS file extension **.plist** may not be recognised by the Windows IIS Server and can lead to build issues. If this happens, add the file's MIME type to the server's MIME Types list, associating the **application/xml** MIME type with the **.plist** file name extension.

    </div>

1. In the **Deploy Action** list, select **Deploy to Target Directory**. Leave the **Target Directory** field empty.

    ![Shows how to add Firebase configuration files to a mobile app in Service Studio](images/firebase-resources-ss.png "Firebase Configuration Files in Service Studio")


1. In your app's Extensibility Configurations, add the following:

        {
            "resources": {
                "android": {
                    "AndroidResource": {
                        "src": "www/google-services.json",
                        "target": "app/google-services.json"
                    }
                },
                "ios": {
                    "IosResource": {
                        "src": "www/GoogleService-Info.plist",
                        "target": "GoogleService-Info.plist"
                    }
                }
            }
        }

1. (Optional) If you want to use different configurations for each environment, repeat steps 2 to 6 for each environment. For details on pointing the mobile application to the correct configuration files in each environment, see [Override Mobile Extensibility Configurations](../../../deploying-apps/override-extensibility-configurations.md).

    ![Shows the process of adding multiple Firebase configuration files for different environments in Service Studio](images/firebase-multiple-configurations-ss.png "Multiple Firebase Configurations in Service Studio")

### Additional setup for the Dynamic Links plugin

The Firebase Dynamic Links Plugin requires the following additional setup steps to work correctly:

* Include a global preference in the Extensibility Configurations of the application using the plugin. Ensure that the value for this preference matches the URL prefix you set in the Dynamic Links page in the Firebase console. For example:
```JSON
{
     "preferences": {
         "global": [
            {
                "name": "FIREBASE_DOMAIN_URL_PREFIX",
                "value": "outsystemsfirebase.page.link"
            },
        ]
    }
}
```

* For iOS, use a provisioning profile from Apple that contains the Associated Domains capability. For more information, see [Configuring an Associated Domain](https://developer.apple.com/documentation/xcode/configuring-an-associated-domain) by Apple. Ensure that the app is compliant with Apple’s Data Use and Sharing guidelines.

Starting with iOS 14.5, apps on the App Store must request the user’s permission to collect tracking data through the AppTrackingTransparency framework. For more information, see [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency).

![Shows the Firebase request tracking authorization prompt in a mobile application](images/firebase-request-tracking-authorization.png "Firebase Request Tracking Authorization")

To trigger the native AppTrackingTransparency framework, use the **RequestTrackingAuthorization** client action from the Firebase Analytics Plugin. Apple recommends triggering this prompt as soon as the app loads.
If you want to present an alert before the iOS tracking permission dialog, enable the parameter **ShowInformation** on the action. To provide more context to app users in the dialog, set a **Title** and **Message**.

By default, the **NSUserTrackingUsageDescription** field is set to `AppName needs your attention.`. As explained by Apple [here](https://developer.apple.com/documentation/apptrackingtransparency), this property must contain "a message that informs the user why an app is requesting permission to use data for tracking the user or the device.". You can set your custom description by including an iOS-specific preference (`USER_TRACKING_DESCRIPTION_IOS`) in the Extensibility Configurations of the application, as follows:

```JSON
{
    "preferences": {
        "ios": [{
            "name": "USER_TRACKING_DESCRIPTION_IOS",
            "value": "This is an example of a description."
        }]
    }
}
```

You can use the **RequestTrackingAuthorization** action multiple times in the same app because iOS remembers a user's choice and only prompts users again after they uninstall and then reinstall the app on the device.

By default, an app using the Firebase Analytics plugin is able to trigger the native AppTrackingTransparency framework. It also contains the **NSUserTrackingUsageDescription** field in the app's **\*-Info.plist** file. If you don't want to trigger the framework and don't want to include the description field in the **.plist** file, you can disable this through the Extensibility Configurations as follows:

```JSON
{
    "preferences": {
        "ios": [{
            "name": "EnableAppTrackingTransparencyPrompt",
            "value": "false"
        }]
    }
}
```

<div class="info" markdown="1">

If your app collects user data for advertising purposes, also known as Attribution, within Firebase Analytics context, it must prompt the AppTrackingTransparency framework.

</div>

### Additional information for Firebase Analytics

#### Ecommerce events

Starting in version **2.0.1**, Firebase Analytics plugin users can log ecommerce events, which are specifically tailored to collect information about your user's shopping behavior.

It's important to note that Google's ecommerce API enforces a set of constraints for each event. For example, the API ensures you include a `item_list_id` parameter when logging a `view_item_list` event.

The Firebase Analytics plugin performs the validations when `LogECommerceEvent` is invoked. You can find the details of the validations for each event, by following the Google's documentation link, in the list below.

To further illustrate this example, the following shows a typical usage of the `LogECommerceEvent client action`:

![Shows the Firebase Analytics LogECommerceEvent client action for a `view_item_list`](images/firebase-ecommerce-run-client-action-ss.png "Firebase Analytics LogECommerceEvent client action example")

Currently, the Firebase Analytics plugin supports the following events:

* [add_payment_info](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#add_payment_info)
* [add_shipping_info](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#add_shipping_info)
* [add_to_cart](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#add_to_cart)
* [add_to_wishlist](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#add_to_wishlist)
* [begin_checkout](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#begin_checkout)
* [purchase](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#purchase)
* [refund](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#refund)
* [remove_from_cart](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#remove_from_cart)
* [select_item](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#select_item)
* [select_promotion](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#select_promotion)
* [view_cart](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#view_cart)
* [view_item_list](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#view_item_list)
* [view_item](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#view_item)
* [view_promotion](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#view_promotion)

From the provided entity `ECommerceEvent`, users can select the event type.

![Shows the `ECommerceEvent` entity](images/firebase-entity-ecommerce-event-ss.png "Firebase Analytics LogECommerceEvent entity")

Select the key for each parameter to be included on the event logging from the  `ECommerceEventParameterKey` entity.

![Shows the `ECommerceEvent` entity](images/firebase-ecommerce-parameterkey-ss.png "Firebase Analytics LogECommerceEvent entity")

For more information on which event requires which parameters, refer to [Google's documentation page regarding 'measure ecommerce'](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce).

#### Enable/disable data collection

Starting in version **2.1.1**, the Firebase Analytics plugin can effectively enable and disable data collection. For the `SetEnabled` client action to properly work, the following needs to be added to your app's Extensibility Configurations:

```JSON
{
    "preferences": {
        ...
        "global": [
            ...,
            {
                "name": "ANALYTICS_COLLECTION_ENABLED",
                "value": "false"
            },
            ...
        ],
        ...
    }
}
```

<div class="info" markdown="1">

Keep in mind that:

* For `SetEnabled` to have any effect on the data collection, the preference needs to be included.
* The preference only needs to be added when you want to control the collection. If not provided or is used with another value (for example: `true`), the collection will be enabled and it won't be possible to change it.

</div>
