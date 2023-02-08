---
summary: Check the causes and recommendations on how to solve Invalid Link TrueChange errors.
tags:
locale: en-us
guid: 5debccff-1599-4aa2-9c84-3b2732758e6a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---
 
# Invalid Link Error

Message
:   `'Destination' must be a screen or a screen reference in links with 'Method' set to 'Navigate'`

Cause
:   You have a [Link widget](../../lang/auto/Class.Link Widget.final.md) with the **Method** property set to `Navigate` but you set the **Destination** property to an action. If you set the **Method** property to `Navigate` because you want to navigate between screens, you must set the **Destination** property to the target Screen.

Recommendation
:   Edit the **Method** and **Destination** properties of the Link widget according to the desired behavior:

    * If you want to navigate to another screen, keep the **Method** property to `Navigate` and set the **Destination** property to the target Screen or Screen reference.
 
    * If you want to execute an action submitting the end user inputs through POST HTTP method, set the **Method** property to `Submit` and the **Destination** property to the action you want to execute. This method refreshes the screen.
    
    * If you want to execute an action submitting the end user inputs asynchronously using Ajax techniques, set the **Method** property to `Ajax Submit` and the **Destination** property to the action you want to execute. This keeps the state of the screen.

---

Message
:  `Arguments of '<type>' data type are not allowed in links with 'Method' property set to 'Navigate'`

Cause
:   You have a [Link widget](../../lang/auto/Class.Link Widget.final.md) with the **Method** property set to `Navigate` having a **Destination** argument set to a parameter of Binary Data, Record, or List data type.

Recommendation
:   Edit the Link widget and do one of the following:

    * If the parameter is optional, don't set any value for the corresponding Destination argument.
    
    * Set the **Method** property to `Submit` or `Ajax Submit`.
