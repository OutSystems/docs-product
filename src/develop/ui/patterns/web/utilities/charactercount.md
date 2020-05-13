---
tags: runtime-traditionalweb; 
summary: Character Count displays the number of characters left to be entered in a target input field.
---

# Character Count

> We've been working on this article. Let us know what you think. Vote now.

You can use the Character Count UI Pattern to display the number of characters a user has entered or has remaining for an onscreen text area. 

 ![](<images/charactercount-image-5.png>)

**How to use the Character Count UI Pattern**

<!---1. In Service Studio, in the Toolbox, search for `Input`. 

    The Input widget is displayed.

    ![](<images/charactercount-image-6.png>)

1. From the Toolbox, drag the Input widget onto your application’s screen.

1. On the **Properties** tab, enter a name for the Input widget, for example, CharacterCount.

    ![](<images/charactercount-image-3.png>)

1. From the **Main Flow** menu, right-click **CharacterCount**, and choose **Add Local Variable**.
 

1. Set the variable's **Data Type** to **Text**.

    ![](<images/charactercount-image-4.png>) -->

**Prerequisites:** You have created an [Input widget](<../../../../../ref/lang/auto/Class.Input Widget.final.md>) called MyInput and created a Local Variable called MyInputVariable with its Data Type set to Text.

1. In Service Studio, in the Toolbox, search for `Character Count`. 

    The Character Count widget is displayed.

    ![](<images/charactercount-image-7.png>)

1. From the Toolbox, drag the Character Count widget into the Main Content area of your application's screen.

    ![](<images/charactercount-image-8.png>)

1. On the **Properties** tab, from the **InputWidgetId** drop-down, select the Input widget Id you have already created (MyInput).

    ![](<images/charactercount-image-9.png>)

1. In the **Limit** property, enter the maximum number of characters allowed, for example, 180, and set the **IsDescending** property to True.
    
    ![](<images/charactercount-image-10.png>)

    By setting the **Limit** property to 180, the user can enter up to 180 characters, and by setting the **IsDescending** property to True, the character count will go from 180 to 0. 

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| InputWidgetId (Text): Mandatory | The Input widget name that counts the characters. <p> Examples <ul><li>_MyInput.Id_ - Counts the characters in the MyInput input widget.</li></ul> </p>|
| Limit (Integer): Mandatory  | Character count limit. This value should be the same as the maximum length of the Input widget. <p> Examples <ul><li>180 - Sets the maximum number of characters a user can enter into the Input widget to 180</li></ul> </p>|
| IsDescending (Boolean): Optional  | Defines whether the count is ascending or descending. <p> Examples <ul><li>_False_ - The count goes from 0 to the value set for the **Limit** property</li><li>_True_ - The count goes from the value set in the **Limit** property to 0. This is the default setting.</li></ul></p> |
