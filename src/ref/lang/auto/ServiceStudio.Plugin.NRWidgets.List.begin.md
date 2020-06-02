---
tags: runtime-mobileandreactiveweb;
---

Use the List widget to display a simple list, for example a list of Expressions, or to display more complex items by adding a [List Item widget](ServiceStudio.Plugin.NRWidgets.ListItem.final.md). List requires a source to populate the item.

## Virtualization

The List widget uses virtualization to render only those elements that are visible in the screen. You can set the value for virtualized pixels with `virtualization-threshold-before` and `virtualization-threshold-after` in the **Attributes** of List. Use them to tweak the scroll experience of List when the virtualization is enabled.

You can also deactivate the virtualization with `disable-virtualization=True`. 

## Scroll threshold

When List reaches the scroll threshold value, the app requests new records and then adds them to the list of items. The default value is 2000 pixels. Set the scroll threshold with `infinite-scroll-threshold` in the **Attributes** of List.
