---
tags: runtime-traditionalweb; 
summary: Modal is a box with content that interrupts the end user and demands an action.
---

# Modal

A box with content that is displayed as an overlay on top of the screen.

Use the Modal to interrupt the end user and demand an action. It is implemented to direct an end user’s attention to important information. Ideal for when the end user is requested to enter information critical to continuing the current process.

 ![](<images/modal-image-1.png>)

**How to use**

After placing a Modal on the screen, open it by calling a new screen action using a button with its method set to Ajax submit and use the Toggle Modal action (found in the Logic Tab). Use the pattern parameters to define if it has an Overlay, its Position in the page and the Enter/Leave animations. Note that you need to enter a value in the Name field of the widgets to be able to select their IDs.

1. Drag the Modal pattern into the preview.
1. Set the content in the placeholders.
1. Use a Button Widget or a Link with Ajax Submit to open the Modal Pattern.
1. In the Destination property, create a new screen action to trigger the modal.

    ![](<images/modal-image-2.png>)

1. Inside the action created, use the action ToggleModal and set the WidgetID.

    ![](<images/modal-image-3.png>)

1. Set the Input Parameters to change the default values.

    ![](<images/modal-image-4.png>)
   
When adding Modal to your app, set the correct TriggerButtonId to ensure accessibility support, as this ensures proper focus and accessibility support.
    
**How to close Modal**

Users can close the modal widget by pressing the ESC key. If you want to give users an option to close the modal with the button or a link:

1. Add a button or a link into the Modal widget.
1. Go to the link/button properties and in the **On Click** section:
    
    * In the **Method** list select **Ajax Submit**.
    * In the **Destination** list select the same action you created to open the modal dialog.
    
    The **ToggleModal** action in the existing action closes the modal if it's opened, and opens the modal if it's closed.
 
 1. Publish the app and verify the modal closes correctly.

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Position | Set the position of the Modal on the screen. | PositionExtended Identifier | False | Entities.PositionExtended.Center |
| HasOverlay | When true, an overlay is enabled behind the modal. | Boolean | False | True |
| EnterAnimation | Set the enter animation. | EnterAnimation Identifier | False | Entities.EnterAnimation.EnterScale |
| LeaveAnimation | Set the leave animation. | LeaveAnimation Identifier | False | Entities.LeaveAnimation.LeaveScale |
| ExtendedClass  |  Add custom style classes to this Block. |  Text | False | None |


## Layout and Classes

![](<images/modal-image-5.png>)

## Advanced Use Case

### Change the animation speed

It is possible to change the animation speed of Modal by using custom CSS. To implement this in your application, copy the CSS to the theme.

```css
.modal .animate {
    -webkit-animation-duration: 500ms;
            animation-duration: 500ms;
}
```
