---
summary: Learn how to integrate contact access in your applications using the Contacts Plugin in OutSystems O11 (O11).
tags: contacts, plugin installation, error handling
locale: en-us
guid: 777b0874-e06c-4ff3-8d62-a973e1866f9f
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

# Contacts plugin

Use the contacts plugin to enable an app to access the contact list of a user's device.

<div class="info" markdown="1">

Refer to [Use mobile plugins](../intro.md#adding-plugins) to learn how to install and reference a plugin in your OutSystems apps.

</div>

## Add necessary permission (property list keys) for contact access (iOS only)

To use the contacts plugin on iOS, provide the description for the property list key: **NSContactsUsageDescription**.

Set the iOS permission in your app's extensibility configurations file, as follows:

(Recommended) Using the universal extensibility configurations schema:

```json
{
  "appConfigurations": {
    "permissions": {
      "ios": {
        "NSContactsUsageDescription": "We access your contacts to create or search them."
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
        "name": "NSContactsUsageDescription",
        "value": "We access your contacts to create or search them."
      }
    ]
  }
}
```

If you don't explicitly set these descriptions, default values are used (the same shown in the example).

## Using the plugin

To use the contacts plugin actions:

1. In **Service Studio**, go to **Logic** > **Client Actions** > **ContactsPlugin**.
1. Drag the desired action to your logic flow.
1. Handle the **Success** output to verify the action completed. If **False**, use the **Error** output to handle the failure.

<div class="info" markdown="1">

To prevent errors, check if the plugin is available with the action **CheckContactsPlugin** before calling any other client action.

</div>

## Add a contact

To add a contact to the device's contact list, use the **AddToContacts** action. Set the **FirstName**, **LastName**, **Phone**, and **Email** input parameters.

## Find a contact

To search for a contact in the device's contact list, use the **FindContact** action:

1. Set the **SearchParameter** (the text to search for) and **MultipleContacts** (to return one or all matches).
1. The matching contacts are returned in the **Contacts** output list.

## Pick a contact

To let the user select a contact using the device's native contact picker, use the **PickContact** action. The selected contact is returned in the **Contact** output parameter.

## Remove a contact

To remove a contact from the device's contact list, use the **RemoveFromContacts** action.

You must provide the **Contact** input parameter. Typically, you first retrieve this contact by calling **FindContact** or **PickContact**.

## Handling errors

Apps with the Contacts Plugin run on many Android or iOS devices, with different hardware and configurations. To ensure a good user experience and prevent the app from crashing, handle the errors within the app.

The following actions help you handle errors. Use these actions with **If** nodes to check for errors and control how the app works.

| Variable    | Action              | Description                                                                    |
| :---------- | :------------------ | :----------------------------------------------------------------------------- |
| IsAvailable | CheckContactsPlugin | True if the Contacts Plugin is available in the app.                           |
| Success     | AddToContacts       | True if adding a contact was successful.                                       |
| Success     | FindContact         | True if finding contacts was successful.                                       |
| Success     | PickContact         | True if picking a contact was successful.                                      |
| Success     | RemoveFromContacts  | True if removing a contact was successful.                                     |

## Actions

The following actions are available in the plugin. For more information, see [cordova-plugin-contacts](https://github.com/OutSystems/cordova-plugin-contacts/tree/outsystems).

| Action              | Description                                                                                 |
| :------------------ | :------------------------------------------------------------------------------------------ |
| CheckContactsPlugin | Checks if the Contacts Plugin is available in the app.                                      |
| AddToContacts       | Use this action to add a contact to the device's address book.                              |
| FindContact         | Use this action to search for a contact from the device's address book.                     |
| PickContact         | Opens the device specific contact picker to pick a contact from the device's address book.  |
| RemoveFromContacts  | Use this action to remove a contact from the device's address book.                         |

## MABS compatibility

The table shows the compatibility of the Contacts Plugin with the Mobile Apps Builds Service (MABS).

| Plugin version  | Compatible with MABS version | Notes |
| :-------------- | :--------------------------- | :---- |
| 4.0.7 and later | MABS 11.0 and later.         |       |
