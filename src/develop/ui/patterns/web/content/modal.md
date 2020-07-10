---
tags: runtime-traditionalweb; 
summary: Modal is a box with content that interrupts the end user and demands an action.
---

# Modal

You can use the Modal UI Pattern to interrupt the end user and demand an action. It is implemented to direct an end user’s attention to important information. Ideal for when the end user is requested to enter information critical to continuing the current process.

![](<images/modal-1.png?width=800>)

**How to use the Modal UI Pattern**

For the purposes of this example, our app already contains a form where the user can enter their queries, and once they send their message, a confirmation message appears by using the Modal widget.

1. In Service Studio, in the Toolbox, search for `Modal`.
  
    The Modal widget is displayed.

    ![](<images/modal-5-ss.png>)

1. To From the Toolbox, drag the Modal widget into the Main Content area of your application's screen, and on the **Properties** tab, enter a name for the widget. In this example we enter `Confirmation`.

    ![](<images/modal-6-ss.png?width=800>)

    By default, the Modal widget contains Title, Icon, Content, and Footer placeholders.

1. Add your content to the placeholders. In this example we add text to the Title placeholder, text to the Content placeholder, and 2 buttons (Yes and No) to the Footer placeholder.

    ![](<images/modal-7-ss.png?width=800>)

1. In this example, to open the Modal widget, we need to set the **Method** and **Destination** properties for the **Yes** button. To do this, select the **Yes** button, and on the **Properties** tab, from the **Method** drop-down, select **Ajax Submit** and from the **Destination** select **New Screen Action**.

    ![](<images/modal-8-ss.png?width=800>)

1. Enter a name for the screen action. In this example, we enter `ConfirmSend`.

    ![](<images/modal-11-ss.png>)

1. Select the **Logic** tab, navigate to **OutSystemsUIWeb > Modal** and drag the **ToggleModal** onto the screen action.

    ![](<images/modal-9-ss.png?width=800>)

1. On the **properties** tab, from the **WidgetId** drop-down, select the Id of the Modal widget. In this example, we select **Confirmation.Id**.

    ![](<images/modal-10-ss.png>)

1. In this example, to close the Modal, we need to set the **Method** and **Destination** properties for the **No** button. To do this, double-click your screen name, select the **No** button, and on the **Properties** tab, from the **Method** drop-down, select **Ajax Submit** and from the **Destination** select the screen action you previously created. In this case **ConfirmSend**.

    ![](<images/modal-12-ss.png>)

1. On the **Properties** tab, you can change the Modal's look and feel by setting the (optional) properties.

    ![](<images/modal-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

The result of this example looks something like the following:

![](<images/modal-13-ss.png?width=800>)

## Properties

| **Property** |  **Description** |  
|---|---|
| Position (PositionExtended Identifier): Optional| Set the position of the Modal on the screen. <p>Examples</p><ul><li>_Blank_ - The modal is positioned in the center of the screen (_Entities.PositionExtended.Center_). This is the default.</li><li>_Entities.PositionExtended.TopLeft_ - The modal is positioned top-left of the screen.</li></ul>|
| HasOverlay (Boolean): Optional | If True, an overlay is enabled behind the modal. This is the default. If False, there is no overlay. |
| EnterAnimation (EnterAnimation Identifier): Optional | Define from where the animation enters the screen. <p>Examples</p><ul><li>_Blank_ - The animation goes from a small size to its rendered size (_Entities.EnterAnimation.EnterScale_). This is the default.</li><li>_Entities.EnterAnimation.EnterBottom_ - The animation enters from the bottom of the screen.</li></ul> |  
| LeaveAnimation (LeaveAnimation Identifier ): Optional | Define from where the animation leaves the screen. <p>Examples</p><ul><li>_Blank_ - The animation goes from its rendered size to a small size.(_Entities.LeaveAnimation.EnterScale_). This is the default.</li><li>_Entities.LeaveAnimation.EnterBottom_ - The animation leaves from the bottom of the screen.</li></ul>|
| ExtendedClass (Text): Optional |  Add custom style classes to the Modal UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Modal UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Modal UI styles being applied.</li></ul></p> |
