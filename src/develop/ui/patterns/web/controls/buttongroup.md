---
tags: runtime-traditionalweb; 
summary: Button Group displays available choices to the user.
---

# Button Group

You can use the Button Group UI Pattern to display radio button choices to the user. This pattern is ideal when you have between two to four options. To show a larger number of options, consider using a the Dropdown UI Pattern.

**How to use the Button Group UI Pattern**

1. In Service Studio, in the Toolbox, search for `Button Group`.

    The Button Group widget is displayed.

    ![](<images/buttongroup-image-1.png>)

1. From the Toolbox, drag the Button Group widget into the Main Content area of your application's screen.

     ![](<images/buttongroup-image-2.png>)

    By default, the pattern contains 3 Button Group Items. You can add or delete as many Button Group Items as required.

1. From the Widget Tree, select the **radio-button** element, and on the **Properties** tab, set the **Variable** and **Value** properties.

    ![](<images/buttongroup-image-3.png>)

1. Change the text in the label of the ButtonGroupItems.

## Properties

| **Property** |  **Description** | 
|---|---|
| IsJustified (Boolean): Optional  | If True, the Button Group items are evenly distributed in the space available. If False, the Button Group items are left aligned. This is the default. |

