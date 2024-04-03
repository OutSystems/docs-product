---
tags: runtime-traditionalweb; 
summary: Modal is a box with content that interrupts the end user and demands an action.
locale: en-us
guid: 64cf2199-6b69-480b-a63e-49b91965e777
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=222:101
---

# Modal

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Modal UI Pattern to interrupt the end user and demand an action. It is implemented to direct an end user’s attention to important information. Ideal for when the end user is requested to enter information critical to continuing the current process.

![Example of a Modal UI Pattern in use](images/modal-1.png "Modal UI Pattern Example")

**How to use the Modal UI Pattern**

For the purposes of this example, our app already contains a form where the user can enter their queries, and once they send their message, a confirmation message appears by using the Modal widget.

1. In Service Studio, in the Toolbox, search for `Modal`.
  
    The Modal widget is displayed.

    ![Screenshot showing the Modal widget in OutSystems Service Studio](images/modal-5-ss.png "Modal Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. To From the Toolbox, drag the Modal widget into the Main Content area of your application's screen, and on the **Properties** tab, enter a name for the widget. In this example we enter `Confirmation`.

    ![Screenshot of dragging the Modal widget into the Main Content area in Service Studio](images/modal-6-ss.png "Adding Modal Widget to Main Content")

    By default, the Modal widget contains Title, Icon, Content, and Footer placeholders.

1. Add your content to the placeholders. In this example we add text to the Title placeholder, text to the Content placeholder, and 2 buttons (Yes and No) to the Footer placeholder.

    ![Screenshot of adding content to the Modal widget placeholders in Service Studio](images/modal-7-ss.png "Modal Widget Content Configuration")

1. In this example, to open the Modal widget, we need to set the **Method** and **Destination** properties for the **Yes** button. To do this, select the **Yes** button, and on the **Properties** tab, from the **Method** drop-down, select **Ajax Submit** and from the **Destination** select **New Screen Action**.

    ![Screenshot of setting the Method and Destination properties for the Yes button in the Modal widget](images/modal-8-ss.png "Setting Modal Widget Properties")

1. Enter a name for the screen action. In this example, we enter `ConfirmSend`.

    ![Screenshot of entering a name for the screen action in the Modal widget configuration](images/modal-11-ss.png "Naming Screen Action for Modal")

1. Select the **Logic** tab, navigate to **OutSystemsUIWeb > Modal** and drag the **ToggleModal** onto the screen action.

    ![Screenshot of the ToggleModal action being dragged onto the screen action in Service Studio](images/modal-9-ss.png "ToggleModal Logic in Service Studio")

1. On the **properties** tab, from the **WidgetId** drop-down, select the Id of the Modal widget. In this example, we select **Confirmation.Id**.

    ![Screenshot of selecting the WidgetId for the Modal widget from the Properties tab in Service Studio](images/modal-10-ss.png "Selecting WidgetId for Modal")

1. In this example, to close the Modal, we need to set the **Method** and **Destination** properties for the **No** button. To do this, double-click your screen name, select the **No** button, and on the **Properties** tab, from the **Method** drop-down, select **Ajax Submit** and from the **Destination** select the screen action you previously created. In this case **ConfirmSend**.

    ![Screenshot of setting the Method and Destination properties for the No button in the Modal widget](images/modal-12-ss.png "Configuring No Button in Modal")

1. On the **Properties** tab, you can change the Modal's look and feel by setting the (optional) properties.

    ![Screenshot of the optional properties for changing the Modal's look and feel in Service Studio](images/modal-4-ss.png "Modal Properties Configuration")

After following these steps and publishing the module, you can test the pattern in your app.

The result of this example looks something like the following:

![Example of the final appearance of the Modal UI Pattern after configuration](images/modal-13-ss.png "Final Look of Modal UI Pattern")

## Properties

| **Property** | **Description** |
|---|---|
| Position (PositionExtended Identifier): Optional | Set the position of the Modal on the screen. <p>Examples</p><ul><li>Blank - The modal is positioned in the center of the screen (Entities.PositionExtended.Center). This is the default.</li><li>Entities.PositionExtended.TopLeft - The modal is positioned top-left of the screen.</li></ul> |
| HasOverlay (Boolean): Optional | If True, an overlay is enabled behind the modal. This is the default. If False, there is no overlay. |
| EnterAnimation (EnterAnimation Identifier): Optional | Define from where the animation enters the screen. <p>Examples</p><ul><li>Blank - The animation goes from a small size to its rendered size (Entities.EnterAnimation.EnterScale). This is the default.</li><li>Entities.EnterAnimation.EnterBottom - The animation enters from the bottom of the screen.</li></ul> |
| LeaveAnimation (LeaveAnimation Identifier ): Optional | Define from where the animation leaves the screen. <p>Examples</p><ul><li>Blank - The animation goes from its rendered size to a small size.(Entities.LeaveAnimation.EnterScale). This is the default.</li><li>Entities.LeaveAnimation.EnterBottom - The animation leaves from the bottom of the screen.</li></ul> |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
