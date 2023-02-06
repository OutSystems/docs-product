---
tags: runtime-mobileandreactiveweb;  
summary: The Notification UI Pattern is a contextual short message that provides important information to the user. 
locale: en-us
guid: 90ae661d-b0d0-4001-b2b1-efe5c50bb056
app_type: mobile apps, reactive web apps
---

# Notification

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

<div class="info" markdown="1">

**This component is deprecated for versions of OutSystems UI lower than 2.8.3.** For more information on how to migrate old versions, see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).

To find out what version of OutSystems UI you are using, see [OutSystems UI version](../../intro.md#outsystems-ui-version).

</div>

The Notification UI Pattern is a contextual short message that provides important information to the user, such as app crashes, new updates, task reminders, and new messages.

**How to use the Notification UI Pattern**

1. In Service Studio, in the Toolbox, search for `Notification`.

    The Notification widget is displayed.

    ![Notification widget](<images/notification-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

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

1. Define the actions for the buttons and set the **WidgetId** to the Notification widget.

    In this example, for the **Open** button, the **On Click** event is set to a **New Client Action** that runs the **NotificationOpen** client action. For the **Close** button, the **On Click** event is set to a **New Client Action** that runs the **NotificationClose** client action.

    ![Define action for Open button](<images/notification-open-ss.png>)

    ![Define action for Close button](<images/notification-close-ss.png>)

1. You can configure the Notification by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties. For more configurations, expand the **OptionalConfigs** property.

    ![Define action for Close button](<images/notification-properties-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

![Notification example](<images/notification-example.png>)

## Properties

| Property | Description |
|---|---|
| StartsOpen(Boolean): Optional| Defines the initial state of the Notification. If True, the notification is open. Use one of the following actions to change the value afterward:<ul><li>NotificationOpen</li><li>NotificationClose</li></ul>  |
| Width(Text): Optional | Define the Notification width. Accepts any kind of unit (px, %, vw). The default width is "370px".</br>If the value defined is bigger than the screen size, the notification width will be 100%. |
| Position(Position Identifier): Optional| Define the position where the notification appears on the screen.</br></br>The predefined options are:<ul><li>Bottom</li><li>BottomLeft</li><li>BottomRight</li><li>Center</li><li>Left</li><li>Right</li><li>Top</li><li>TopLeft</li><li>TopRight</li></ul>Examples<ul><li>"Entities.Position.Right" - The notification is displayed on the right side of the screen.</li><li>"Entities.Position.Bottom" - The notification is displayed on the bottom of the screen.</li></ul> |
| OptionalConfigs(NotificationOptionalConfigs): Optional | Defines additional parameters to customize the notification behavior and functionality. |
| OptionalConfigs.InteractToClose(Boolean): Optional | Set to True to close the notification when the user clicks on it. |
| OptionalConfigs.CloseAfterTime(Integer): Optional| Define the delay time (in milliseconds) to close the notification.</br>Example: "3000" |
| ExtendedClass (Text): Optional| Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS.</br></br>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

## Events

|Event| Description  | 
|---|---|
|Initialized: Optional  | Event triggered when the Notification instance is ready. | 
|OnToggle: Optional  | Triggered when the Notification is toggled.  | 
