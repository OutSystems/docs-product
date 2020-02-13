# Unused Callback Error

The `Unused Callback` error is issued in the following situation:

* `(<callback action name>) is not used by (<REST API name>) REST API`

    You have a callback for simple customizations in the REST API but is not being used.

    Use the 'On Before Request' or 'On After Request' properties of the REST API to set the callback action, or delete the callback action.
