---
locale: en-us
guid: a2b93961-e935-4710-9afe-8727e23b0b99
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Miscellaneous


<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#GeneratePassword">GeneratePassword</a>(&#8203;Integer, Boolean)</td>
<td>Generates and returns a password string of length 'l'. If 'alpha' is True the string can contain both digits and letters, if False the string can only contain digits. The generated password string is a random combination of letters and digits, or just digits, depending on 'alpha'.</td>
</tr>
<tr>
<td><a href="#If">If</a>(&#8203;Boolean, Generic, Generic)</td>
<td>Returns 'true_return' if 'value' is True, otherwise returns 'false_return'.<br/>The return data type of the function is the type of 'true_return' unless there's an implicit conversion from 'true_return' type to 'false_return' type.<br/>When there's no implicit type conversion an invalid data type error will occur.</td>
</tr>
<tr>
<td><a href="#IsLoadingScreen">IsLoadingScreen</a>()</td>
<td>Returns true only when invoked within a screen Preparation execution and only if the screen is loading its content. Otherwise, if the screen is just being redrawn, i.e. posted back, it returns False.</td>
</tr>
<tr>
<td><a href="#CurrentThemeIsMobile">CurrentThemeIsMobile</a>()</td>
<td>Returns true when the current web screen is using a mobile theme.</td>
</tr>
</tbody>
</table>

## GeneratePassword { #GeneratePassword }

Generates and returns a password string of length 'l'. If 'alpha' is True the string can contain both digits and letters, if False the string can only contain digits. The generated password string is a random combination of letters and digits, or just digits, depending on 'alpha'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

l
:    Type: Integer. Mandatory.  
The length of the Text string to be generated.

alpha
:    Type: Boolean. Mandatory.  
Indicates if the generated Text string can contain digits and letters or digits only.

### Output

Type: Text  

### Examples

```
GeneratePassword(10, True) = "3fgp7lzmqt"
GeneratePassword(6, False) = "038013"
```

## If { #If }

Returns 'true_return' if 'value' is True, otherwise returns 'false_return'.  
The return data type of the function is the type of 'true_return' unless there's an implicit conversion from 'true_return' type to 'false_return' type.  
When there's no implicit type conversion an invalid data type error will occur.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

value
:    Type: Boolean. Mandatory.  
The condition to be evaluated.

true_return
:    Type: Generic. Mandatory.  
The expression to be evaluated and returned when the condition is true.

false_return
:    Type: Generic. Mandatory.  
The expression to be evaluated and returned when the condition is false.

### Output

Type: Generic  

### Examples

```
If(countVar = 0, 0, 1/countVar) = 0 when countVar is 0 or 1/countVar when countVar is different from 0.
If(True, 2.34, "xpto") = "2.34"
If(False, "xpto", #2016-05-02#) = "2016-05-02"
If(False, #2015-05-02#, #2016-05-02#) = #2016-05-02#
If(False, 2.34, #2016-05-02#) = Invalid Data Type error.
```

## IsLoadingScreen { #IsLoadingScreen }

Returns true only when invoked within a screen Preparation execution and only if the screen is loading its content. Otherwise, if the screen is just being redrawn, i.e. posted back, it returns False.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: Boolean  

## CurrentThemeIsMobile { #CurrentThemeIsMobile }

Returns true when the current web screen is using a mobile theme.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: Boolean  

