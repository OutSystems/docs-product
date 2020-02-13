# Invalid Data Type Error

The `Invalid Data Type` error is issued in the following situations:

* `Incompatible data types in <operator> operator`
  
    You have data types that are not compatible with the operator being used.

    Check the allowed data types for that operator and use only those.

* `<data type> data type required instead of <data type>`
  
    You have the wrong data type in a property or in the operator being used.

    Check the allowed data types for the property or operator and use only those.

* `Invalid 'Null Value' data type for specified variable`
  
    You have specified an invalid null value for a the variable data type.

* `Cannot send a 'Binary Data' parameter in the request '<send in>' of a method with '<request format>' request format. Change the parameter data type or the method request format.`
  
    In a REST API method, the request format does not allow sending Binary Data in the place that is set for the parameter.
