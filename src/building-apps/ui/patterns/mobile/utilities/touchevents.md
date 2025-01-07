---
tags: ui patterns, mobile development, web development, touch interaction, user interface design
summary: Learn how to enable and customize touch events in mobile and reactive web apps using the Touch Events UI Pattern in OutSystems 11 (O11).
locale: en-us
guid: 543a0aea-546e-48ce-92e6-dcc08e9fd2be
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=222:10
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Touch Events

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Touch Events UI Pattern to enable touch events on a specific widget.

![Screenshot of the Touch Events utilities in a mobile or reactive web app interface](images/touch_events_utilities.png "Touch Events Utilities")

## How to create custom patterns using the Touch Events UI Pattern

You can call the **event.preventDefault()** to prevent the default action associated with each event from occurring. The touchstart and touchend events don't need this action, but touchmove requires it to stop screen scrolling when the user is moving the finger inside the element.

![Illustration of how to create custom patterns using the Touch Events UI Pattern](images/touch_events_custom_patterns.png "Custom Touch Events Patterns")

To use the **event.preventDefault()**, use the following string of code:

`$parameters.Evt.preventDefault();`

## How to hide a header during a scroll action

You can use the Touch Events UI pattern to hide a header during a scroll action.

1. Add the **TouchEvents** pattern to the **Layout** block.

    ![Image showing the addition of the TouchEvents pattern to the Layout block](images/touch_events_layour.png "Touch Events Layout")

1. Add an **End** event.

    ![Image depicting the process of adding an End event in the Touch Events pattern](images/add_end_event.png "Adding an End Event")

1. Add logic.

    ![Image showing the logic configuration for the Touch Events pattern](images/touch_events_logic.png "Touch Events Logic")

After following these steps and publishing the module, you can test the pattern in your app.

| Element | Code |
|---|---|
|![JavaScript code snippet to hide a header during a scroll action using Touch Events](images/JS_hide.png "JavaScript Code to Hide Header") |  var header = document.querySelector(".header");<br/>header.classList.add("hide");<br/>header.classList.add("header-on-scroll"); |
|![JavaScript code snippet to show a header during a scroll action using Touch Events](images/JS_show.png "JavaScript Code to Show Header") |  var header = document.querySelector(".header");<br/>header.classList.remove("hide");<br/>header.classList.remove("header-on-scroll"); | 
  
**Result**

<iframe src="https://player.vimeo.com/video/991471309" width="492" height="750" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video demonstrating the end result of using Touch Events to hide a header during scroll.</iframe>

## Properties

|**Property** | **Description** |
|---|---| 
| WidgetId | This is the element that responds to the touch you configure.|

## Compatibility with other patterns

There might be conflicts with any pattern with touch events (unless the code is altered to expect this behavior).

## Samples

The following sample uses the Touch Events pattern:

![Sample image of a mobile or reactive web app using the Touch Events pattern](images/TouchEvents-Sample-1.png "Touch Events Sample")

