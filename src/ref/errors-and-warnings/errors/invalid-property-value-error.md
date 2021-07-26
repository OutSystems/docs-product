# Invalid Property Value Error

The `Invalid Property Value` error is issued in the following situations:

Message
:   `<property> must be set in <element>`
  
Cause
:   There's a mandatory property in `<element>` that you haven't set. For example, the **Destination** property in a Link widget.

    ![Mandatory property not set. Link example.](images/ref-error-invalid-property-link.png)

Recommendation
:   Set a value in the mandatory property.

---

Message
:   `'Default Value' must be set to a <literal> literal`

Cause
:   The **Default Value** property must be a literal. You can't set the property with an expression as, for example: `1 + 1`.

    ![Literal value error](images/ref-error-literal-value.png)

Recommendation
:   Edit the **Default Value** property of the element and set a literal value.

    In all the elements (except Session Variables and Site Properties), you can use one of the following built-in functions as default value: `NullDate()`, `NullIdentifier`, `NullObject()`, `NullTextIdentifier()`, `CurrDate()`, `CurrTime()`, `CurrDateTime()`, and `NewLine()`.
