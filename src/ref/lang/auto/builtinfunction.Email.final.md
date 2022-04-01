# Email


<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#EmailAddressCreate">EmailAddressCreate</a>(&#8203;Text, Text)</td>
<td>Returns a full email address string containing the display name (usually it's the name of the email address owner) and the email address itself. The resulting full email address may then be used in the Send Email element (action flows) or in the Send Email activity (process flows).<br/>To build a list of email addresses use the EmailAddressesConcatenate built-in function.</td>
</tr>
<tr>
<td><a href="#EmailAddressesConcatenate">EmailAddressesConcatenate</a>(&#8203;Text, Text)</td>
<td>Returns the concatenation of email addresses, or list of email addresses, into a new list of email addresses separated by a comma (','). The resulting list may then be used in the Send Email element (action flows) or in the Send Email activity (process flows).</td>
</tr>
<tr>
<td><a href="#EmailAddressValidate">EmailAddressValidate</a>(&#8203;Text)</td>
<td>Returns true if Text 'address' is a valid email address. Note that EmailAddressValidate("") returns True.<br/>This built-in function implements the validation specified by HTML5 (https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address) which has a practical approach to RFC 5322.</td>
</tr>
</tbody>
</table>

## EmailAddressCreate { #EmailAddressCreate }

Returns a full email address string containing the display name (usually it's the name of the email address owner) and the email address itself. The resulting full email address may then be used in the Send Email element (action flows) or in the Send Email activity (process flows).  
To build a list of email addresses use the EmailAddressesConcatenate built-in function.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

name
:    Type: Text. Mandatory.  
The display name of the email address which usually is the name of the email address owner as, for example, "John Smith".

email
:    Type: Text. Mandatory.  
The email address itself, for example, john.smith@example.com.

### Output

Type: Text  

### Examples

```
EmailAddressCreate("John Smith", "john.smith​@​example.com") = "John Smith" <john.smith​@example.com>
EmailAddressCreate("Mary Jones", "mary.jones​@example.com") = "Mary Jones" <mary.jones​@example.com>
```

## EmailAddressesConcatenate { #EmailAddressesConcatenate }

Returns the concatenation of email addresses, or list of email addresses, into a new list of email addresses separated by a comma (','). The resulting list may then be used in the Send Email element (action flows) or in the Send Email activity (process flows).  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

address1
:    Type: Text. Mandatory.  
The email address or email addresses list

address2
:    Type: Text. Mandatory.  
The email address or email addresses list

### Output

Type: Text  

### Examples

```
EmailAddressesConcatenate(EmailAddressCreate("John Smith", "john.smith​@example.com"), EmailAddressCreate("Mary Adams", "mary.adams​@example.com")) = "John Smith" <john.smith​@example.com>, "Mary Adams" <mary.adams​@example.com>
```

## EmailAddressValidate { #EmailAddressValidate }

Returns true if Text 'address' is a valid email address. Note that EmailAddressValidate("") returns True.  
This built-in function implements the validation specified by HTML5 (https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address) which has a practical approach to RFC 5322.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

address
:    Type: Text. Mandatory.  
The email address to validate.

### Output

Type: Boolean  

### Examples

```
EmailAddressValidate(EmailAddressCreate("John Smith", "john.smith​@example.com")) = True
EmailAddressValidate("John Smith <john.smith​@​>") = False
```

