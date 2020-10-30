# Invalid Property Value Error

The `Invalid Property Value` error is issued in the following situations:

* Message: `<property> must be set in <element>`
  
    * Cause: You have a mandatory property that has not been set. For example, the Destination property in a Link widget.

        ![Mandatory property not set. Link example. ](images/ref-error-invalid-property-link.png)

* `'Default Value' must be set to a <literal> literal`
  

    Edit the Default Value property of the element and set a literal value.

* Message: `'Default Value' must be set to a <literal> literal`
  
    * Cause: The Default Value property must be a literal. You cannot set the property with an expression as, for example: `1 + 1`.

        ![Literal value error](images/ref-error-literal-value.png)

    * Solution: Edit the Default Value property of the element and set a literal value.

        In all the elements (except Session Variables and Site Properties), you can use one of the following built-in functions as default value: `NullDate()`, `NullIdentifier`, `NullObject()`, `NullTextIdentifier()`, `CurrDate()`, `CurrTime()`, `CurrDateTime()`, and `NewLine()`.

  * Message: `'<property>' cannot be set to the content of a widget`
  
    * Cause: You have a Record widget that is populated with the content of another widget or the widget itself. For example a Show Record widget whose Source Record is TableRecords1.List.Current.

        ![Record widget populated with the content of another widget](images/ref-error-source-record.png)

    * Solution: Edit the Source Record or Source Record List (depending on the widget), and use a variable that is not a runtime property of any of the widgets available on the screen. You must use local variables, queries, or lists evaluated in the Screen Preparation.
