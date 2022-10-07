---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Search Balloon UI Pattern.
locale: en-us
guid: f2455c53-89bf-4a8e-89c5-3fd31f5fadb7
app_type: traditional web apps
---

# Balloon Search Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](images/searchballoon-2-diag.png?width=800)

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

![](images/searchballoon-1-ss.gif?width=800)

![](images/searchballoon-2-ss.gif?width=800)
