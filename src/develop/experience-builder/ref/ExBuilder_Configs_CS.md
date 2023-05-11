---
locale: en-us
guid: 1233ca21-be96-4571-abab-4b38a30aa237
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# ExBuilder_Configs_CS

Module that contains several configuration site properties used across the mobile application.

## Summary

Action | Description
---|---
[AgentNumber_Get](<#AgentNumber_Get>) | Server action to expose the value of the site property &quot;AgentNumber&quot;.
[DoctorNumber_Get](<#DoctorNumber_Get>) | Server action to expose the value of the site property &quot;DoctorNumber&quot;.
[GenericValidationMessage_Get](<#GenericValidationMessage_Get>) | Server action to expose the value of the site property &quot;GenericValidationMessage&quot;.
[SitePropertiesInsurance_GetAll](<#SitePropertiesInsurance_GetAll>) | Server action that fetches the site properties that support the app on Insurance template scenarios.
[SitePropertiesSupport_GetAll](<#SitePropertiesSupport_GetAll>) | Server action that fetches the site properties that support the app.
[SupportEmail_Get](<#SupportEmail_Get>) | Server action to expose the value of the site property &quot;SupportEmail&quot;.
[SupportNumber_Get](<#SupportNumber_Get>) | Server action to expose the value of the site property &quot;SupportNumber&quot;.
[WebSiteAboutUs_Get](<#WebSiteAboutUs_Get>) | Server action to expose the value of the site property &quot;WebSiteAboutUs&quot;.

## Actions

### AgentNumber_Get { #AgentNumber_Get }

Server action to expose the value of the site property &quot;AgentNumber&quot;.

*Outputs*

Value
:   Type: Phone Number.  
    Returned site property &quot;AgentNumber&quot; value.

### DoctorNumber_Get { #DoctorNumber_Get }

Server action to expose the value of the site property &quot;DoctorNumber&quot;.

*Outputs*

Value
:   Type: Phone Number.  
    Returned site property &quot;DoctorNumber&quot; value.

### GenericValidationMessage_Get { #GenericValidationMessage_Get }

Server action to expose the value of the site property &quot;GenericValidationMessage&quot;.

*Outputs*

Value
:   Type: Text.  
    Returned site property &quot;GenericValidationMessage&quot; value.

### SitePropertiesInsurance_GetAll { #SitePropertiesInsurance_GetAll }

Server action that fetches the site properties that support the app on Insurance template scenarios.

*Outputs*

AgentNumber
:   Type: Phone Number.  
    Returned phone number for the agent.

DoctorNumber
:   Type: Phone Number.  
    Returned phone number for the doctor.

### SitePropertiesSupport_GetAll { #SitePropertiesSupport_GetAll }

Server action that fetches the site properties that support the app.

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

### SupportEmail_Get { #SupportEmail_Get }

Server action to expose the value of the site property &quot;SupportEmail&quot;.

*Outputs*

Value
:   Type: Email.  
    Returned site property &quot;SupportEmail&quot; value.

### SupportNumber_Get { #SupportNumber_Get }

Server action to expose the value of the site property &quot;SupportNumber&quot;.

*Outputs*

Value
:   Type: Text.  
    Returned site property &quot;SupportNumber&quot; value.

### WebSiteAboutUs_Get { #WebSiteAboutUs_Get }

Server action to expose the value of the site property &quot;WebSiteAboutUs&quot;.

*Outputs*

Value
:   Type: Text.  
    Returned sit property &quot;WebSiteAboutUs&quot; value.

