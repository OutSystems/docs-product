---
summary: Explore the Firebase Cloud Messaging Plugin functionalities in OutSystems 11 (O11), including client actions, web blocks, and data structures.
tags:
  - Android
  - Blocks
  - Events
  - iOS
  - Mobile app
  - Native App
  - Plugins
locale: en-us
guid: 7d2a4a8a-baba-4456-a353-bf46bcde6b3b
app_type: mobile apps
platform-version: o11
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - service studio
coverage-type:
  - remember
isautopublish: true
---

# Firebase cloud messaging plugin reference

<div class="info" markdown="1">

This reference article applies to Firebase Cloud Messaging Plugin version 4.0.0 and newer. For setup and usage, refer to [Firebase Cloud Messaging Plugin using server actions](firebase-messaging.md).

</div>

## Plugin elements

### Client actions

#### `CheckCloudMessagingPlugin`

Verifies if the Firebase Cloud Messaging Plugin is available or properly installed in the application.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| IsAvailable | Output | Boolean | Indicates if the plugin is available ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### `RegisterDevice`

Registers the device on the Firebase Cloud Messaging service so it can receive push notifications. On first use, it triggers the native notifications permission request.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### `UnregisterDevice`

Removes the device registration from the Firebase Cloud Messaging service, so it stops receiving push notifications.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### `GetToken`

Returns the Firebase Cloud Messaging registration token of the active device. Use this token to target the device when sending notifications.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Token | Output | Text | The device's Firebase Cloud Messaging registration token. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### `GetAPNsToken`

Returns the Apple Push Notification service (APNs) token of the device. Available on iOS only.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Token | Output | Text | The device's APNs token. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### Subscribe

Subscribes the device to a topic. If the topic doesn't exist in the Firebase project, it's created.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Topic | Input | Text | The name of the topic to subscribe to. Topic names can't contain spaces. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### Unsubscribe

Unsubscribes the device from a topic.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Topic | Input | Text | The name of the topic to unsubscribe from. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### SendLocalNotification

Triggers a local notification on the device. On Android, this action is also used to set the app icon badge number.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| NotificationTitle | Input | Text | Sets the title of the local notification. |
| NotificationBody | Input | Text | Sets the body text of the local notification. |
| BadgeNumber | Input | Integer | Sets the badge number based on the provided value. If it's "0", it clears the badge number. Note that, starting on Android 14, most devices do not show the badge number. |
| ChannelName | Input | Text | Sets the channel name for the local notification. Android only. |
| ChannelDescription | Input | Text | Sets the channel description for the local notification. Android only. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### `ClearNotifications`

Clears all the app's notifications remaining in the device's notification center.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### `GetBadgeNumber`

Returns the current app icon badge number. Available on iOS only.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| BadgeNumber | Output | Integer | The current app icon badge number. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### `SetBadgeNumber`

Sets the app icon badge number. Available on iOS only.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| BadgeNumber | Input | Integer | The number to show on the app icon badge. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### `GetPendingNotifications`

Returns the pending silent notifications stored on the device. Silent notifications have no visual or auditory representation but can deliver a data package (extra data) to the app.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| ClearFromDatabase | Input | Boolean | Sets whether the returned silent notifications are cleared from the local database. |
| Notifications | Output | List of [SilentNotification Structure](#silentnotification-data-structure) | The list of pending silent notifications. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### BuildInternalDeepLink

Builds an internal deep link to a screen in the app. Use it to navigate to a screen when the user clicks a notification.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| ScreenName | Input | Text | The name of the destination screen. |
| ParameterList | Input | List of [ExtraDataElement Structure](#extradataelement-data-structure) | The query parameters to include in the deep link, as key-value pairs. |
| DeepLink | Output | Text | The generated deep link. |

#### `DeliveryMetricsExportToBigQueryEnabled`

Determines whether Firebase Cloud Messaging exports message delivery metrics to BigQuery. Available from plugin version 4.3.0.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Enabled | Output | Boolean | Indicates if the export is enabled ('True') or not ('False'). |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### `SetDeliveryMetricsExportToBigQuery`

Enables or disables exporting Firebase Cloud Messaging message delivery metrics to BigQuery. Available from plugin version 4.3.0.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Enable | Input | Boolean | Sets whether to enable ('True') or disable ('False') the export. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

### Web blocks

#### `NotificationsHandler`

Handles the notification experience inside the app. Add this block to each screen that needs to react to notifications. It triggers events that pass the parameters of both notifications and silent notifications.

| Event | Description |
| - | - |
| NotificationClicked | Triggered when the user clicks a notification. |
| InternalRouteActionClicked | Triggered when the user clicks a custom internal-route action on a notification. |
| DefaultNotificationReceived | Triggered when the app receives a notification while in the foreground. |
| SilentNotificationReceived | Triggered when the app receives a silent notification. |

#### `NotificationDialog`

Provides a notification dialog UI inside the app to present a received notification.

### Data structures and Static Entities

#### Platform static entity

Indicates the target platform when sending notifications. Used in the plugin's server actions.

| Value | Description |
| - | - |
| Android | Targets Android devices. |
| iOS | Targets iOS devices. |

#### ExtraDataElement data structure

The data structure for a key-value pair, used for notification extra data.

| Parameter | Data Type | Description |
| - | - | - |
| Key | Text | The key of the pair. |
| Value | Text | The value of the pair. |

#### `SilentNotification` Data structure

The data structure for returning a pending silent notification.

| Parameter | Data Type | Description |
| - | - | - |
| Timestamp | Date Time | The date and time the notification was received. |
| MessageID | Text | The notification's unique identifier. |
| TimeToLive | Date Time | The notification's time to live. |
| ExtraDataList | List of [ExtraDataElement Structure](#extradataelement-data-structure) | The notification's extra data, as key-value pairs. |

## Related resources

* [Firebase plugins](intro.md)
* [Firebase Cloud Messaging Plugin using server actions](firebase-messaging.md)
* [Firebase Cloud Messaging Plugin using configurator APIs](firebase-cloud-messaging-plugin-configurator-api.md)
