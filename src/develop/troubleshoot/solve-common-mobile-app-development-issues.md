---
summary: Check how to solve some issues you might find while developing your mobile app.
tags: runtime-mobile; support-application_development; support-Application_Troubleshooting; support-Application_Troubleshooting-overview; support-Mobile_Apps; support-Mobile_Apps-overview
---

# Solve Common Mobile App Development Issues

While developing mobile apps you might need some help troubleshooting a problem in your app. Check below for some common issues that you may encounter, as well as their possible solutions.

We also recommend that you watch the "[Mobile Apps in Trouble](https://www.outsystems.com/learn/lesson/1197/mobile-apps-in-trouble/)" webinar, if you haven't done so. It addresses some of the common problems presented in this topic and the steps taken to overcome them.

## Common Issues

### Element Flicker

#### Observed Behavior

A given screen element changes its contents or style very rapidly and in a
repeated way, causing a bad user experience.

![screen-flicker.gif](images/screen-flicker.gif)

#### Possible Causes

A "flickering element" effect can have different causes, namely the following two:

Rapid screen state changes
:   When data being fetched is associated with a given widget displayed on the screen or with some logic condition that affects a widget's visibility/styling, rapid changes in the data (like going from a non-empty list to an empty one and vice-versa) might cause a flickering effect. 

Dynamic or delayed CSS styling
:   Doing calculations after the screen is rendered that affect the style of a widget.   
    Also, screen-specific CSS might be taking some time to load and cause flickering when some of the screen-level CSS is applied to screen elements.  

#### Possible Solutions

If data changes are causing the flickering:

* Analyze and review conditional logic used in the screen and its components.
* Analyze the timing of aggregates and data actions in runtime (e.g. when will the resulting data be available and its consequences on the implemented logic).
* Use buffer data (i.e. keep the previous state while determining the new one) during the transitions to keep the transition smooth. 

For style-related flickering:

* Avoid showing elements before style calculations are done. 
* Show a placeholder for the element, like a spinner. 
* Consider defining part of your CSS in the theme and not in the screen — this will keep it loaded during transitions. 
* When defining CSS at the theme level, use selectors to target a given screen — this will prevent your overrides from affecting other screens. 

### Slow Transition between Screens

#### Observed Behavior

The transition between two given screens takes too long.  

#### Possible Cause

This behavior can have the following cause:

Slow operations being done in On Initialize screen event handler
:   Slow operations like calling native plugin actions or invoking server actions are being done in the On Initialize event handler of the destination screen. Since this event occurs before the screen DOM is loaded, this might have an impact on the screen load time.   

#### Possible Solutions

* Do not perform slow operations in the On Initialize screen event handler. Move these operations to another event handler like On Ready, which occurs after the page is displayed. This might have an impact on the behavior of your application, so test your app thoroughly before deploying your changes. 

* If the above suggestion does not help in your case, use the [Performance tab](<advanced-mobile-app-troubleshooting-using-chrome.md#performance-tab>) in Chrome's Developer Tools for doing additional performance troubleshooting. 

### Missing Data in Device

#### Observed Behavior

A mobile app screen is not displaying data that should present in the device.  

#### Possible Causes

Synchronization issues
:   The offline synchronization process in your application has errors, and not all the necessary data is being copied to the device.  
    The filtering rules used to determine which data should be copied to the device are not well defined, and necessary data are not being copied in the synchronization process.  
    Your synchronization process implementation is synchronizing too much data at once and the whole process eventually times out and aborts after some time.  

Aggregates are not well defined
:   The data are synchronizing correctly, but an aggregate that is querying local storage entities is configured in such a way that is filtering out necessary data.   

#### Possible Solutions

* Ensure that the missing data is present in the server database. If it is, the error can be in the implementation of the synchronization process between the server and the device.

* Ensure that the missing data is in the local storage contents in your device. For example, create a screen in your app that allows you to browse data of a local storage entity on your mobile device.

* If your data is **present** in the device's local storage, review your application queries, namely your aggregate definitions. Pay special attention to any JOINs and their "Only With"/"With or Without" setting.

* If your data is **not present** in the device's local storage, review your data synchronization implementation to find any errors in filters (e.g. by User ID or by date range) that you might be using in the synchronization process.
