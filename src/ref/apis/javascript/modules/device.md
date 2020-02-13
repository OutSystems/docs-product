---
tags: runtime-mobileandreactiveweb
summary: Provides methods to access native capabilities of the device.
---

# Device

Provides methods to access native capabilities of the device.

## Summary

<table markdown="1">
<thead>
<tr>
<th colspan="2">Functions</th>
</tr>
</thead>
<tbody>
<tr>
<td>[whenReady](device.md#whenready)</td>
<td>
Promise that is resolved when the 'deviceready' event is caught.
</td>
</tr>
</tbody>
</table>

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

