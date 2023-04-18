---
summary: Use watches to examine module elements while debugging threads in your module.
locale: en-us
guid: de70f6a6-f126-4ebd-85f3-b98d0a5d613c
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Watches

Watches allow you to examine module elements in Service Studio while debugging your module. These elements are always displayed in the Watches Tab, regardless of being in or out of scope of the element being debugged. This behavior contrasts with the rest of the [scope tabs](<debugger-ui-reference.md#scope-tabs-area>), where the displayed content depends on the current scope.

Using watches you can inspect:

* Parameter values
* Variables
* Screen widgets


## Add a Watch

To watch a module element do the following:

1. Run the module in Debug mode.
1. Right-click the element to watch, either in the Scope tabs or in the module tree.
1. Select the "Add To Debug Watches" option in the pop-up menu. 

All watched module elements are alphabetically listed in the Watches Tab. 


## Remove a Watch

To remove a watch from a module element do the following:

1. Right-click on the watched element in the Watches Tab.
1. Select the option "Remove Watch" in the pop-up menu.


## Remove All Watches

To remove all watches do the following:

1. Right-click anywhere on the Watches Tab area.
1. Select the "Remove All Watches" option in the pop-up menu. 

Alternatively, select the "Remove All Watches" option available in the Debugger menu.

