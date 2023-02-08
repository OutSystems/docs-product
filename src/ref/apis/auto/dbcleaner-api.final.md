---
summary: Allows freeing-up database space.
tags: support-application_development; support-Database
locale: en-us
guid: 9fdba27d-69ca-46b4-9a7b-6dee299c8084
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# DbCleaner API


The DbCleaner API provides functionality for freeing up database space. This is accomplished through actions that enable you to:

* drop database tables/columns corresponding to Entities/Attributes that are no longer in use by any of your applications
* delete module versions that are too old and no longer needed

When you delete Entities and Attributes in your applications, OutSystems doesn't delete the corresponding table or column in the database. Your data is safely stored just in case you want to rollback your application. This API allows you to delete module versions, entities, and attributes that are no longer used, thus freeing database space.

All calls to the DbCleaner API are audited and logged. Audit logs are displayed in the General Log section of the environment management console, and errors are logged under the Error Log section.

To use this API simply reference the DbCleaner_API module using the References Window in the development environment.

## Requirements

To use this API, there are the following requirements:

* The module invoking this API needs to have Service Center set as User Provider module.
* The logged user needs to have 'Change & Deploy' permissions, or the 'Administrator' built-in role depending on the action being invoked. Check the action documentation to learn more. 

When deleting multi-tenant Entities, or Static Entities with translations, the 9.0.0.23 version of this API requires republishing the modules using the deleted tables or columns. This implies republishing the module that had the Entity or Attribute and all the modules that reference it.

## Summary

Action | Description
---|---
[Attribute_DropColumn](<#Attribute_DropColumn>) | Physically deletes the database table column associated with the specified entity attribute.  If the entity attribute still exists in a module’s meta model, the delete operation will not be performed.<br/>The logged user needs to have the 'Administrator' built-in role.
[Attribute_ListDeleted](<#Attribute_ListDeleted>) | Returns a list of attributes, with their information, that have been deleted from module’s meta model but are still physically present in the database.<br/>The logged user needs to have the 'Administrator' built-in role.
[Entity_DropTable](<#Entity_DropTable>) | Physically deletes the database table associated with the specified entity.  If the entity still exists in a module’s meta model, the delete operation will not be performed.<br/>The logged user needs to have the 'Administrator' built-in role.
[Entity_ListDeleted](<#Entity_ListDeleted>) | Returns a list of entities, with their information, that have been deleted from module’s meta model but are still physically present in the database.<br/>The logged user needs to have the 'Administrator' built-in role.
[ModuleVersion_Delete](<#ModuleVersion_Delete>) | Deletes the specified module version of the specified module from the database.<br/>The logged user needs to have 'Change & Deploy' permissions.
[ModuleVersion_DeleteAll](<#ModuleVersion_DeleteAll>) | Deletes module versions that were published before the specified date and time. This action does not delete the module version that is currently published or module versions used in tagged versions of applications or solutions.<br/>The logged user needs to have 'Change & Deploy' permissions.
[ModuleVersion_ListOldest](<#ModuleVersion_ListOldest>) | Returns a list of module versions that are stored in the database and that were published before the specified date and time. This action does not return the module version that is currently published or module versions used in tagged versions of applications or solutions.<br/>The logged user needs to have 'Change & Deploy' permissions.

Structure | Description
---|---
[AttributeInfo](<#Structure_AttributeInfo>) | Information about a specific entity attribute.
[EntityInfo](<#Structure_EntityInfo>) | Information about a specific entity.
[ModuleInfo](<#Structure_ModuleInfo>) | Information about a specific module.
[ModuleVersionInfo](<#Structure_ModuleVersionInfo>) | Information about a specific module version.

Static Entity | Description
---|---
[ModuleType](<#StaticEntity_ModuleType>) | Types of modules.

## Actions

### Attribute_DropColumn { #Attribute_DropColumn }

Physically deletes the database table column associated with the specified entity attribute.  If the entity attribute still exists in a module’s meta model, the delete operation will not be performed and the reason for failure will be recorded in the platform logs.  
The logged user needs to have the 'Administrator' built-in role.

*Inputs*

AttributeId
:   Type: mandatory, Integer.  
    The attribute identifier.

*Outputs*

Success
:   Type: Boolean.  
    True if the column was successfully deleted. False otherwise.

### Attribute_ListDeleted { #Attribute_ListDeleted }

Returns a list of attributes, with their information, that have been deleted from module’s meta model but are still physically present in the database.  
The logged user needs to have the 'Administrator' built-in role.

*Outputs*

DeletedAttributes
:   Type: [AttributeInfo](<#Structure_AttributeInfo>) List.  
    List of attributes, with their information, that have been deleted from module’s meta model.

### Entity_DropTable { #Entity_DropTable }

Physically deletes the database table associated with the specified entity.  If the entity still exists in a module’s meta model, the delete operation will not be performed and the reason for failure will be recorded in the platform logs.  
The logged user needs to have the 'Administrator' built-in role.

*Inputs*

EntityId
:   Type: mandatory, Integer.  
    The entity identifier.

*Outputs*

Success
:   Type: Boolean.  
    True if the table was successfully deleted. False otherwise.

### Entity_ListDeleted { #Entity_ListDeleted }

Returns a list of entities, with their information, that have been deleted from module’s meta model but are still physically present in the database.  
The logged user needs to have the 'Administrator' built-in role.

*Outputs*

DeletedEntities
:   Type: [EntityInfo](<#Structure_EntityInfo>) List.  
    List of entities, with their information, that have been deleted from module’s meta model.

### ModuleVersion_Delete { #ModuleVersion_Delete }

Deletes the specified module version of the specified module from the database.  
The logged user needs to have 'Change & Deploy' permissions.

*Inputs*

ModuleVersionId
:   Type: mandatory, Integer.  
    The module version identifier.

ModuleId
:   Type: mandatory, Integer.  
    The module identifier.

### ModuleVersion_DeleteAll { #ModuleVersion_DeleteAll }

Deletes module versions that were published before the specified date and time. This action does not delete the module version that is currently published or module versions used in tagged versions of applications or solutions.  
The logged user needs to have 'Change & Deploy' permissions.

*Inputs*

OlderThan
:   Type: mandatory, Date Time.  
    Date and time that indicates the most recent point in time from which onward module versions are not to be deleted from the database.

ModuleId
:   Type: optional, Integer.  
    The module identifier. If not specified, returns module versions of all modules.

MaxNumberOfVersions
:   Type: optional, Integer.  
    The maximum number of versions to get. If not specified, returns the oldest 100 module versions. Set to 0 (zero) to get all the module versions.

*Outputs*

HasMoreVersions
:   Type: Boolean.  
    Returns True if there are still module versions to delete.

### ModuleVersion_ListOldest { #ModuleVersion_ListOldest }

Returns a list of module versions that are stored in the database and that were published before the specified date and time. This action does not return the module version that is currently published or module versions used in tagged versions of applications or solutions.  
The logged user needs to have 'Change & Deploy' permissions.

*Inputs*

OlderThan
:   Type: mandatory, Date Time.  
    Date and time that indicates the most recent point in time from which onward module versions are not to be deleted from the database.

ModuleName
:   Type: optional, Text.  
    The name of the module. If not specified, returns module versions of modules with any name.

ModuleTypeId
:   Type: optional, ModuleType Identifier.  
    The type of the module. If not specified, returns module versions of modules of any type.

MaxNumberOfVersions
:   Type: optional, Integer.  
    The maximum number of versions to get. If not specified, returns the oldest 100 module versions. Set to 0 (zero) to get all the module versions

*Outputs*

ModuleVersions
:   Type: [ModuleVersionInfo](<#Structure_ModuleVersionInfo>) List.  
    List of module versions, with their information, that have been published in the past and are kept stored in the database.

HasMoreVersions
:   Type: Boolean.  
    Returns True if there are more module versions than the ones listed.


## Structures

### AttributeInfo { #Structure_AttributeInfo }

Information about a specific entity attribute.

*Attributes*

Id
:   Type: Integer.  
    Attribute unique identifier

Name
:   Type: Text.  
    Name of the attribute

IsDeleted
:   Type: Boolean.  
    Indicates if the attribute was deleted

EntityInfo
:   Type: [EntityInfo](<#Structure_EntityInfo>).  
    Information about the entity to which the attribute belongs

### EntityInfo { #Structure_EntityInfo }

Information about a specific entity.

*Attributes*

Id
:   Type: Integer.  
    Entity unique identifier

Name
:   Type: Text.  
    Name of the entity

IsDeleted
:   Type: Boolean.  
    Indicates if the entity was deleted

ModuleInfo
:   Type: [ModuleInfo](<#Structure_ModuleInfo>).  
    Information about the module to which the entity belongs

### ModuleInfo { #Structure_ModuleInfo }

Information about a specific module.

*Attributes*

Id
:   Type: Integer.  
    Module unique identifier

Name
:   Type: Text.  
    Name of the module

IsDeleted
:   Type: Boolean.  
    Indicates if the module was deleted

ModuleTypeId
:   Type: ModuleType Identifier.  
    Module type identifier

### ModuleVersionInfo { #Structure_ModuleVersionInfo }

Information about a specific module version.

*Attributes*

Id
:   Type: Integer.  
    Module version unique identifier

Version
:   Type: Text.  
    Version number

UploadedDate
:   Type: Date Time.  
    Date and time when the version was uploaded to the server

LastPublishedDate
:   Type: Date Time.  
    Date and time of the last publish of the module version

ModuleInfo
:   Type: [ModuleInfo](<#Structure_ModuleInfo>).  
    Information about the module to which the module version belongs


## Static Entities

### ModuleType { #StaticEntity_ModuleType }

Types of modules.

*Attributes*

Id
:   Type: Integer.  
    

Label
:   Type: Text (50).  
    

*Records*

* Extension
* Espace


