---
summary: Reference information on the List widget for allowing users to get a list of records on a screen.
tags: runtime-mobileandreactiveweb; outsystems-designing-screens; reference; designing-screens; list-widget
---

Use the List widget to display a simple list, for example a list of Expressions, or to display more complex items by adding a [List Item widget](ServiceStudio.Plugin.NRWidgets.ListItem.final.md). The List widget requires a source to populate the items.

## Virtualization

The List widget uses virtualization to render only those elements that are visible in the screen. You can set the value for virtualized pixels with `virtualization-threshold-before` and `virtualization-threshold-after` in the **Attributes** of List. Adjust the threshold values to tweak the scroll behavior.

You can also deactivate the virtualization with `disable-virtualization=True`. 

## Scroll threshold

When List reaches the scroll threshold value, the app requests new records and then adds them to the list of items. The default value is 2000 pixels. Set the scroll threshold with `infinite-scroll-threshold` in the **Attributes** of List.
