---
locale: en-us
guid: f4d76631-b342-403c-bbfc-516c9b53f250
---

# Email

|Name|Description|
|--- |--- |
|[EmailAddressCreate](#emailaddresscreate--emailaddresscreate)(​Text, Text)|Returns a full email address string containing the display name (usually it's the name of the email address owner) and the email address itself. The resulting full email address may then be used in the Send Email element (action flows) or in the Send Email activity (process flows).To build a list of email addresses use the EmailAddressesConcatenate built-in function.|
|[EmailAddressesConcatenate](#emailaddressesconcatenate--emailaddressesconcatenate)(​Text, Text)|Returns the concatenation of email addresses, or list of email addresses, into a new list of email addresses separated by a comma (','). The resulting list may then be used in the Send Email element (action flows) or in the Send Email activity (process flows).|
|[EmailAddressValidate](#emailaddressvalidate--emailaddressvalidate)(​Text)|Returns true if Text 'address' is a valid email address. Note that EmailAddressValidate("") returns True.This built-in function implements the validation specified by HTML5 (https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address) which has a practical approach to RFC 5322.|

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

