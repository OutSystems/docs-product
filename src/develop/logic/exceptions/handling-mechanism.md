---
summary: Learn about exception handling in OutSystems.
tags: support-Application_Troubleshooting; support-webapps
locale: en-us
guid: aa97807f-3db5-4d86-a746-7fe2506481a6
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Exception Handling Mechanism

The exceptions raised in your module are handled in a flow starting with an Exception Handler element. In an action, you can have more than one Exception Handler flow to handle different types of exceptions.

An exception can be raised by OutSystems or in your logic at any point of your module. For typical UI requests, you can handle the raised exceptions by:

* Adding an [Exception Handler](<../../../ref/lang/auto/class-exception-handler.md>) element and its logic in your action's flow.
* Adding an On Exception action in your UI Flows.
* Let the Global Exception Handler of your module do the work. By default, Global Exception Handler property of your module is set to the On Exception action of the "Common" UI Flow.

In action flows starting in Timers you can only handle the raised exceptions by adding Exception Handler elements in your logic, otherwise, the execution flow is interrupted and the error is logged.

When an exception is raised, the current execution flow is interrupted and the flow restarts in the first Exception Handler element which handles that type of exception.

As an example, consider an Action B raising a User Exception named MyUserException. Action B is invoked by Action A, which is a screen action. When MyUserException is raised in Action B, the exception handling mechanism works as follows:

![Workflow used by the platform to determine the exception handling flow to execute](images/handling-mechanism.png)

You should have, at least, one Exception Handler in your application flow to inform and allow the end user to continue to navigate.

<div class="info" markdown="1">

**OnApplicationReady** is a special event handler that is not covered by the Global Exception Handler. For that reason, error handling should be implemented in the action itself.

</div>

## Handling exceptions raised by integrations

When you are handling exceptions raised by an integration you are consuming (such as an action of an Extension or a method of a REST API) you won't be able to determine the type of exception. In these situations, you should handle the exception with an All Exceptions Handler. Then, you can use the **ExceptionMessage** property of the Exception Handler element to identify the exception.

For more information on handling errors in consumed REST APIs, check [Handling REST Errors](../../../extensibility-and-integration/rest/consume-rest-apis/handling-rest-errors.md).
