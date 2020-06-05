---
tags: runtime-traditionalweb; 
summary: Modal is a box with content that interrupts the end user and demands an action.
---

# Modal

You can use the Modal UI Pattern to interrupt the end user and demand an action. It is implemented to direct an end user’s attention to important information. Ideal for when the end user is requested to enter information critical to continuing the current process.

 ![](<images/modal-1.png>)

**How to use the Modal UI Pattern**

After placing a Modal on the screen, open it by calling a new screen action using a button with its method set to Ajax submit and use the Toggle Modal action (found in the Logic Tab). Use the pattern parameters to define if it has an Overlay, its Position in the page and the Enter/Leave animations. Note that you need to enter a value in the Name field of the widgets to be able to select their IDs.

1. In Service Studio, in the Toolbox, search for `Modal`.
  
     The Modal widget is displayed.

    ![](<images/modal-5-ss.png>)

1. To From the Toolbox, drag the Modal widget into the Main Content area of your application's screen. 

   ![](<images/modal-6-ss.png>)

    By default, the Modal widget contains Title, Icon, Content, and Footer placeholders.

1. Add your content to the placeholders.
1. Use a Button Widget or a Link with Ajax Submit to open the Modal Pattern.
1. In the Destination property, create a new screen action to trigger the modal.

    ![](<images/modal-2-ss.png>)

1. Inside the action created, use the action ToggleModal and set the WidgetID.

    ![](<images/modal-3-ss.png>)

1. On the **Properties** tab, change the Modal's look and feel by setting the (optional) properties.

    ![](<images/modal-4-ss.png>)
   
When adding Modal to your app, set the correct TriggerButtonId to ensure accessibility support, as this ensures proper focus and accessibility support.

After following these steps and publishing the module, you can test the pattern in your app.
    
**How to close the Modal**

Users can close the modal widget by pressing the ESC key. If you want to give users an option to close the modal with the button or a link:

1. Add a button or a link into the Modal widget.
1. Go to the link/button properties and in the **On Click** section:
    
    * In the **Method** list select **Ajax Submit**.
    * In the **Destination** list select the same action you created to open the modal dialog.
    
    The **ToggleModal** action in the existing action closes the modal if it's opened, and opens the modal if it's closed.
 
 1. Publish the app and verify the modal closes correctly.

## Properties

| **Property** |  **Description** |  
|---|---|
| Position (PositionExtended Identifier): Optional| Set the position of the Modal on the screen. <p>Examples</p><ul><li>_Blank_ - The modal is positioned in the center of the screen (_Entities.PositionExtended.Center_). This is the default.</li><li>_Entities.PositionExtended.TopLeft_ - The modal is positioned top-left of the screen.</li></ul>| 
| HasOverlay (Boolean): Optional | If True, an overlay is enabled behind the modal. This is the default. If False, there is no overlay. | 
| EnterAnimation (EnterAnimation Identifier): Optional | Define from where the animation enters the screen. <p>Examples</p><ul><li>_Blank_ - The animation goes from a small size to its rendered size (_Entities.EnterAnimation.EnterScale_). This is the default.</li><li>_Entities.EnterAnimation.EnterBottom_ - The animation enters from the bottom of the screen.</li></ul> |  
| LeaveAnimation (LeaveAnimation Identifier ): Optional | Define from where the animation leaves the screen. <p>Examples</p><ul><li>_Blank_ - The animation goes from its rendered size to a small size.(_Entities.LeaveAnimation.EnterScale_). This is the default.</li><li>_Entities.LeaveAnimation.EnterBottom_ - The animation leaves from the bottom of the screen.</li></ul>|
| ExtendedClass (Text): Optional |  Add custom style classes to the Modal UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Modal UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Modal UI styles being applied.</li></ul></p> |
