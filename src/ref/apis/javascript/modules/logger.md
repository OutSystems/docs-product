---
tags: runtime-mobileandreactiveweb
summary: Provides methods to log messages or errors. Used as "console.log" but also logs messages in Service Center.
---

# Logger

Provides methods to log messages or errors. Used as "console.log" but also logs messages in Service Center.

This logger will work both as a `console.log` logger and as server logger, sending the log messages to Service Center. When offline, the log messages will be temporarily saved in local storage; when online, they will be sent to Service Center.

## Summary

|Functions|Description|
|---|---|
|[error](logger.md#error)|Logs an error.|
|[log](logger.md#log)|Logs a message.|

## Functions

### error

**error(module: string, messageOrError: string \| Error, [error: Error]): void**

Logs an error.

If both `messageOrError` and `error` arguments are supplied, message information (and stack information, if `messageOrError` is an Error object) will be concatenated using `\n` as separator before being logged.

Example 1:

```javascript
try {
  // do some synchronous operations
} catch(e) {
  $public.Logger.error("MainModule", e);
}
```

Example 2 (error logging in asynchronous code):

```javascript
yourClientAsyncAction().then(function() {
  // do some operations that can throw an error
}).catch(function(err) {
  $public.Logger.error("MainModule", err);
});
```

Parameters:

* **module**: string<br/> Name of a module to log.
* **messageOrError**: string \| Error<br/> Error or message to log.
* (Optional) **error**: Error<br/> Error object.

Returns: void

### log

**log(module: string, message: string): void**

Logs a message.

Parameters:

* **module**: string<br/> Name of a module to log.
* **message**: string<br/> Log message.

Returns: void

