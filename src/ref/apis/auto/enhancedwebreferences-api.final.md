---
summary: API to dynamically change Web Service and Web Reference URLs, SOAP headers, credentials, and proxies.
tags: 
locale: en-us
guid: aa9f7cd6-bf5d-4cd6-8079-df516cd3277c
---

# EnhancedWebReferences API


API to dynamically change Web Service and Web Reference URLs, SOAP headers, credentials, and proxies.

Use this API to customize requests of:

* exposed SOAP web services
* consumed SOAP web services that were upgraded to OutSystems 11

<div class="warning" style="overflow: hidden" markdown="1">

This API is **deprecated** and it will not work with the new implementation of **consumed** SOAP web services which supports up to SOAP 1.2. This applies to consumed SOAP web services that were created in OutSystems 11.

To customize requests of consumed SOAP web services that were created in OutSystems 11 you must use the [SOAP Extensibility API](<../soap-extensibility-api.md>).

</div>

## Summary

Action | Description
---|---
[ClearWebReferenceHeaders](<#ClearWebReferenceHeaders>) | Use this action after a call to SetWebReferenceSoapHeaders to make a new Web Reference request without SOAP headers.<br/>NOTE: since this action receives the Web Reference name as a parameter, if two Web References have the same name both are affected by this action.<br/>This only occurs in Consumer/Producer scenarios.
[GetWebReferenceSoapHeaders](<#GetWebReferenceSoapHeaders>) | Obtain the SOAP headers sent in the response of a Web Reference call. Use this action after invoking a Web Reference action.<br/>NOTE: since this action receives the Web Reference name as a parameter, if two Web References have the same name both are affected by this action.<br/>This only occurs in Consumer/Producer scenarios.
[GetWebServiceSoapHeaders](<#GetWebServiceSoapHeaders>) | Gets the SOAP headers sent to the Web Service. Use this action inside the Web Service logic.
[SetWebReferenceCredencials](<#SetWebReferenceCredencials>) | Sets Web Reference HTTP credentials. The username can be used in the form of DOMAIN\USER.<br/>The HTTP credentials persist for the request duration: all Web Reference calls placed during the same request use the specified credentials.<br/>To invoke Web References in the same request without the credentials, use this action without specifying the Username and Password.<br/>NOTE: since this action receives the Web Reference name as a parameter, if two Web References have the same name both are affected by this action.<br/>This only occurs in Consumer/Producer scenarios.
[SetWebReferenceProxy](<#SetWebReferenceProxy>) | Specifies a proxy through which a Web Reference action can be invoked.<br/>This action allows specifying the credentials to authenticate in the proxy. The specified proxy persists for the request duration: all Web Reference calls placed during the same request use that proxy.<br/>To invoke Web References in the same request using the default internet configurations, use this action without specifying the ProxyURL.<br/>NOTE: since this action receives the Web Reference name as a parameter, if two Web References have the same name both are affected by this action.<br/>This only occurs in Consumer/Producer scenarios.
[SetWebReferenceSoapHeaders](<#SetWebReferenceSoapHeaders>) | Sets SOAP headers to be used in Web Reference calls.<br/>The SOAP headers persist for the request duration: all Web Reference calls placed during the same request use the specified headers.<br/>To invoke Web References in the same request without the SOAP headers, use the ClearWebReferenceHeaders action.<br/>NOTE: since this action receives the Web Reference name as a parameter, if two Web References have the same name both are affected by this action.<br/>This only occurs in Consumer/Producer scenarios.
[SetWebReferenceURL](<#SetWebReferenceURL>) | Sets another effective URL for the Web Reference<br/>The specified URL persists for the request duration: all Web Reference calls placed during the same request use the URL.<br/>To invoke Web References in the same request using the default URL, use this action without specifying the URL.<br/>NOTE: since this action receives the Web Reference name as a parameter, if two Web References have the same name both are affected by this action.<br/>This only occurs in Consumer/Producer scenarios.
[SetWebServiceSoapHeaders](<#SetWebServiceSoapHeaders>) | Sets the SOAP headers to be sent by the Web Service in the response. Use this action inside the Web Service Logic.

Structure | Description
---|---
[SOAPHeader](<#Structure_SOAPHeader>) | 

## Actions

### ClearWebReferenceHeaders { #ClearWebReferenceHeaders }

Use this action after a call to SetWebReferenceSoapHeaders to make a new Web Reference request without SOAP headers.  
  
NOTE: since this action receives the Web Reference name as a parameter, if two Web References have the same name both are affected by this action.  
This only occurs in Consumer/Producer scenarios.

*Inputs*

WebReferenceName
:   Type: Text. Mandatory.  
    The Name of the WebReference In Service Studio.

### GetWebReferenceSoapHeaders { #GetWebReferenceSoapHeaders }

Obtain the SOAP headers sent in the response of a Web Reference call. Use this action after invoking a Web Reference action.  
  
NOTE: since this action receives the Web Reference name as a parameter, if two Web References have the same name both are affected by this action.  
This only occurs in Consumer/Producer scenarios.

*Inputs*

WebReferenceName
:   Type: Text. Mandatory.  
    The Name of the WebReference In Service Studio.

*Outputs*

SoapHeaders
:   Type: RecordList of [SOAPHeader](<#Structure_SOAPHeader>).  
    Structure representing the SOAP headers.

### GetWebServiceSoapHeaders { #GetWebServiceSoapHeaders }

Gets the SOAP headers sent to the Web Service. Use this action inside the Web Service logic.

*Outputs*

SoapHeaders
:   Type: RecordList of [SOAPHeader](<#Structure_SOAPHeader>).  
    Structure representing the SOAP headers.

### SetWebReferenceCredencials { #SetWebReferenceCredencials }

Sets Web Reference HTTP credentials. The username can be used in the form of DOMAIN\USER.  
The HTTP credentials persist for the request duration: all Web Reference calls placed during the same request use the specified credentials.  
To invoke Web References in the same request without the credentials, use this action without specifying the Username and Password.  
  
NOTE: since this action receives the Web Reference name as a parameter, if two Web References have the same name both are affected by this action.  
This only occurs in Consumer/Producer scenarios.

*Inputs*

WebReferenceName
:   Type: Text. Mandatory.  
    The Name of the WebReference In Service Studio.

UserName
:   Type: Text. Mandatory.  
    

Password
:   Type: Text. Mandatory.  
    

### SetWebReferenceProxy { #SetWebReferenceProxy }

Specifies a proxy through which a Web Reference action can be invoked.  
This action allows specifying the credentials to authenticate in the proxy. The specified proxy persists for the request duration: all Web Reference calls placed during the same request use that proxy.  
To invoke Web References in the same request using the default internet configurations, use this action without specifying the ProxyURL.  
  
NOTE: since this action receives the Web Reference name as a parameter, if two Web References have the same name both are affected by this action.  
This only occurs in Consumer/Producer scenarios.

*Inputs*

WebReferenceName
:   Type: Text. Mandatory.  
    The Name of the WebReference In Service Studio.

ProxyURL
:   Type: Text. Mandatory.  
    

ProxyUserName
:   Type: Text.  
    

ProxyPassword
:   Type: Text.  
    

### SetWebReferenceSoapHeaders { #SetWebReferenceSoapHeaders }

Sets SOAP headers to be used in Web Reference calls.  
The SOAP headers persist for the request duration: all Web Reference calls placed during the same request use the specified headers.  
To invoke Web References in the same request without the SOAP headers, use the ClearWebReferenceHeaders action.  
  
NOTE: since this action receives the Web Reference name as a parameter, if two Web References have the same name both are affected by this action.  
This only occurs in Consumer/Producer scenarios.

*Inputs*

WebReferenceName
:   Type: Text. Mandatory.  
    The Name of the WebReference In Service Studio.

SoapHeaders
:   Type: RecordList of [SOAPHeader](<#Structure_SOAPHeader>). Mandatory.  
    Structure representing the SOAP headers.

### SetWebReferenceURL { #SetWebReferenceURL }

Sets another effective URL for the Web Reference  
The specified URL persists for the request duration: all Web Reference calls placed during the same request use the URL.  
To invoke Web References in the same request using the default URL, use this action without specifying the URL.  
  
NOTE: since this action receives the Web Reference name as a parameter, if two Web References have the same name both are affected by this action.  
This only occurs in Consumer/Producer scenarios.

*Inputs*

WebReferenceName
:   Type: Text. Mandatory.  
    The Name of the WebReference In Service Studio.

URL
:   Type: Text. Mandatory.  
    The URL of the new Web Reference to point to.  
    The Web Reference in the specified URL must be compatible with the previous one.  
    Generally this action is used to specify the same Web Reference as the original, made available in a different machine.

### SetWebServiceSoapHeaders { #SetWebServiceSoapHeaders }

Sets the SOAP headers to be sent by the Web Service in the response. Use this action inside the Web Service Logic.

*Inputs*

SoapHeaders
:   Type: RecordList of [SOAPHeader](<#Structure_SOAPHeader>). Mandatory.  
    Structure representing the SOAP headers.


## Structures

### SOAPHeader { #Structure_SOAPHeader }



*Attributes*

Actor
:   Type: Text (500).  
    Recipient of the SOAP header.

DidUnderstand
:   Type: Boolean.  
    A value indicating whether an XML Web service method properly processed a SOAP header.

Element
:   Type: Text (500000). Mandatory.  
    XML Header element for a SOAP request or response.

EncodedMustUnderstand
:   Type: Text (10). Default: "0".  
    Value of the mustUnderstand XML attribute for the SOAP header when communicating with SOAP protocol version 1.1. Valid values are 0, 1, true or false.

EncodedMustUnderstand12
:   Type: Text (10). Default: "0".  
    Value of the mustUnderstand XML attribute for the SOAP header when communicating with SOAP protocol version 1.2. Valid values are 0, 1, true or false.

EncodedRelay
:   Type: Text (10). Default: "0".  
    Relay attribute of the SOAP 1.2 header. Valid values are 0, 1, true or false.

MustUnderstand
:   Type: Boolean.  
    Value indicating whether the SoapHeader must be understood.

Relay
:   Type: Boolean.  
    Value that indicates whether the SOAP header is to be relayed to the next SOAP node if the current node does not understand the header.

Role
:   Type: Text (500).  
    Recipient of the SOAP header.

