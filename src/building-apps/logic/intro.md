---
summary: Learn more about implementing and reuse actions, iterating lists, and handling exceptions. Find more about the lifecycle of screens and blocks.
tags:
locale: en-us
guid: 1eef31a3-6807-412e-98e1-0e3b93fc6050
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Application Logic

In OutSystems, the logic of your applications is implemented through **Actions**. While developing your applications, you can create your own custom actions and use the actions OutSystems provides you:

* **OutSystems built-in actions:** Actions that are defined by the platform and cannot be modified or inspected. You can use them in your action flows, such as Entity Actions, System Actions, or Role Actions.

* **Custom actions:** The actions that you create to define your business rules, fetch data from the database, run integrations with external systems, among other operations.

* **Actions that handle System Events:** Actions that run at specific moments of the application life cycle, such as when a web session starts or a mobile app resumes. You are able to design the flow of these actions according to your business rules.

## Actions in Reactive Web and Mobile apps

The architecture of Reactive Web and Mobile apps is different from the architecture of Tradtional Web and Service apps and this affects the type of actions available and in which context the logic runs. While in Traditional Web and Service apps all the logic runs on the server, in Reactive Web and Mobile apps some of the logic may run on the server and some logic may run on the client — the user's device.

When developing the logic of your Reactive Web and Mobile apps you must take into account that every time your client side logic needs to execute server side logic, the user's device will make a request to the server and wait for the server response. This communication requires that the user's device is online (connected to the internet).

