---
summary: Explore debugging features in OutSystems 11 (O11) that allow for monitoring module elements via the Watches tab in Service Studio.
locale: en-us
guid: de70f6a6-f126-4ebd-85f3-b98d0a5d613c
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=4036:29260
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

    ![Screenshot showing how to add a watch to a module element in Service Studio](images/watches-add-ss.png "Adding a Watch in Service Studio")

All watched module elements are alphabetically listed in the **Watches** tab. 

![Screenshot of the Watches tab in Service Studio displaying a list of watched module elements](images/watches-tab-ss.png "Watches Tab in Service Studio")

## Remove a Watch

To remove a watch from a module element, follow these steps:

1. In the **Watches** tab, right-click the watched element you want to remove.
1. Select the **Remove Watch** option.

    ![Screenshot illustrating the removal of a watch from a module element in Service Studio](images/watches-remove-ss.png "Removing a Watch in Service Studio")


## Remove All Watches

To remove all watches, follow these steps:

1. Right-click anywhere in the **Watches** tab area.
1. Select the **Remove All Watches** option. 

    ![Screenshot showing the option to remove all watches at once in Service Studio](images/watches-removeall-ss.png "Removing All Watches in Service Studio")

Alternatively, you can select the **Remove All Watches** option available in the **Debugger** menu.

