---
tags: runtime-traditionalweb; 
summary: AnimatedLabel allows end-users to keep context by focusing on the input.
---

# AnimatedLabel

An input label that animates when there is user input.

Use AnimatedLabel inputs to allow end-users to keep context by focusing on the input.

**How to use**

Drag the pattern to the screen and configure the input and label text. You may use the IsInline parameter to define if it should use the default input style.

1. Drag AnimatedLabel pattern into the preview.

1. Set the Variable property of the Input widget.
    
    ![](<images/animatedlabel-image-1.png>)

1. Change the text in Label Placeholder.
    
    ![](<images/animatedlabel-image-2.png>)
    
1. Publish and test.
    
    ![](<images/animatedlabel-image-3.png>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| IsInline  |  If set as false, the input style in the block as default (white background). | Boolean | False | True |
| ExtendedClass  |  Add custom style classes to this Block. | Text | False | None |

## Layout and Classes
    
![](<images/animatedlabel-image-4.png>)

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .animated-label | .animated-label-inline |  When IsInline Input Parameter is true |


## Advanced Use Case

### Change the position of the label when it is active 

1. Write the following CSS code in the CSS editor.

    ```css
    .animated-label.active .animated-label-text {
        top: 50px;
    }
    ```
1. Publish and test.

Before 

![](<images/animatedlabel-image-5.png>)

After 

![](<images/animatedlabel-image-6.png>)
