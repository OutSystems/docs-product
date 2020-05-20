---
tags: runtime-mobileandreactiveweb;  
summary:  Swipe Events UI Pattern enables swiping on a specific widget.
---

# Swipe Events

You can use the Swipe Events UI Pattern to enable swiping on a specific widget.

## How to use the Swipe Events UI Pattern

The following example shows how you can use the Swipe Events UI pattern to open a sidebar.

1. In Service Studio, in the Toolbox, search for  `Swipe Events`. 

    The Swipe Events widget is displayed.

    ![](images/swipeevents-icon.png)

1. From the Toolbox, drag the Swipe Events widget onto your application's screen.

     ![](images/swipeevents-image-1.png)

1. On the **Properties** tab, create a local variable called **isOpen**. This is used in the sidebar.

    ![](images/swipe_events_create.png)

After following these steps and publishing the module, you can test the pattern in your app. The result should look something like the following:

![](images/SwipeEvents_EndResult.gif)

## Properties

**Property** |  **Description** | 
|---|---| 
| WidgetId (Text): Mandatory |  Element that is swipeable.  |
  
  
## Compatibility with other patterns

There might be conflicts with any pattern with touch events (unless the code is altered to support the behavior). For example, using the sidebar ID  instead of a container in the previous example.

  * Horizontal Scroll 
  * [Carousel](<carousel.md>)
  * [TouchEvents](<touchevents.md>)
  * [StackedCards](<stackedcards.md>)
  * Notification 
  * Sidebar 

## Samples

The following sample uses the Swipe Events UI Pattern:

![](images/SwipeEvents-Sample-1.PNG)

