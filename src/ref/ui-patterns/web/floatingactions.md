---
tags: runtime-traditionalweb;
summary: Explore the Floating Actions UI Pattern in OutSystems 11 (O11) for Traditional Web Apps, detailing layout, events, CSS selectors, and advanced use cases.
locale: en-us
guid: ada89c16-a9f3-45b5-b488-1dec777600c5
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=615%3A478&mode=design&t=Cx8ecjAITJrQMvRn-1
---

# Floating Actions Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of the Floating Actions UI Pattern for Traditional Web Apps](images/floatingactions-2-diag.png "Floating Actions Layout Diagram")

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnToggle | Event fired after the floating actions are toggled |  False  |

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---|
| .floating-actions |  .is--open|  Set when the Floating Actions Pattern is open  |

## Advanced Use Case

### Change Floating Actions position

1. Write the following CSS code in the CSS editor.

        .floating-actions {
            -webkit-box-align: start;
            -ms-flex-align: start;
                align-items: flex-start;
            left: 0;
            right: auto;
        }
        
        .floating-actions-items {
            -webkit-box-align: start;
            -ms-flex-align: start;
                align-items: flex-start;
            padding-left: var(--space-s);
        }
        
        .floating-actions-item {
            -webkit-box-orient: horizontal;
            -webkit-box-direction: reverse;
            -ms-flex-direction: row-reverse;
                flex-direction: row-reverse;
        }
        
        .floating-actions-item-button {
            margin-left: 0;
            margin-right: var(--space-base); 
        }

1. Publish and test.

    <iframe src="https://player.vimeo.com/video/1002673080" width="238" height="276" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video demonstrating the change of position for Floating Actions in a Traditional Web App.</iframe>


### Use Floating Actions with List Records

1. Drag the Floating Actions Pattern into the preview.

1. In the Items placeholder, drag a List Records widget.

1. Set the Line Separator property of the List Records to None.

1. In the List Records, drag a Floating Actions Item.

1. In the Floating Actions Item, use expressions to display the required content.

1. Publish and test.
