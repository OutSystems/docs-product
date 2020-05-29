---
tags: runtime-mobileandreactiveweb;  
summary: 
---

# Touch Events

The TouchEvents pattern enables touch events on a specific widget.

![](images/touch_events_utilities.png)

## How to Create Custom Patterns with TouchEvents

You can call the **event.preventDefault()** to prevent the default action associated with each event from occurring. The touchstart and touchend events don't need this action, but touchmove requires it to stop screen scrolling when the user is moving the finger inside the element.

![](images/touch_events_custom_patterns.png)

To use the **event.preventDefault()** , use this string of code:

`$parameters.Evt.preventDefault();`

## How to Hide a Header During a Scroll Action

You can use the pattern to hide a header during a scroll action.

1\. Add the **TouchEvents** pattern to the **Layout** block.

![](images/touch_events_layour.png)

2\. Add an **End** event.

![](images/add_end_event.png)

3\. Add logic.

![](images/touch_events_logic.png)

Element | Code
---|---  
![](images/JS_hide.png) |  var header = document.querySelector(".hearder");%%header.classList.add("hide");%%header.classList.add("header-on-scroll");  
![](images/JS_show.png) |  var header = document.querySelector(".header");%%header.classList.remove("hide");%%header.classList.remove("header-on-scroll");  
  
Result:

![](images/TouchEvents_EndResult.gif)

## Input Parameters

**Input Name** |  **Description** |  **Default Value**  
---|---|---  
![](images/input.png) WidgetId  |  This is the element that responds to the touch you configure.  |  none  
  
## Events

**Event Name** |  **Description** |  **Mandatory**  
---|---|---  
![](images/Event.png) End  |  The event is triggered after the movement event finishes.  |  _False_  
![](images/Event.png) Move  |  The event is triggered after the movement starts.  |  _False_  
![](images/Event.png) Start  |  The event is triggered as the touch movement starts.  |  _False_  
  
## Compatibility with other Patterns

There might be conflicts with any pattern with touch events used together with this pattern (unless the code is altered to expect this behavior).

## Samples

The following sample uses the TouchEvents pattern:

![](images/TouchEvents-Sample-1.PNG)
