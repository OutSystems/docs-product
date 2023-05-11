---
tags: runtime-traditionalweb; 
summary: Character Count displays the number of characters left to be entered in a target input field.
locale: en-us
guid: 35ae7f29-b021-4f09-a081-66c668b816e4
app_type: traditional web apps
platform-version: o11
---

# Character Count

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Character Count UI Pattern to display the number of characters a user has entered or has remaining for an onscreen text area. 

![](<images/charactercount-5-ss.png>)

**How to use the Character Count UI Pattern**

**Prerequisites:** You have created an [Input widget](<../../../../../ref/lang/auto/class-input-widget.md>) called MyInput and created a Local Variable called MyInputVariable with its Data Type set to Text.

1. In Service Studio, in the Toolbox, search for `Character Count`.

    The Character Count widget is displayed.

    ![](<images/charactercount-7-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Character Count widget into the Main Content area of your application's screen.

    ![](<images/charactercount-8-ss.png>)

1. On the **Properties** tab, from the **InputWidgetId** drop-down, select the Input widget Id you have already created (MyInput).

    ![](<images/charactercount-9-ss.png>)

1. In the **Limit** property, enter the maximum number of characters allowed, for example, 180, and set the **IsDescending** property to True.

    ![](<images/charactercount-10-ss.png>)

    By setting the **Limit** property to 180, the user can enter up to 180 characters, and by setting the **IsDescending** property to True, the character count will go from 180 to 0.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                         | Description                                                                                                                                                                                                                                                                          |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| InputWidgetId (Text): Mandatory  | The Input widget name that counts the characters. <p> Examples <ul><li>MyInput.Id - Counts the characters in the MyInput input widget.</li></ul> </p>                                                                                                                                |
| Limit (Integer): Mandatory       | Character count limit. This value should be the same as the maximum length of the Input widget. <p> Examples <ul><li>180 - Sets the maximum number of characters a user can enter into the Input widget to 180</li></ul> </p>                                                        |
| IsDescending (Boolean): Optional | Defines whether the count is ascending or descending. <p> Examples <ul><li>_False_ - The count goes from 0 to the value set for the **Limit** property</li><li>_True_ - The count goes from the value set in the **Limit** property to 0. This is the default setting.</li></ul></p> |
