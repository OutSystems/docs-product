---
summary: Explore the deprecated and updated features of OutSystems 11 (O11) Cloud Messaging Configurator APIs for enhanced notification management.
locale: en-us
guid: 612389e2-3fb0-455c-8506-eebc7627615b
app_type: mobile apps
platform-version: o11
figma:
tags: api, deprecated features, notification management, outsystems platform, firebase cloud messaging
audience:
  - mobile developers
  - backend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Cloud Messaging Configurator APIs

<div class="info" markdown="1">

The Cloud Messaging Configurator, version 1.1.0 and older, is deprecated. For more information, see [Firebase Cloud Messaging HTTP protocol](https://firebase.google.com/docs/cloud-messaging/http-server-ref). This means the **v2** and **v1** endpoints will no longer be functional.

To provide a better OutSystems experience, the Configurator's REST APIs have been replaced by Server Actions available on the Firebase Cloud Messaging Plugin. If you are consuming these APIs, you should start the migration process as soon as possible.

</div>

Use OutSystems' Cloud Messaging Configurator REST APIs to do the following:

* Send notifications (normal or silent) to all users associated with a topic or group of topics.

* Send a notification (normal or silent) to a user or group of users.

Following are the versions of the Cloud Messaging Configurator REST API in OutSystem:

* [v1 endpoint](#v1)

* [v2 endpoint](#v2)

## v1

Following are the v1 versions of the Cloud Messaging Configurator REST API:

* [SendNotificationToTopics](#sendnotificationtotopics)

* [SendNotificationToUsers](#sendnotificationtousers)

* [SendSilentNotificationToTopics](#sendsilentnotificationtotopics)

* [SendSilentNotificationToUsers](#sendsilentnotificationtousers)

### SendNotificationToTopics

Version: v1

Purpose: Sends a notification to all users associated with a topic or group of topics.

Operation: `POST`

Base URL: `/CloudMessagingConfigurator/rest/v1/notification/topics`

**Request parameters**

|Parameter| Data Type | Description |
|:--------|:----------|:------------|
| FCMServerKey | Text | Identifies the Firebase Cloud Messaging (FCM) Server Key. To send out a notification to users or user groups, you must enter a text value to authorize a connection to FCM. You can find this value in the Firebase Project Settings under the Cloud Messaging tab. |
| SendToTopics | SendToTopicsV1 Data Structure | Identifies the topics that will receive the notification. |
| Notification | NotificationV1 Data Structure | Identifies the notification parameters. |
| ExtraDataList | ExtraDataItem List | Identifies the extra data for the notification. |
| ShowIfAppOpen | Boolean | Identifies if the push notifications are shown as in-app messages and the app must be open when the device receives the notification ('True'), or not open ('False'). |

**Response**

|Parameter| Data Type | Description |
|:--------|:----------|:------------|
| Message_id | Text | Displays the ID of an error, if applicable. |
| Error | Text | Displays error information, or null if successful. |

Following is an example of a request.

```
{
    "SendToTopics": {
       "Condition": "'Sports' in topics || 'Games' in topics"
    },
    "FCMServerKey": "AAAABBBBCCCCDDDD",
    "Notification": {
        "Title": "Notification to Sample Apps",
        "Body": "Notification to Games and Sports",
        "Image": "https://img-08.stickers.cloud/packs/7dd850be-bf96-4be9-ab60-92abdf31c4fe/webp/eb89452e-6463-47f8-8a3c-87fb8a93300d.webp"
        
    },
    "ShowIfAppOpen": true,
    "ExtraDataList": [
        {
            "Key": "Key1",
            "Value": "Value1"
        },
        {
            "Key": "Key2",
            "Value": "Value2"
        }
    ]
}
```

### SendNotificationToUsers

Version: v1

Purpose: Sends a notification to users or group of users.

Operation: `POST`

Base URL: `/CloudMessagingConfigurator/rest/v1/notification/users`

**Request parameters**

|Parameter| Data Type | Description |
|:--------|:----------|:------------|
| FCMServerKey | Text | Identifies the Firebase Cloud Messaging (FCM) Server Key. To send out a notification to users or user groups, you must enter a text value to authorize a connection to FCM. You can find this value in the Firebase Project Settings under the Cloud Messaging tab. |
| SendToPlatform | Text | Identifies the platform that will receive the notification. |
| SendToUsers | Text List | Identifies a list of users that will receive notifications. If empty, the notification is sent to all platform users. |
| SenderID | Text | Identifies the Sender ID. You can find this ID in the Firebase Project Settings under the Cloud Messaging tab. |
| Notification | NotificationV1 Data Structure | Identifies the notification parameters. |
| ExtraDataList | ExtraDataItem List | Identifies the extra data for the notification. |
| ShowIfAppOpen | Boolean | Identifies if the push notifications are shown as in-app messages and the app must be open when the device receives the notification ('True'), or not open ('False').|

**Response**

|Parameter| Data Type | Description |
|:--------|:----------|:------------|
| MulticastID | Text | Returns the Multicast ID. |
| NoSuccess | Text | Returns the number of notifications successfully sent. |
| NoError | Text | Returns the number of notifications not sent due to an error. |
| ResultList | TokenResult List | Displays the ResultList. |

Following is an example of a request.

```
{
    "SendToUsers": [ "{{ValidToken}}"],
    "FCMServerKey": "{{ServerKey}}",
    "Notification": {
        "Title": "Notification to one user",
        "Body": "Automatically sent from API Tests.",
        "Image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaYEDLX5fpwM9F1YS8RO8CKPq04nDmQS9gVA&usqp=CAU"
    },
    "ExtraDataList": [
        {
            "Key": "Key1",
            "Value": "Value1"
        },
        {
            "Key": "Key2",
            "Value": "Value2"
        }
    ]
}
```

### SendSilentNotificationToTopics

Version: v1

Purpose: Sends a silent notification to all users associated with a topic or group of topics.

Operation: `POST`

Base URL: `/CloudMessagingConfigurator/rest/v1/notification/silent/topics`

**Request parameters**

|Parameter| Data Type | Description |
|:--------|:----------|:------------|
| FCMServerKey | Text | Identifies the Firebase Cloud Messaging (FCM) Server Key. To send out a notification to users or user groups, you must enter a text value to authorize a connection to FCM. You can find this value in the Firebase Project Settings under the Cloud Messaging tab. |
| SendToTopics | SendToTopicsV1 Data Structure | Identifies the topics that will receive the notification. |
| ExtraDataList | ExtraDataItem List | Identifies the extra data for the notification. |
| TimeToLive | TimeToLive Data Structure | Identifies the expiration time to deliver the notification. If TimeValue for a specific TimeUnit is different than 0, the message persists and is delivered at the first opportunity until the expiration time is reached. |

**Response**

|Parameter| Data Type | Description |
|:--------|:----------|:------------|
| Message_id | Text | Displays the ID of an error, if applicable. |
| Error | Text | Displays error information, or null if successful. |

Following is an example of a request.

```
{
    "SendToTopics": {
        "TopicList": ["Games"]
    },
     "FCMServerKey": "{{serverKey}}",
     "TimeToLive": {
        "TimeUnit": "Hours",
        "TimeValue": 1
    },
    "ExtraDataList": [
        {
            "Key": "Key1",
            "Value": "Value1"
        },
        {
            "Key": "Key2",
            "Value": "Value2"
        }
    ]
}

```

### SendSilentNotificationToUsers

Version: v1

Purpose: Sends a silent notification to users or group of users.

Operation: `POST`

Base URL: `/CloudMessagingConfigurator/rest/v1/notification/users`

**Request parameters**

|Parameter| Data Type | Description |
|:--------|:----------|:------------|
| FCMServerKey | Text | Identifies the Firebase Cloud Messaging (FCM) Server Key. To send out a notification to users or user groups, you must enter a text value to authorize a connection to FCM. You can find this value in the Firebase Project Settings under the Cloud Messaging tab. |
| SendToUsers | Text List | Identifies a list of users that will receive notifications. If empty, the notification is sent to all platform users. |
| SendToPlatform | Platform Identifier | Identifies the platform that will receive the notification. |
| SenderID | Text | Identifies the Sender ID. You can find this ID in the Firebase Project Settings under the Cloud Messaging tab. |
| ExtraDataList | ExtraDataItem List | Identifies the extra data of the notification. |
| TimeToLive | TimeToLive Data Structure | Identifies the expiration time to deliver the notification. If TimeValue for a specific TimeUnit is different than 0, the message persists and is delivered at the first opportunity until the expiration time is reached. |

**Response**

|Parameter| Data Type | Description |
|:--------|:----------|:------------|
| MulticastID | Text | Returns the Multicast ID. |
| NoSuccess | Text | Returns the number of notifications successfully sent. |
| NoError | Text | Returns the number of notifications not sent due to an error. |
| ResultList | TokenResult List | Displays the ResultList. |

Following is an example of a request.

```
{
   "SendToUsers": ["{{ValidToken}}"],
   "FCMServerKey": "{{ServerKey}}",
    "TimeToLive": {
        "TimeUnit": "Days",
        "TimeValue": 2
    },
    "ExtraDataList": [
        {
            "Key": "Key1",
            "Value": "Value1"
        },
        {
            "Key": "Key2",
            "Value": "Value2"
        }
    ]
}
```


## v2

Following are the v2 versions of the Cloud Messaging Configurator REST API:

* [SendNotificationToTopics](#sendnotificationtotopics-1)

* [SendNotificationToUsers](#sendnotificationtousers-1)

### SendNotificationToTopics

Version: v2

Purpose: Sends a notification to all users associated with a topic or group of topics.

Operation: `POST`

Base URL: `/CloudMessagingConfigurator/rest/v2/notification/topics`

**Request parameters**

|Parameter| Data Type | Description |
|:--------|:----------|:------------|
| FCMServerKey | Text | Identifies the Firebase Cloud Messaging (FCM) Server Key. To send out a notification to users or user groups, you must enter a text value to authorize a connection to FCM. You can find this value in the Firebase Project Settings under the Cloud Messaging tab. |
| SendToTopics | SendToTopicsV2 Data Structure | Identifies the topics that will receive the notification. |
| Notification | NotificationV2 Data Structure | Identifies the notification parameters. |
| ExtraDataList | ExtraDataItem List | Identifies the extra data for the notification. |
| ShowIfAppOpen | Boolean | Identifies if the push notifications are shown as in-app messages and the app must be open when the device receives the notification ('True'), or not open ('False').|

**Response**

|Parameter| Data Type | Description |
|:--------|:----------|:------------|
| Message_id | Text | Displays the ID of an error, if applicable. |
| Error | Text | Displays error information, or null if successful. |

Following is an example of a request.

```
{
    "SendToTopics": {
       "Condition": "'Sports' in topics || 'Games' in topics"
    },
    "FCMServerKey": "{{serverKey}}",
    "Notification": {
        "Title": "Notification to Sample Apps",
        "Body": "Notification to Games and Sports",
        "Image": "https://img-08.stickers.cloud/packs/7dd850be-bf96-4be9-ab60-92abdf31c4fe/webp/eb89452e-6463-47f8-8a3c-87fb8a93300d.webp",
        "Sound": "la-cucaracha.wav"
        "ActionList": [
            {
                "Identifier": "IDOne",
                "Label": "Click me!",
                "Type": "standard",
                "Event": "internalRoute",
                "TextField": {
                    "Placeholder": "Hello!",
                    "InputTextKey": "inputKey",
                    "InputFeedback": "Sent!"
                }
                "RouteData": {
                    "DeepLinkScheme": "DeepLinkScreen",
                    "ParameterData": [
                        {
                            "Key": "oneDeepLinkParameter",
                            "Value": "A value"
                        },
                        {
                            "Key": "anotherDeepLinkParameter",
                            "Value": "Another Value"
                        }
                    ]
                }
            },
            {
                "Identifier": "IDTwo",
                "Label": "Web Route",
                "Type": "standard",
                "Event": "webRoute",
                "RouteData": {
                    "DeepLinkScheme": "https",
                    "Identifier": "google.com/search",
                    "ParameterData": [
                        {
                            "Key": "q",
                            "Value": "Outsystems"
                        }
                    ]
                }
            },
            {
                "Identifier": "UmID",
                "Label": "Take me to facebook",
                "Type": "standard",
                "Event": "appRoute",
                "RouteData": {
                    "DeepLinkScheme": "fb",
                    "Identifier": "friends",
                    "FallbackUrl": {
                        "iOS": "https://apps.apple.com/us/app/facebook/id284882215",
                        "Android": "https://play.google.com/store/apps/details?id=com.facebook.katana"
                    }
                }
            }
        ]
    },
    "ShowIfAppOpen": true,
    "ExtraDataList": [
        {
            "Key": "Key1",
            "Value": "Value1"
        },
        {
            "Key": "Key2",
            "Value": "Value2"
        }
    ]
}
```

### SendNotificationToUsers

Version: v2

Purpose: Sends a notification to users or group of users.

Operation: `POST`

Base URL: `/CloudMessagingConfigurator/rest/v2/notification/users`

**Request parameters**

|Parameter| Data Type | Description |
|:--------|:----------|:------------|
| FCMServerKey | Text | Identifies the Firebase Cloud Messaging (FCM) Server Key. To send out a notification to users or user groups, you must enter a text value to authorize a connection to FCM. You can find this value in the Firebase Project Settings under the Cloud Messaging tab. |
| SendToPlatform | Text | Identifies the platform that will receive the notification. |
| SendToUsers | Text List | Identifies a list of users that will receive notifications. If empty, the notification is sent to all platform users. |
| SenderID | Text | Identifies the Sender ID. You can find this ID in the Firebase Project Settings under the Cloud Messaging tab. |
| Notification | NotificationV2 Data Structure | Identifies the notification parameters. |
| ExtraDataList | ExtraDataItem List | Identifies the extra data for the notification. |
| ShowIfAppOpen | Boolean | Identifies if the push notifications are shown as in-app messages and the app must be open when the device receives the notification ('True'), or not open ('False').|

**Response**

|Parameter| Data Type | Description |
|:--------|:----------|:------------|
| MulticastID | Text | Returns the Multicast ID. |
| NoSuccess | Text | Returns the number of notifications successfully sent. |
| NoError | Text | Returns the number of notifications not sent due to an error. |
| ResultList | TokenResult List | Displays the ResultList. |

Following is an example of a request.

```
{
    "SendToUsers": ["{{ValidToken}}"],
    "FCMServerKey":  {{ServerKey}},
    "Notification": {
        "Title": "Notification to Sample Apps",
        "Body": "Notification to Games and Sports",
        "Image": "https://img-08.stickers.cloud/packs/7dd850be-bf96-4be9-ab60-92abdf31c4fe/webp/eb89452e-6463-47f8-8a3c-87fb8a93300d.webp",
        "Sound": "la-cucaracha.wav"
        "ActionList": [
            {
                "Identifier": "IDOne",
                "Label": "Click me!",
                "Type": "standard",
                "Event": "internalRoute",
                "TextField": {
                    "Placeholder": "Hello!",
                    "InputTextKey": "inputKey",
                    "InputFeedback": "Sent!"
                }
                "RouteData": {
                    "DeepLinkScheme": "DeepLinkScreen",
                    "ParameterData": [
                        {
                            "Key": "oneDeepLinkParameter",
                            "Value": "A value"
                        },
                        {
                            "Key": "anotherDeepLinkParameter",
                            "Value": "Another Value"
                        }
                    ]
                }
            },
            {
                "Identifier": "IDTwo",
                "Label": "Web Route",
                "Type": "standard",
                "Event": "webRoute",
                "RouteData": {
                    "DeepLinkScheme": "https",
                    "Identifier": "google.com/search",
                    "ParameterData": [
                        {
                            "Key": "q",
                            "Value": "Outsystems"
                        }
                    ]
                }
            },
            {
                "Identifier": "UmID",
                "Label": "Take me to Facebook",
                "Type": "standard",
                "Event": "appRoute",
                "RouteData": {
                    "DeepLinkScheme": "fb",
                    "Identifier": "friends",
                    "FallbackUrl": {
                        "iOS": "https://apps.apple.com/us/app/facebook/id284882215",
                        "Android": "https://play.google.com/store/apps/details?id=com.facebook.katana"
                    }
                }
            }
        ]
    },
    "ShowIfAppOpen": true,
    "ExtraDataList": [
        {
            "Key": "Key1",
            "Value": "Value1"
        },
        {
            "Key": "Key2",
            "Value": "Value2"
        }
    ]
}
```
