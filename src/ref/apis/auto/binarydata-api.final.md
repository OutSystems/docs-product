---
summary: Provides Actions to manipulate BinaryData contents, such as retrieving the length or transforming binary content into Text.
tags: 
---

# BinaryData API


Provides Actions to manipulate BinaryData contents, such as retrieving the length or transforming binary content into Text or Base64.

## Summary

Action | Description
---|---
[Base64ToBinary](<#Base64ToBinary>) | Converts Base64 Text into BinaryData.
[BinaryDataSize](<#BinaryDataSize>) | Returns the size in bytes of a binary content.
[BinaryDataToText](<#BinaryDataToText>) | Reads the content of a text file using a given encoding. If no encoding is supplied, the system's default ANSI encoding will be used.
[BinaryToBase64](<#BinaryToBase64>) | Converts BinaryData into Base64 Text.
[Compare](<#Compare>) | Performs a binary comparison between two Binary Data contents.
[ConvertEncoding](<#ConvertEncoding>) | Converts a range of bytes in a BinaryData from one encoding to another.
[TextToBinaryData](<#TextToBinaryData>) | Converts a Text into binary content. If no encoding is supplied, the system's default ANSI encoding will be used.

## Actions

### Base64ToBinary { #Base64ToBinary }

Converts Base64 Text into BinaryData.

*Inputs*

Base64
:   Type: Text. Mandatory.  
    Base64 Text to convert to BinaryData.

*Outputs*

Binary
:   Type: BinaryData.  
    Result of conversion from Base64 Text to BinaryData.

### BinaryDataSize { #BinaryDataSize }

Returns the size in bytes of a binary content.

*Inputs*

BinaryData
:   Type: BinaryData. Mandatory.  
    Binary content.

*Outputs*

Size
:   Type: Integer.  
    Size in bytes of binary content.

### BinaryDataToText { #BinaryDataToText }

Reads the content of a text file using a given encoding. If no encoding is supplied, the system's default ANSI encoding will be used.

*Inputs*

BinaryData
:   Type: BinaryData. Mandatory.  
    Binary content to convert to text.

Encoding
:   Type: Text.  
    Encoding used when reading text from a binary content. Possible values are: unicode, utf-8, utf-16, ascii.

*Outputs*

Text
:   Type: Text.  
    Result of conversion from BinaryData to Text.

### BinaryToBase64 { #BinaryToBase64 }

Converts BinaryData into Base64 Text.

*Inputs*

Binary
:   Type: BinaryData. Mandatory.  
    Binary content to convert to Base64 Text.

*Outputs*

Base64
:   Type: Text.  
    Result of conversion from BinaryData to Base64 Text.

### Compare { #Compare }

Performs a binary comparison between two Binary Data contents.

*Inputs*

BinaryData1
:   Type: BinaryData. Mandatory.  
    First content in comparison.

BinaryData2
:   Type: BinaryData. Mandatory.  
    Second content in comparison.

*Outputs*

Equal
:   Type: Boolean.  
    True if the two binary contents are equal. False otherwise.

### ConvertEncoding { #ConvertEncoding }

Converts a range of bytes in a BinaryData from one encoding to another.

*Inputs*

BytesToConvert
:   Type: BinaryData. Mandatory.  
    The byte array to convert.

SourceEncoding
:   Type: Text. Mandatory.  
    The source of encoding. Possible values are: unicode, utf-8, utf-16, ascii.

DestinationEncoding
:   Type: Text. Mandatory.  
    The destination of encoding. Possible values are: unicode, utf-8, utf-16, ascii.

*Outputs*

ConvertedBytes
:   Type: BinaryData.  
    The converted byte array.

### TextToBinaryData { #TextToBinaryData }

Converts a Text into binary content. If no encoding is supplied, the system's default ANSI encoding will be used.

*Inputs*

Text
:   Type: Text. Mandatory.  
    Text to convert to BinaryData.

Encoding
:   Type: Text.  
    Character encoding of the text. Possible values are: unicode, utf-8, utf-16, ascii.

*Outputs*

BinaryData
:   Type: BinaryData.  
    Result of conversion from Text to BinaryData.


