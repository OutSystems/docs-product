---
tags: runtime-mobileandreactiveweb;  
summary: The Touch Events UI Pattern enables touch events on a specific widget.
---

# Touch Events 

You can use the Touch Events UI Pattern to enable touch events on a specific widget.

![](images/touch_events_utilities.png)

## How to create custom patterns using the Touch Events UI Pattern

You can call the **event.preventDefault()** to prevent the default action associated with each event from occurring. The touchstart and touchend events don't need this action, but touchmove requires it to stop screen scrolling when the user is moving the finger inside the element.

![](images/touch_events_custom_patterns.png)

To use the **event.preventDefault()**, use the following string of code:

`$parameters.Evt.preventDefault();`

## How to hide a header during a scroll action

You can use the Touch Events UI pattern to hide a header during a scroll action.

1. Add the **TouchEvents** pattern to the **Layout** block.

    ![](images/touch_events_layour.png)

1. Add an **End** event.

    ![](images/add_end_event.png)

1. Add logic.

    ![](images/touch_events_logic.png)

After following these steps and publishing the module, you can test the pattern in your app.

| Element | Code |
|---|---| 
|![](images/JS_hide.png) |  var header = document.querySelector(".hearder");%%header.classList.add("hide");%%header.classList.add("header-on-scroll");  |
|![](images/JS_show.png) |  var header = document.querySelector(".header");%%header.classList.remove("hide");%%header.classList.remove("header-on-scroll"); | 
  
**Result**

![](images/TouchEvents_EndResult.gif)

## Properties

|**Property** |  **Description** |
|---|---| 
| WidgetId  |  This is the element that responds to the touch you configure.| 

## Compatibility with other patterns

There might be conflicts with any pattern with touch events (unless the code is altered to expect this behavior).

## Samples

The following sample uses the Touch Events pattern:

![](images/TouchEvents-Sample-1.PNG)