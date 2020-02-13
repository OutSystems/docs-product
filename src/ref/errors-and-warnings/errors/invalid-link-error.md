# Invalid Link Error

The `Invalid Link` error is issued in the following situations:

* `'Destination' must be a screen or a screen reference in link with 'Method' set to 'Navigate'`
  
    You have a Link widget with the Method property set to Navigate but the Destination property is set with an action. It should be a Screen because you are just navigating between Screens.

    Edit the Link widget and change one of the following properties (depending on whether you want to submit the end-user data or not): 
    
    * Set the Method property to Submit or Ajax.
    * Set the Destination property to a Screen or a Screen reference.

* `Arguments of '<type>' data type are not allowed in links with 'Method' property set to 'Navigate'`
  
    You have a Link widget with the Method property set to Navigate but the arguments map parameters of the Binary Data, Record, or List data type.

    Edit the Link widget and do one of the following: 
    
    * _(if the parameter is optional)_ Do not map the corresponding Destination argument.
    * Set the Method property to Submit or Ajax.

Double-click on the error line to take you directly to the invalid Link widget.
