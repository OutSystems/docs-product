---
tags: runtime-mobileandreactiveweb;  
summary: 
---

# Swipe Events

The SwipeEvents pattern enables swiping on a specific widget.

![](images/swipe_events.png)

## How to Use the SwipeEvents Pattern

You can use the SwipeEvents pattern to open a sidebar.

![](images/swipe_area.png)

Create a local variable, called isOpen to be used in the sidebar.

![](images/swipe_events_create.png)

Result:

![](images/SwipeEvents_EndResult.gif)

## Input Parameters

**Input Name** |  **Description** |  **Default Value**  
---|---|---  
![](images/input.png) |  WidgetId  |  Element that will be swipeable.  |  none  
  
## Events

**Event Name** |  **Description** |  **Mandatory**  
---|---|---  
![](images/Event.png) SwipeDown  |  The event is triggered after a swipe down.  |  _False_  
![](images/Event.png) SwipeLeft  |  The event is triggered after a swipe left.  |  _False_  
![](images/Event.png) SwipeRight  |  The event is triggered after a swipe right.  |  _False_  
![](images/Event.png) SwipeUp  |  The event is triggered after a swipe up.  |  _False_  
  
## Compatibility with other Patterns

There might be conflicts with any pattern with touch events (unless the code is altered to support the behavior). For example: using the id of a sidebar instead of a container in the previous example.

  * HorizontalScroll 
  * [Carousel](<carousel.md>)
  * [TouchEvents](<touchevents.md>)
  * [StackedCards](<stackedcards.md>)
  * Notification 
  * Sidebar 

## Samples

The following sample uses the SwipeEvents pattern:

![](images/SwipeEvents-Sample-1.PNG)
