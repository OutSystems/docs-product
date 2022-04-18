---
locale: en-us
guid: cb5587c1-009b-4ef4-bf65-297a48c62902
app_type: traditional web apps, mobile apps, reactive web apps
---

# Format


<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#FormatCurrency">FormatCurrency</a>(&#8203;Currency, Text, Integer, Text, Text)</td>
<td>Builds a Text output of the specified Currency 'value', preceded by the currency 'symbol', using 'decimal_digits' after the decimal point. The decimal point is specified using 'decimal_separator', while the thousands can be separated with the 'group_separator'.<br/><br/>When rounding, the function behaves differently depending on where you use it:<br/><br/>- In the <b>application server</b>, it applies the method round half up (rounds to the nearest integer, 0.5 rounds up).<br/>- In <b>client-side logic</b>, it applies the method round half to even (rounds to the nearest integer, 0.5 rounds to the nearest even integer).</td>
</tr>
<tr>
<td><a href="#FormatDecimal">FormatDecimal</a>(&#8203;Decimal, Integer, Text, Text)</td>
<td>Builds a Text output of the specified Decimal 'value', using 'decimal_digits' after the decimal point. The decimal point is specified using 'decimal_separator', while the thousands can be separated with the 'group_separator'.<br/><br/>When rounding, the function behaves differently depending on where you use it:<br/><br/>- In the <b>application server</b>, it applies the method round half up (rounds to the nearest integer, 0.5 rounds up).<br/>- In <b>client-side logic</b>, it applies the method round half to even (rounds to the nearest integer, 0.5 rounds to the nearest even integer).</td>
</tr>
<tr>
<td><a href="#FormatPercent">FormatPercent</a>(&#8203;Decimal, Integer, Text)</td>
<td>Builds a Text output of the specified Decimal 'value', followed by '%' using 'decimal_digits' after the decimal point. The decimal point is specified using 'decimal_separator'.<br/><br/>When rounding, the function behaves differently depending on where you use it:<br/><br/>- In the <b>application server</b>, it applies the method round half up (rounds to the nearest integer, 0.5 rounds up).<br/>- In <b>client-side logic</b>, it applies the method round half to even (rounds to the nearest integer, 0.5 rounds to the nearest even integer).</td>
</tr>
<tr>
<td><a href="#FormatPhoneNumber">FormatPhoneNumber</a>(&#8203;Text, Integer, Integer, Integer, Text, Text, Text)</td>
<td>Builds a Text output of the specified phone number Text 'value', starting with the international separator 'int_separator', followed by the first 'int_code_digits' of 'value', then the 'area_separator', then the following 'area_code_digits' of 'value', then the 'phone_separator' and finally the following 'phone_digits' of 'value'.</td>
</tr>
<tr>
<td><a href="#FormatText">FormatText</a>(&#8203;Text, Integer, Integer, Boolean, Text)</td>
<td>Builds a Text output of the specified Text 'value', by limiting it to the specified 'max_chars' count. If 'value' has less than the 'min_chars' characters limit, enough 'padding_char' characters are added to expand the length to that limit. In this case, 'left_padding' determines where the padding should be added.</td>
</tr>
<tr>
<td><a href="#FormatDateTime">FormatDateTime</a>(&#8203;DateTime, Text)</td>
<td>Builds a Text output of the specified Date Time 'value' using the specified 'format'. Formatting pattern can be any combination of the following:<br/>Day:<br/>- d: day without leading zero;<br/>- dd: day WITH leading zero;<br/>- ddd: abbreviated day name;<br/>- dddd: full day name;<br/>Month:<br/>- M: month without leading zero;<br/>- MM: month WITH leading zero;<br/>- MMM: abbreviated month name;<br/>- MMMM: full month name;<br/>Year:<br/>- y: last one or two digits of the year;<br/>- yy: last two digits of the year;<br/>- yyyy: year;<br/>Hour:<br/>- h: hour from 0 to 12 without leading zero;<br/>- hh: hour from 0 to 12 WITH leading zero;<br/>- H: hour from 0 to 24 without leading zero;<br/>- HH: hour from 0 to 24 WITH leading zero;<br/>Minute:<br/>- m: minutes without leading zero;<br/>- mm: minutes WITH leading zero;<br/>Second:<br/>- s: seconds without leading zero;<br/>- ss: seconds WITH leading zero;<br/>AM Designator:<br/>- t: first letter of AM or PM;<br/>- tt: AM or PM.<br/><br/>If you want to output any of these characters then precede it with '\'.<br/>Changing the environment date format does not change the way the FormatDateTime function formats the dates.</td>
</tr>
</tbody>
</table>

## FormatCurrency { #FormatCurrency }

Builds a Text output of the specified Currency 'value', preceded by the currency 'symbol', using 'decimal_digits' after the decimal point. The decimal point is specified using 'decimal_separator', while the thousands can be separated with the 'group_separator'.  
  
When rounding, the function behaves differently depending on where you use it:  
  
- In the <b>application server</b>, it applies the method round half up (rounds to the nearest integer, 0.5 rounds up).  
- In <b>client-side logic</b>, it applies the method round half to even (rounds to the nearest integer, 0.5 rounds to the nearest even integer).  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

value
:    Type: Currency. Mandatory.  
The Currency value to be formatted.

symbol
:    Type: Text. Mandatory.  
The currency symbol.

decimal_digits
:    Type: Integer. Mandatory.  
The number of decimal digits.

decimal_separator
:    Type: Text. Mandatory.  
The decimal separator symbol.

group_separator
:    Type: Text. Mandatory.  
The group separator symbol.

### Output

Type: Text  

### Examples

```
FormatCurrency(1.2, "$", 1, "#", ".") = "$1#2"
FormatCurrency(1.2, "$", 3, ",", ".") = "$1,200"
FormatCurrency(1.24, "$", 1, ",", ".") = "$1,2"
FormatCurrency(1.25, "$", 1, ",", ".") = "$1,3" (in the application server) or "$1,2" (in client-side logic)
FormatCurrency(1.251, "$", 1, ",", ".") = "$1,3"
FormatCurrency(1.35, "$", 1, ",", ".") = "$1,4"
FormatCurrency(12345.67, "$", 2, ",", ".") = "$12.345,67"
FormatCurrency(-12345.67, "$", 2, ",", ".") = "$-12.345,67"
```

## FormatDecimal { #FormatDecimal }

Builds a Text output of the specified Decimal 'value', using 'decimal_digits' after the decimal point. The decimal point is specified using 'decimal_separator', while the thousands can be separated with the 'group_separator'.  
  
When rounding, the function behaves differently depending on where you use it:  
  
- In the <b>application server</b>, it applies the method round half up (rounds to the nearest integer, 0.5 rounds up).  
- In <b>client-side logic</b>, it applies the method round half to even (rounds to the nearest integer, 0.5 rounds to the nearest even integer).  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

value
:    Type: Decimal. Mandatory.  
The Decimal value to be formatted.

decimal_digits
:    Type: Integer. Mandatory.  
The number of decimal digitis.

decimal_separator
:    Type: Text. Mandatory.  
The decimal separator symbol.

group_separator
:    Type: Text. Mandatory.  
The group separator symbol.

### Output

Type: Text  

### Examples

```
FormatDecimal(1.2, 1, "#", ".") = "1#2"
FormatDecimal(1.2, 3, ",", ".") = "1,200"
FormatDecimal(1.24, 1, ",", ".") = "1,2"
FormatDecimal(1.25, 1, ",", ".") = "1,3" (in the application server) or "1,2" (in client-side logic)
FormatDecimal(1.251, 1, ",", ".") = "1,3"
FormatDecimal(1.35, 1, ",", ".") = "1,4"
FormatDecimal(12345.67, 2, ",", ".") = "12.345,67"
FormatDecimal(-12345.67, 2, ",", ".") = "-12.345,67"
```

## FormatPercent { #FormatPercent }

Builds a Text output of the specified Decimal 'value', followed by '%' using 'decimal_digits' after the decimal point. The decimal point is specified using 'decimal_separator'.  
  
When rounding, the function behaves differently depending on where you use it:  
  
- In the <b>application server</b>, it applies the method round half up (rounds to the nearest integer, 0.5 rounds up).  
- In <b>client-side logic</b>, it applies the method round half to even (rounds to the nearest integer, 0.5 rounds to the nearest even integer).  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

value
:    Type: Decimal. Mandatory.  
The Decimal value to format as a percentage.

decimal_digits
:    Type: Integer. Mandatory.  
The number of decimal digits to use.

decimal_separator
:    Type: Text. Mandatory.  
The symbol to use as decimal separator.

### Output

Type: Text  

### Examples

```
FormatPercent(0.12, 3, "#") = "12#000%"
FormatPercent(0.124, 0, ",") = "12%"
FormatPercent(0.125, 0, ",") = "13%" (in the application server) or "12%" (in client-side logic)
FormatPercent(0.1251, 0, ",") = "13%"
FormatPercent(0.135, 0, ",") = "14%"
FormatPercent(12345.6789, 2, ",") = "1234567,89%"
FormatPercent(-12345.6789, 2, ",") = "-1234567,89%"
```

## FormatPhoneNumber { #FormatPhoneNumber }

Builds a Text output of the specified phone number Text 'value', starting with the international separator 'int_separator', followed by the first 'int_code_digits' of 'value', then the 'area_separator', then the following 'area_code_digits' of 'value', then the 'phone_separator' and finally the following 'phone_digits' of 'value'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

value
:    Type: Text. Mandatory.  
The phone number to be formatted.

int_code_digits
:    Type: Integer. Mandatory.  
The number of digits composing the international code.

area_code_digits
:    Type: Integer. Mandatory.  
The number of digits composing the area code.

phone_digits
:    Type: Integer. Mandatory.  
The number of digitis composing the phone number without international or area codes.

int_separator
:    Type: Text. Mandatory.  
The symbol for the international code.

area_separator
:    Type: Text. Mandatory.  
The symbol to use as separator between the international code and the area code.

phone_separator
:    Type: Text. Mandatory.  
The symbol to use as separator between the area code and the phone number.

### Output

Type: Text  

### Examples

```
FormatPhoneNumber("351214153737", 3, 2, 7, "+", "-", ".") = "+351-21.4153737"
```

## FormatText { #FormatText }

Builds a Text output of the specified Text 'value', by limiting it to the specified 'max_chars' count. If 'value' has less than the 'min_chars' characters limit, enough 'padding_char' characters are added to expand the length to that limit. In this case, 'left_padding' determines where the padding should be added.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

value
:    Type: Text. Mandatory.  
The Text to be formatted.

min_chars
:    Type: Integer. Mandatory.  
The minimum number of characters in the output.

max_chars
:    Type: Integer. Mandatory.  
The maximum number of characters in the output.

left_padding
:    Type: Boolean. Mandatory.  
Indicates in which side the Text is padded.

padding_char
:    Type: Text. Mandatory.  
The character to use for padding the string to the minimum length.

### Output

Type: Text  

### Examples

```
FormatText("123456789", 3, 9, True, "#") = "123456789"
FormatText("123456789876", 3, 9, True, "#") = "456789876"
FormatText("123456789876", 3, 9, False, "#") = "123456789"
FormatText("12345", 10, 20, True, "#") = "#####12345"
FormatText("12345", 10, 20, False, "#") = "12345#####"
```

## FormatDateTime { #FormatDateTime }

Builds a Text output of the specified Date Time 'value' using the specified 'format'. Formatting pattern can be any combination of the following:  
Day:  
- d: day without leading zero;  
- dd: day WITH leading zero;  
- ddd: abbreviated day name;  
- dddd: full day name;  
Month:  
- M: month without leading zero;  
- MM: month WITH leading zero;  
- MMM: abbreviated month name;  
- MMMM: full month name;  
Year:  
- y: last one or two digits of the year;  
- yy: last two digits of the year;  
- yyyy: year;  
Hour:  
- h: hour from 0 to 12 without leading zero;  
- hh: hour from 0 to 12 WITH leading zero;  
- H: hour from 0 to 24 without leading zero;  
- HH: hour from 0 to 24 WITH leading zero;  
Minute:  
- m: minutes without leading zero;  
- mm: minutes WITH leading zero;  
Second:  
- s: seconds without leading zero;  
- ss: seconds WITH leading zero;  
AM Designator:  
- t: first letter of AM or PM;  
- tt: AM or PM.  
  
If you want to output any of these characters then precede it with '\'.  
Changing the environment date format does not change the way the FormatDateTime function formats the dates.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

value
:    Type: DateTime. Mandatory.  
The Date Time to be formatted.

format
:    Type: Text. Mandatory.  
The formatting pattern.

### Output

Type: Text  

### Examples

```
FormatDateTime(#2015-06-09 10:05:20#, "ddd, dd MMM yyyy") = "Tue, 09 Jun 2015"
FormatDateTime(CurrDateTime(),"To\da\y i\s: dddd") = "Today is: Tuesday"
```

