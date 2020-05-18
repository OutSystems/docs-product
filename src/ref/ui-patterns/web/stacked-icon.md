---
tags:
summary: 
---

# Stacked Icon UI Pattern Reference

## Layout and classes

![](<images/stackedicon-image-3.png>)

## CSS Selectors

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

    ![](<images/stackedicon-image-4.png>)

1. In the Widget placeholder, drag a StackedIcon Pattern.

1. Set the parameters for the SatckedIcon Pattern.

    ![](<images/stackedicon-image-5.png>)

1. In the Content placeholder, from the Tooltip Pattern, set the desired label for the icon.

    ![](<images/stackedicon-image-6.png>)

1. Publish and test.

    ![](<images/stackedicon-gif-1.gif>)

## Notes

The InvertSize parameter changes the sizes of the back and front icons with each other. This means toggling the `.fa-stack-1x` and `.fa-stack-2x` CSS classes.


 ## See also

* OutSystems UI Pattern Documentation: [Stacked Icon](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Patterns/Using_Web_Patterns/Utilities/StackedIcon)

