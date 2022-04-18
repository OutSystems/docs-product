---
locale: en-us
guid: 88c149c0-76f4-49ab-b7ad-328a35be02ea
app_type: traditional web apps, mobile apps, reactive web apps
---

# Math


<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#Abs">Abs</a>(&#8203;Decimal)</td>
<td>Returns the absolute value (unsigned magnitude) of the decimal number 'n'.</td>
</tr>
<tr>
<td><a href="#Mod">Mod</a>(&#8203;Decimal, Decimal)</td>
<td>Returns the remainder of decimal division of 'n' by 'm'.</td>
</tr>
<tr>
<td><a href="#Power">Power</a>(&#8203;Decimal, Decimal)</td>
<td>Returns 'n' raised to the power of 'm'.</td>
</tr>
<tr>
<td><a href="#Round">Round</a>(&#8203;Decimal, Integer)</td>
<td>Returns the Decimal number 'n' rounded to a specific number of 'fractional digits'.<br/>The round method applied depends on where the function is used:<br/>- In <b>expressions in client-side and server-side logic</b>, applies the method round half to even (rounds to the nearest integer, 0.5 rounds to the nearest even integer).<br/>- In aggregates that query <b>SQL Server or Oracle databases</b>, applies the method round half away from 0 (rounds to the nearest integer, 0.5 rounds the number further away from 0).<br/>- In aggregates that query <b>iDB2 databases</b>, applies the method round half up (rounds to the nearest integer, 0.5 rounds up).</td>
</tr>
<tr>
<td><a href="#Sqrt">Sqrt</a>(&#8203;Decimal)</td>
<td>Returns the square root of the Decimal number 'n'.</td>
</tr>
<tr>
<td><a href="#Trunc">Trunc</a>(&#8203;Decimal)</td>
<td>Returns the Decimal number 'n' truncated to integer removing the decimal part of 'n'.</td>
</tr>
</tbody>
</table>

## Abs { #Abs }

Returns the absolute value (unsigned magnitude) of the decimal number 'n'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

n
:    Type: Decimal. Mandatory.  
The number to extract the absolute value from.

### Output

Type: Decimal  

### Examples

```
Abs(-10.89) = 10.89
```

## Mod { #Mod }

Returns the remainder of decimal division of 'n' by 'm'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

n
:    Type: Decimal. Mandatory.  
The dividend in the modulo operation.

m
:    Type: Decimal. Mandatory.  
The divisor in the modulo operation.

### Output

Type: Decimal  

### Examples

```
Mod(10, 3) = 1
Mod(4, 3.5) = 0.5
```

## Power { #Power }

Returns 'n' raised to the power of 'm'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

n
:    Type: Decimal. Mandatory.  
The base value.

m
:    Type: Decimal. Mandatory.  
The exponent value.

### Output

Type: Decimal  

### Examples

```
Power(100, 2) = 10000
Power(-10.89, 2.3) = 0
Power(-10.89, -5) = -6.52920946044017E-06
```

## Round { #Round }

Returns the Decimal number 'n' rounded to a specific number of 'fractional digits'.  
The round method applied depends on where the function is used:  
- In <b>expressions in client-side and server-side logic</b>, applies the method round half to even (rounds to the nearest integer, 0.5 rounds to the nearest even integer).  
- In aggregates that query <b>SQL Server or Oracle databases</b>, applies the method round half away from 0 (rounds to the nearest integer, 0.5 rounds the number further away from 0).  
- In aggregates that query <b>iDB2 databases</b>, applies the method round half up (rounds to the nearest integer, 0.5 rounds up).  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

n
:    Type: Decimal. Mandatory.  
The Decimal number to round

fractionalDigits
:    Type: Integer.  
Use it to specify the number of fractional digits that n has to be rounded to. The default value is 0. Note: In aggregates this parameter is not specified.

### Output

Type: Decimal  

### Examples

```
When used in expressions in client-side and server-side logic:
Round(-10.89) = -11
Round(-5.5) = -6
Round(9.3) = 9
Round(2.5) = 2
Round(3.5) = 4
Round(9.123456789, 5) = 9.12346

When used in aggregates that query SQL Server or Oracle database:
Round(-10.89) = -11
Round(-5.5) = -6
Round(9.3) = 9
Round(2.5) = 3
Round(3.5) = 4

When used in aggregates that query iDB2 database:
Round(-10.89) = -11
Round(-5.5) = -5
Round(9.3) = 9
Round(2.5) = 3
Round(3.5) = 4
```

## Sqrt { #Sqrt }

Returns the square root of the Decimal number 'n'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

n
:    Type: Decimal. Mandatory.  
The number to calculate the square root from.

### Output

Type: Decimal  

### Examples

```
Sqrt(2.3) = 1.51657508881031
```

## Trunc { #Trunc }

Returns the Decimal number 'n' truncated to integer removing the decimal part of 'n'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

n
:    Type: Decimal. Mandatory.  
The number to truncate.

### Output

Type: Decimal  

### Examples

```
Trunc(-10.89) = -10
Trunc(7.51) = 7
```

