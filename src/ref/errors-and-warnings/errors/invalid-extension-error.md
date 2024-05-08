---
summary: Learn how to resolve the 'Invalid Extension' error in OutSystems 11 (O11) by setting literal default values for input parameters in Integration Studio.
locale: en-us
guid: 0b8a546c-b037-4bc9-a9f0-ae936c88c951
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Invalid Extension Error

The `Invalid Extension` error is issued in the following situation:

* `Change <parameter> default value in Integration Studio, go to Add/Remove References and refresh Extension reference`
  
    The definition of an Extension action has a default value for an input parameter that is not a literal.

    Open Integration Studio to edit the extension. Select the action, and change the default value of the parameter to a literal. In Service Studio you have to refresh this reference.
