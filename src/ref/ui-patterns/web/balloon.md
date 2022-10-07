---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Balloon UI Pattern.
locale: en-us
guid: d95ffaba-85b3-4152-95f5-71804d0aa12b
app_type: traditional web apps
---

# Balloon Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/balloon-image-2.png>)

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnHide | Event triggered once the balloon is hidden.  |  False  |
| OnShow | Event triggered once the balloon is shown.  |  False  |

## Advanced

Here are some more advanced use-cases of the widget.

### Show Balloon on init

1. Drag Balloon to the preview.
1. Set the AdvancedFormat parameter to `{ showOnInit: true }`.

### Change the animation

1. Drag Balloon to the preview.

1. Set the AdvancedFormat parameter to `{ animation: 'perspective' }`.

    ![](<images/balloon-gif-1.gif>)

Changed animation:

![](<images/balloon-gif-2.gif>)
