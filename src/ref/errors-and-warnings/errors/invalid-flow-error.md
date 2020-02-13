# Invalid Flow Error

The `Invalid Flow` error is issued in the following situations:

* `<element> must have at least one incoming connector in <flow>`
  
    You have an element in your flow that is not connected to any other element. For example, you have an Assign element in an action that is not connected to that action flow.

    Edit your flow and connect the element to one of the existing elements, otherwise that element will not be executed.

* `<element> must have <number> outgoing connector(s) in <flow>`
  
    You have an element in your flow that does not contain required outgoing connectors. For example, you have an If element with only one outgoing connector.

    Edit your flow and add the necessary outgoing connectors from the element.

Double-click on the error line to take you directly to the parent flow and highlights the particular element.