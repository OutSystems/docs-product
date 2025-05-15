---
tags: ui patterns, css customization, web design, iconography, tooltips
summary: Explore the Stacked Icon UI Pattern in OutSystems 11 (O11) for enhancing Traditional Web Apps with scalable icons and tooltips.
locale: en-us
guid: fb849376-d199-4131-af7d-fb890d688676
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:575
audience:
  - frontend developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Stacked Icon UI Pattern Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and CSS class associations for the Stacked Icon UI Pattern](images/stackedicon-3-diag.png "Stacked Icon Layout Diagram")

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

    ![Screenshot showing the configuration of Tooltip Pattern parameters for the Stacked Icon](images/stackedicon-4-ss.png "Tooltip Parameter Configuration")

1. In the Widget placeholder, drag a StackedIcon Pattern.

1. Set the parameters for the SatckedIcon Pattern.

    ![Screenshot displaying the StackedIcon Pattern parameters setup in the user interface](images/stackedicon-5-ss.png "StackedIcon Pattern Configuration")

1. In the Content placeholder, from the Tooltip Pattern, set the desired label for the icon.

    ![Screenshot indicating where to input the label for the icon within the Tooltip Pattern content placeholder](images/stackedicon-6-ss.png "Tooltip Content Label Setting")

1. Publish and test.

<iframe src="https://player.vimeo.com/video/998188456" width="750" height="417" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video demonstrating the interaction with the Stacked Icon UI Pattern.</iframe>

## Notes

The InvertSize parameter changes the sizes of the back and front icons with each other. This means toggling the `.fa-stack-1x` and `.fa-stack-2x` CSS classes.
