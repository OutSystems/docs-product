---
tags: runtime-mobileandreactiveweb
summary: Provides methods to access native capabilities of the device.
locale: en-us
guid: cb9a46ef-3b0c-48e2-9307-8fa4d00567e3
app_type: mobile apps, reactive web apps
platform-version: o11
---

# Device

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

Provides methods to access native capabilities of the device.

## Summary

|Functions|Description|
|---|---|
|[whenReady](device.md#whenready)|Promise that is resolved when the 'deviceready' event is caught.|

## Functions

### whenReady

**whenReady(): Promise&lt;void&gt;**

Promise that is resolved when the 'deviceready' event is caught.

You should bind your code on this promise (`whenReady().then(...)`) instead of using the traditional approach of binding the event on `document.addEventListener("deviceready", ...)`. The event fires when Cordova is fully loaded, i.e. it signals that Cordova's device APIs are loaded and are ready for use.

Example:

```javascript
// get device information
if (cordova) {
  $public.Device.whenReady().then(function() {
    $parameters.DeviceModel = device.model;
    $parameters.CordovaVersion = device.cordova;
    $parameters.Platform = device.platform;
    $parameters.UUID = device.uuid;
    $parameters.Version = device.version;
    $parameters.Manufacturer = device.manufacturer;
    $parameters.IsSimulator = device.isVirtual;
    $parameters.SerialNumber = device.serial;
    $resolve();
  });
} else {
  // fallback when testing on desktop browser
  $resolve();
}
```

Returns: Promise&lt;void&gt;

A `Promise` object that is fulfilled when the 'deviceready' event is caught.

