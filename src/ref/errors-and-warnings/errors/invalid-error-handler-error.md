---
summary: Learn how to resolve common `Invalid Error Handler` errors in OutSystems 11 (O11) by managing exception flows and screen parameters.
locale: en-us
guid: c2ae03b0-1005-4a66-a5c6-72b8387e779c
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, security best practices, application development, access control, user experience
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Error Handler Error

The `Invalid Error Handler` error is issued in the following situations:

* `More than one error handler for <exception> exception in flow`
  
    You are catching the same exception in more than one Error Handler in your flow.

    Remove Error Handlers are catching the exception in duplicate.

* `'Destination' screen of 'Security' error handler must have 'Anonymous' role set in <flow>`
  
    You have an error handler to catch security exceptions that navigates to a screen that does not allow Anonymous users. The exception flow of an error handler that catches Security or Not Registered exceptions must start with an Anonymous screen, otherwise it won't be possible to execute the exception flow.

    Depending on your application requirements, you have to do one of the following: 
    
    * Change the destination of your security error handler to an Anonymous screen.
    * Change the role of the screen.

* `<exception> error handler cannot be connected to a screen with mandatory parameter(s) in <flow>`
  
    You have an Error Handler linked to a Screen with mandatory parameters. This is not allowed because when the exception occurs it won't be possible to send values to these parameters.

    Depending on your application requirements, you have to do one of the following:
    
    * Change the Is Mandatory property of the screen input parameter.
    * Change the destination of the error handler to a different screen with optional parameters.

* `'Exception' must be set`

    You have an error handler that is not catching any exceptions.

    Edit the error handler and set a value in the Exception property.

Double-click on the error line to take you directly to the error handler.
