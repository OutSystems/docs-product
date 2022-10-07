---
summary: Breakpoints are used to suspend the execution of your application while troubleshooting and debugging issues.
locale: en-us
guid: 9f051835-5900-4113-aedd-9ac7a5b4d4fa
app_type: traditional web apps, mobile apps, reactive web apps
---

# Breakpoints

A **breakpoint** in Service Studio marks an element where the execution of a [thread](<threads.md>) is going to be suspended for debugging. 

Breakpoints can be added to all of the following elements (except for Comment elements):

* Elements of a process flow
* Elements of a screen or block flow (in Traditional Web applications only)
* Elements of an action flow

It's not possible to set a breakpoint in a given line inside a JavaScript element, only in the element itself.

The execution is also suspended on exceptions when the option "Break On All Exceptions" is set, even when no breakpoints are defined in the module. When an exception occurs, the execution will be stopped at the element that raised the exception. If an Exception Handler is defined, the execution will stop before the handler is executed.

While it is a common practice to add breakpoints before running a module, you may add or remove breakpoints anytime during a debug session.

Breakpoints are stored in your user settings. They will be available in Service Studio, even between restarts, as long as you keep working in the same computer.


## Add or Remove a Breakpoint

To add or remove a breakpoint in an element:

1. Right-click on that element (either in the canvas or in the module tree).
1. Select the "Add Breakpoint" or "Remove Breakpoint" option in the pop-up menu. 

Or:

1. Click on that element to select it and press `F8`. This shortcut toggles between add/remove breakpoint. 

The element where the breakpoint was set will show a small red circle.

You can remove all breakpoints at once by selecting the "Remove All Breakpoints" option in the Debugger menu or in the context menu displayed by right-clicking anywhere in the Breakpoints Tab area.


## Disable a Breakpoint

To temporarily disable a breakpoint without removing it, do the following:

1. Right-click on that element (either in the canvas or in the module tree).
1. Select the "Disable Breakpoint" option in the pop-up menu. 

Or:

1. Click on that element to select it and press `Ctrl+F8`. This shortcut toggles between enable/disable breakpoint. 

The element where the breakpoint was disabled will show a hollowed red circle.

Follow the same procedure to re-enable a breakpoint, selecting the "Enable Breakpoint" option.

You can also disable all breakpoints at once by selecting the "Disable All Breakpoints" option in the Debugger menu or in the context menu displayed by right-clicking anywhere in the Breakpoints Tab area.
