---
tags: runtime-traditionalweb; 
summary: FloatingActions display an action that floats in the bottom right corner of the screen.
---

# FloatingActions 

Display an action that floats in the bottom right corner of the screen, providing access to a set of additional actions.

Use the Floating Action to show the primary action on a screen. Choose actions such as create, share, explore and so on. Avoid actions such as delete, archive or an alert. Exclude limited actions such as cut-and-paste text or actions that should be in a toolbar.

**How to use**

1. Drag FloatingAction pattern into the preview.

    ![](<images/floatingactions-image-1.png>)

1. Set the content in the placeholders.

1. Publish and test.


## Input Parameters

### FloatingActions

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Trigger  | Set the type of trigger for the Button. | Trigger Identifier | No | Entities.Trigger.Click |
| ExtendedClass  | Add custom style classes to this Block. | Text | No | none |

### FloatingActionsItem

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| ExtendedClass  | Add custom style classes to this Block. | Text | No | none |
  
## Layout and Classes

![](<images/floatingactions-image-2.png>)

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnToggle | Event fired after the floating actions are toggled |  False  |

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---|
| .floating-actions |  .is--open|  Set when the Floating Actions Pattern is open  |


## Advanced Use Case

### Change FloatingActions position

1. Write the following CSS code in the CSS editor.

    ```css
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
    ```
1. Publish and test.

    ![](<images/floatingactions-gif-1.gif>)

### Use FloatingActions with ListRecords

1. Drag the FloatingActions Pattern into the preview.

1. In the Items placeholder, drag a ListRecords widget.

1. Set the Line Separator property of the ListRecords to None.

1. In the ListRecords, drag a FloatingActionsItem.

1. In the FloatingActionsItem, use expressions to display the required content.

1. Publish and test.
