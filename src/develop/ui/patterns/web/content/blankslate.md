---
tags: runtime-traditionalweb; 
summary: BlankSlate informs end users when they start using the application, complete a task or when there is no data available for display.
---

# BlankSlate

Content on the screen to show end users that there is no data available for display.

Use BlankSlate to inform end users when they start using the application, complete a task or when there is no data available for display.

**How to use**

Drag the pattern to the screen and edit the content as per your requirements.

1. Drag the BlankSlate pattern into the preview.
1. Set the content you need in the placeholder.
1. Publish and test.

![](<images/blankslate-image-1.png>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Position | Set the position around the widget element. | PositionExtended Identifier | False | Entities.PositionExtended.Center |
| ExtendedClass  |  Add custom style classes to this Block. | Text | False | none |

## Layout and Classes

![](<images/blankslate-image-2.png>)

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

## Advanced Use Case

### Show the BlankSlate Pattern when the list is empty

1. Drag the If Widget and enter the Empty runtime property in the condition.

    ![](<images/blankslate-image-3.png>)

1. Inside the True branch of the condition, use the BlankSlate Pattern.
1. Inside the False branch of the condition, use your list.

    ![](<images/blankslate-image-4.png>)
