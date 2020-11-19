---
summary: Use the Exception Handler element to catch an exception and to start a logic flow for handling that exception.
---

The Exception Handler element starts an action flow for handling all exceptions or exceptions of a certain type. You can define logic to handle exceptions pre-defined exceptions (like Database Exceptions), or custom exceptions (called User Exceptions) raised by your application logic.

Set the Exception Handler's **Exception** property to the exception type you want to handle in the flow of the Exception Handler. To handle all types of exceptions, set the **Exception** property to `All Exceptions`.

For example, the following flow handles the **Not Registered** exception:

![Exception Handler example](images/exception-handler-example-ss.png)

<div class="info" markdown="1">

There's a hierarchy of exception types in OutSystems. If you define an Exception Handler that handles a "parent" exception type, this Exception Handler can also handle any "children" exception type. Check [Handle Exceptions](../../../develop/logic/exceptions/intro.md) for more information.

</div>

In the exception-handling flow started by an Exception Handler element you can perform tasks like displaying a feedback message, logging exception details, and even raising a different type of exception.

Check [Exception Handling Mechanism](../../../develop/logic/exceptions/handling-mechanism.md) to learn more about the chain of Exception Handlers that the platform searches for when an exception occurs.

## Logging exceptions { #logging }

If you set the **Log Error** property to **Yes**, the platform creates a log for the exception type configured in the **Exception** property, when such an exception occurs. You can check for logged exceptions in Service Center under **Monitoring** > **Errors**.

## Aborting database transactions { #aborting }

When you handle an exception in an [action running on server side](../../../develop/logic/actions.md), you can choose what happens to the database transaction by setting the **Abort Transaction** property of the Exception Handler:

* Set the **Abort Transaction** property to **Yes** if you want that all the database transactions that weren't committed are aborted and changes rolled back in the database.

* Set the **Abort Transaction** property to **No** if you want that the database transaction to continue as if no exception had occurred. This transaction is committed by the next [CommitTransaction](../../data/database/handling-transactions.md) Server Action or implicitly by OutSystems, typically at the end of request execution.

<div class="info" markdown="1">

In Reactive Web and Mobile apps, the **Abort Transaction** property isn't available when you are handling exceptions in client side.

</div>
