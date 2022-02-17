---
tags: runtime-mobileandreactiveweb;  
summary: The Notification UI Pattern is a contextual short message that provides important information to the user. 
---

# Notification

The Notification UI Pattern is a contextual short message that provides important information to the user, such as app crashes, new updates, task reminders, and new messages.

![](<images/notification-1-ss.png>)

**How to use the Notification UI Pattern**

1. In Service Studio, in the Toolbox, search for `Notification`.

    The Notification widget is displayed.

    ![](<images/notification-2-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.
    
    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Animate widget into the Main Content area of your application's screen.

    ![](<images/notification-3-ss.png>)

 1. Add the relevant content to the Content placeholder. 

    In this example, we add an icon, some text. We also add Show and Close buttons to the Main Content area of the screen.

    ![](<images/notification-4-ss.png>)

1. Select and right-click your screen name, and select **Add Local Variable**. Enter a name for the variable. In this example, we enter ``ShowNotification`` and set the **Default Value** to **False**.

    ![](<images/notification-5-ss.png>)

1. Select the Notification widget, and on the **Properties** tab, from the **IsOpen** dropdown, enter the newly created variable. 

    ![](<images/notification-6-ss.png>)

1. Define the actions for the Show and Close buttons, by selecting the button widget, and on the **Properties**, from the **OnClick** dropdown select **New Client Action**.

    In this example, for the Show button we assign the ShowNotification variable to True, and for the Close button we assign the ShowNotification variable to False.

    ![](<images/notification-7-ss.png?width=800>)

1. After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property |  Description |
|---|---|
|IsOpen (Boolean): Mandatory | If True, the notification is immediately visible on screen. If False, the notification is not visible on screen. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the myclass style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
