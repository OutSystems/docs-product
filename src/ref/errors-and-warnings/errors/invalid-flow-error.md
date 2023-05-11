---
locale: en-us
guid: e5f289e4-8fb1-444e-816c-faaeff668755
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Invalid Flow Error

Message
:   `<element> must have at least one incoming connector in <action-flow>`

![Incoming connector error](images/invalid-flow-error-1-ss.png?width=800)  
     
Cause
:   You have an element in your flow that's not connected to any other element. For example, you have an End element in an action that doesn't have an incoming connector.

Recommendation
:       Edit your flow and connect the element to one of the existing elements, otherwise that element won't be executed.

![Incoming connector error](images/invalid-flow-error-3-ss.png?width=800) 

---

Message
:   `<element> must have <number> outgoing connector(s) in <action-flow>`

![Incoming connector error](images/invalid-flow-error-2-ss.png?width=800) 


Cause
:   You have an element in your flow that doesn't contain the required outgoing connectors. For example, you have an If element with only one outgoing connector.

Recommendation
:        Edit your flow and add the necessary outgoing connectors from the element.

![Incoming connector error](images/invalid-flow-error-3-ss.png?width=800) 