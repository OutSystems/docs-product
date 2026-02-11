---
summary: Learn how to integrate contact access in your applications using the Calendar Plugin in OutSystems O11 (O11).
tags: calendar, contacts, plugin installation, error handling
locale: en-us
guid: 1b5a1418-e474-41d8-a233-4f0a80130aa7
app_type: mobile apps
figma: 
audience:
  - mobile developers
  - frontend developers
  - full stack developers
platform-version: o11
coverage-type:
  - none
outsystems-tools:
  - service studio
---

# Calendar plugin

Use the calendar plugin to enable an app to access the calendar of a user's device.

<div class="info" markdown="1">

Refer to [Use mobile plugins](../intro.md#adding-plugins) to learn how to install and reference a plugin in your OutSystems apps.

</div>

## Add necessary permissions (property list keys) for calendar access (iOS only)

To use the calendar plugin on iOS, provide descriptions for the following property list keys: **NSCalendarsUsageDescription** and **NSCalendarsFullAccessUsageDescription**.

Set the iOS permissions in your app's extensibility configurations file, as follows:

(Recommended) Using the universal extensibility configurations schema:

```json
{
  "appConfigurations": {
    "permissions": {
      "ios": {
        "NSCalendarsUsageDescription": "We access your calendar to create or view events.",
        "NSCalendarsFullAccessUsageDescription": "We access your calendar to create or view events."
      }
    }
  }
}
```

Using the Cordova-based extensibility configurations schema (for MABS versions lower than 12):

```json
{
  "preferences": {
    "ios": [
      {
        "name": "NSCalendarsUsageDescription",
        "value": "We access your calendar to create or view events."
      },
      {
        "name": "NSCalendarsFullAccessUsageDescription",
        "value": "We access your calendar to create or view events."
      }
    ]
  }
}
```

If you don't explicitly set these descriptions, default values are used (the same shown in the example).

## Using the plugin

To use the calendar plugin in your app:

1. In **Service Studio**, go to **Logic** > **Client Actions** > **CalendarPlugin**.
1. Drag the desired action to your flow.
1. Set the required input parameters (such as **Title** or **EventID**).
1. Handle the **Success** and **Error** output parameters to ensure the app handles failures gracefully.

<div class="info" markdown="1">

To prevent errors, check if the plugin is available with the action **CheckCalendarPlugin** before calling any other client action.

</div>

### Creating events

You can create events using two actions:

* **CreateEvent**: Creates a basic event.
* **CreateEventWithOptions**: Creates an event with additional options, such as a URL or recurrence (for example, daily, weekly, monthly). Use this for complex events like weekly video conferences.

### Deleting events

You can delete events by title or by ID:

* **DeleteEvent**: Deletes events based on the **Title**, **StartEndTime**, and **EndDateTime**. The **Title** matches events exactly or by prefix (for example, **Team meeting** matches all events starting with that text). The date parameters define the deletion timeframe (for example, set **StartEndTime** to Jan 29 and **EndDateTime** to Jan 31 to delete events on Jan 30).
* **DeleteEventById**: Deletes a specific event using its **EventID**. You can retrieve the ID using **FindEvent**. The **FromDate** parameter sets the start of the timeframe for deletion.

### Finding and viewing events

Use the following actions to find or view calendar items:

* **FindEvent**: Searches for events. It returns a list in the **Events** output parameter.
* **ListCalendars** (Android only): Lists available calendars on the device. You can optionally set **GetAllCalendars** to retrieve all calendars.
* **OpenCalendar**: Opens the device's native calendar app. You can optionally specify the **OnDate** parameter to open the calendar on a specific date.

## Handling errors

Apps with the Calendar plugin run on many Android or iOS devices, with different hardware and configurations. To ensure a good user experience and prevent the app from crashing, handle the errors within the app.

The following actions help you handle errors. Use these actions with **If** nodes to check for errors and control how the app works.

| Variable    | Action                 | Description                                                                    |
| :---------- | :--------------------- | :----------------------------------------------------------------------------- |
| IsAvailable | CheckCalendarPlugin    | True if the Calendar Plugin is available in the app.                           |
| Success     | CreateEvent            | True if creating a calendar event was successful.                              |
| Success     | CreateEventWithOptions | True if creating a calendar event with options was successful.                 |
| Success     | DeleteEvent            | True if deleting a calendar event was successful.                              |
| Success     | DeleteEventById        | True if deleting an event from the calendar was successful.                    |
| Success     | FindEvent              | True if finding a calendar event was successful.                               |
| Success     | ListCalendars          | True if listing calendars was successful.                                      |
| Success     | OpenCalendar           | True if opening the calendar was successful.                                   |

## Actions

The following actions are available in the plugin. For more information, see [Calendar-PhoneGap-Plugin](https://github.com/OutSystems/Calendar-PhoneGap-Plugin/tree/outsystems).

| Action                 | Description                                                                                 |
| :--------------------- | :------------------------------------------------------------------------------------------ |
| CheckCalendarPlugin    | Checks if the Calendar Plugin is available in the app.                                      |
| CreateEvent            | Create an event on the device's calendar.                                                   |
| CreateEventWithOptions | Create an event with additional recurrence, URL and reminder options.                       |
| DeleteEvent            | Deletes matching events within a timeframe.                                                 |
| DeleteEventById        | Delete the event by its ID from a specific date onwards.                                    |
| FindEvent              | Find events on the device's calendar.                                                       |
| ListCalendars          | Find calendars on the device (Android only).                                                |
| OpenCalendar           | Open the calendar app in a specific date.                                                   |

## MABS compatibility

The table shows the compatibility of the Calendar Plugin with the Mobile Apps Builds Service (MABS).

| Plugin version  | Compatible with MABS version | Notes |
| :-------------- | :--------------------------- | :---- |
| 3.1.6 and later | MABS 11.0 and later.         |       |
