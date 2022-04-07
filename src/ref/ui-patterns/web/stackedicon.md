---
tags: runtime-traditionalweb; 
summary: Advanced uses cases for the Stacked Icon UI Pattern. 
locale: en-us
guid: fb849376-d199-4131-af7d-fb890d688676
---

# Stacked Icon UI Pattern Reference

## Layout and classes

![](<images/stackedicon-3-diag.png>)

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .stacked-icon  | .fa-2x |  Change the icon size, to 2em  |
| .stacked-icon  | .fa-3x |  Change the icon size, to 3em  |
| .stacked-icon  | .fa-4x |  Change the icon size, to 4em  |
| .stacked-icon  | .fa-5x |  Change the icon size, to 5em  |
| .stacked-icon  | .fa-lg |  Change the icon size, to 1.33333333em  |

## Advanced use case

### Use the Stacked Icon Pattern with a tooltip

1. Drag a Tooltip Pattern into the page.

1. Set the parameters for the Tooltip behavior.

    ![](<images/stackedicon-4-ss.png>)

1. In the Widget placeholder, drag a StackedIcon Pattern.

1. Set the parameters for the SatckedIcon Pattern.

    ![](<images/stackedicon-5-ss.png>)

1. In the Content placeholder, from the Tooltip Pattern, set the desired label for the icon.

    ![](<images/stackedicon-6-ss.png>)

1. Publish and test.

![](<images/stackedicon-1.gif>)

## Notes

The InvertSize parameter changes the sizes of the back and front icons with each other. This means toggling the `.fa-stack-1x` and `.fa-stack-2x` CSS classes.
