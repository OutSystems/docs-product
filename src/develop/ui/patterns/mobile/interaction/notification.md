---
tags: runtime-mobileandreactiveweb;  
summary: The Notification UI Pattern is a contextual short message that provides important information to the user. 
---

# Notification

The Notification UI Pattern is a contextual short message that provides important information to the user, such as app crashes, new updates, task reminders, and new messages.

**How to use the Notification UI Pattern**

1. In Service Studio, in the Toolbox, search for `Notification`.

    The Notification widget is displayed.

    ![](<images/notification-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Notification widget into the Main Content area of your application's screen.

    ![Drag the Animate widget to the screen](<images/notification-dragwidget-ss.png>)

 1. Add the relevant content to the Content placeholder. 

    In this example, an icon, some text are added. **Open** and **Close** buttons are also added to the Main Content area of the screen.

    ![Add content to Content placeholder](<images/notification-content-ss.png>)

1. Select and right-click your screen name, and select **Add Local Variable**. Enter a name for the variable, for example, ``ShowNotification`` and set the **Default Value** to **False**.

    ![Add a local variable](<images/notification-variable-ss.png>)

1. Select the Notification widget, and on the **Properties** tab, from the **StartsOpen** dropdown, enter the newly created variable (``ShowNotification``). 

    ![Set the StartsOpen property ](<images/notification-startopen-ss.png>)

1. Define the actions for the **Open** and **Close** buttons, by selecting the button widget, and on the **Properties**, from the **OnClick** dropdown select **New Client Action**.

    In this example, for the **Open** button, the **ShowNotification** variable is set to **True**, and for the **Close** button the **ShowNotification** variable is set to False.

    ![Define action for Open button](<images/notification-open-ss.png>)

    ![Define action for Close button](<images/notification-close-ss.png>)

1. You can configure the Notification by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties. For more configurations, expand the **OptionalConfigs** property.

    ![Define action for Close button](<images/notification-properties-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

![Notification example](<images/notification-example.png>)

## Properties

| Property |  Description |
|---|---|
|IsOpen (Boolean): Mandatory | If True, the notification is immediately visible on screen. If False, the notification is not visible on screen. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the myclass style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
