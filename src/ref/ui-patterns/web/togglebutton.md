---
tags: runtime-traditionalweb;
summary: Advanced use cases for the Toggle Button UI Pattern.
locale: en-us
guid: 0a3ed4d0-92d8-42d3-8cb5-076de9b5752a
---

# Toggle Button Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/togglebutton-3-diag.png>)

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .toggle-button | .toggle-button-checked | Is the Class Selector to style the Toggle Button when the Boolean Variable is true |
| .toggle-button | .toggle-button-disabled | Is the Class Selector to style the Toggle Button when is disabled |
| .toggle-button | .toggle-button:after | Is the Pseudo Element Selector to style the circle of Toggle Button |

## Advanced use case

### Disable the Toggle Button pattern

1. Drag the Toggle Button pattern into the preview.

1. Set a variable of type boolean to the checkbox.

    ![](<images/togglebutton-1-ss.png>)

1. In the Checkbox, set the parameter Enabled to False.

    ![](<images/togglebutton-4-ss.png>)

1. Publish and test.

    ![](<images/togglebutton-5-ss.png>)
