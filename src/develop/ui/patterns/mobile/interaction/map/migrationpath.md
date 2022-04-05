---
tags: runtime-mobileandreactiveweb;  
summary: OutSystems Maps version 1.1.0 introduces some changes in the component structure. This page aims to help you migrate deprecated functionalities to new ones.
---

# Migration Path

OutSystems Maps version 1.1.0 introduces some changes in the component structure. This page aims to help you migrate deprecated functionalities to new ones.

<div class = "info" markdown = "1" >

The following properties and events will be permanently removed in three releases.

If you have any questions, comments, or need some assistance you can post a question on the [Support tab of the Forge component](https://www.outsystems.com/forge/component-discussions/9909/OutSystems+Maps). Customers entitled to Support Services may obtain assistance through [Support](https://www.outsystems.com/supportportal).

</div>

## Deprecated map properties and how to migrate them

* **Markers**

    Instead of a Map block input parameter, Markers are now represented by blocks. [Learn how to add a list of markers to the map.](map.md)

* **StaticMap**

    To create a static map, use the [Static Map](intro.md) block.

* **ExtendedClass**

    To customize a map, use the [custom style classes](../../../../look-feel/css.md).

## Deprecated map events and how to migrate them

* **Map_EventTriggered**

    Use the **MapEvent** block to listen to handle events, such as **click**, **doubleClick**, **dragEnd**, **rightClick**, and **zoomChanged**.

* **Markers_EventTriggered**

    Use the **MarkerEvent** block to handle the multiple marker events, such as **doubleClick**, **dragEnd** and **rightClick**. 

* **Markers_OnClick**

    use the **Marker** block event to handle the markers **OnClick** event.

* **Markers_OnMouseout**

    Use the **MarkerEvent** block to handle the multiple marker events such as **doubleClick**, **dragEnd** and **rightClick**. It’s also possible to extend this list by setting the **EventName** as 
    **TextToIdentifier** (Mouseout).

* **Map_OnMouseover**

    Use the **MarkerEvent** block to handle the multiple marker events, such as **doubleClick**, **dragEnd**, and **rightClick**. It’s also possible to extend this list by setting the **EventName** as **TextToIdentifier** (Mouseover).
