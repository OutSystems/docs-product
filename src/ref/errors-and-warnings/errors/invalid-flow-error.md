---
locale: en-us
guid: e5f289e4-8fb1-444e-816c-faaeff668755
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=609:446
summary: OutSystems 11 (O11) troubleshooting guide for resolving invalid flow errors by ensuring proper connector configurations in action flows.
---
# Invalid Flow Error

Message
:   `<element> must have at least one incoming connector in <action-flow>`

![Screenshot illustrating an invalid flow error with a missing incoming connector in an action flow](images/invalid-flow-error-1-ss.png "Invalid Flow Error Example 1")  
     
Cause
:   You have an element in your flow that's not connected to any other element. For example, you have an End element in an action that doesn't have an incoming connector.

Recommendation
:       Edit your flow and connect the element to one of the existing elements, otherwise that element won't be executed.

![Screenshot showing how to correct an invalid flow error by connecting elements in the action flow](images/invalid-flow-error-3-ss.png "Invalid Flow Error Recommendation") 

---

Message
:   `<element> must have <number> outgoing connector(s) in <action-flow>`

![Screenshot demonstrating an invalid flow error due to insufficient outgoing connectors in an action flow](images/invalid-flow-error-2-ss.png "Invalid Flow Error Example 2") 


Cause
:   You have an element in your flow that doesn't contain the required outgoing connectors. For example, you have an If element with only one outgoing connector.

Recommendation
:        Edit your flow and add the necessary outgoing connectors from the element.

![Screenshot showing how to correct an invalid flow error by connecting elements in the action flow](images/invalid-flow-error-3-ss.png "Invalid Flow Error Recommendation") 