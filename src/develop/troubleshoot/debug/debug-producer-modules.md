---
summary: Check how to debug functionality exposed by a producer Module being consumed in a different module.
tags:
---

# Debugging Producer Modules


When you are debugging a producer Module the debugger will not stop in any breakpoints set in the consumer Module unless you also start a debug session in the consumer Module.

<div class="info" markdown="1">

See [this article](https://success.outsystems.com/Documentation/11/Developing_an_Application/Reuse_and_Refactor/Expose_and_reuse_functionality_between_modules) for more information about consumer and producer modules in OutSystems.

</div>

The procedure for debugging producer Modules differs depending on the type of exposed Actions: 

## Public Client Actions or public Server Actions

### Pre-Requisites { #pre-requisites }

Your consumer Module must fulfill the following conditions:

* It must be a consumer of a Client or Server Action from the producer Module by referencing it.
* The reference to the producer Module is up-to-date.
* You have permissions to publish the consumer Module.

### How to debug the producer Module

To debug the functionality being exposed in a public Action by the producer Module, follow these steps:

1. Open the **producer Module** and set the entry Module for debugging to be the consumer Module. You can set the entry Module in the Debugger pane or in the Debugger menu, by choosing the "Select Entry Module..." option.

    *Note:* If the desired consumer is not in the list, check the [pre-requisites](<#pre-requisites>) listed above.

1. Place breakpoints where you want the execution to stop. The execution will only stop on breakpoints of the producer Module.

1. Start the debugger in the producer Module. If the producer Module is part of a mobile app, the **consumer Module** will automatically be opened; if it's part of an application, you can open the **consumer Module** in a browser.

1. Interact with the application to execute the functionality that calls the producer logic where the breakpoints are set.

## Service Actions { #service-actions }

Unlike public Server Actions, Service Actions run in the context of the producer Module; to debug a Service Action, follow these steps:

1. Open the **producer Module** and set the Entry Module to `(this module)`. 

    You can set the entry Module in the Debugger pane or in the Debugger menu, by choosing the "Select Entry Module..." option.

1. Place breakpoints where you want the execution to stop. The execution will only stop on breakpoints of the producer Module.

1. Start the debugger on the producer Module.

*Note:* Stepping into a service action from a consumer module is not supported.