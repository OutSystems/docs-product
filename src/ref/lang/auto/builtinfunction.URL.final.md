---
locale: en-us
guid: ee8d9725-b38d-4d95-8294-71e7d838ee7b
---

# URL


<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#AddPersonalAreaToURLPath">AddPersonalAreaToURLPath</a>(&#8203;Text)</td>
<td>Returns a string where the Personal Area is added (if applicable) to the URL path set in Text 't' input parameter. This function enables you to run any page (or resource) of your module in the Personal Area without having to manually change their paths.<br/>This function adds the Personal Area of the developer that is running the module to the URL path provided by the input parameter.</td>
</tr>
<tr>
<td><a href="#GetBookmarkableURL">GetBookmarkableURL</a>()</td>
<td>Returns the URL of the screen that is currently being processed.<br/>The URL returned by this function is a complete URL with the format http://server/module/personal_area/screen?param1=value&amp;param2=value... <br/>Parameters and their values aren't included when parameters are optional and their values aren't set.</td>
</tr>
<tr>
<td><a href="#GetPersonalAreaName">GetPersonalAreaName</a>()</td>
<td>Returns the name of the Personal Area where the module is currently running.</td>
</tr>
<tr>
<td><a href="#GetOwnerURLPath">GetOwnerURLPath</a>()</td>
<td>Returns the URL path of the module that owns the element that is being processed. Note that this function does not return the complete URL but only the component containing the location of the resource within the domain and, if applicable, the personal area.</td>
</tr>
<tr>
<td><a href="#GetExceptionURL">GetExceptionURL</a>()</td>
<td>Returns the absolute URL of the screen where the last exception was raised.</td>
</tr>
</tbody>
</table>

## AddPersonalAreaToURLPath { #AddPersonalAreaToURLPath }

Returns a string where the Personal Area is added (if applicable) to the URL path set in Text 't' input parameter. This function enables you to run any page (or resource) of your module in the Personal Area without having to manually change their paths.  
This function adds the Personal Area of the developer that is running the module to the URL path provided by the input parameter.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

url
:    Type: Text. Mandatory.  
The url to add the personal area path to.

### Output

Type: Text  

### Examples

```
Consider that Dave Lauper is running the Customers module in his Personal Area and that his username is 'dlauper':
AddPersonalAreaToURLPath("/Customers/ListCustomers.aspx") = "/Customers/dlauper/ListCustomers.aspx"
AddPersonalAreaToURLPath("http://myserverat.outsystemscloud.com/Customers/ListCustomers.aspx") = "http://myserverat.outsystemscloud.com/Customers/dlauper/ListCustomers.aspx"

In this next example the same developer is running the module in the public area:
AddPersonalAreaToURLPath("/Customers/ListCustomers.aspx") = "/Customers/ListCustomers.aspx"
```

## GetBookmarkableURL { #GetBookmarkableURL }

Returns the URL of the screen that is currently being processed.  
The URL returned by this function is a complete URL with the format http://server/module/personal_area/screen?param1=value&amp;param2=value...   
Parameters and their values aren't included when parameters are optional and their values aren't set.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
GetBookmarkableURL() = "http://myserverat.outsystemscloud.com/Customers/EditCustomer.aspx?CustomerId=1"
```

## GetPersonalAreaName { #GetPersonalAreaName }

Returns the name of the Personal Area where the module is currently running.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
Consider that Dave Lauper is running the Customers module in his Personal Area and that his username is 'dlauper':
GetPersonalAreaName() = "dlauper"
```

## GetOwnerURLPath { #GetOwnerURLPath }

Returns the URL path of the module that owns the element that is being processed. Note that this function does not return the complete URL but only the component containing the location of the resource within the domain and, if applicable, the personal area.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
GetOwnerURLPath() = "/Customers/"
```

## GetExceptionURL { #GetExceptionURL }

Returns the absolute URL of the screen where the last exception was raised.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
GetExceptionURL() = "http://myserverat.outsystemscloud.com/Customers/ListCustomers.aspx"
```

