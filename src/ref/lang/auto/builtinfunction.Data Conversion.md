---
---

# Data Conversion

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#BooleanToInteger">BooleanToInteger</a>(&#8203;Boolean)</td>
<td>Converts Boolean 'b' to an Integer value, either 1 if 'b' is True or 0 if 'b' is False.</td>
</tr>
<tr>
<td><a href="#BooleanToText">BooleanToText</a>(&#8203;Boolean)</td>
<td>Converts Boolean 'b' to a Text value, either "True" or "False".</td>
</tr>
<tr>
<td><a href="#DateTimeToDate">DateTimeToDate</a>(&#8203;DateTime)</td>
<td>Converts Date Time 'dt' to a Date value dropping the Time component.</td>
</tr>
<tr>
<td><a href="#DateTimeToText">DateTimeToText</a>(&#8203;DateTime)</td>
<td>Converts Date Time 'dt' to a Text value in the format specified in the environment configuration (by default, "yyyy-MM-dd HH:mm:ss").</td>
</tr>
<tr>
<td><a href="#DateTimeToTime">DateTimeToTime</a>(&#8203;DateTime)</td>
<td>Converts Date Time 'dt' to a Time value dropping the Date component.</td>
</tr>
<tr>
<td><a href="#DateToDateTime">DateToDateTime</a>(&#8203;Date)</td>
<td>Converts Date 'd' to a Date Time value, adding the Time component (#00:00:00#).</td>
</tr>
<tr>
<td><a href="#DateToText">DateToText</a>(&#8203;Date)</td>
<td>Converts Date 'd' to a Text value in the format specified in the environment configuration (by default, "yyyy-MM-dd").</td>
</tr>
<tr>
<td><a href="#DecimalToBoolean">DecimalToBoolean</a>(&#8203;Decimal)</td>
<td>Converts Decimal 'd' to a Boolean value. Decimal value of 0.0 is False. Any other value is True.</td>
</tr>
<tr>
<td><a href="#DecimalToInteger">DecimalToInteger</a>(&#8203;Decimal)</td>
<td>Converts Decimal 'd' to an Integer value.<br/>In client-side and server-side logic, the function rounds the input using the round half to even method. In Aggregate expressions the function truncates to the integer part of the input.<br/>To check if the conversion is possible you can use the DecimalToIntegerValidate function.</td>
</tr>
<tr>
<td><a href="#DecimalToIntegerValidate">DecimalToIntegerValidate</a>(&#8203;Decimal)</td>
<td>Returns true if Decimal 'd' can be converted to an Integer value.</td>
</tr>
<tr>
<td><a href="#DecimalToLongInteger">DecimalToLongInteger</a>(&#8203;Decimal)</td>
<td>Converts Decimal 'd' to a Long Integer value.<br/>In client-side and server-side logic, the function rounds the input using the round half to even method. In Aggregate expressions the function truncates to the integer part of the input.<br/>To check if the conversion is possible you can use the DecimalToLongIntegerValidate function.</td>
</tr>
<tr>
<td><a href="#DecimalToLongIntegerValidate">DecimalToLongIntegerValidate</a>(&#8203;Decimal)</td>
<td>Returns true if Decimal 'd' can be converted to a Long Integer value.</td>
</tr>
<tr>
<td><a href="#DecimalToText">DecimalToText</a>(&#8203;Decimal)</td>
<td>Converts Decimal 'd' to a Text value.</td>
</tr>
<tr>
<td><a href="#LongIntegerToInteger">LongIntegerToInteger</a>(&#8203;LongInteger)</td>
<td>Converts Long Integer 'l' to an Integer value. If 'l' is outside the boundaries of the Integer values, the function will return the Integer default value. To check if the conversion is possible you can use the LongIntegerToIntegerValidate function.</td>
</tr>
<tr>
<td><a href="#LongIntegerToIntegerValidate">LongIntegerToIntegerValidate</a>(&#8203;LongInteger)</td>
<td>Returns true if Long Integer 'l' can be converted to an Integer value.</td>
</tr>
<tr>
<td><a href="#LongIntegerToIdentifier">LongIntegerToIdentifier</a>(&#8203;LongInteger)</td>
<td>Converts Long Integer 'l' to a Long Integer Identifier.</td>
</tr>
<tr>
<td><a href="#LongIntegerToText">LongIntegerToText</a>(&#8203;LongInteger)</td>
<td>Converts Long Integer 'l' to a Text value.</td>
</tr>
<tr>
<td><a href="#IdentifierToInteger">IdentifierToInteger</a>(&#8203;EntityReference)</td>
<td>Converts Identifier 'Id' to an Integer value.</td>
</tr>
<tr>
<td><a href="#IdentifierToLongInteger">IdentifierToLongInteger</a>(&#8203;EntityReferenceLongInteger)</td>
<td>Converts Identifier 'Id' to a Long Integer value.</td>
</tr>
<tr>
<td><a href="#IdentifierToText">IdentifierToText</a>(&#8203;EntityReferenceText)</td>
<td>Converts Identifier 'Id' to a Text value.</td>
</tr>
<tr>
<td><a href="#IntegerToBoolean">IntegerToBoolean</a>(&#8203;Integer)</td>
<td>Converts Integer 'i' to a Boolean value. Boolean value of 0 is False. Any other value is True.</td>
</tr>
<tr>
<td><a href="#IntegerToDecimal">IntegerToDecimal</a>(&#8203;Integer)</td>
<td>Converts Integer 'i' to a Decimal value.</td>
</tr>
<tr>
<td><a href="#IntegerToIdentifier">IntegerToIdentifier</a>(&#8203;Integer)</td>
<td>Converts Integer 'i' to an Integer Identifier.</td>
</tr>
<tr>
<td><a href="#IntegerToText">IntegerToText</a>(&#8203;Integer)</td>
<td>Converts Integer 'i' to a Text value.</td>
</tr>
<tr>
<td><a href="#NullDate">NullDate</a>()</td>
<td>Returns a null Date value.</td>
</tr>
<tr>
<td><a href="#NullIdentifier">NullIdentifier</a>()</td>
<td>Returns a null Identifier valid for Integer and Long Integer Identifiers.</td>
</tr>
<tr>
<td><a href="#NullObject">NullObject</a>()</td>
<td>Returns a null Object value.</td>
</tr>
<tr>
<td><a href="#NullBinary">NullBinary</a>()</td>
<td>Returns a null Binary Data value.</td>
</tr>
<tr>
<td><a href="#NullTextIdentifier">NullTextIdentifier</a>()</td>
<td>Returns a null Text Identifier.</td>
</tr>
<tr>
<td><a href="#TextToDate">TextToDate</a>(&#8203;Text)</td>
<td>Converts Text 't' to a Date value.<br/>If 't' can't be converted to a valid Date value, the function will return the Date default value. To check if the conversion is possible you can use the TextToDateValidate function.<br/>You should check the limits of the Date data type. You should also ensure that the date you type in the argument complies with the default date format (yyyy-mm-dd, yyyy/mm/dd, and yyyy.mm.dd) or the server's environment configuration. Note that, when using the date format defined in the environment configuration, the function will only accept the separator character defined in that date format. For example, if the environment date format is set to 'DD-MM-YYYY', you cannot use '/' or '.' as separators in 't'.</td>
</tr>
<tr>
<td><a href="#TextToDateTime">TextToDateTime</a>(&#8203;Text)</td>
<td>Converts Text 't' to a Date Time value.<br/>If 't' can't be converted to a valid Date Time value, the function will return a Date Time default value. To check if the conversion is possible you can use the TextToDateTimeValidate function.<br/>You should check the limits of the Date Time data type. You should also ensure that the Date Time you type in the argument complies with the default Date Time format (yyyy-mm-dd hh:mm:ss, yyyy/mm/dd hh:mm:ss, and yyyy.mm.dd hh:mm:ss) or the server's environment configuration. Note that, when using the date format defined in the environment configuration, the function will only accept the separator character defined in that date format. For example, if the environment date format is set to 'DD-MM-YYYY', you cannot use '/' or '.' as separators in 't'.</td>
</tr>
<tr>
<td><a href="#TextToDateTimeValidate">TextToDateTimeValidate</a>(&#8203;Text)</td>
<td>Returns true if Text 't' can be converted to a Date Time value.</td>
</tr>
<tr>
<td><a href="#TextToDateValidate">TextToDateValidate</a>(&#8203;Text)</td>
<td>Returns true if Text 't' can be converted to a Date value.</td>
</tr>
<tr>
<td><a href="#TextToDecimal">TextToDecimal</a>(&#8203;Text)</td>
<td>Converts Text 't' to a Decimal value. The only allowed decimal separator is "." (period).<br/>If 't' is outside the boundaries of Decimal values, the function returns the Decimal default value. However, if you use TextToDecimal in an Aggregate and 't' is outside the boundaries of Decimal values, the function throws an exception. To check if the conversion is possible, use the TextToDecimalValidate function.</td>
</tr>
<tr>
<td><a href="#TextToDecimalValidate">TextToDecimalValidate</a>(&#8203;Text)</td>
<td>Returns true if Text 't' can be converted to a Decimal value.</td>
</tr>
<tr>
<td><a href="#TextToIdentifier">TextToIdentifier</a>(&#8203;Text)</td>
<td>Converts Text 't' to a Text Identifier.</td>
</tr>
<tr>
<td><a href="#TextToInteger">TextToInteger</a>(&#8203;Text)</td>
<td>Converts Text 't' to an Integer value.<br/>If 't' is outside the boundaries of Integer values, the function returns the Integer default value. However, if you use TextToInteger in an Aggregate and 't' is outside the boundaries of Integer values, the function throws an exception. To check if the conversion is possible, use the TextToIntegerValidate function.</td>
</tr>
<tr>
<td><a href="#TextToLongInteger">TextToLongInteger</a>(&#8203;Text)</td>
<td>Converts Text 't' to a Long Integer value.<br/>If 't' is outside the boundaries of the Long Integer values the function will return a Long Integer default value. To check if the conversion is possible you can use the TextToLongIntegerValidate function.</td>
</tr>
<tr>
<td><a href="#TextToIntegerValidate">TextToIntegerValidate</a>(&#8203;Text)</td>
<td>Returns true if Text 't' can be converted to an Integer value.</td>
</tr>
<tr>
<td><a href="#TextToLongIntegerValidate">TextToLongIntegerValidate</a>(&#8203;Text)</td>
<td>Returns true if Text 't' can be converted to a Long Integer value.</td>
</tr>
<tr>
<td><a href="#TextToTime">TextToTime</a>(&#8203;Text)</td>
<td>Converts Text 't' to a Time value.<br/>If 't' can't be converted to a valid Time value, the function will return the Time default value. To check if the conversion is possible you can use the TextToTimeValidate function.<br/>You should check the limits of the Time data type. You should also ensure that the Time you type in the argument complies with the Time format (hh:mm:ss).</td>
</tr>
<tr>
<td><a href="#TextToTimeValidate">TextToTimeValidate</a>(&#8203;Text)</td>
<td>Returns true if Text 't' can be converted to a Time value.</td>
</tr>
<tr>
<td><a href="#TimeToText">TimeToText</a>(&#8203;Time)</td>
<td>Converts Time 't' to a Text value in the format "HH:mm:ss".</td>
</tr>
<tr>
<td><a href="#ToObject">ToObject</a>(&#8203;Generic)</td>
<td>Converts expression 'exp' to an Object value.</td>
</tr>
</tbody>
</table>

## BooleanToInteger { #BooleanToInteger }

Converts Boolean 'b' to an Integer value, either 1 if 'b' is True or 0 if 'b' is False.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

b
:    Type: Boolean. Mandatory.  
The value to be converted

### Output

Type: Integer  

### Examples

```
BooleanToInteger(True) = 1
BooleanToInteger(False) = 0
```

## BooleanToText { #BooleanToText }

Converts Boolean 'b' to a Text value, either "True" or "False".  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

b
:    Type: Boolean. Mandatory.  
The value to be converted

### Output

Type: Text  

### Examples

```
BooleanToText(True) = "True" 
BooleanToText(False) = "False"
```

## DateTimeToDate { #DateTimeToDate }

Converts Date Time 'dt' to a Date value dropping the Time component.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The value to be converted

### Output

Type: Date  

### Examples

```
DateTimeToDate(#2013-11-30 22:20:30#) = #2013-11-30#
```

## DateTimeToText { #DateTimeToText }

Converts Date Time 'dt' to a Text value in the format specified in the environment configuration (by default, "yyyy-MM-dd HH:mm:ss").  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The value to be converted

### Output

Type: Text  

### Examples

```
DateTimeToText(#2015-05-21 22:20:30#) = "2015-05-21 22:20:30"
DateTimeToText(#2015-05-21#) = "2015-05-21 00:00:00"
DateTimeToText(#22:20:30#) = "1900-01-01 22:20:30"
```

## DateTimeToTime { #DateTimeToTime }

Converts Date Time 'dt' to a Time value dropping the Date component.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

dt
:    Type: DateTime. Mandatory.  
The value to be converted

### Output

Type: Time  

### Examples

```
DateTimeToTime(#1982-05-21 22:20:30#) = #22:20:30#
```

## DateToDateTime { #DateToDateTime }

Converts Date 'd' to a Date Time value, adding the Time component (#00:00:00#).  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

d
:    Type: Date. Mandatory.  
The value to be converted

### Output

Type: DateTime  

### Examples

```
DateToDateTime(#2001-09-14#) = #2001-09-14 00:00:00#
```

## DateToText { #DateToText }

Converts Date 'd' to a Text value in the format specified in the environment configuration (by default, "yyyy-MM-dd").  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

d
:    Type: Date. Mandatory.  
The value to be converted

### Output

Type: Text  

### Examples

```
DateToText(#2010-05-17#) = "2010-05-17"
DateToText(#2010-05-17 22:30:32#) = "2010-05-17"
```

## DecimalToBoolean { #DecimalToBoolean }

Converts Decimal 'd' to a Boolean value. Decimal value of 0.0 is False. Any other value is True.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

d
:    Type: Decimal. Mandatory.  
The value to be converted

### Output

Type: Boolean  

### Examples

```
DecimalToBoolean(0.0) = False
DecimalToBoolean(0.05) = True
```

## DecimalToInteger { #DecimalToInteger }

Converts Decimal 'd' to an Integer value.  
In client-side and server-side logic, the function rounds the input using the round half to even method. In Aggregate expressions the function truncates to the integer part of the input.  
To check if the conversion is possible you can use the DecimalToIntegerValidate function.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

d
:    Type: Decimal. Mandatory.  
The value to be converted

### Output

Type: Integer  

### Examples

```
When used in client-side and server-side logic:
DecimalToInteger(134.2) = 134
DecimalToInteger(134.5) = 134
DecimalToInteger(133.5) = 134
DecimalToInteger(134.7) = 135
DecimalToInteger(134) = 134
DecimalToInteger(12345678999.9) = 0

When used in Aggregates:
DecimalToInteger(134.2) = 134
DecimalToInteger(134.5) = 134
DecimalToInteger(133.5) = 133
DecimalToInteger(134.7) = 134
DecimalToInteger(134) = 134
DecimalToInteger(12345678999.9) = Arithmetic Overflow Error
```

## DecimalToIntegerValidate { #DecimalToIntegerValidate }

Returns true if Decimal 'd' can be converted to an Integer value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

d
:    Type: Decimal. Mandatory.  
The value to be converted

### Output

Type: Boolean  

### Examples

```
DecimalToIntegerValidate(134.2) = True
DecimalToIntegerValidate(134.5) = True
DecimalToIntegerValidate(133.5) = True
DecimalToIntegerValidate(134.7) = True
DecimalToIntegerValidate(134) = True
DecimalToIntegerValidate(12345678999.9) = False
```

## DecimalToLongInteger { #DecimalToLongInteger }

Converts Decimal 'd' to a Long Integer value.  
In client-side and server-side logic, the function rounds the input using the round half to even method. In Aggregate expressions the function truncates to the integer part of the input.  
To check if the conversion is possible you can use the DecimalToLongIntegerValidate function.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

d
:    Type: Decimal. Mandatory.  
The value to be converted

### Output

Type: LongInteger  

### Examples

```
When used in client-side and server-side logic:
DecimalToLongInteger(134.2) = 134
DecimalToLongInteger(134.5) = 134
DecimalToLongInteger(133.5) = 134
DecimalToLongInteger(134.7) = 135
DecimalToLongInteger(134) = 134
DecimalToLongInteger(157898999999988844444.2) = 0

When used in Aggregates:
DecimalToLongInteger(134.2) = 134
DecimalToLongInteger(134.5) = 134
DecimalToLongInteger(133.5) = 133
DecimalToLongInteger(134.7) = 134
DecimalToLongInteger(134) = 134
DecimalToLongInteger(157898999999988844444.2) = Arithmetic Overflow Error
```

## DecimalToLongIntegerValidate { #DecimalToLongIntegerValidate }

Returns true if Decimal 'd' can be converted to a Long Integer value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

d
:    Type: Decimal. Mandatory.  
The value to be converted

### Output

Type: Boolean  

### Examples

```
DecimalToLongIntegerValidate(134.2) = True
DecimalToLongIntegerValidate(134.5) = True
DecimalToLongIntegerValidate(133.5) = True
DecimalToLongIntegerValidate(134.7) = True
DecimalToLongIntegerValidate(134) = True
DecimalToLongIntegerValidate(157898999999988844444.2) = False
```

## DecimalToText { #DecimalToText }

Converts Decimal 'd' to a Text value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

d
:    Type: Decimal. Mandatory.  
The value to be converted

### Output

Type: Text  

### Examples

```
DecimalToText(200.482) = "200.482"
DecimalToText(200) = "200"
```

## LongIntegerToInteger { #LongIntegerToInteger }

Converts Long Integer 'l' to an Integer value. If 'l' is outside the boundaries of the Integer values, the function will return the Integer default value. To check if the conversion is possible you can use the LongIntegerToIntegerValidate function.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

l
:    Type: LongInteger. Mandatory.  
The value to be converted

### Output

Type: Integer  

### Examples

```
LongIntegerToInteger(3000) = 3000
LongIntegerToInteger(5645245584135987412) = 0
```

## LongIntegerToIntegerValidate { #LongIntegerToIntegerValidate }

Returns true if Long Integer 'l' can be converted to an Integer value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

l
:    Type: LongInteger. Mandatory.  
The value to be converted

### Output

Type: Boolean  

### Examples

```
LongIntegerToIntegerValidate(3000) = True
LongIntegerToIntegerValidate(5645245584135987412) = False
```

## LongIntegerToIdentifier { #LongIntegerToIdentifier }

Converts Long Integer 'l' to a Long Integer Identifier.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

l
:    Type: LongInteger. Mandatory.  
The value to be converted

### Output

Type: EntityReferenceLongInteger  

### Examples

```
LongIntegerToIdentifier(5090493034304) = 5090493034304
```

## LongIntegerToText { #LongIntegerToText }

Converts Long Integer 'l' to a Text value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

l
:    Type: LongInteger. Mandatory.  
The value to be converted

### Output

Type: Text  

### Examples

```
LongIntegerToText(5092039102) = "5092039102"
```

## IdentifierToInteger { #IdentifierToInteger }

Converts Identifier 'Id' to an Integer value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

id
:    Type: EntityReference. Mandatory.  
The value to be converted

### Output

Type: Integer  

### Examples

```
IdentifierToInteger(GetUserId()) = 504 (the result may be different in your module)
```

## IdentifierToLongInteger { #IdentifierToLongInteger }

Converts Identifier 'Id' to a Long Integer value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

id
:    Type: EntityReferenceLongInteger. Mandatory.  
The value to be converted

### Output

Type: LongInteger  

### Examples

```
IdentifierToLongInteger(GetUserId()) = 30 (the result may be different in your module)
```

## IdentifierToText { #IdentifierToText }

Converts Identifier 'Id' to a Text value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

id
:    Type: EntityReferenceText. Mandatory.  
The value to be converted

### Output

Type: Text  

### Examples

```
IdentifierToText(GetUserId()) = "30" (the result may be different in your module)
```

## IntegerToBoolean { #IntegerToBoolean }

Converts Integer 'i' to a Boolean value. Boolean value of 0 is False. Any other value is True.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

i
:    Type: Integer. Mandatory.  
The value to be converted

### Output

Type: Boolean  

### Examples

```
IntegerToBoolean(10) = True
IntegerToBoolean(-10) = True
IntegerToBoolean(0) = False
```

## IntegerToDecimal { #IntegerToDecimal }

Converts Integer 'i' to a Decimal value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

i
:    Type: Integer. Mandatory.  
The value to be converted

### Output

Type: Decimal  

### Examples

```
IntegerToDecimal(200) = 200
```

## IntegerToIdentifier { #IntegerToIdentifier }

Converts Integer 'i' to an Integer Identifier.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

i
:    Type: Integer. Mandatory.  
The value to be converted

### Output

Type: EntityReference  

### Examples

```
IntegerToIdentifier(5) = 5
```

## IntegerToText { #IntegerToText }

Converts Integer 'i' to a Text value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

i
:    Type: Integer. Mandatory.  
The value to be converted

### Output

Type: Text  

### Examples

```
IntegerToText(200) = "200"
```

## NullDate { #NullDate }

Returns a null Date value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Output

Type: Date  

### Examples

```
NullDate() = #1900-01-01#
```

## NullIdentifier { #NullIdentifier }

Returns a null Identifier valid for Integer and Long Integer Identifiers.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Output

Type: EntityReference  

### Examples

```
NullIdentifier() = 0
```

## NullObject { #NullObject }

Returns a null Object value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: Object  

### Examples

```
ObjectVariable = NullObject()
```

## NullBinary { #NullBinary }

Returns a null Binary Data value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: BinaryData  

### Examples

```
BinaryDataVariable = NullBinary()
```

## NullTextIdentifier { #NullTextIdentifier }

Returns a null Text Identifier.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Output

Type: EntityReferenceText  

### Examples

```
NullTextIdentifier() = ""
```

## TextToDate { #TextToDate }

Converts Text 't' to a Date value.  
If 't' can't be converted to a valid Date value, the function will return the Date default value. To check if the conversion is possible you can use the TextToDateValidate function.  
You should check the limits of the Date data type. You should also ensure that the date you type in the argument complies with the default date format (yyyy-mm-dd, yyyy/mm/dd, and yyyy.mm.dd) or the server’s environment configuration.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

t
:    Type: Text. Mandatory.  
The value to be converted

### Output

Type: Date  

### Examples

```
TextToDate("2002-01-01") = #2002-01-01#
TextToDate("2002/01/01") = #2002-01-01#
TextToDate("2002.01.01") = #2002-01-01#
TextToDate("2002-25-01") = #1900-01-01#
TextToDate("2002/02/31") = #1900-01-01#
TextToDate("10000.01.01") = #1900-01-01#
```

## TextToDateTime { #TextToDateTime }

Converts Text 't' to a Date Time value.  
If 't' can't be converted to a valid Date Time value, the function will return a Date Time default value. To check if the conversion is possible you can use the TextToDateTimeValidate function.  
You should check the limits of the Date Time data type. You should also ensure that the Date Time you type in the argument complies with the default Date Time format (yyyy-mm-dd hh:mm:ss, yyyy/mm/dd hh:mm:ss, and yyyy.mm.dd hh:mm:ss) or the server’s environment configuration.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

t
:    Type: Text. Mandatory.  
The value to be converted

### Output

Type: DateTime  

### Examples

```
TextToDateTime("2002-01-01 01:01:01") = #2002-01-01 01:01:01#
TextToDateTime("2002/01/01 01:01:01") = #2002-01-01 01:01:01#
TextToDateTime("2002.01.01 01:01:01") = #2002-01-01 01:01:01#
TextToDateTime("20-01-01 01:01:01") = #1900-01-01 00:00:00#
TextToDateTime("date time") = #1900-01-01 00:00:00#
TextToDateTime("2002.1.1 1-1-1") = #1900-01-01 00:00:00#
TextToDateTime("2002-01-01") = #2002-01-01 00:00:00#
TextToDateTime("01-01-01") = #1900-01-01 00:00:00#
```

## TextToDateTimeValidate { #TextToDateTimeValidate }

Returns true if Text 't' can be converted to a Date Time value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

t
:    Type: Text. Mandatory.  
The value to be converted

### Output

Type: Boolean  

### Examples

```
TextToDateTimeValidate("2002-01-01 01:01:01") = True
TextToDateTimeValidate("2002/01/01 01:01:01") = True
TextToDateTimeValidate("2002.01.01 01:01:01") = True
TextToDateTimeValidate("20-01-01 01:01:01") = False
TextToDateTimeValidate("date time") = False
TextToDateTimeValidate("2002.1.1 1-1-1") = False
TextToDateTimeValidate("2002-01-01") = True
TextToDateTimeValidate("01-01-01") = False
```

## TextToDateValidate { #TextToDateValidate }

Returns true if Text 't' can be converted to a Date value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

t
:    Type: Text. Mandatory.  
The value to be converted

### Output

Type: Boolean  

### Examples

```
TextToDateValidate("2002-01-01") = True
TextToDateValidate("2002/01/01") = True
TextToDateValidate("2002.01.01") = True
TextToDateValidate("2002-25-01") = False
TextToDateValidate("2002/02/31") = False
TextToDateValidate("10000.01.01") = False
```

## TextToDecimal { #TextToDecimal }

Converts Text 't' to a Decimal value. The only allowed decimal separator is "." (period).  
If 't' is outside the boundaries of Decimal values, the function returns the Decimal default value. However, if you use TextToDecimal in an Aggregate and 't' is outside the boundaries of Decimal values, the function throws an exception. To check if the conversion is possible, use the TextToDecimalValidate function.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

t
:    Type: Text. Mandatory.  
The value to be converted

### Output

Type: Decimal  

### Examples

```
TextToDecimal("200") = 200
TextToDecimal("-200") = -200
TextToDecimal("200.482") = 200.482
TextToDecimal("-200.482") = -200.482
TextToDecimal("0.99999999") = 0.99999999
TextToDecimal("abc") = 0
```

## TextToDecimalValidate { #TextToDecimalValidate }

Returns true if Text 't' can be converted to a Decimal value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

t
:    Type: Text. Mandatory.  
The value to be converted

### Output

Type: Boolean  

### Examples

```
TextToDecimalValidate("200")	= True
TextToDecimalValidate("-200") = True
TextToDecimalValidate("200.482") = True
TextToDecimalValidate("-200.482") = True
TextToDecimalValidate("0.99999999") = True
TextToDecimalValidate("abc") = False
```

## TextToIdentifier { #TextToIdentifier }

Converts Text 't' to a Text Identifier.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

t
:    Type: Text. Mandatory.  
The value to be converted

### Output

Type: EntityReferenceText  

### Examples

```
TextToIdentifier("NEW") = 'NEW'
```

## TextToInteger { #TextToInteger }

Converts Text 't' to an Integer value.  
If 't' is outside the boundaries of Integer values, the function returns the Integer default value. However, if you use TextToInteger in an Aggregate and 't' is outside the boundaries of Integer values, the function throws an exception. To check if the conversion is possible, use the TextToIntegerValidate function.

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

t
:    Type: Text. Mandatory.  
The value to be converted

### Output

Type: Integer  

### Examples

```
TextToInteger("200") = 200
TextToInteger("-200") = -200
TextToInteger("200.482") = 0
TextToInteger("not a number") = 0
```

## TextToLongInteger { #TextToLongInteger }

Converts Text 't' to a Long Integer value.  
If 't' is outside the boundaries of the Long Integer values the function will return a Long Integer default value. To check if the conversion is possible you can use the TextToLongIntegerValidate function.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

t
:    Type: Text. Mandatory.  
The value to be converted

### Output

Type: LongInteger  

### Examples

```
TextToLongInteger("200") = 200
TextToLongInteger("-200") = -200
TextToLongInteger("56452455841359874121") = 0
TextToLongInteger("not a number") = 0
```

## TextToIntegerValidate { #TextToIntegerValidate }

Returns true if Text 't' can be converted to an Integer value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

t
:    Type: Text. Mandatory.  
The value to be converted

### Output

Type: Boolean  

### Examples

```
TextToIntegerValidate("200") = True
TextToIntegerValidate("-200") = True
TextToIntegerValidate("200.482") = False
TextToIntegerValidate("not a number") = False
```

## TextToLongIntegerValidate { #TextToLongIntegerValidate }

Returns true if Text 't' can be converted to a Long Integer value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

t
:    Type: Text. Mandatory.  
The value to be converted

### Output

Type: Boolean  

### Examples

```
TextToLongIntegerValidate("200") = True
TextToLongIntegerValidate("-200") = True
TextToLongIntegerValidate("56452455841359874121") = False
TextToLongIntegerValidate("not a number") = False
```

## TextToTime { #TextToTime }

Converts Text 't' to a Time value.  
If 't' can't be converted to a valid Time value, the function will return the Time default value. To check if the conversion is possible you can use the TextToTimeValidate function.  
You should check the limits of the Time data type. You should also ensure that the Time you type in the argument complies with the Time format (hh:mm:ss).  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

t
:    Type: Text. Mandatory.  
The value to be converted

### Output

Type: Time  

### Examples

```
TextToTime("12:12:12") = #12:12:12#
TextToTime("23:68:12") = #00:00:00#
TextToTime("0-0-0") = #00:00:00#
TextToTime("abc") = #00:00:00#
```

## TextToTimeValidate { #TextToTimeValidate }

Returns true if Text 't' can be converted to a Time value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

t
:    Type: Text. Mandatory.  
The value to be converted

### Output

Type: Boolean  

### Examples

```
TextToTimeValidate("12:12:12") = True
TextToTimeValidate("23:68:12") = False
TextToTimeValidate("0-0-0") = False
TextToTimeValidate("abc") = False
```

## TimeToText { #TimeToText }

Converts Time 't' to a Text value in the format "HH:mm:ss".  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

t
:    Type: Time. Mandatory.  
The value to be converted

### Output

Type: Text  

### Examples

```
TimeToText(#12:30:24#) = "12:30:24"
TimeToText(#2015-07-02 12:30:34#) = "12:30:34"
```

## ToObject { #ToObject }

Converts expression 'exp' to an Object value.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

exp
:    Type: Generic. Mandatory.  
The element to be converted

### Output

Type: Object  

