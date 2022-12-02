---
summary: Available data types in OutSystems, their default values and constraints, and available built-in functions to convert them into another data type.
locale: en-us
guid: 811f5c4c-11f5-4998-87c2-d5629a8fe0a2
app_type: traditional web apps, mobile apps, reactive web apps
---

# Available Data Types

This page describes the data types available in OutSystems, their default values and constraints, and the built-in functions to convert them into another data type.

## Basic data types

Type | Default Value | Example | Comment
---|---|---|---
Binary Data | Byte array with no elements | n/a |
Boolean | false | true or false |
Currency | 0.0 | 545870.025 | See Decimal type.
Date | #1900-01-01# | #1988-08-28# | The  supported range is [#1900-01-01#, #3000-12-31#]
Time | #00:00:00# | #12:20:56# | Minimum value: #00:00:00# <br/><br/>Maximum value: #23:59:59#
Date Time | #1900-01-01 00:00:00# | #1988-08-28 23:59:59# | The supported range is [#1900-01-01 00:00:00#, #3000-12-31 23:59:59#]<br/><br/>Refer to the [additional notes](<#date-time-notes>) about the time zone conversions.
Integer | 0 | 2147483600 | Minimum value: -2^31, which is -2147483648.<br/><br/>Maximum value: 2^31-1, which is 2147483647.
Long Integer | 0 | 5645245584135987412 | Minimum value: -2^63<br/>Maximum value: 2^63-1
Decimal | 0.0 | -158121.025 <br/>4000.0 | Integer and decimal parts must be separated by a period. <br/><br/>Minimum value: -2^96 <br/><br/>Maximum value: 2^96-1<br/><br/>The maximum number of digits in the decimal part is 8.
Email | "" (empty string) | "fran.wilson@example.com" |
Phone Number | "" (empty string) | "+1 555 565 3730" |
Text | "" (empty string) | "My name is Christina Sharp." |
&lt;Entity&gt; Identifier | When an Entity is created, the &lt;Entity&gt; identifier data type is created for the identifier attribute. | |

<a id="date-time-notes"></a>**Date Time Notes**

* When you work with Date Time data type in the server, you always deal with the time zone of the server.
* Date Time in reactive and mobile apps is always UTC, even when requested from the server.
* When you use Date Time in the reactive or mobile app UI, the value is converted to the local time of the device.

Here is an example for a server that's in GMT+01 (Paris) and a mobile device in GMT-05 (New York). The mobile device requests a certain Date Time value from the server, for example `#2007-12-18 17:00:00#`. What happens is:

1. The value is converted by the server to UTC `#2007-12-18 16:00:00#` and sent to the mobile device.
1. When you store the value in the mobile app, the value is handled as UTC and saved as `#2007-12-18 16:00:00#`.
1. When you display the value in the UI, the end users see `#2007-12-18 11:00:00#`.

If you don't need this scenario in your logic, use data types Date and Time separately to deal with the respective values.

<a id="text-notes"></a>**Text Notes**

If your database is SQL Server, the length of a Text attribute represents the number of **byte-pairs** that you can store in a column of type Text, rather than the number of characters. Characters defined in the Unicode range 0-65,535 can be stored in one byte-pair. However, characters defined in higher Unicode ranges (65,536-1,114,111), such as emojis, kanji, hiragana, and katakana characters, may use two byte-pairs. This is a [limitation of SQL Server itself](https://docs.microsoft.com/en-us/sql/t-sql/data-types/nchar-and-nvarchar-transact-sql?view=sql-server-ver15#remarks).

If your application needs to store characters defined in higher Unicode ranges, you must take this into account when defining the length of a Text attribute. You must also adjust your client-side and server-side validations so that they take this into consideration.

## Compound data types

|Type|Comments|
|--- |--- |
|`<Entity>` or `<Structure>`|When an Entity or [Structure](../../../develop/data/structure-create-use.md) is created, a data type is also created with all the attributes of that Entity or Structure. For example, when the Customer entity is created, the Customer data type is created. To create a variable of this data type, simply set its **Data Type** property to `Customer`.<br/>To access an attribute of the variable, use the following syntax: `.`, for example `MyCustomerVar.Name`.|
|Object|OutSystems supports the Object data type to allow to reuse your own .NET classes. The default value is NullObject().|
|Record|A [Record](../../../develop/data/structure-create-use.md) is a data type that's composed of a fixed number of attributes, each one with its own data type. Use a Record to define a compound data type that is used for a single variable. If you need to define more than one variable with the same compound data type, use a Structure instead. Some use cases for using the Record data type are:<br/>• You need to return the result of an Aggregate on a User Action. In this case, you can define the user action output parameter using the record data type.<br/>• You need a user action that returns compound information, but don't want to define a new Structure.|
  
## Collection data types

|Type|Comments|
|--- |--- |
|List|A [List](list.md) is a sequence of elements of the same data type, either basic or compound. Elements can be inserted, fetched, and removed from a List.|
  
## Default and null values

OutSystems does not use the concept of the NULL value, except for the Entity Identifier data type. Therefore, each data type has an associated default value that is assigned at creation.

## Data type conversions

OutSystems enables the conversion between different data types. This can be made implicitly, or explicitly by using [data type conversion functions](<../../lang/auto/builtinfunction.Data Conversion.final.md>).

### Implicit conversion

OutSystems automatically converts values of the following types:

Expected Type | Accepted Types | Obs.
---|---|---
Boolean | - |
Currency | Decimal, Integer, Boolean, Entity Identifier(Integer) |
Date | Date Time |
Date Time | Date, Text, Time |
Integer | Decimal, Boolean, Currency, Entity Identifier(Integer) | When converting Decimal to Integer implicitly, the decimals are truncated.
Long Integer | Long Integer, Integer, Decimal, Boolean, Currency, Entity Identifier(Integer), Entity Identifier(Long Integer) |
Decimal | Integer, Boolean, Currency, Entity Identifier(Integer) |
Entity Identifier | Entity Identifier |  A certain Entity Identifier can be converted into another Entity's Identifier, but a warning is displayed.
Email | Text, Phone Number, Integer, Decimal, Boolean, Currency, Entity Identifier(Integer), Entity Identifier(Text), Date Time, Date, Time |
Phone Number | Text, Email, Integer, Decimal, Boolean, Currency, Entity Identifier(Integer), Entity Identifier(Text), Date Time, Date, Time |
Text | Integer, Decimal, Boolean, Currency, Phone Number, Email, Entity Identifier(Integer), Entity Identifier(Text) |

### Explicit conversion functions

To convert values from one data type to another use [data type conversion functions](<../../lang/auto/builtinfunction.Data Conversion.final.md>).

Here is a summary about the possible explicit conversions:

From | To | Function
---|---|---
 Boolean | Integer<br/>Text | [BooleanToInteger](<../../lang/auto/builtinfunction.Data Conversion.final.md#BooleanToInteger>)<br/>[BooleanToText](<../../lang/auto/builtinfunction.Data Conversion.final.md#BooleanToText>)
Date | Date Time<br/>Text | [DateToDateTime](<../../lang/auto/builtinfunction.Data Conversion.final.md#DateToDateTime>)<br/>[DateToText](<../../lang/auto/builtinfunction.Data Conversion.final.md#DateToText>)
Date Time | Date<br/>Text<br/>Time | [DateTimeToDate](<../../lang/auto/builtinfunction.Data Conversion.final.md#DateTimeToDate>)<br/>[DateTimeToText](<../../lang/auto/builtinfunction.Data Conversion.final.md#DateTimeToText>)<br/>[DateTimeToTime](<../../lang/auto/builtinfunction.Data Conversion.final.md#DateTimeToTime>)
Integer | Boolean<br/>Decimal<br/>Text<br/>Integer Identifier | [IntegerToBoolean](<../../lang/auto/builtinfunction.Data Conversion.final.md#IntegerToBoolean>)<br/>[IntegerToDecimal](<../../lang/auto/builtinfunction.Data Conversion.final.md#IntegerToDecimal>)<br/>[IntegerToText](<../../lang/auto/builtinfunction.Data Conversion.final.md#IntegerToText>)<br/>[IntegerToIdentifier](<../../lang/auto/builtinfunction.Data Conversion.final.md#IntegerToIdentifier>)
Long Integer | Long Integer Identifier<br/>Integer<br/>Text | [LongIntegerToIdentifier](<../../lang/auto/builtinfunction.Data Conversion.final.md#LongIntegerToIdentifier>)<br/>[LongIntegerToInteger](<../../lang/auto/builtinfunction.Data Conversion.final.md#LongIntegerToInteger>)<br/>[LongIntegerToText](<../../lang/auto/builtinfunction.Data Conversion.final.md#LongIntegerToText>)
Decimal | Boolean<br/>Integer<br/>Text | [DecimalToBoolean](<../../lang/auto/builtinfunction.Data Conversion.final.md#DecimalToBoolean>)<br/>[DecimalToInteger](<../../lang/auto/builtinfunction.Data Conversion.final.md#DecimalToInteger>)<br/>[DecimalToText](<../../lang/auto/builtinfunction.Data Conversion.final.md#DecimalToText>)
Entity Identifier (Integer) | Integer | [IdentifierToInteger](<../../lang/auto/builtinfunction.Data Conversion.final.md#IdentifierToInteger>)
Entity Identifier (Long Integer) |  Long Integer  | [IdentifierToLongInteger](<../../lang/auto/builtinfunction.Data Conversion.final.md#IdentifierToLongInteger>)
Entity Identifier (Text) | Text | [IdentifierToText](<../../lang/auto/builtinfunction.Data Conversion.final.md#IdentifierToText>)
Text | Date<br/>Date Time<br/>Decimal<br/>Integer<br/>Time<br/>Text Identifier | [TextToDate](<../../lang/auto/builtinfunction.Data Conversion.final.md#TextToDate>)<br/>[TextToDateTime](<../../lang/auto/builtinfunction.Data Conversion.final.md#TextToDateTime>)<br/>[TextToDecimal](<../../lang/auto/builtinfunction.Data Conversion.final.md#TextToDecimal>)<br/>[TextToInteger](<../../lang/auto/builtinfunction.Data Conversion.final.md#TextToInteger>)<br/>[TextToTime](<../../lang/auto/builtinfunction.Data Conversion.final.md#TextToTime>)<br/>[TextToIdentifier](<../../lang/auto/builtinfunction.Data Conversion.final.md#TextToIdentifier>)
Time | Text | [TimeToText](<../../lang/auto/builtinfunction.Data Conversion.final.md#TimeToText>)
Any data type | Object | [ToObject](<../../lang/auto/builtinfunction.Data Conversion.final.md#ToObject>)
