---
tags: runtime-traditionalweb; 
summary: Explore the Balloon UI Pattern features and advanced use-cases in OutSystems 11 (O11) for enhancing traditional web applications.
locale: en-us
guid: d95ffaba-85b3-4152-95f5-71804d0aa12b
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:387
---

# Balloon Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Screenshot showing the layout and classes of the Balloon UI Pattern in a traditional web application](images/balloon-image-2.png "Balloon UI Pattern Layout")

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

    ![Animated example of the Balloon UI Pattern with default animation in a traditional web application](images/balloon-gif-1.gif "Balloon UI Pattern Animation Example")

Changed animation:

![Animated example of the Balloon UI Pattern with perspective animation in a traditional web application](images/balloon-gif-2.gif "Balloon UI Pattern Changed Animation")
