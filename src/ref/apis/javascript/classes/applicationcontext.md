---
tags: runtime-mobileandreactiveweb
summary: Provides contextual information based on the screen that is being presented. Used to identify the screen, module and application that is currently running.
locale: en-us
guid: 1441aa35-5b4b-44f1-81de-52be529e2583
app_type: mobile apps, reactive web apps
---

# ApplicationContext

<div class="info" markdown="1">

Applies only to Mobile Apps and Reactive Web Apps

</div>

Provides contextual information based on the screen that is being presented. Used to identify the screen, module and application that is currently running.

## Hierarchy

**ApplicationContext**

## Summary

|Methods|Description|
|---|---|
|[getCurrentContext](applicationcontext.md#getcurrentcontext)|Gets the current context based on the screen being presented.|

## Methods

### &lt;Static&gt; getCurrentContext

**getCurrentContext(): object**

Gets the current context based on the screen being presented.

Example:

```javascript
var context = $public.ApplicationContext.getCurrentContext();

// Example of the returned object:
// {
//     "applicationKey": "7926523f-0206-4f9e-8203-c8f009c12f2a",
//     "applicationName": "EmployeeApp",
//     "moduleKey": "7f38d717-c625-4d00-9e04-5e5e3eca65e5",
//     "moduleName": "EmployeeMainModule",
//     "screenKey": "9584046a-827a-4035-aedc-23dfe4bf10b5",
//     "screenName": "MainFlow.HomeScreen"
// }
```

Returns: object

Returns an object with the following attributes: `applicationKey`, `applicationName`, `moduleKey`, `moduleName`, `screenKey`, `screenName`.

