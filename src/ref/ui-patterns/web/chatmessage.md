---
tags: runtime-traditionalweb; 
summary: Explore the features and customization options of the Chat Message UI Pattern in OutSystems 11 for Traditional Web Apps.
locale: en-us
guid: 6a62f636-ac37-4f02-8dde-b125bbb18919
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=615%3A427&mode=design&t=Cx8ecjAITJrQMvRn-1
---

# Chat Message Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of the Chat Message UI Pattern for Traditional Web Apps](images/chatmessage-2-diag.png "Chat Message Layout Diagram")

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnClick | Event triggered when the user clicks the message container.  |  False  |

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .chat-message-actions |  is--hidden|  When the server action ToggleChatActions hides the content  |
| .chat-message-actions |  is--visible|  When the server action ToggleChatActions shows the content  |


## Advanced use case

### Change Chat Message styles according to user

1. Drag a ListRecords widget into the preview with the chat users as the Source Record List.

    ![Screenshot showing the ListRecords widget with Chat Message pattern in a Traditional Web App interface](images/chatmessage-6-ss.png "Chat Message ListRecords Widget Screenshot")

1. In the ListRecords widget, drag a ChatMessage pattern.

1. In the IsRight parameter, type `If(Chat.List.Current.ChatUser.Sender, True, False)` to make the message appear on the right for the active user.

1. In the Color parameter, type `If(Chat.List.Current.ChatUser.Sender, Entities.Color.Primary, Entities.Color.Neutral3)` to change the background according to the user.

1. In the ExtendedClass property, use `If(Chat.List.Current.ChatUser.Sender, "color-neutral-0", "")` to change the color of text to white, if the background has the primary color. If the primary color is white, change the following code to `color-neutral-10`.

1. In the UserInitials pattern, set the Color parameter inside the Image placeholder to `If(Chat.List.Current.ChatUser.Sender, Entities.Color.Primary, Entities.Color.Neutral3)` in order to change the text color and to match the same conditions set above.

1. Set the IsLight parameter to `If(Chat.List.Current.ChatUser.Sender, True, False)`.

1. Publish and test.

The result would be something like this:

![Example of a Chat Message with customized styles according to the user, featuring different background and text colors](images/chatmessage-3.png "Styled Chat Message Example")

### Show/Hide actions placeholder on click

1. Drag the Chat Message Pattern into the preview.

1. Type a name for the pattern.

1. In the Events property, choose a New Screen Action for the Handler.

1. In this new action, drag the ToggleChatActions. You can find it under the Logic tab - OutSystemsUIWeb - Chat Message folder.

    ![Screenshot displaying the ToggleChatActions action within the Logic tab of the OutSystemsUIWeb environment](images/chatmessage-4-ss.png "ToggleChatActions in Logic Tab Screenshot")

1. In the WidgetId parameter, type the name of the Chat Message pattern.

1. Publish and test.

The result is something like this:

<iframe src="https://player.vimeo.com/video/996232208" width="238" height="214" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video demonstrating the show and hide actions on a Chat Message pattern upon clicking.</iframe>
