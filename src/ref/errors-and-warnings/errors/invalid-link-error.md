---
summary: Check the causes and recommendations on how to solve an Invalid Link TrueChange error.
tags:
---

# Invalid Link Error

Message
:   `'Destination' must be a screen or a screen reference in links with 'Method' set to 'Navigate'`

Cause
:   You have a [Link widget](../../lang/auto/Class.Link Widget.final.md) with the **Method** property set to `Navigate` but you set the **Destination** property to an action. If you set the **Method** property to `Navigate` because you want to navigate between screens, you must set the **Destination** property to the target Screen.

Recommendation
:   Edit the **Method** and **Destination** properties of the Link Widget according to the desired behavior:

    * If you want to navigate to another screen, keep the **Method** property to `Navigate` and set the **Destination** property to the target Screen or Screen reference.

    * If you want to execute an action submitting the end user inputs through POST HTTP method, set the **Method** property to `Submit` and the **Destination** property to the action you want to execute. This method refreshes the screen.
    
    * If you want to execute an action submitting the end user inputs asynchronously using Ajax techniques, set the **Method** property to `Ajax Submit` and the **Destination** property to the action you want to execute. This keeps the state of the screen.

---

Message
:  `Arguments of '<type>' data type are not allowed in links with 'Method' property set to 'Navigate'`

Cause
:   You have a [Link widget](../../lang/auto/Class.Link Widget.final.md) with the **Method** property set to `Navigate` having a **Destination** argument mapped to a parameter of Binary Data, Record, or List data type.

Recommendation
:   You should avoid having screen input parameters of Binary Data, Record, or List data type. If you can't avoid it, edit the Link widget and do one of the following:

    * If the parameter is optional, don't map the corresponding Destination argument.
    
    * Set the **Method** property to `Submit` or `Ajax Submit`.

---

Double-click the error line in Service Studio TrueChange to take you directly to the source of the error.
