---
tags: runtime-traditionalweb; 
summary: ToggleButton prompts end-users to choose between two states.
---

# ToggleButton

Prompts end-users to choose between two states.

Use the Toggle Button and prompt end-users to choose between two incompatible states, selecting a preference. There is always a default value as toggles are digital on/off switches. 

**How to use**

After placing the Block on your Web Screen, drag a checkbox inside the placeholder and the pattern will automatically use it.

1. Drag the ToggleButton pattern into the preview.

1. Set a variable of type Boolean to the checkbox.

    ![](<images/togglebutton-image-1.png>)

1. Publish and test.

    ![](<images/togglebutton-image-2.png>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| ExtendedClass  |  Add custom style classes to this Block. | Text | False | None |

## Layout and Classes

![](<images/togglebutton-image-3.png>)

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .toggle-button | .toggle-button-checked | Is the Class Selector to style the Toggle Button when the Boolean Variable is true |
| .toggle-button | .toggle-button-disabled | Is the Class Selector to style the Toggle Button when is disabled |
| .toggle-button | .toggle-button:after | Is the Pseudo Element Selector to style the circle of Toggle Button |


## Advanced Use Case

### Disable the ToggleButton Pattern

1. Drag the ToggleButton pattern into the preview.

1. Set a variable of type boolean to the checkbox.

    ![](<images/togglebutton-image-1.png>)

1. In the Checkbox, set the parameter Enabled to False.

    ![](<images/togglebutton-image-4.png>)

1. Publish and test.

    ![](<images/togglebutton-image-5.png>)
