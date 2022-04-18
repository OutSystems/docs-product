---
locale: en-us
guid: c3a15acb-2ada-4d0b-93f8-e897e74752fb
app_type: traditional web apps, mobile apps, reactive web apps
---

# Create an Extension

Integration Studio enables you to create an extension — a set of **Actions**, **Entities**, and **Structures** available in Service Studio but implemented in third-party technologies. An extension can be [used in any module](<../extension-life-cycle/extension-use.md>) after it's published in the Platform Server.

To publish a new extension you must be granted the "Change & Deploy Applications" permission.

If you don't have LifeTime installed in your infrastructure, User Management is done in Service Center. In this case, to publish a new extension you must be granted the "Allow Extensions" permission. The "Allow Foreign Entities" permission is also required if your extension exports entities.

## How to create an extension

1. In the **File** menu or in the toolbar, click ![](images/new.png) **New**.

1. Provide the information in the **Connect to Environment** window and click **Connect**. This step is required only once per session.  

1. Specify the values for the following properties:

    * **Name**: name of the extension.
    * **DBMS**: indicates the Database Management System (DBMS) type that the extension is prepared to work with.
    * **Description**: description of the extension.

You can later change the properties in [Extension Editor](<../../../ref/integration-studio/editor/extension.md>).

## Extension Elements

After creating the extension, you define [actions](<../managing-extensions/action-define.md>), [structures](<../managing-extensions/structure-define.md>), [entities](<../managing-extensions/entity-define.md>), and [resources](<../managing-extensions/resource-define.md>) that correspond to the elements exported by the external component you are using.

Integration Studio automatically creates the necessary [source files](<../getting-started/extension-source-files.md>) that allow you to start developing the behavior of the actions. You can check them in the [Resources](<../../../ref/integration-studio/resources-tree.md>) tree of this extension.
