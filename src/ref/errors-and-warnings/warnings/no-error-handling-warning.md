---
summary: Check the causes and recomendations on how to solve the different No Error Handling TrueChange warnings.
tags:
locale: en-us
guid: 1515b96c-fb4b-463c-836b-976a822b00fa
app_type: traditional web apps, mobile apps, reactive web apps
---

# No Error Handling Warning

## Errors are not being handled in the web flow. Add error handlers or select a theme with error handling

**Cause**

The web flow does not have error handlers, and the Theme does not have a web flow for error handling.

**Recommended action**

Change the web flow to implement [error handlers](../../../ref/lang/auto/Class.Exception%20Handler.final.md), or change the [error handling](../../../develop/logic/exceptions/handling-mechanism.md) Flow property of the [Theme](../../../develop/ui/look-feel/themes.md) to use a web flow that already implements error handling.
