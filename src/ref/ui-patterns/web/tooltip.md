---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Tooltip UI Pattern.
locale: en-us
guid: 421bf73a-44ad-44ee-ba61-b2d234472c54
app_type: traditional web apps
---

# Tooltip Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/tooltip-3-diag.png>)

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnHide | Event triggered once the tooltip is hidden.  |  False  |
| OnShow | Event triggered once the tooltip is shown.  |  False  |

## Advanced use case

### Change animation of tooltip

1. Drag a Tooltip to the preview.
1. Set the AdvancedFormat parameter to `{ animation: 'perspective' }`.

    ![](<images/tooltip-1.gif>)
