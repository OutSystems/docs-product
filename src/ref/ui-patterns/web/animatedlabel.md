---
tags: runtime-traditionalweb;
summary: Advanced use cases for the Animated Label UI Pattern.
---

# Animated Label Reference

## Layout and classes
  
![](<images/animatedlabel-4-diag.png>)

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .animated-label | .animated-label-inline |  When IsInline Input Parameter is true |

## Advanced use case

### Change the position of the label when it is active

1. Write the following CSS code in the CSS editor.

        .animated-label.active .animated-label-text {
            top: 50px;
        }

1. Publish and test.

**Before** 

![](<images/animatedlabel-5-ss.png>)

**After** 

![](<images/animatedlabel-6-ss.png>)
