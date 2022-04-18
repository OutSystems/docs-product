---
summary: Learn more about threads in OutSystems.
locale: en-us
guid: 6ed6cc03-b8a8-4bc7-b3b6-e5a7e7fc2e01
app_type: traditional web apps, mobile apps, reactive web apps
---

# Threads

In OutSystems a **thread** may result from the following:

* A server action requested to the Platform Server.
* A client action triggered by the user in a mobile app, or an event triggered in a mobile app (e.g. OnReady event of a screen).
* An awakened Timer action.
* A Process instance execution.
* An integration method (belonging to a SOAP web service or a REST service) exposed by a module. 

The execution of a thread follows its designed action flow, e.g. an action to be executed when a button is pressed or a Web Service method (Web Service method call).

You can suspend thread execution in your module where you want to examine module elements and runtime values by using [breakpoints](<breakpoints.md>).

The debugger behaves differently when suspending the execution flow at breakpoints, depending on the kind of thread:

* **Threads from client/server actions or mobile app events**: these threads are originated by some action taken by the user on a screen in a web or a mobile app, or from events triggered in a mobile app (e.g. OnReady, OnInitialize). These threads are isolated and suspended at the breakpoints you set; the same happens for all other users in their machines.

* **Other types of threads**: threads like the ones executing Process flows, Timer actions, or integration methods are suspended from execution whenever they run into a breakpoint of a debug session started in the Public Area, either yours or of any other user because they're not isolated. In this case, you might be debugging not only your threads, but also threads from other users and vice-versa. To overcome this situation, you should check in the Users Tab if there are other users debugging the module. If that is the case, each suspended thread should have its module elements and runtime values examined by you (in the [scope tabs](<debugger-ui-reference.md#scope-tabs-area>)) to check if the suspended thread is yours.

<div class="info" markdown="1"> 

In **mobile apps** there can only be one client-side thread being executed due to the [event loop](<https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop>) concurrency model of JavaScript. However, when the execution point is suspended in an action executed in the server (e.g. a server action or a data action), another client-side event might occur, e.g. an OnAfterFetch event of an aggregate. 

In this case, the Threads Tab inside the [Debugger Tab](<debugger-ui-reference.md#debugging-context-area>) will display an additional thread. If a breakpoint is set in the event handler action and this breakpoint is hit, Service Studio will display that action flow in the canvas.

</div>


## Abort an Executing Server Thread

While debugging a server thread (corresponding to an action being performed in the server) you may abort its execution, terminating it.

Use the ![](images/toolbar-button-abort.png) Abort Running Server Threads button available on the Debugger Toolbar or in the Debugger Menu.


## Suspend All Executing Server Threads

If you feel that one or more server threads are taking longer than expected and something might be wrong, you can suspend their execution.

Select the ![](images/toolbar-button-suspend.png) Suspend Running Server Threads option in the Debugger menu. An entry is created for each one of them in the Threads Tab. 

When suspended, Service Studio will focus the element that was being executed by the server thread when the thread was suspended.

<div class="info" markdown="1">

This option may not work instantaneously if what is currently being executed is not controlled by the platform, such as a Web Service method invocation or a database query. In the latter situation, the query must finish before the server thread is effectively suspended.

</div>

