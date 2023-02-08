---
summary: Customize how deeplinks are handled in your mobile app.
tags: runtime-mobile
locale: en-us
guid: 411e538e-743c-4e9f-a78b-1a4c8fdf3932
app_type: mobile apps
platform-version: o11
---

# Customize Deeplink Behavior

<div class="info" markdown="1">

Applies only to Mobile Apps built with MABS 9 or newer.

</div>

Prior to MABS 9, all deeplinks that were handled by a mobile app caused a reload of the page. In MABS 9 this behavior was changed, and deeplinks trigger a screen navigation instead.

## Customizing the behavior

This behavior can be changed by using the `DeepLinksHandlerType` preference in the [extensibility configurations](./extensibility-configurations-json-schema.md). The preference can have 4 different values:
* `default`: performs a screen navigation to the URL *(the default behavior)*
* `event`: fires an event to the `OSDeepLinksHandlerChannel` *(does not navigate)*
* `function`: calls the `handleOpenURL` function *(does not navigate)*
* `legacy`: loads the URL in the webview directly, which performs a page reload *(the behavior from MABS 8 and earlier)*

In order to use the `event` and `function` options, the specific handler must be defined in a script that's loaded by the app module.

Example for `event`:
```
var channel = cordova.require("cordova/channel");
if (channel) {
    channel.OSDeepLinksHandlerChannel.subscribe(function (url) {
        ...
    });
}
```

Example for `function`:
```
window.handleOpenURL = function (url) {
    ...
}
```

## Distribution

To make this change available for the users, [publish and generate a new mobile application](<../generate-distribute-mobile-app/intro.md>) and distribute it.
