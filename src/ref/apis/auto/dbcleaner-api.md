# DbCleaner API

For Platform Version 9.10.0.14. Allows freeing-up database space.

## Summary

Action | Description
---|---
[Attribute_DropColumn](<#Attribute_DropColumn>) | Physically deletes the database table column associated with the specified entity attribute.  If the entity attribute still exists in a module’s meta model, the delete operation will not be performed.%%The logged user needs to have the 'Administrator' built-in role.
[Attribute_ListDeleted](<#Attribute_ListDeleted>) | Returns a list of attributes, with their information, that have been deleted from module’s meta model but are still physically present in the database.%%The logged user needs to have the 'Administrator' built-in role.
[Entity_DropTable](<#Entity_DropTable>) | Physically deletes the database table associated with the specified entity.  If the entity still exists in a module’s meta model, the delete operation will not be performed.%%The logged user needs to have the 'Administrator' built-in role.
[Entity_ListDeleted](<#Entity_ListDeleted>) | Returns a list of entities, with their information, that have been deleted from module’s meta model but are still physically present in the database.%%The logged user needs to have the 'Administrator' built-in role.
[ModuleVersion_Delete](<#ModuleVersion_Delete>) | Deletes the specified module version of the specified module from the database.%%The logged user needs to have 'Change & Deploy' permissions.
[ModuleVersion_DeleteAll](<#ModuleVersion_DeleteAll>) | Deletes module versions that were published before the specified date and time. This action does not delete the module version that is currently published or module versions used in tagged versions of applications or solutions.%%The logged user needs to have 'Change & Deploy' permissions.
[ModuleVersion_ListOldest](<#ModuleVersion_ListOldest>) | Returns a list of module versions that are stored in the database and that were published before the specified date and time. This action does not return the module version that is currently published or module versions used in tagged versions of applications or solutions.%%The logged user needs to have 'Change & Deploy' permissions.

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


