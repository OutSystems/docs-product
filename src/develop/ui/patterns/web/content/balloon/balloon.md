---
tags: runtime-traditionalweb; 
summary: Balloon shows a content overlay to users, without forcing them to lose the UI context.
---

# Balloon

Displays an additional overlay of content.

Use the Balloon when you need to display content that you need occasionally on a small area, without losing the context in the UI.

**How to use**

Add the content inside the Balloon placeholders. Then configure the WidgetId that triggers the Balloon. You may also choose the Position, and the type of Trigger.

1. Drag the balloon into the preview.
1. Set content into the title, content and footer placeholders.

    ![](<images/balloon-image-1.png>)


## Demo

<iframe width="750" height="500" src="https://www.youtube.com/embed/FYTapAjZPj8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe>

## Input parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| WidgetId | Element name that triggers the element to be visible. | Text | True | none |
| Position |  Sets the position around the widget element. | PositionBase Identifier | False | Entities.PositionBase.Bottom |
| Trigger |  Sets the type of trigger for the content. Manual requires the tooltip to be triggered programmatically. | Trigger Identifier | False | Entities.Trigger.Hover |
| ExtendedClass  |  Adds custom style classes to the Tabs Block. |  Text | False | none |
| AdvancedFormat  |  Enables you to use more options than what is provided in the input parameters. Example: `{ arrow: false,   showOnInit: true }` For more information visit: https://atomiks.github.io/tippyjs/ |  Text | False | none |

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
