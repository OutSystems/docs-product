---
tags: runtime-traditionalweb; 
summary: Tooltip dynamically displays simple informative content on end user interaction.
---

# Tooltip

Dynamically displays simple informative content on end user interaction.

Use the Tooltip to show informative text when end users hover over, focus on or tap an element. Tooltips can identify or describe an element with simple text, not supporting complex text or operations.

**How to use**

Drag the Block to the screen, add your content and the tooltip text in the placeholders.

1. Drag the tooltip into preview.
1. Set the widget in the Widget Placeholder.
1. Set the content on the Content Placeholder.

    ![](<images/tooltip-image-1.png?width=500>) 
    
    ![](<images/tooltip-image-2.png>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Trigger | Set the type of trigger for the content. | Trigger Identifier | False | Entities.Trigger.Hover |
| IsVisible | If set as true, the block is visible when the page is first loaded (without the need for the initial trigger). | Boolean | False | False |
| Position | Set the position around the widget element. | PositionBase Identifier | False | Entities.PositionBase.Top |
| ExtendedClass |  Add custom style classes to this Block. | Text | False | none |
| AdvancedFormat | Allow for more options beyond what it's provided through the input parameters. Example: `{ arrow: false }` For more information visit: https://atomiks.github.io/tippyjs/ | Text | False | none |

## Layout and Classes

![](<images/tooltip-image-3.png>)

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnHide | Event triggered once the tooltip is hidden.  |  False  |
| OnShow | Event triggered once the tooltip is shown.  |  False  |

## Advanced Use Case

### Change Animation of tooltip

1. Drag a Tooltip to the preview.
1. Set the AdvancedFormat parameter to `{ animation: 'perspective' }`.

    ![](<images/tooltip-gif-1.gif>) 
