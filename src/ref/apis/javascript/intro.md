---
tags: article-page; runtime-mobileandreactiveweb
---

# JavaScript API

<div class="info" markdown="1">

Applies only to Mobile Apps and Reactive Web Apps

</div>

The OutSystems JavaScript API allows you to call OutSystems specific actions and act upon mobile app events in your JavaScript code, to tweak and customize the mobile app experience of the final user using the [JavaScript flow element](https://success.outsystems.com/Documentation/11/Extensibility_and_Integration/JavaScript). For example, to show and hide feedback messages in JavaScript, or handle application upgrade/load events in a specific way.

The available API modules can be accessed through the predefined object “$public”. This object contains references to each supported JavaScript API.

The following example shows how to call the “showFeedbackMessage” function of the “FeedbackMessage” module:

```javascript
$public.FeedbackMessage.showFeedbackMessage("Your data has been submitted.", 1);
```

## Summary

|Modules|Description|
|---|---|
|[ApplicationLifecycle](modules/applicationlifecycle.md)|Provides information about the status of the application's lifecycle. Used to protect the app during upgrades, when local model access shouldn't be allowed, and to customize the application loading process.|
|[Device](modules/device.md)|Provides methods to access native capabilities of the device.|
|[FeedbackMessage](modules/feedbackmessage.md)|Displays feedback messages to the user. Used to display personalized feedback messages, specifying options like custom style and auto-close behavior.|
|[Logger](modules/logger.md)|Provides methods to log messages or errors. Used as "console.log" but also logs messages in Service Center.|
|[Security](modules/security.md)|Provides methods for doing client side role checks. Used to programmatically show or hide UI elements depending on a given role.|

|Classes|Description|
|---|---|
|[ApplicationContext](classes/applicationcontext.md)|Provides contextual information based on the screen that is being presented. Used to identify the screen, module and application that is currently running.|
|[Navigation](classes/navigation.md)|Provides the ability to perform normal and history navigations, and to override some navigation behaviors (e.g. back). Used to create new transition animations instead of overriding the existing ones using CSS.|
|[Validation](classes/validation.md)|Provides methods to show validation messages on widgets and set their validation values. Used when validating widgets inside iterators, since it's not possible to do it in the usual way.|
|[View](classes/view.md)|Provides methods to deal with active view components and their state.|

|Type aliases|Description|
|---|---|
|[ApplicationLoadEventHandlers](intro.md#applicationloadeventhandlers)|Event handlers called when the status of the application load changes.|


## Type aliases

### ApplicationLoadEventHandlers

**ApplicationLoadEventHandlers: object**

Event handlers called when the status of the application load changes.

Used in [ApplicationLifecycle.listen](modules/applicationlifecycle.md#listen) function.

#### Type declaration

(Optional)  **onLoadComplete**: function

Callback for when the application is fully loaded and ready to use.

`(): void`

Returns: void

(Optional)  **onUpgradeProgress**: function

Callback for when there is progress, during a version upgrade.

`(loaded: number, total: number): void`

Parameters:

* **loaded**: number
* **total**: number

Returns: void

