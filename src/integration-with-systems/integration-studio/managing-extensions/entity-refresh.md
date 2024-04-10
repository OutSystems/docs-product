---
locale: en-us
guid: b6fd826d-d92b-4c58-870e-da6c7311fad8
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
summary: The article explains how to update an entity definition in Integration Studio by refreshing it from the database, which replaces the existing definition and retains only the entity name
---
# Refresh an Entity

Once an entity is [added to your extension](<entity-define.md>), the definition of the corresponding table is copied into Integration Studio: columns, data types, and descriptions are imported into the extension. If the table definition changes, for example, if a new column is created, you can refresh the entity definition and retrieve it again from the database.

<div class="info" markdown="1">

The entity definition in Integration Studio is replaced by the information available in the Database. Therefore, all the changes you have made to the entity will be lost. The only property that remains is the name of the entity.  

</div>

To refresh an entity definition:

* Right-click the **Entities** folder and select ![Context menu with 'Refresh Entity' option highlighted](images/refresh.gif "Refresh Entity Option") **Refresh Entity**. Integration Studio connects the database where the corresponding table is stored and fetches the new definition.

You must be [connected to the server](<../extension-life-cycle/server-connect.md>) where the extension will be deployed and hosted. The connection between Integration Studio and the database is established through the Platform Server.

If there are invalid attributes names, Integration Studio provides you with a warning where you can see which attributes are invalid. In this situation, the entity definition is refreshed but the invalid attributes are ignored.

![Lightbulb icon indicating a tip for importing multiple entities from the database](images/tip.gif "Import Entity from Database Tip") If you want to refresh the definition of several entities, you can use the [Import Entity from Database](<entity-import-from-database.md>) wizard.
