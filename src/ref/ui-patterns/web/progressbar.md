---
tags:
summary: 
---

# Progress Bar UI Pattern Reference

## Layout and classes

![](<images/progressbar-image-3.png?width=650>)

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .progress-container | .progress-container.flex-direction-column |  When IsInline parameter is False  |
| .progress-container | .progress-container.flex-direction-row |  When IsInline parameter is False  |

## Advanced use case

### Change color of progress bar based on value

1. Create a local Integer variable "Value".

1. Drag the ProgressBar pattern into the preview.

1. Set the Value of the ProgressBar's Percentage parameter.

1. To change the color of your ProgressBar based on values, create a condition and set limits to use color. In this example, 3 colors represent diferent states of progress. Set the Color parameter to `If(Value <= 50, Entities.Color.Red, If( Value > 50 and Value < 75,  Entities.Color.Yellow ,  Entities.Color.Green))`.
    
    ![](<images/progressbar-image-4.png>)

1. Publish and test.

    ![](<images/progressbar-image-5.gif>)

### Change the style of progress bar

It is possible to change the style of Progress bar by using custom CSS. To implement this in your application, copy the CSS and add it to the theme.

```css
.progress {
    padding: var(--space-s);`
    border: var(--space-xs) solid var(--color-primary);`
}
```
![](<images/progressbar-image-6.png>)

### Remove background of progress Bar

To remove the background, use this CSS snippet.

```css
.progress {
    background-color: transparent;
}
```
![](<images/progressbar-image-7.png>)

 ## See also

* OutSystems UI Pattern Documentation: [Progress Bar](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Patterns/Using_Web_Patterns/Numbers/ProgressBar)

