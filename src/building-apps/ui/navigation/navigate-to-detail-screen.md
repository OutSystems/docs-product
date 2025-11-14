---
summary: Explore how to navigate to a detail screen in OutSystems 11 (O11) for both Reactive Web and Mobile, and Traditional Web applications.
tags: ui navigation, list item interaction, web development, user interface, event handling
locale: en-us
guid: 407dfc26-80f5-440c-b3e1-56d8e7d27ce8
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=249:17
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
topic:
  - navigate-screens
---

# Navigate to a Detail Screen

You can allow end users to check the details of a given record by navigating to a different screen while providing the item identifier as an input parameter.

## In Reactive Web and Mobile

To navigate to a detail screen in Reactive Web and Mobile:

1. On the screen that displays the list, select the List Item widget.
1. In the properties of the List Item widget, select the target detail screen as handler for the On Click event and define the identifier of the current list item as an input argument to the target screen.

![Example of navigating to a detail screen in Reactive Web and Mobile using the List Item widget](images/navigate-mobile.png "Navigation to Detail Screen in Reactive Web and Mobile")

## In Traditional Web

To navigate to a detail screen in Traditional Web:

1. On the screen that displays the list, associate a Link widget with a detail of the item displayed in the list.
1. In the properties of the Link widget, select the target detail screen in the Destination property and define the identifier of the current list item as an input argument to the target screen.

![Illustration of linking to a detail screen in Traditional Web using the Link widget](images/navigate-web.png "Navigation to Detail Screen in Traditional Web")
