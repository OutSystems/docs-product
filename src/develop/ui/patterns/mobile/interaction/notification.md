---
tags: runtime-mobileandreactiveweb;  
summary: The Notification UI Pattern is a contextual short message that provides important information to the user. 
---

# Notification

The Notification UI Pattern is a contextual short message that provides important information to the user, such as app crashes, new updates, task reminders, and new messages.

**How to use the Notification UI Pattern**

1. In Service Studio, in the Toolbox, search for `Notification`.

    The Notification widget is displayed.

    ![Notifiation widget](<images/notification-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.
    
    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Notification widget into the Main Content area of your application's screen and on the **Properties** tab, enter a **Name**.

    ![Drag the Notification widget to the screen](<images/notification-dragwidget-ss.png>)

 1. Add the relevant content to the Content placeholder. 

    In this example, an icon and some text are added. 

    ![Add content to Content placeholder](<images/notification-content-ss.png>)

1. From the Toolbox, drag 2 **Button** widgets into the Main Content area of your application's screen to **Open** and **Close** the Notification. 

    ![Add Open and Close buttons](<images/notification-buttons-ss.png>)

1. In this example, for the **Open** button, the **On Click** event is set to a **New Client Action** that runs the **NotificationOpen** client action. For the **Close** button, the **On Click** event is set to a **New Client Action** that runs the **NotificationClose** client action.

    ![Define action for Open button](<images/notification-open-ss.png>)

    ![Define action for Close button](<images/notification-close-ss.png>)

1. You can configure the Notification by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties. For more configurations, expand the **OptionalConfigs** property.

    ![Define action for Close button](<images/notification-properties-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

![Notification example](<images/notification-example.png>)

## Properties

| Property |  Description |
|---|---|
|StartsOpen(Boolean): Optional | If True, the notification is immediately visible on screen. If False, the notification is not visible on screen. The default value is False. <br/> Use one of the following actions to change the value after :<ul><li>NotificationOpen</li><li>NotificationClose</li></ul> |
|Width(Text): Optional|Set the Notification width. Accepts any kind of unit (for example, px, %, vw).|
|Position(Position Identifier): Optional|Set where the notification appears on the screen. The predefined options are as follows:<ul><li>Bottom</li><li>BottomLeft</li><li>BottomRight</li><li>Center</li><li>Left</li><li>Right</li><li>Top</li><li>TopLeft</li><li>TopRight</li></ul><br/>Examples<ul><li>``Entities.Position.Right`` - The notification is displayed on the right side of the screen.</li><li>``Entities.Position.Bottom`` - The notification is displayed on the bottom of the screen.</li>|
|InteractToClose(Boolean): Optional|If True, the notification closes when the notification is clicked. |
|CloseAfterTime(Integer): Optional|Set the delay time, in ms, to close the notification.|
|ExtendedClass (Text): Optional| Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
