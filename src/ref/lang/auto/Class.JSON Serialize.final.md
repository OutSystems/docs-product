---
kinds: ServiceStudio.Model.Nodes+JSONSerialize+Kind
helpids: 30002
locale: en-us
guid: a1cf5074-f5ba-48cf-a229-206358fd55c0
---

# JSON Serialize

JSON Serialize converts the following data types to JSON data-interchange format text:

* Record
* List of Records

## Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Mandatory</th>
<th>Default value</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Data">Data</td>
<td>Record or List with the data to be serialized to a JSON string.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Serialize Default Values">Serialize Default Values</td>
<td>Set to Yes to serialize non-mandatory JSON attributes with a default value set.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Date Format">Date Format</td>
<td>Date format used in the JSON string.</td>
<td>Yes</td>
<td>2014-01-01T00:00:00Z (ISO)</td>
<td></td>
</tr>
</tbody>
</table>

## Runtime Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Read Only</th>
<th>Type</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td>JSON</td>
<td>String in JSON format.</td>
<td></td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

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

