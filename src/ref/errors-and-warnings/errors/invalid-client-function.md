---
summary: Explore common errors in OutSystems 11 (O11) related to invalid client functions and their resolutions.
locale: en-us
guid: ca17ad44-8f4c-4e6f-8744-8fb87aff9244
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, client actions, synchronous programming, asynchronous javascript, outsystems development
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
isautopublish: true
---

# Invalid Client Function

The `Invalid Client Function` error is issued in the following situations:

* `'<Server Action>' cannot be used in '<Client Action>' because server actions are not available in client functions. Change the 'Function' property of the action '<Client Action>' to 'No'.`
  
    Client Actions marked as functions must be synchronous and cannot execute Server Actions.

    Change the Function property of the Client Action to `No` or avoid executing the Server Action.

* `'<Local Storage Aggregate>' cannot be used in '<Client Action>' because local storage is not available in client functions. Change the 'Function' property of the action '<Client Action>' to 'No'.`
  
    Client Actions marked as functions must be synchronous and cannot execute Local Storage Aggregates.
  
    Change the Function property of the Client Action to `No` or avoid executing the Aggregate.

* `'<JavaScript Node>' cannot be used in '<Client Action>' because the execution of an asynchronous JavaScript node is not available in client functions. Change the 'Function' property of the action '<Client Action>' to 'No'.`
  
    Client Actions marked as functions must be synchronous and cannot execute JavaScript nodes that include the function `$resolve()`.
  
    Change the Function property of the Client Action to `No` or avoid executing the asynchronous JavaScript node.

* `'<Client Action>' action cannot be used in the '<Client Action>' action. Only actions that are functions can be used in other functions. Change the 'Function' property of the '<Client Action>' action to 'Yes' or the 'Function' property of the '<Client Action>' action to 'No'.`

* `'<Client Action>' action cannot be used in the '<Client Action>' action. Only actions that are functions can be used in other functions. Change the 'Function' property of the '<Client Action>' action to 'No'.`

    In OutSystems 11, only actions marked as functions can be used inside other functions or in the Expression Editor. Some System Client Actions aren't defined as functions. For example, `ListIndexOf` isn't marked with `Is Function?` set to `Yes`, while actions like `ListDistinct` and `ListDuplicate` are.

    If the called action is a user-defined action, change its **Function** property to `Yes`. If the called action is a System action or you need to call non-function actions, change the calling action's **Function** property to `No`.

Double-click on the error line to take you directly to the source of the error.
