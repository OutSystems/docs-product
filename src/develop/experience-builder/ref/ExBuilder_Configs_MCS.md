# ExBuilder_Configs_MCS

Module that contains several methods to expose configurations used across the mobile application.

## Summary

Client Action | Description
---|---
[LocalSitePropertiesInsurance_CreateOrUpdate](<#Client_LocalSitePropertiesInsurance_CreateOrUpdate>) | Creates or updates a LocalSitePropertiesInsurance.
[LocalSitePropertiesInsurance_Get](<#Client_LocalSitePropertiesInsurance_Get>) | Client action that fetches the local site properties for LocalSitePropertiesInsurance.
[LocalSitePropertiesInsurance_Set](<#Client_LocalSitePropertiesInsurance_Set>) | Client action that stores the local site properties for Insurance for app configuration.%%This method will also add the data to a client variables.
[LocalSitePropertiesSupport_CreateOrUpdate](<#Client_LocalSitePropertiesSupport_CreateOrUpdate>) | Creates or updates a LocalSitePropertiesSupport.
[LocalSitePropertiesSupport_Get](<#Client_LocalSitePropertiesSupport_Get>) | Client action that fetches the local site properties for LocalSitePropertiesSupport.
[LocalSitePropertiesSupport_Set](<#Client_LocalSitePropertiesSupport_Set>) | Client action that stores the local site properties for app configuration.%%This method will also add the data to a client variables.

## Client Actions

### LocalSitePropertiesInsurance_CreateOrUpdate { #Client_LocalSitePropertiesInsurance_CreateOrUpdate }

Creates or updates a LocalSitePropertiesInsurance.

*Inputs*

LocalSitePropertiesInsuranceRec
:   Type: mandatory.  
    Record to be created or updated the entry on LocalSitePropertiesInsurance.

### LocalSitePropertiesInsurance_Get { #Client_LocalSitePropertiesInsurance_Get }

Client action that fetches the local site properties for LocalSitePropertiesInsurance.

*Outputs*

AgentNumber
:   Type: Phone Number.  
    Phone number for the agent.

DoctorNumber
:   Type: Phone Number.  
    Phone number for the doctor.

### LocalSitePropertiesInsurance_Set { #Client_LocalSitePropertiesInsurance_Set }

Client action that stores the local site properties for Insurance for app configuration.  
This method will also add the data to a client variables.

### LocalSitePropertiesSupport_CreateOrUpdate { #Client_LocalSitePropertiesSupport_CreateOrUpdate }

Creates or updates a LocalSitePropertiesSupport.

*Inputs*

LocalSitePropertiesSupportRec
:   Type: mandatory.  
    Record to be created or updated the entry on LocalSitePropertiesSupport.

### LocalSitePropertiesSupport_Get { #Client_LocalSitePropertiesSupport_Get }

Client action that fetches the local site properties for LocalSitePropertiesSupport.

*Outputs*

GenericValidationMessage
:   Type: Text.  
    Text to be shown on the error message for a generic error.

SupportNumber
:   Type: Phone Number.  
    Phone number for the support.

WebSiteAboutUs
:   Type: Text.  
    Website URL for the about us page.

SupportEmail
:   Type: Email.  
    Email for the company support.

GoogleMapsAPIKey
:   Type: Text.  
    Google Maps API Key.

### LocalSitePropertiesSupport_Set { #Client_LocalSitePropertiesSupport_Set }

Client action that stores the local site properties for app configuration.  
This method will also add the data to a client variables.
