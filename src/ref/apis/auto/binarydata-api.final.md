---
summary: Explore the BinaryData API in OutSystems 11 (O11) for manipulating binary content, including conversions and size calculations.
tags: binary data manipulation, api documentation, data transformation, encoding, base64 encoding
locale: en-us
guid: 17494f81-67a9-4e24-833a-a4a7713e0255
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# BinaryData API

Provides Actions to manipulate BinaryData contents, such as retrieving the length or transforming binary content into Text or Base64.

## Summary

| Action | Description |
| ---|--- |
| [Base64ToBinary](<#Base64ToBinary>) | Converts Base64 Text into BinaryData. |
| [BinaryDataSize](<#BinaryDataSize>) | Returns the size in bytes of a binary content. |
| [BinaryDataToText](<#BinaryDataToText>) | Reads the content of a text file using a given encoding. If no encoding is supplied, the system's default ANSI encoding will be used. |
| [BinaryToBase64](<#BinaryToBase64>) | Converts BinaryData into Base64 Text. |
| [Compare](<#Compare>) | Performs a binary comparison between two Binary Data contents. |
| [ConvertEncoding](<#ConvertEncoding>) | Converts a range of bytes in a BinaryData from one encoding to another. |
| [TextToBinaryData](<#TextToBinaryData>) | Converts a Text into binary content. If no encoding is supplied, the system's default ANSI encoding will be used. |

## Actions

### Base64ToBinary { #Base64ToBinary }

Converts Base64 Text into BinaryData.

_Inputs_

Base64
:   Type: Text. Mandatory.  
    Base64 Text to convert to BinaryData.

_Outputs_

Binary
:   Type: BinaryData.  
    Result of conversion from Base64 Text to BinaryData.

### BinaryDataSize { #BinaryDataSize }

Returns the size in bytes of a binary content.

_Inputs_

BinaryData
:   Type: BinaryData. Mandatory.  
    Binary content.

_Outputs_

Size
:   Type: Integer.  
    Size in bytes of binary content.

### BinaryDataToText { #BinaryDataToText }

Reads the content of a text file using a given encoding. If no encoding is supplied, the system's default ANSI encoding will be used.

_Inputs_

BinaryData
:   Type: BinaryData. Mandatory.  
    Binary content to convert to text.

Encoding
:   Type: Text.  
    Encoding used when reading text from a binary content. Possible values are: unicode, utf-8, utf-16, ascii.

_Outputs_

Text
:   Type: Text.  
    Result of conversion from BinaryData to Text.

### BinaryToBase64 { #BinaryToBase64 }

Converts BinaryData into Base64 Text.

_Inputs_

Binary
:   Type: BinaryData. Mandatory.  
    Binary content to convert to Base64 Text.

_Outputs_

Base64
:   Type: Text.  
    Result of conversion from BinaryData to Base64 Text.

### Compare { #Compare }

Performs a binary comparison between two Binary Data contents.

_Inputs_

BinaryData1
:   Type: BinaryData. Mandatory.  
    First content in comparison.

BinaryData2
:   Type: BinaryData. Mandatory.  
    Second content in comparison.

_Outputs_

Equal
:   Type: Boolean.  
    True if the two binary contents are equal. False otherwise.

### ConvertEncoding { #ConvertEncoding }

Converts a range of bytes in a BinaryData from one encoding to another.

_Inputs_

BytesToConvert
:   Type: BinaryData. Mandatory.  
    The byte array to convert.

SourceEncoding
:   Type: Text. Mandatory.  
    The source of encoding. Possible values are: unicode, utf-8, utf-16, ascii.

DestinationEncoding
:   Type: Text. Mandatory.  
    The destination of encoding. Possible values are: unicode, utf-8, utf-16, ascii.

_Outputs_

ConvertedBytes
:   Type: BinaryData.  
    The converted byte array.

### TextToBinaryData { #TextToBinaryData }

Converts a Text into binary content. If no encoding is supplied, the system's default ANSI encoding will be used.

_Inputs_

Text
:   Type: Text. Mandatory.  
    Text to convert to BinaryData.

Encoding
:   Type: Text.  
    Character encoding of the text. Possible values are: unicode, utf-8, utf-16, ascii.

_Outputs_

BinaryData
:   Type: BinaryData.  
    Result of conversion from Text to BinaryData.
