---
summary: OutSystems 11 (O11) provides a comprehensive HTTPRequestHandler API for managing HTTP requests and responses across various application types.
tags: http, api management, web development, header manipulation, response customization
locale: en-us
guid: 762585b4-510c-4749-b5d9-646e1c46f2e0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# HTTPRequestHandler API


Provides actions to manipulate HTTP Requests and Responses.

## Summary

Action | Description | App type
---|---|---
[AddAttributeToHtmlTag](<#AddAttributeToHtmlTag>) | Adds an attribute to the outermost HTML tag of the document (e.g. xmlns, manifest...).<br/>This method has no effect in Ajax Requests. | Applies to Traditional Web apps only. 
[AddFaviconTag](<#AddFaviconTag>) | Allows setting the favicon for the current page. You can use &quot;omlresources&quot; to add an icon file to your oml.<br/>This method has no effect in Ajax Requests. | Applies to Traditional Web apps only.  
[AddHeader](<#AddHeader>) | Adds a header to the current HTTP response.<br/>This method has no effect in Ajax Requests. |Applies to all app types.
[AddJavaScriptTag](<#AddJavaScriptTag>) | Adds a `<script>` tag to the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests. | Applies to Traditional Web apps only.
[AddLinkTag](<#AddLinkTag>) | Adds a `<link>` tag to the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests.| Applies to Traditional Web apps only.  
[AddMetaHttpEquivTag](<#AddMetaHttpEquivTag>) | Adds a `<meta>` tag with the http-equiv attribute to the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests. | Applies to Traditional Web apps only.  
[AddMetaTag](<#AddMetaTag>) | Adds a `<meta>` tag to the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests.| Applies to Traditional Web apps only.
[AddPostProcessingFilter](<#AddPostProcessingFilter>) | This method has no effect in Ajax Requests.<br/>Not implemented in Java. | Applies to Traditional Web apps only.  
[AddSessionToURL](<#AddSessionToURL>) | Adds the current session identifier to a specified URL. | Applies to Traditional Web apps only.  
[AddStyleSheetTag](<#AddStyleSheetTag>) | Adds a `<link rel="stylesheet">` tag to the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests. | Applies to Traditional Web apps only.  
[GetCookie](<#GetCookie>) | Gets a cookie value. | Applies to all app types.
[GetEntryURL](<#GetEntryURL>) | Returns the URL of an Entry. Includes the Personal Area and the session identifier if applicable. | Applies to Traditional Web apps only.  
[GetFormValue](<#GetFormValue>) | Gets the value of a form field of the current HTTP request.<br/>If the field does not exist in the request an empty String will be returned. The same applies when the field exists but has an empty string as a value. | Applies to Traditional Web apps only.  
[GetIP](<#GetIP>) | Gets the IP host address of the remote client (IP of the user machine performing the HTTP request). | Applies to all app types.
[GetPageExtension](<#GetPageExtension>) | Returns the extension of the physical page that corresponds to the current screen, including the dot. Examples: &quot;.aspx&quot; or &quot;.jsf&quot;. | Applies to Traditional Web apps only.  
[GetPageName](<#GetPageName>) | Returns the name of the physical page that corresponds to the current screen. It is usually the same as the screen name, except when name clashes occur. | Applies to Traditional Web apps only.
[GetRawURL](<#GetRawURL>) | Returns the current relative requested URL, without the http://[server] part and without the session identifier.<br/>If SEO rules are being applied, the URL displayed in the user's browser is returned, and not the final URL after the rule is applied. | Applies to all app types.
[GetReferrerURL](<#GetReferrerURL>) | Gets the URL of the page that referred the user to the current page (HTTP referer header). Returns an empty string if no referer is available. |Applies to all app types.
[GetRequest_AddArgument](<#GetRequest_AddArgument>) | Builds the arguments string for an HTTP request with method GET, adding a new parameter to the arguments string. | Applies to all app types.
[GetRequest_Submit](<#GetRequest_Submit>) | Submit an HTTP GET request given the GET arguments and the URL. Returns the response content as a string and as binary data. | Applies to all app types.
[GetRequestContent](<#GetRequestContent>) | Gets the content of the current HTTP request. | Applies to all app types.
[GetRequestDomain](<#GetRequestDomain>) | Returns the host part of the current HTTP request as seen by the browser.<br/>Example: when the browser uses the address &quot;http://support.domain.com/site/welcome.aspx?id=12345&quot;, GetRequestDomain() returns &quot;support.domain.com&quot;. | Applies to all app types.
[GetRequestFiles](<#GetRequestFiles>) | Returns the list of files submitted in the current HTTP request. | Applies to all app types
[GetRequestHeader](<#GetRequestHeader>) | Gets the value of a specific header in the current HTTP request. Returns an empty string if the header is not present or has no value. | Applies to all app types.
[GetRunningESpaceJQueryVersion](<#GetRunningESpaceJQueryVersion>) | Returns the jQueryVersion of the Running ESpace. | Applies to Traditional Web apps only.  
[GetSessionId](<#GetSessionId>) | Gets the session identifier of the current HTTP request. | Applies to Traditional Web apps only. 
[GetURL](<#GetURL>) | Returns the current absolute requested URL, without the session identifier.<br/>If SEO rules are being applied, the final URL after the rule is applied is returned, and not the URL displayed in the user's browser. | Applies to all app types.
[GetURLMethod](<#GetURLMethod>) | Gets the request method (GET or POST) of the current requested URL. |Applies to all app types.
[GetURLWithSession](<#GetURLWithSession>) | Gets the current requested URL (with the session identifier). | Applies to Traditional Web apps only. 
[GetUserAgent](<#GetUserAgent>) | Gets the user agent of the current HTTP request. | Applies to all app types.
[GetUserLanguages](<#GetUserLanguages>) | Gets a sorted record list of client language preferences. | Applies to all app types.
[GetValueFromInputId](<#GetValueFromInputId>) | Gets the URL encoded value from an input form. | Applies to Traditional Web apps only. 
[GetValueFromInputIdDecoded](<#GetValueFromInputIdDecoded>) | Gets the decoded value from an input form.  | Applies to Traditional Web apps only.
[IsAjaxRequest](<#IsAjaxRequest>) | Returns true if this is running in an AJAX request.<br/>Not Implemented in Java. | Applies to Traditional Web apps only.
[IsSecureConnection](<#IsSecureConnection>) | Tells if the current request is being made via HTTPS. | Applies to all app types.
[MakeAbsoluteURL](<#MakeAbsoluteURL>) | Makes an absolute URL based on the URL provided. | Applies to all app types.
[PostRequest_AddArgument](<#PostRequest_AddArgument>) | Builds arguments list for a POST HTTP request, adding a new text parameter to the arguments list. If argument name is not supplied, the post will only submit the supplied value (this can be used for xml posts for example). | Applies to all app types.
[PostRequest_AddBinaryArgument](<#PostRequest_AddBinaryArgument>) | Builds arguments list for an HTTP request, adding a new binary parameter to the arguments list. If argument name is not supplied, the post will only submit the supplied value (this can be used for xml posts for example). | Applies to all app types.
[PostRequest_Submit](<#PostRequest_Submit>) | Submit an HTTP POST request given the POST arguments and the URL. Returns the response content as a string and as binary data. | Applies to all app types.
[ReplaceURLDomain](<#ReplaceURLDomain>) | Replaces the domain in the URL by the new domain. This function doesn't accept JavaScript as an URL. If the new domain is not provided, the domain of the current request is used.<br/>If the URL starts with the protocol (`http:` or `https:`), the host is removed from the URL and the remaining part is concatenated with the domain of the current request. Otherwise, the URL is considered as relative and it's concatenated with the one from the current request. | Applies to all app types.
[RunJavaScript](<#RunJavaScript>) | Runs the provided JavaScript code in the browser.| Applies to Traditional Web apps only.
[SetBaseTag](<#SetBaseTag>) | Sets the base tag of the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests. | Applies to Traditional Web apps only.
[SetCookie](<#SetCookie>) | Sets a cookie. | Applies to all app types.
[SetLastModified](<#SetLastModified>) | Sets the Last Modified Date HTTP header of the current response. | Applies to all app types.
[SetPageTitle](<#SetPageTitle>) | Sets the page title of the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests. | Applies to Traditional Web apps only.
[SetRequestTimeout](<#SetRequestTimeout>) | Sets the timeout of the current HTTP request. | Applies to all app types.
[SetStatusCode](<#SetStatusCode>) | Sets the status code of the current HTTP response. | Applies to Traditional Web apps only.
[URLEncode](<#URLEncode>) | Encodes a URL string for reliable HTTP transmission from the Web server to a client. | Applies to all app types.
[ValidateRequestSource](<#ValidateRequestSource>) | Validates if the income request is coming from the local machine and/or from the list of TrustedAddresses, ignoring<br/>Trusted Proxies configurations, so that by default it only allows real local requests that are not being handled by a proxy/loadbalancer. | Applies to all app types.

Structure | Description
---|---
[RequestFile](<#Structure_RequestFile>) | Represents a file submitted in an HTTP request, containing file metadata and binary content.
[UserLanguage](<#Structure_UserLanguage>) | Represents a client language preference with its priority value.

## Actions

### AddAttributeToHtmlTag { #AddAttributeToHtmlTag }

Adds an attribute to the outermost HTML tag of the document (e.g. xmlns, manifest...).  
This method has no effect in Ajax Requests. Not compatible with reactive web and mobile apps.

*Inputs*

Name
:   Type: Text. Mandatory.  
    

Value
:   Type: Text. Mandatory.  
    

### AddFaviconTag { #AddFaviconTag }

Allows setting the favicon for the current page. You can use &quot;omlresources&quot; to add an icon file to your oml.  
This method has no effect in Ajax Requests. Not compatible with reactive web and mobile apps.

*Inputs*

IconFilename
:   Type: Text. Mandatory.  
    The filename of the icon, e.g. &quot;outsystems.ico&quot;.

MimeType
:   Type: Text. Default: "image/x-icon".  
    The mime type of the icon file. By default this is &quot;image/x-icon&quot;.

### AddHeader { #AddHeader }

Adds a header to the current HTTP response.  
This method has no effect in Ajax Requests.

*Inputs*

Name
:   Type: Text. Mandatory.  
    Name of the header.

Value
:   Type: Text. Mandatory.  
    Value of the header.

### AddJavaScriptTag { #AddJavaScriptTag }

Adds a `<script>` tag to the HTML of the current HTTP response.  
This method has no effect in Ajax Requests. Not compatible with reactive web and mobile apps.

*Inputs*

JavaScriptURL
:   Type: Text. Mandatory.  
    The URL of the JavaScript file.

Defer
:   Type: Boolean. Default: False.  
    Defines if the defer attribute is added to the `<script>` tag. Defaults to False.

Charset
:   Type: Text. Default: "UTF-8".  
    The charset attribute of the `<script>` tag. Defaults to UTF-8.

### AddLinkTag { #AddLinkTag }

Adds a `<link>` tag to the HTML of the current HTTP response.  
This method has no effect in Ajax Requests. Not compatible with reactive web and mobile apps.

*Inputs*

Rel
:   Type: Text. Mandatory.  
    

Href
:   Type: Text. Mandatory.  
    

Type
:   Type: Text.  
    

### AddMetaHttpEquivTag { #AddMetaHttpEquivTag }

Adds a `<meta>` tag with the http-equiv attribute to the HTML of the current HTTP response.  
This method has no effect in Ajax Requests. Not compatible with reactive web and mobile apps.

*Inputs*

HttpEquiv
:   Type: Text. Mandatory.  
    

Content
:   Type: Text. Mandatory.  
    

### AddMetaTag { #AddMetaTag }

Adds a `<meta>` tag to the HTML of the current HTTP response.  
This method has no effect in Ajax Requests. Not compatible with reactive web and mobile apps.

*Inputs*

Name
:   Type: Text. Mandatory.  
    

Content
:   Type: Text. Mandatory.  
    

### AddPostProcessingFilter { #AddPostProcessingFilter }

This method has no effect in Ajax Requests.  
Not implemented in Java. Not compatible with reactive web and mobile apps.

*Inputs*

matchingRegexp
:   Type: Text. Mandatory.  
    

replacement
:   Type: Text. Mandatory.  
    

### AddSessionToURL { #AddSessionToURL }

Adds the current session identifier to a specified URL. Not compatible with reactive web and mobile apps.

*Inputs*

URL
:   Type: Text. Mandatory.  
    URL without session id.

*Outputs*

URLWithSession
:   Type: Text.  
    URL with session id.

### AddStyleSheetTag { #AddStyleSheetTag }

Adds a `<link rel="stylesheet">` tag to the HTML of the current HTTP response.  
This method has no effect in Ajax Requests. Not compatible with reactive web and mobile apps.

*Inputs*

StyleSheetURL
:   Type: Text. Mandatory.  
    The URL of the CSS file.

Charset
:   Type: Text. Default: "UTF-8".  
    The charset attribute of the `<script>` tag. Defaults to UTF-8.

### GetCookie { #GetCookie }

Gets a cookie value.

*Inputs*

CookieName
:   Type: Text. Mandatory.  
    Cookie name.

*Outputs*

CookieValue
:   Type: Text.  
    Value for the specified cookie.

### GetEntryURL { #GetEntryURL }

Returns the URL of an Entry. Includes the Personal Area and the session identifier if applicable. Not compatible with reactive web and mobile apps.

*Inputs*

EntryName
:   Type: Text. Mandatory.  
    Name of the Entry.

eSpaceName
:   Type: Text.  
    Name of the eSpace. If not specified, assumes the current eSpace and gives a relative URL.

FirstParameterName
:   Type: Text.  
    First parameter name.

FirstParameterValue
:   Type: Text.  
    First parameter value.

SecondParameterName
:   Type: Text.  
    Second parameter name.

SecondParameterValue
:   Type: Text.  
    Second parameter value.

ThirdParameterName
:   Type: Text.  
    Third parameter name.

ThirdParameterValue
:   Type: Text.  
    Third parameter value.

FourthParameterName
:   Type: Text.  
    Fourth parameter name.

FourthParameterValue
:   Type: Text.  
    Fourth parameter value.

FifthParameterName
:   Type: Text.  
    Fifth parameter name.

FifthParameterValue
:   Type: Text.  
    Fifth parameter value.

*Outputs*

URL
:   Type: Text.  
    URL of the Entry.

### GetFormValue { #GetFormValue }

Gets the value of a form field of the current HTTP request.  
If the field does not exist in the request an empty String will be returned. The same applies when the field exists but has an empty string as a value. Not compatible with reactive web and mobile apps.

*Inputs*

Name
:   Type: Text. Mandatory.  
    

*Outputs*

Value
:   Type: Text.  
    

### GetIP { #GetIP }

Gets the IP host address of the remote client (IP of the user machine performing the HTTP request).

*Outputs*

UserIP
:   Type: Text.  
    IP of the user machine performing the HTTP request.

### GetPageExtension { #GetPageExtension }

Returns the extension of the physical page that corresponds to the current screen, including the dot. Examples: &quot;.aspx&quot; or &quot;.jsf&quot;. Not compatible with reactive web and mobile apps.

*Outputs*

PageExtension
:   Type: Text.  
    Extension of the physical page that corresponds to the current screen.

### GetPageName { #GetPageName }

Returns the name of the physical page that corresponds to the current screen. It is usually the same as the screen name, except when name clashes occur. Not compatible with reactive web and mobile apps.
*Outputs*

PageName
:   Type: Text.  
    Name of the physical page that corresponds to the current screen.

### GetRawURL { #GetRawURL }

Returns the current relative requested URL, without the http://[server] part and without the session identifier.  
If SEO rules are being applied, the URL displayed in the user's browser is returned, and not the final URL after the rule is applied.

*Outputs*

RawURL
:   Type: Text.  
    

### GetReferrerURL { #GetReferrerURL }

Gets the URL of the page that referred the user to the current page (HTTP referer header). Returns an empty string if no referer is available.

*Outputs*

ReferrerURL
:   Type: Text.  
    The URL of the referring page, or an empty string if no referer is available.

### GetRequest_AddArgument { #GetRequest_AddArgument }

Builds the arguments string for an HTTP request with method GET, adding a new parameter to the arguments string.

*Inputs*

ArgumentsIn
:   Type: Text.  
    Current arguments string.

Name
:   Type: Text. Mandatory.  
    New argument name.

Value
:   Type: Text. Mandatory.  
    New argument value.

*Outputs*

ArgumentsOut
:   Type: Text.  
    Inputed arguments string concatenated with the pair `<argument name> = <argument value>`.

### GetRequest_Submit { #GetRequest_Submit }

Submit an HTTP GET request given the GET arguments and the URL. Returns the response content as a string and as binary data.

*Inputs*

URL
:   Type: Text. Mandatory.  
    URL for which to create the GET HTTP request.  
    Ex: &quot;http://mydomain.com/hello/test.aspx&quot;

Arguments
:   Type: Text. Mandatory.  
    GET arguments string.  
    Ex: &quot;param1=valueOne&amp;param2=valueTwo&quot;

Timeout
:   Type: Integer.  
    Number of milliseconds to wait before the request times out.

KeepAlive
:   Type: Boolean.  
    Indicates whether to make a persistent connection (True) to the Internet resource or not (False).

*Outputs*

TextContent
:   Type: Text.  
    Response text content.

BinaryContent
:   Type: BinaryData.  
    Response binary content.

BinaryContentType
:   Type: Text.  
    Value of the Content-Type header returned with the response.

### GetRequestContent { #GetRequestContent }

Gets the content of the current HTTP request.

*Inputs*

IncludeHeaders
:   Type: Boolean. Default: True.  
    Defines if the headers are included. Defaults to True.

*Outputs*

RawContent
:   Type: Text.  
    The content of the current HTTP request.

### GetRequestDomain { #GetRequestDomain }

Returns the host part of the current HTTP request as seen by the browser.  
Example: when the browser uses the address &quot;http://support.domain.com/site/welcome.aspx?id=12345&quot;, GetRequestDomain() returns &quot;support.domain.com&quot;.

*Outputs*

Domain
:   Type: Text.  
    The domain of the current HTTP request.

### GetRequestFiles { #GetRequestFiles }

Returns the list of files submitted in the current HTTP request.

*Outputs*

RequestFiles
:   Type: RecordList of [RequestFile](<#Structure_RequestFile>).  
    

### GetRequestHeader { #GetRequestHeader }

Gets the value of a specific header in the current HTTP request. Returns an empty string if the header is not present or has no value.

*Inputs*

HeaderName
:   Type: Text. Mandatory.  
    The name of the header

*Outputs*

Value
:   Type: Text.  
    Returns an empty string if the header is not present or has no value.

### GetRunningESpaceJQueryVersion { #GetRunningESpaceJQueryVersion }

Returns the jQueryVersion of the Running ESpace. Not compatible with reactive web and mobile apps.

*Outputs*

JQueryVersion
:   Type: Text.  
    

### GetSessionId { #GetSessionId }

Gets the session identifier of the current HTTP request. Not compatible with reactive web and mobile apps.

*Outputs*

SessionId
:   Type: Text.  
    Session identifier.

### GetURL { #GetURL }

Returns the current absolute requested URL, without the session identifier.  
If SEO rules are being applied, the final URL after the rule is applied is returned, and not the URL displayed in the user's browser.

*Outputs*

URL
:   Type: Text.  
    Current requested URL.

### GetURLMethod { #GetURLMethod }

Gets the request method (GET or POST) of the current requested URL.

*Outputs*

Method
:   Type: Text.  
    Current request method (GETor POST).

### GetURLWithSession { #GetURLWithSession }

Gets the current requested URL (with the session identifier). Not compatible with reactive web and mobile apps.

*Outputs*

URL
:   Type: Text.  
    Current requested URL with the session identifier.

### GetUserAgent { #GetUserAgent }

Gets the user agent of the current HTTP request.

*Outputs*

UserAgent
:   Type: Text.  
    

### GetUserLanguages { #GetUserLanguages }

Gets a sorted record list of client language preferences.

*Outputs*

Languages
:   Type: RecordList of [UserLanguage](<#Structure_UserLanguage>).  
    Sorted record list of client language preferences.

### GetValueFromInputId { #GetValueFromInputId }

Gets the URL encoded value from an input form. Not compatible with reactive web and mobile apps.

*Inputs*

InputId
:   Type: Text. Mandatory.  
    

*Outputs*

Value
:   Type: Text.  
    
### GetValueFromInputIdDecoded { #GetValueFromInputIdDecoded }

Gets the decoded value from an input form. Not compatible with reactive web and mobile apps.

*Inputs*

InputId
:   Type: Text. Mandatory.  
    

*Outputs*

Value
:   Type: Text.  
    
### IsAjaxRequest { #IsAjaxRequest }

Returns true if this is running in an AJAX request.  
Not Implemented in Java. Not compatible with reactive web and mobile apps.

*Outputs*

IsAjaxRequest
:   Type: Boolean.  
    Returns true if this is running in an AJAX request.

### IsSecureConnection { #IsSecureConnection }

Tells if the current request is being made via HTTPS.

*Outputs*

IsSecureConnection
:   Type: Boolean.  
    

### MakeAbsoluteURL { #MakeAbsoluteURL }

Makes an absolute URL based on the URL provided.

*Inputs*

URL
:   Type: Text. Mandatory.  
    Relative or absolute URL.

*Outputs*

AbsoluteURL
:   Type: Text.  
    Absolute URL.

### PostRequest_AddArgument { #PostRequest_AddArgument }

Builds arguments list for a POST HTTP request, adding a new text parameter to the arguments list. If argument name is not supplied, the post will only submit the supplied value (this can be used for xml posts for example).

*Inputs*

ArgumentsIn
:   Type: BinaryData.  
    Current arguments list in Binary format.

Name
:   Type: Text.  
    New text argument name.

Value
:   Type: Text. Mandatory.  
    New text argument value.

*Outputs*

ArgumentsOut
:   Type: BinaryData.  
    Inputed arguments list concatenated with the pair `<argument name> = <argument value>` in binary format.

### PostRequest_AddBinaryArgument { #PostRequest_AddBinaryArgument }

Builds arguments list for an HTTP request, adding a new binary parameter to the arguments list. If argument name is not supplied, the post will only submit the supplied value (this can be used for xml posts for example).

*Inputs*

ArgumentsIn
:   Type: BinaryData.  
    Current arguments list in Binary format.

Name
:   Type: Text.  
    New text argument name.

Value
:   Type: BinaryData. Mandatory.  
    New binary argument value.

*Outputs*

ArgumentsOut
:   Type: BinaryData.  
    Inputed arguments list concatenated with the pair `<argument name> = <argument value>` in binary format.

### PostRequest_Submit { #PostRequest_Submit }

Submit an HTTP POST request given the POST arguments and the URL. Returns the response content as a string and as binary data.

*Inputs*

URL
:   Type: Text. Mandatory.  
    URL for which to create the GET HTTP  request.

Arguments
:   Type: BinaryData.  
    POST arguments.

Timeout
:   Type: Integer.  
    Number of milliseconds to wait before the request times out.

KeepAlive
:   Type: Boolean.  
    Indicates whether to make a persistent connection (True) to the Internet resource or not (False).

*Outputs*

TextContent
:   Type: Text.  
    Response text content.

BinaryContent
:   Type: BinaryData.  
    Response binary content.

BinaryContentType
:   Type: Text.  
    Value of the Content-Type header returned with the response.

### ReplaceURLDomain { #ReplaceURLDomain }

Replaces the domain in the URL by the new domain. This function doesn't accept JavaScript as an URL. If the new domain is not provided, the domain of the current request is used.  
If the URL starts with the protocol (`http:` or `https:`), the host is removed from the URL and the remaining part is concatenated with the domain of the current request. Otherwise, the URL is considered as relative and it's concatenated with the one from the current request.

*Inputs*

URL
:   Type: Text. Mandatory.  
    The URL to replace the domain

Domain
:   Type: Text.  
    The new domain to put in the URL.

*Outputs*

SafeURL
:   Type: Text.  
    The URL with the new domain.

### RunJavaScript { #RunJavaScript }

Runs the provided JavaScript code in the browser. Not compatible with reactive web and mobile apps.

<div class="info" markdown="1">

The RunJavaScript action sends the response to the browser. This means that you can't call other actions to manipulate the response after RunJavaScript, for example the SetCookie action.

</div>

*Inputs*

Script
:   Type: Text. Mandatory.  
    JavaScript code to be sent to the browser.

### SetBaseTag { #SetBaseTag }

Sets the base tag of the HTML of the current HTTP response.  
This method has no effect in Ajax Requests. Not compatible with reactive web and mobile apps.

*Inputs*

HREF
:   Type: Text. Mandatory.  
    

Target
:   Type: Text. Default: "".  
    
### SetCookie { #SetCookie }

Sets a cookie.

*Inputs*

CookieName
:   Type: Text. Mandatory.  
    Cookie name.

CookieValue
:   Type: Text.  
    Cookie value.

CookieExpirationSpan
:   Type: Integer.  
    Cookie expiration span in minutes. If lower than or equal to zero the cookie will only be valid during current session.

CookiePath
:   Type: Text.  
    Cookie path. Defaults to path of the current eSpace, Tenant and Personal Area combination.

CookieDomain
:   Type: Text.  
    Cookie domain. Defaults to the current domain.

CookieHttpOnly
:   Type: Boolean.  
    Cookie HttpOnly attribute. Defaults to False. When set to True, the cookie value is not available in JavaScript code. Normally used in security-sensitive cookies.

CookieSecure
:   Type: Boolean.  
    Cookie Secure attribute. Defaults to what is defined in the security settings for the current environment.  
    It's not possible to lower the security specified at the environment level.

CookieSameSite
:   Type: Text.  
    Cookie SameSite attribute. Possible values: &quot;&quot;, &quot;None&quot;, &quot;Lax&quot;, and &quot;Strict&quot;. Defaults to what is defined in the security settings for the current environment.

### SetLastModified { #SetLastModified }

Sets the Last Modified Date HTTP header of the current response.

*Inputs*

LastModifiedDate
:   Type: DateTime. Mandatory.  
    Last Modified Date.

### SetPageTitle { #SetPageTitle }

Sets the page title of the HTML of the current HTTP response.  
This method has no effect in Ajax Requests. Not compatible with reactive web and mobile apps.

*Inputs*

Title
:   Type: Text. Mandatory.  
    
### SetRequestTimeout { #SetRequestTimeout }

Sets the timeout of the current HTTP request.

*Inputs*

Timeout
:   Type: Integer. Mandatory.  
    Timeout in seconds, or -1 for an infinite timeout.

### SetStatusCode { #SetStatusCode }

Sets the status code of the current HTTP response. Not compatible with reactive web and mobile apps.
Note: Setting custom HTTP status codes is an advanced extensibility scenario, so be sure to test if it works as intended in your specific infrastructure (for example, HTTP status code 204 is known to cause issues). Check the list of standard HTTP status codes used in OutSystems.

*Inputs*

StatusCode
:   Type: Integer. Mandatory.  
    Status code of the response. Examples: 404, 403.

### URLEncode { #URLEncode }

Encodes a URL string for reliable HTTP transmission from the Web server to a client

*Inputs*

StrIn
:   Type: Text. Mandatory.  
    String URL

Encoding
:   Type: Text.  
    Encoding type: ASCII, Unicode, UTF7 or UTF8

*Outputs*

StrOut
:   Type: Text.  
    Encoded string URL

### ValidateRequestSource { #ValidateRequestSource }

Validates if the income request is coming from the local machine and/or from the list of TrustedAddresses, ignoring  
Trusted Proxies configurations, so that by default it only allows real local requests that are not being handled by a proxy/loadbalancer.

*Inputs*

TrustedAddresses
:   Type: Text. Default: "".  
    A comma separeted list with IP addresses or Fully Quallified Domain Names. E.g: 127.0.0.1,mydomain.com.

UseOnlyTrustedAddresses
:   Type: Boolean. Default: False.  
    By default (False), will verify if the request is coming from the local machine or from one the addresses in TrustedAddresses. Otherwise, If enabled (True)  the request source will only be validated against the list of TrustedAddresses.

*Outputs*

Result
:   Type: Boolean.  
    Returns true if the request is coming from a trusted source. This can be from local machine and/or the list of Trusted Addresses.

RequestOrigin
:   Type: Text.  
    The request source IP or Hostname.

## Structures

### RequestFile { #Structure_RequestFile }

*Attributes*

FileName
:   Type: Text (50). Mandatory.  
    
FileType
:   Type: Text (50). Mandatory.  
    
FileSize
:   Type: Integer. Mandatory.  
    
BinaryContent
:   Type: BinaryData. Mandatory.  
    
### UserLanguage { #Structure_UserLanguage }

*Attributes*

Value
:   Type: Text (50). Mandatory.  
    


