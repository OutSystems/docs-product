# Invalid Property Value Error

The `Invalid Property Value` error is issued in the following situations:

* `<property> must be set in <element>`
  
    You have a mandatory property that has not been set. For example, the Destination property in a Link widget.

    Set a value in the mandatory property.

* `'Default Value' must be set to a <literal> literal`
  
    The Default Value property must be a literal. You cannot set the property with an expression as, for example: 1 + 1.

    Edit the Default Value property of the element and set a literal value.

    In all the elements (except Session Variables and Site Properties), you can use one of the following built-in functions as default value: `NullDate()`, `NullIdentifier`, `NullObject()`, `NullTextIdentifier()`, `CurrDate()`, `CurrTime()`, `CurrDateTime()`, and `NewLine()`.

* `<function> is not supported as default value in <element>`
  
    You have a Session Variable or a Site Property with a function in the Default Value.

    Edit the session variable or the site property and use a literal value in the Default Value property.

* `'<Property>' must be set in pixels ('px') or percentage`

    The value of a property must be in pixels or percentage. This occurs, for example, with the Width property of a table.

    Edit the property and append its value with px or %. If no measure is defined, Service Studio considers px.

* `<property> no longer set in <element>`
  
    You have a mandatory property for which the value is no longer available or is invalid. For example, an Execute Action whose Action property does not have a value due to a Merge operation between modules or because the action to execute was deleted. This message usually appears when the property is read-only and you cannot set it directly in the element.

    To solve this error you must replace the element with a new element. For example, delete the Execute Action and add another one.

  * `'<property>' cannot be set to the content of a widget`
  
    You have a Record widget that is populated with the content of another widget or the widget itself. For example a Show Record widget whose Source Record is TableRecords1.List.Current.

    Edit the Source Record or Source Record List (depending on the widget), and use a variable that is not a runtime property of any of the widgets available on the screen. You must use local variables, queries, or lists evaluated in the Screen Preparation.

* `Property '[Name in Request/Name in Response]' has characters that are invalid when the '[Send In / Receive In]' is set to 'Header'. Make sure you only use valid header characters`
  
    You receive this error because the 'Name in Request'/'Name in Response' property contains characters that are not valid for an HTTP request header. 
    
    To solve this error, use valid characters only:

    * Uppercase and lowercase letters: `A-Z`, `a-z`
    * Digits: `0-9`
    * These special characters: `! # $ % & * + \- . ~ | _ ^`

    Alternatively you can change the value of the 'Send In' or 'Receive In' property, to send the parameter in the HTTP request body, or in the URL.

Double-click on the error line to take you directly to the mismatched property.
