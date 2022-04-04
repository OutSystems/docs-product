---
summary: API for including scripts in Web Screens for all web apps running in the environment.
tags: runtime-traditionalweb
---

# IncludeJavascript API


API for including scripts in Web Screens for all web apps running in the environment.

To use this API reference the **IncludeJavascript_API extension** using the References Window in Service Studio.

## Summary

Action | Description
---|---
[Application_AddExclusionRule](<#Application_AddExclusionRule>) | Creates exclusion rules for a script. The specified script is not included in the specified application.
[Application_RemoveExclusionRule](<#Application_RemoveExclusionRule>) | Removes a script exclusion rule. The specified script is to be included in the specified application.
[Espace_AddExclusionRule](<#Espace_AddExclusionRule>) | Creates exclusion rules for a script. The specified script is not included in the specified module.
[Espace_RemoveExclusionRule](<#Espace_RemoveExclusionRule>) | Removes a script exclusion rule. The specified script is to be included in the specified module.
[Script_CreateOrUpdate](<#Script_CreateOrUpdate>) | Creates or updates a javascript. The script is inserted in the HTML of all Web Screens of all modules.<br/>If the script name already exists, the script is updated, otherwise a new script is created.
[Script_Delete](<#Script_Delete>) | Deletes a script: the script is no longer included in Web Screens.
[Script_Get](<#Script_Get>) | Returns the information of a script.
[Script_List](<#Script_List>) | Returns a list of scripts to be included in Web Screens.
[Script_SetActive](<#Script_SetActive>) | Activates a certain script to be included in Web Screens.
[Script_SetInactive](<#Script_SetInactive>) | Deactivates a certain script. The script is not included in Web Screens.

Structure | Description
---|---
[ExcludedApplications](<#Structure_ExcludedApplications>) | Represents an exclusion rule for a specific application. Exclusion rules specify applications in which scripts are not to be inserted.
[ExcludedEspaces](<#Structure_ExcludedEspaces>) | Represents an exclusion rule for a specific module. Exclusion rules specify modules in which scripts are not to be inserted.
[JavaScript](<#Structure_JavaScript>) | Represents a script to be included in the HTML of Web Screens.

## Actions

### Application_AddExclusionRule { #Application_AddExclusionRule }

Creates exclusion rules for a script. The specified script is not included in the specified application.

*Inputs*

ScriptName
:   Type: Text. Mandatory.  
    The name of the script.  
    

ApplicationKey
:   Type: Text. Mandatory.  
    The application unique key.

### Application_RemoveExclusionRule { #Application_RemoveExclusionRule }

Removes a script exclusion rule. The specified script is to be included in the specified application.

*Inputs*

ScriptName
:   Type: Text. Mandatory.  
    The name of the script.

ApplicationKey
:   Type: Text. Mandatory.  
    The application unique key.

### Espace_AddExclusionRule { #Espace_AddExclusionRule }

Creates exclusion rules for a script. The specified script is not included in the specified module.

*Inputs*

ScriptName
:   Type: Text. Mandatory.  
    The name of the script.  
    

EspaceKey
:   Type: Text. Mandatory.  
    The unique key of the module.

### Espace_RemoveExclusionRule { #Espace_RemoveExclusionRule }

Removes a script exclusion rule. The specified script is to be included in the specified module.

*Inputs*

ScriptName
:   Type: Text. Mandatory.  
    The name of the script to be included.

EspaceKey
:   Type: Text. Mandatory.  
    The unique key of the module.

### Script_CreateOrUpdate { #Script_CreateOrUpdate }

Creates or updates a javascript. The script is inserted in the HTML of all Web Screens of all modules.  
If the script name already exists, the script is updated, otherwise a new script is created.

*Inputs*

ScriptName
:   Type: Text. Mandatory.  
    The name of the script.

ScriptOrURL
:   Type: Text. Mandatory.  
    The inline script or a URL specifying where the script is located. This parameter needs to comply with the isUrl parameter.

IncludeAt
:   Type: Text. Mandatory.  
    The location in the HTML where the script is to be included. Valid locations are ‘HeadTop’, ‘HeadBottom’, ‘BodyTop’, ‘BodyBottom’.

Order
:   Type: Integer.  
    Specifies the order in which the script is to be included in the Web Screen or Web Block.

Description
:   Type: Text.  
    The documentation of the script.  
    

### Script_Delete { #Script_Delete }

Deletes a script: the script is no longer included in Web Screens.

*Inputs*

ScriptName
:   Type: Text. Mandatory.  
    The name of the script.

### Script_Get { #Script_Get }

Returns the information of a script.

*Inputs*

ScriptName
:   Type: Text. Mandatory.  
    The name of the script.

*Outputs*

JavaScript
:   Type: Record of [JavaScript](<#Structure_JavaScript>).  
    The script to be included in Web Screens.

### Script_List { #Script_List }

Returns a list of scripts to be included in Web Screens.

*Inputs*

ShowInactive
:   Type: Boolean. Mandatory.  
    If true returns all scripts, including scripts marked as inactive.

*Outputs*

JavaScriptList
:   Type: RecordList of [JavaScript](<#Structure_JavaScript>).  
    List of scripts.

### Script_SetActive { #Script_SetActive }

Activates a certain script to be included in Web Screens.

*Inputs*

ScriptName
:   Type: Text. Mandatory.  
    The name of the script.

### Script_SetInactive { #Script_SetInactive }

Deactivates a certain script. The script is not included in Web Screens.

*Inputs*

ScriptName
:   Type: Text. Mandatory.  
    The name of the script.


## Structures

### ExcludedApplications { #Structure_ExcludedApplications }

Represents an exclusion rule for a specific application. Exclusion rules specify applications in which scripts are not to be inserted.

*Attributes*

ApplicationKey
:   Type: Text (50). Mandatory.  
    The unique key of the application.

ApplicationName
:   Type: Text (50). Mandatory.  
    The name of the application.

### ExcludedEspaces { #Structure_ExcludedEspaces }

Represents an exclusion rule for a specific module. Exclusion rules specify modules in which scripts are not to be inserted.

*Attributes*

EspaceKey
:   Type: Text (50). Mandatory.  
    The unique key of the module.

EspaceName
:   Type: Text (50). Mandatory.  
    The name of the module.

### JavaScript { #Structure_JavaScript }

Represents a script to be included in the HTML of Web Screens.

*Attributes*

Name
:   Type: Text (50). Mandatory.  
    The name of the script.

ScriptOrURL
:   Type: Text (4096). Mandatory.  
    The inline script or an absolute URL specifying where the script is located.

IncludeAt
:   Type: Text (50). Mandatory.  
    The location in the HTML where the script is to be included. Valid locations are ‘HeadTop’, ‘HeadBottom’, ‘BodyTop’, ‘BodyBottom’.

Order
:   Type: Integer.  
    Specifies the order in which the script is to be included in the Web Screen or Web Block.

Description
:   Type: Text (50).  
    The documentation of the script.

IsActive
:   Type: Boolean. Mandatory.  
    Describes whether the script is globally enabled or disabled.

ExcludedApplications
:   Type: RecordList of [ExcludedApplications](<#Structure_ExcludedApplications>). Mandatory.  
    The script is not inserted in the Web Screens of these applications.

ExcludedEspaces
:   Type: RecordList of [ExcludedEspaces](<#Structure_ExcludedEspaces>). Mandatory.  
    The script is not inserted in the Web Screens of these modules.

