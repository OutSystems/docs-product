---
tags: runtime-traditionalweb; 
summary: Chat Message displays conversation posts in notifications or chat screens.
---

# Chat Message 

You can use the Chat Message UI Pattern to display conversational posts in notifications or chat screens. It can be used to display content such as photos, text, images, delivery times, and statuses.

![](<images/chatmessage-3.png>)

**How to use the Chat Message UI Pattern**

1. In Service Studio, in the Toolbox, search for `Chat Message`.
  
     The Chat Message widget is displayed.

    ![](<images/chatmessage-1-ss.png>)

1. To From the Toolbox, drag the Chat Message widget into the Main Content area of your application's screen. 

    ![](<images/chatmessage-2-ss.png>)

    By default, the Chat Message widget contains Image, Name, Content, and Actions placeholders.

1. Add your content to the placeholders.

After following these steps and publishing the module, you can test the pattern in your app.


## Properties

| **Property** |  **Description** | 
|---|---|
| IsRight (Boolean): Optional  | If True, the pattern is right aligned. If False, the pattern is left aligned. This is the default value.  |
| IsInline (Boolean): Optional  | If False, the chat message is displayed inside a balloon-style box. This is the default value. If True, the chat message does appear inside the balloon-style box. | 
| Color (Color Identifier): Optional  | Set the chat message background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available. <p>Examples <ul><li>_Blank_ - The background is a nuetral color (Entities.Color.Neutral3). This is the default value.</li><li>_Entities.Color.Red_ - The background color is red.</li></ul></p> |
| ExtendedClass (Text): Optional |  Add custom style classes to the Chat Message UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Chat Message UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Chat Message UI styles being applied.</li></ul></p> |

