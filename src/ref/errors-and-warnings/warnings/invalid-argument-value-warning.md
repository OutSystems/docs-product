---
locale: en-us
guid: 36a6a5c3-e263-4d21-960a-8b7b409ad21f
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Invalid Argument Value Warning

Message
:   `Unable to validate if the ‘WebReferenceName’ argument of the action ‘<actionName>’ refers a web service consumed in your module because the name supplied is not a literal.`

Cause
:   Some actions have parameters that receive the name of Web Services consumed inside the module. The web service name you supplied is not a literal so Service Studio has no way of validating at design time if the consumed web service exists in your module.
