---
locale: en-us
guid: ca17ad44-8f4c-4e6f-8744-8fb87aff9244
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
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

Double-click on the error line to take you directly to the source of the error.
