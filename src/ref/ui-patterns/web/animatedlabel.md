---
tags: ui patterns, css customization, web development, design systems, outsystems ui
summary: Explore the features and customization options of the Animated Label UI Pattern in OutSystems 11 (O11).
locale: en-us
guid: eb80a9ee-c99a-4136-85b4-ec06d6b8e8d4
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:379
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Animated Label Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes
  
![Diagram showing the layout and classes of the Animated Label UI Pattern](images/animatedlabel-4-diag.png "Animated Label Layout Diagram")

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|--- |
| .animated-label | .animated-label-inline |  When IsInline Input Parameter is true |

## Advanced use case

### Change the position of the label when it is active

1. Write the following CSS code in the CSS editor.

        .animated-label.active .animated-label-text {
            top: 50px;
        }

1. Publish and test.

**Before**

![Screenshot of the Animated Label UI Pattern before activation](images/animatedlabel-5-ss.png "Animated Label Before Activation")

**After**

![Screenshot of the Animated Label UI Pattern after activation, with the label positioned 50px from the top](images/animatedlabel-6-ss.png "Animated Label After Activation")
