---
summary: Use watches to examine module elements while debugging threads in your module.
locale: en-us
guid: de70f6a6-f126-4ebd-85f3-b98d0a5d613c
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Watches

Watches allow you to examine module elements in Service Studio while debugging your module. These elements are always displayed in the **Watches** tab, regardless of being in or out of the scope of the element being debugged. This behavior contrasts with the rest of the [scope tabs](<debugger-ui-reference.md#scope-tabs-area>), where the displayed content depends on the current scope.

Using watches, you can inspect the following:

* Parameter values
* Variables
* Screen widgets


## Add a Watch

To watch a module element, follow these steps:

1. Run the module in Debug mode.
1. Right-click the element you want to watch.
1. Select the **Add To Debug Watches** option. 

    ![Add a watch](images/watches-add-ss.png)

All watched module elements are alphabetically listed in the **Watches** tab. 

![Watches tab](images/watches-tab-ss.png)

## Remove a Watch

To remove a watch from a module element, follow these steps:

1. In the **Watches** tab, right-click the watched element you want to remove.
1. Select the **Remove Watch** option.

    ![Remove a watch](images/watches-remove-ss.png)


## Remove All Watches

To remove all watches, follow these steps:

1. Right-click anywhere in the **Watches** tab area.
1. Select the **Remove All Watches** option. 

    ![Remove all watches](images/watches-removeall-ss.png)

Alternatively, you can select the **Remove All Watches** option available in the **Debugger** menu.

