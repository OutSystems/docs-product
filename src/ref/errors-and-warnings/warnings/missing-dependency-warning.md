---
locale: en-us
guid: 1812425b-e8ab-42e1-a32e-c6ed7dc6f2e6
app_type: traditional web apps, mobile apps, reactive web apps
---

# Missing Dependency Warning

Message
:   `Module '<module name>' uses <element type> '<element name>' that was not found in module '<producer name>'. Runtime errors may occur.`

Cause
:   Your module has a reference to an element that was not found in the producer module.

Recommendation
:   Do one of the following:

    * Check with the producer's owner to determine what the cause might be for this missing dependency.
    * Check with the Service Center administrator.
