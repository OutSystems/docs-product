---
tags: runtime-traditionalweb; 
summary: Chat Message displays conversation posts in notifications or chat screens.
locale: en-us
guid: 2ee63ee6-02cf-4a5a-a348-92e5b46b3946
app_type: traditional web apps
platform-version: o11
---

# Chat Message

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Chat Message UI Pattern to display conversational posts in notifications or chat screens. It can be used to display content such as photos, text, images, delivery times, and statuses.

![](<images/chatmessage-3.png>)

**How to use the Chat Message UI Pattern**

For the purposes of this example, our app already contains a [form](../../../../../develop/ui/forms/form-use.md) where the user can enter their queries, and once they send their message, it will appear as a conversational post by using the Chat Message widget.

1. In Service Studio, in the Toolbox, search for `Chat Message`.
  
    The Chat Message widget is displayed.

    ![](<images/chatmessage-1-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. To From the Toolbox, drag the Chat Message widget into the Main Content area of your application's screen.

    ![](<images/chatmessage-2-ss.png>)

    By default, the Chat Message widget contains Image, Name, Content, and Actions placeholders.

1. Add the relevant content to the placeholders.

    * In this example, so that the name the user enters in the form is displayed, we convert the Name placeholder to an expression and enter the relevant logic. To do this, we right-click the Name placeholder, select **Convert to Expression**, and in the **Expression Value** pop-up, navigate to the Name attribute, and click **Done**.

        ![](<images/chatmessage-4-ss.png>)

        ![](<images/chatmessage-5-ss.png>)

    * So that the message the user enters in the form is displayed, we convert the Content placeholder to an expression and enter the relevant logic. To do this, we repeat the previous step, but this time, navigate to the Message attribute.

        ![](<images/chatmessage-8-ss.png>)

1. You can customize the Chat Message's look and feel by setting the (optional) properties on the **Properties** tab.

    ![](<images/chatmessage-9-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

The result of this example looks something like the following:

![](<images/chatmessage-6-ss.png?width=800>)

## Properties

| **Property**                       | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IsRight (Boolean): Optional        | If True, the pattern is right aligned. If False, the pattern is left aligned. This is the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| IsInline (Boolean): Optional       | If False, the chat message is displayed inside a balloon-style box. This is the default value. If True, the chat message does appear inside the balloon-style box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Color (Color Identifier): Optional | Set the chat message background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available. <p>Examples <ul><li>Blank - The background is a neutral color (Entities.Color.Neutral3). This is the default value.</li><li>Entities.Color.Red - The background color is red.</li></ul></p>                                                                                                                                                                                                                                                                                               |
| ExtendedClass (Text): Optional     | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
