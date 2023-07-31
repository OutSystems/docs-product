---
summary: Disable "Registered Role Required" error logs.
locale: en-us
guid: 7679b3a4-2a80-4ddf-9e85-e470c8af8428
app_type: mobile apps, reactive web apps
platform-version: o11
---

# Disable "Registered Role Required" error logs

It is common to find the error "Registered Role Required" in the platform logs. This error occurs in Reactive and Mobile apps and is related with the asyncronous nature of these types of apps. Sometimes, OutSystems developers consider these messages not relevant and prefer to disable them. This article gives a brief context about these error messages and how to disable them.

## Context

On Reactive and Mobile apps, the session expires if it is idle for more than the time defined in [Max. Idle Time](https://success.outsystems.com/documentation/11/managing_the_applications_lifecycle/secure_the_applications/configure_app_authentication/) (20 minutes by default). The client-side (browser) can only validate the session by contacting the server. This means that the next time the user interacts with the app and it generates one or more server requests (through the execution of Server Actions, Service Actions, Data Actions, or Aggregates), the server will validate if the session is still valid or not. When processing the request, the server will detect that the session is no longer valid and will reject it throwing and logging a "Registered role required" exception (NotRegistered Exception). As a result, the server will invalidate the session by invalidating the session cookies.

The app logic is usually prepared to receive a NotRegistered Exception (or Security Exception) on an exception handler in order to redirect the user to a login or invalid permissions screen. These handlers might have the option Log Error set to "Yes", which will log a second error on the Error Logs.

However, these apps might have a large number of actions that are executed asynchronously. For example, if a screen contains more than 5 Data Actions and the screen is refreshed, each of these requests will generate 2 errors in the logs. This might lead to some log pollution.

## How to disable the errors

When you enable user feedback for an app, by default all users can submit feedback. If you want to restrict the feedback to a specific group of users, select the name of the group in the drop-down list next to the feedback switch.

![User group selection for app feedback](images/app-feedback-enable-3.png?width=800)

If the group of users for which you want to enable feedback doesn't exist, do the following:

1. Select **Create a New Group** in the drop-down list next to the feedback switch. The browser opens a new tab with the Users application.
1. Go to the **Groups** section and create the new group of users you want to get feedback from.
1. Go back to the App Feedback configuration screen, refresh the page, and select the newly created group.
