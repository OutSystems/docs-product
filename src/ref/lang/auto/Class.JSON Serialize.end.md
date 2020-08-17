## Additional notes { #notes }

These are additional notes about JSON Serialize.

## Large numbers

You may run into issues when running JSON Serialize/Deserialize on the client side (for example, in a Client Action) involving large Long Integer or Decimal values, namely values larger than 9007199254740991.

When the serialization/deserialization operation occurs in the server context, the .NET limits apply. However, when running these operations in JavaScript on the client side, the JavaScript limits apply.

JavaScript has a limit when using a Long Integer or Decimal values defined as [`MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER) with the value 9007199254740991. Performing a JSON serialization/deserialization operation involving Long Integer or Decimal values larger than `MAX_SAFE_INTEGER` issues an error.

To support higher numbers in JavaScript (for example, when using a variable of type Long Integer or Decimal), the platform converts the numbers to strings using a custom serialization method. This way, all the platform's internal communications between client and server use strings and not numbers.

You can use the same mechanism used by the platform to serialize/deserialize a number value exceeding `MAX_SAFE_INTEGER`. To do this, execute the JSON serialization/deserialization operation inside a Server Action and not in the client side.

## Serializing default values

If you set **Serialize Default Values** to **Yes**, and you leave the default values empty, the resulting JSON has the JSON equivalents of the [default platform values](../../data/database/default-values-on-database.md). For example:

* Empty Boolean converts to **false**
* Empty Integer converts to **0**
* Empty DateTime converts to **1900-01-01T00:00:00**