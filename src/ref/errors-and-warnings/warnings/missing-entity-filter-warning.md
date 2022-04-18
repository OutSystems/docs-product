---
locale: en-us
guid: 0306c69d-0c0d-440f-9016-34367cda685d
app_type: traditional web apps, mobile apps, reactive web apps
---

# Missing Entity Filter Warning

Message
:   `'<entity name>' entity should be filtered in the '<process activity name>' <process activity type>`

Cause
:   Your process activity is handling an Entity Action events but has no filtering set on the entity attributes. This means that any occurring Entity Action event will be handled by your process activity in all process instances. The most common case is to have a Process Activity handling Entity Action events for the same entity as the one of the process, i.e. the entity attribute Id of the process activity is set with the entity Id input parameter of the process.

Recommendation
:   Check if your process activity has a property set with an Entity Action and set the conditions for which in the listed entity attributes.
