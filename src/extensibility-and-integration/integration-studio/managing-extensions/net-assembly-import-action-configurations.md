---
locale: en-us
guid: 8196d55c-6aeb-47d5-a855-02b92e4244f4
---

# Supported Configurations for Import Actions from .NET Assembly

The following list provides information on the supported configurations and limitations for the **Import Actions from .NET Assembly** wizard in the current Integration Studio version.

For the supported assembly versions please check the [System Requirements](<https://success.outsystems.com/Support/Enterprise_Customers/Installation/OutSystems_Platform_system_requirements>).  
  

## Imported Elements
*  Non-Abstract Public Methods (Static or Instance)
* Non-Abstract Public Properties (Static or Instance)
* Public Fields (Static or Instance)
* Public Instance Constructors
* Web Service Methods

## Limitations
* Can't import Index Properties
* Can't import Delegate Types
* Can't import Structures
* Can't import Enumerations
* Can't import Generic Methods (although Generic Types are supported in its parameters and return value)
* Members of Generic Classes and of their inner classes aren't imported
`* Only static Members of Abstract Classes can be imported

