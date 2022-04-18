---
locale: en-us
guid: a6f3ed0c-94af-4c2a-9083-80ff50ca3083
app_type: traditional web apps, mobile apps, reactive web apps
---

# Unused Callback Error

The `Unused Callback` error is issued in the following situation:

* `(<callback action name>) is not used by (<REST API name>) REST API`

    You have a callback for simple customizations in the REST API but is not being used.

    Use the 'On Before Request' or 'On After Request' properties of the REST API to set the callback action, or delete the callback action.
