---
summary: Learn more about implementing and reuse actions, iterating lists, and handling exceptions. Find more about the lifecycle of screens and blocks.
tags:
---

# Implement Application Logic

In OutSystems, the logic of your applications is implemented through **Actions**. While developing your applications, you can create your own custom actions and use the actions OutSystems provides you:

* **OutSystems built-in actions:** Actions that are defined by the platform and cannot be modified or inspected. You can use them in your action flows, such as Entity Actions, System Actions, or Role Actions.

* **Custom actions:** The actions that you create to define your business rules, fetch data from the database, run integrations with external systems, among other operations.

* **Actions that handle System Events:** Actions that run at specific moments of the application life cycle, such as when a web session starts or a mobile app resumes. You are able to design the flow of these actions according to your business rules.

## Actions in Reactive Web and Mobile apps

In Reactive Web and Mobile apps some of the logic may run on the server and some logic may run on the client — the user's device.

When developing the logic of your Reactive Web and Mobile apps you must take into account that every time your client side logic needs to execute server side logic, the user's device will make a request to the server and wait for the server response. This communication requires that the user's device is online (connected to the internet).

