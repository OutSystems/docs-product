---
tags: runtime-mobileandreactiveweb
summary: Provides information about the status of the application's lifecycle. Used to protect the app during upgrades, when local model access shouldn't be allowed, and to customize the application loading process.
---

# ApplicationLifecycle

Provides information about the status of the application's lifecycle. Used to protect the app during upgrades, when local model access shouldn't be allowed, and to customize the application loading process.

Example:

```javascript
// Check if the app is currently being upgraded
var isUpgrading = $public.ApplicationLifecycle.isUpgradingVersion();

var progressCallback = function(loaded, total) {
  // do something on upgrade progress
};

var loadCompleteCallback = function() {
  // do something on finish
};

$public.ApplicationLifecycle.listen({
  onUpgradeProgress: isUpgrading ? progressCallback : null,
  onLoadComplete: loadCompleteCallback
});
```

## Summary

<table markdown="1">
<thead>
<tr>
<th colspan="2">Functions</th>
</tr>
</thead>
<tbody>
<tr>
<td>[isUpgradingVersion](applicationlifecycle.md#isupgradingversion)</td>
<td>
Returns <code>true</code> if the application version is currently being upgraded.
Used to determine the kind of feedback to provide when the application is initialized (e.g. splash screen).
</td>
</tr>
<tr>
<td>[listen](applicationlifecycle.md#listen)</td>
<td>
Registers listeners for application load events.
</td>
</tr>
</tbody>
</table>

## Functions

### isUpgradingVersion

**isUpgradingVersion(): boolean**

Returns `true` if the application version is currently being upgraded. Used to determine the kind of feedback to provide when the application is initialized (e.g. splash screen).

Returns: boolean

### listen

**listen(eventHandlers: [ApplicationLoadEventHandlers](../README.md#applicationloadeventhandlers)): void**

Registers listeners for application load events.

Parameters:

* **eventHandlers**: [ApplicationLoadEventHandlers](../README.md#applicationloadeventhandlers)<br/> Object containing callbacks for the application loading events you want to listen to.

Returns: void

