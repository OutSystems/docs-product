---
tags: runtime-traditionalweb; 
summary: Explore the features and advanced use-cases of the Search Balloon UI pattern in OutSystems 11 (O11) for Traditional Web Apps.
locale: en-us
guid: f2455c53-89bf-4a8e-89c5-3fd31f5fadb7
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:560
---

# Balloon Search Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of the Search Balloon UI Pattern](images/searchballoon-2-diag.png "Search Balloon Layout Diagram")

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnHide | Event triggered once the balloon is hidden.  |  False  |
| OnShow | Event triggered once the balloon is shown.  |  False  |

## Advanced

Here are some more advanced use-cases of the widget.

### Show results on init

1. Drag Search Balloon to the preview.
1. On the AdvancedFormat parameter add the following line:  
`{ showOnInit: true }`.

### Change animation of results

1. Drag Search Balloon to the preview.
1. On the AdvancedFormat parameter add the following line:  
`{ showOnInit: true }`.

![Animated GIF showing the Search Balloon widget initialization with results displayed](images/searchballoon-1-ss.gif "Search Balloon Initialization")

![Animated GIF demonstrating the change in animation of the Search Balloon widget's results](images/searchballoon-2-ss.gif "Search Balloon Animation Change")
