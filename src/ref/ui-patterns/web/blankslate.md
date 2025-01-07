---
tags: ui design, css customization, web design, ux patterns, design systems
summary: Learn how to implement the Blank Slate UI Pattern in Traditional Web Apps using OutSystems 11 (O11) for optimal content alignment and conditional display.
locale: en-us
guid: 57108c14-9fcd-46a6-9604-489d54277361
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=615%3A391&mode=design&t=Cx8ecjAITJrQMvRn-1
audience:
  - frontend developers
  - ui designers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Blank Slate Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout and classes for the Blank Slate UI Pattern in Traditional Web Apps](images/blankslate-2-diag.png "Blank Slate Layout Diagram")

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .blank-slate | .bottom-center | Vertically aligns the content to Bottom and Horizontally align it to Center. |
| .blank-slate | .bottom-left |  Vertically aligns the content to Bottom and Horizontally align it to Left. |
| .blank-slate | .bottom-right |  Vertically aligns the content to Bottom and Horizontally align it to Right. |
| .blank-slate | .center |  Vertically aligns the content to Center and Horizontally align it to Center. |
| .blank-slate | .center-left |  Vertically aligns the content to Center and Horizontally align it to Left. |
| .blank-slate | .center-right |  Vertically aligns the content to Center and Horizontally align it to Right. |
| .blank-slate | .top-center | Vertically aligns the content to Top and Horizontally align it to Center. |
| .blank-slate | .top-left |  Vertically aligns the content to Top and Horizontally align it to Left. |
| .blank-slate | .top-right |  Vertically aligns the content to Top and Horizontally align it to Right. |

## Advanced use case

### Show the Blank Slate Pattern when the list is empty

1. Drag the If Widget and enter the Empty runtime property in the condition.

    ![Screenshot of the If Widget with the Empty runtime property condition for displaying the Blank Slate Pattern](images/blankslate-3-ss.png "Blank Slate Empty List Condition")

1. Inside the True branch of the condition, use the Blank Slate Pattern.
1. Inside the False branch of the condition, use your list.

    ![Screenshot showing the True and False branches of the If Widget with the Blank Slate Pattern and a list](images/blankslate-4-ss.png "Blank Slate with List")
