---
tags: tooltip implementation, ui design, component customization, event handling, web development
summary: Explore tooltip functionality in Traditional Web Apps using OutSystems 11 (O11), including layout, events, and advanced customization options.
locale: en-us
guid: 421bf73a-44ad-44ee-ba61-b2d234472c54
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:615
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Tooltip Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of a tooltip component in a traditional web app](images/tooltip-3-diag.png "Tooltip Layout Diagram")

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnHide | Event triggered once the tooltip is hidden.  |  False  |
| OnShow | Event triggered once the tooltip is shown.  |  False  |

## Advanced use case

### Change animation of tooltip

1. Drag a Tooltip to the preview.
1. Set the AdvancedFormat parameter to `{ animation: 'perspective' }`.

    <iframe src="https://player.vimeo.com/video/998227283" width="638" height="118" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video showing the change of animation in a Tooltip component within a traditional web app.</iframe>
