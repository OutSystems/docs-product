# Incompatible Date Formats Error

The `Incompatible Date Formats` error is issued in the following situation:

* `(<consumed web service>) date format is set to (<date format>), but its (<method name>) method contains a date in (<date format>) format in its request or response examples`
  
    The example supplied for the request/response of a REST Method contains date values in a format that doesn’t correspond to the 'Date Format' defined in the REST API properties.

    To fix this, do one of the following:

    * In the REST API properties, set the 'Date Format' with the expected format.
    * In the example, change the date values to match the expected format set in the 'Date Format' property of the REST API.
