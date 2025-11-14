---
tags: ui patterns, traditional web development, css customization, toggle button, web design
summary: Explore the detailed guide on using and styling the Toggle Button UI pattern in OutSystems 11 (O11).
locale: en-us
guid: 0a3ed4d0-92d8-42d3-8cb5-076de9b5752a
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:610
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Toggle Button Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout and classes of the Toggle Button UI pattern](images/togglebutton-3-diag.png "Toggle Button Layout Diagram")

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|--- |
| .toggle-button | .toggle-button-checked | Is the Class Selector to style the Toggle Button when the Boolean Variable is true |
| .toggle-button | .toggle-button-disabled | Is the Class Selector to style the Toggle Button when is disabled |
| .toggle-button | .toggle-button:after | Is the Pseudo Element Selector to style the circle of Toggle Button |

## Advanced use case

### Disable the Toggle Button pattern

1. Drag the Toggle Button pattern into the preview.

1. Set a variable of type boolean to the checkbox.

    ![Screenshot of dragging the Toggle Button pattern into the preview](images/togglebutton-1-ss.png "Toggle Button Preview")

1. In the Checkbox, set the parameter Enabled to False.

    ![Screenshot showing the Toggle Button with the Enabled parameter set to False](images/togglebutton-4-ss.png "Toggle Button Disabled Setting")

1. Publish and test.

    ![Screenshot of the published Toggle Button in a disabled state](images/togglebutton-5-ss.png "Toggle Button Published Test")
