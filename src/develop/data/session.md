---
summary: Learn how OutSystems uses Sessions to maintain information about the previous web requests the end user made.
tags: runtime-traditionalweb; support-application_development
locale: en-us
guid: a6784b12-4617-437f-b5e5-ec8c8b579006
---

# Sessions in Web Applications

OutSystems web applications are stateless: each request an end user makes to the server is not aware of the previous requests.

To overcome the limitations of these stateless requests, OutSystems uses several mechanisms that allow the server to maintain information about the previous requests the end user made. One of the mechanisms are **Sessions**.

In OutSystems, a **Session** is created in the first request the end user makes to the Platform Server and allows to keep context during the end user interactions with the server. The session consists in the set of session variables defined in the modules the end user accesses during its interaction. The session variables can be used when you are implementing the business logic of your module, for example, in user-actions, screen preparations, and screen actions.

The session is created on the server and can be shared by several modules if you are using the Single Sign-On feature that enables an unified view of users and sessions by a set of modules.


## OutSystems Session Lifecycle

Sessions are automatically managed by OutSystems and depend on the channel used for the user interaction, as described below.

Web Session
:   The session starts during the first request the end user establishes with the server. The session ends explicitly when the end user logs-out, or automatically due to a time-out caused by the user not making requests to the server for a certain amount of time.

Web Services Session
:   The session is created when the Web Service is invoked and lasts only for this request, which means that there is no persistency of the session between requests.

Timer Session
:   The session is created when the Timer is invoked and lasts only for this request, which means that there is no persistency of the session between Timer executions.


## Session Start

When the end user makes the first request to the server, a new session is created. When this happens the **OnSessionStart** event is fired, and the action that handles it is executed.


## Session Timeout { #session-timeout }

The session timeout specifies the period of time that a session can remain idle, without any end user interaction, before the Platform Server ends the session automatically.

The default value for the session timeout is 20 minutes and this value can be configured in `machine.config` file.

<div class="info" markdown="1">

For PaaS infrastructures use [Factory Configuration](https://www.outsystems.com/forums/discussion/34866/factory-configuration-how-to-change-the-session-timeout-in-factory-configuratio/) to configure the session timeout.

</div>

## Sessions in Consumer and Producer Scenario

When using actions from a referenced module, a session is created with all the producer module session variables. This ensures that the referenced actions can maintain the session variables state between invocations.


## Session Variables

Session variables hold data that is persisted during the session and can be used to save information during the end user interaction. Each application has several session variables automatically created, but you can define new ones.

The session variables are initiated automatically by Service Studio when the Platform Server session is created. While the session exists, you can use these variables in your business logic. When the session ends, the session variables are set to their default value.


## Session Variables in Asynchronous Logic

Asynchronous logic such as sending Emails, Timers execution, Processes execution, and Web Services run on a different session, meaning that all session variables are set with their default value when the logic is executed.

## Pre-defined Session Variables

The following session variables are automatically created by OutSystems. They are read-only and you can use them in the logic of your application.

Username
:   Contains the user name of the end user making the request. This variable is instantiated during the login operation, whether you are using an explicit or implicit login. At logout, this session variable is assigned an empty text value.

TerminalType
:   Indicates the type of terminal that is being used to make the request. The possible values are: Web or SMS. These values are instantiated when the session starts.


## User-defined Session Variables

You can define your own session variables in the Session Variables folder of the Data tab.

Session variables should be used with care since they can affect the scalability of your applications. You should try to avoid storing large quantities of data with session variables because, in each request, these variables need to be fetched from the database and then, when the request ends, updated in the database. When Service Studio detects you are compromising the application's performance and scalability, a warning message is displayed.

When the end user logs in or out, using the **Login**, **LoginPassword**, or **Logout** actions, the user-defined session variables are set to their default value.
