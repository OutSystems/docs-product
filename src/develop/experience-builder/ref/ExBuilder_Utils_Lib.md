---
locale: en-us
guid: 9ecbb8d4-3888-4d93-b72d-b34aef107a1e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# ExBuilder_Utils_Lib

Module that contains several common objects and functions used across the mobile application.

## Summary

Action | Description
---|---
[AddressToCoordinates](<#AddressToCoordinates>) | Server action to get the coordinates for a given address, using the Google Geocoding API.
[CoordinatesToAddress](<#CoordinatesToAddress>) | Server action to get the address for the given coordinates, using the Google Geocoding API.

## Actions

### AddressToCoordinates { #AddressToCoordinates }

Server action to get the coordinates for a given address, using the Google Geocoding API.

*Inputs*

ServerAPIKey
:   Type: mandatory, Text.  
    Input variable with the Server API key to be used on this request.  
    Note: An empty key value may work unexpectedly.

Address
:   Type: mandatory, Text.  
    Input variable with the address to which we'll get the coordinates.

Region
:   Type: optional, Text.  
    Input variable with the region.

*Outputs*

Latitude
:   Type: Text.  
    Returned Latitude coordinate.

Longitude
:   Type: Text.  
    Returned Longitude coordinate.

### CoordinatesToAddress { #CoordinatesToAddress }

Server action to get the address for the given coordinates, using the Google Geocoding API.

*Inputs*

ServerAPIKey
:   Type: mandatory, Text.  
    Input variable with the Server API key to be used on this request.  
    Note: An empty key value may work unexpectedly.

Latitude
:   Type: mandatory, Text.  
    Input variable with the latitude coordinate to which we'll get the address.

Longitude
:   Type: mandatory, Text.  
    Input variable with the longitude coordinate to which we'll get the address.

*Outputs*

Addresses
:   Type: Text List.  
    Returnd list with the returned addresses.


