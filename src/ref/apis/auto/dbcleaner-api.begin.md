---
summary: Allows freeing-up database space.
tags: support-application_development; support-Database
---

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
