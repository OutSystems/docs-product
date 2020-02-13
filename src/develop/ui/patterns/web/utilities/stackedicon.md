---
tags: runtime-traditionalweb; 
summary: StackedIcon expands the icon set and creates new graphical representation of concepts.
---

# StackedIcon

Use this pattern to be able to stack two RichWidget Icons on top of each other.

Use the Stacked Icons to expand the icon set and create new graphical representation of concepts.

**How to use**

Select StackedIcons to be displayed and choose their colors, relative position and swap their sizes.

1. Drag StackedIcon pattern into the preview.

    ![](<images/stackedicon-image-1.png>)

1. Set the Input Parameters to extend the default values.

1. Publish and test.

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| IconFront | The icon to display in front of the other.| IconName Identifier | False | Entities.IconName.camera |
| IconBack | The icon to display behind the other.| IconName Identifier| False | Entities.IconName.ban |
| IconFrontColor | Front icon color. | Color Identifier | False | Entities.Color.Neutral10 |
| IconBackColor | Back Icon color. | Color Identifier | False | Entities.Color.Neutral10 |
| IconSize | Set the size. | IconSize Identifier | False | none |
| InvertSize | Set to True to swap the icon sizes. | Boolean | False | none |
| ExtendedClass  |  Add custom style classes to this Block. | Text | False | None |

## Layout and Classes

![](<images/stackedicon-image-3.png>)

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .stacked-icon  | .fa-2x |  Change the icon size, to 2em  |
| .stacked-icon  | .fa-3x |  Change the icon size, to 3em  |
| .stacked-icon  | .fa-4x |  Change the icon size, to 4em  |
| .stacked-icon  | .fa-5x |  Change the icon size, to 5em  |
| .stacked-icon  | .fa-lg |  Change the icon size, to 1.33333333em  |

## Advanced Use Case

### Use StackedIcon with a Tooltip

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

The InvertSize parameter changes the sizes of the back and front icons, with each other. This means, toggling the `.fa-stack-1x` and `.fa-stack-2x` CSS classes.
