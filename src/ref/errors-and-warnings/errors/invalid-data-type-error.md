---
summary: Check the causes and recomendations on how to solve the different Invalid Data Type TrueChange errors.
tags:
---

# Invalid Data Type Error

Message
:   `Incompatible data types in <operator> operator`

Cause
:   The data types aren't compatible with the operator you are using.

Recommendation
:   Check the [allowed data types for the `<operator>` operator](../../logic/expressions/operators.md), and ensure you only use allowed data types in the operation.

---
  
Message
:   `<data-type-needed> data type required instead of <data-type-used>`

Cause
:   The property or operator is set with the wrong data type, `<data-type-used>`.

Recommendation
:   Set the property or operator to the correct data type, `<data-type-needed>`.

---

Message
:  `Invalid 'Null Value' data type for specified variable`

Cause
:   The **Null Value** property defined is incompatible with the **Variable** assigned to the **Input** widget.

Recommendation
:   Set **Null Value** as a value of the same data type as the **Variable** assigned to the **Input** widget. For example, if you assinged a Boolean variable to the Input set the **Null Value** as `False`.

---

Message
:   `Cannot send a 'Binary Data' parameter in the request '<send in>' of a method with '<request format>' request format. Change the parameter data type or the method request format.`

Cause
:    In a REST API method, the request format doesn't allow you to send Binary Data in the place that's set for the parameter.

Recommendation
:    Change the parameter data type or the method request format.
