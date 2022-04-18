---
locale: en-us
guid: 52c8b0c4-1091-41d6-8c68-a19938e1547f
app_type: traditional web apps, mobile apps, reactive web apps
---

# Extension Life Cycle

The integration process revolves around the extension life cycle. The process steps are executed in both OutSystems  and third party IDE component environments. The illustration below depicts the most significant steps, showing them next to the component where they are executed. 

![](<images/extension-life-cycle.png>)

These are the generic steps that you should take to implement and use a extension in OutSystems:

1. In **Integration Studio**, [create a new extension module](<extension-create.md>) and set its name and the supported DBMS.

1. [Define the new actions](<extension-define.md>) that encapsulate your code. Also define any input and output parameters for your action(s), as well as any entities or structures.

1. Generate the stubs for the declared actions and edit the code implementing the logic of the actions using a **third-party IDE** for .NET.

    Integration Studio provides the necessary facilities to integrate with the IDE you specified in Integration Studio [options](<../../../ref/integration-studio/menu/edit/options.md>), enabling you to:

    * [Implement the logic  of your actions](<extension-code.md>) using the IDE
    * [Edit the extension source code](<extension-code-edit.md>) using the IDE
    * [Update the extension source code](<extension-update-source-code.md>) with the extension definition in order to reflect the changes you have made in Integration Studio

    If your extension does not contain [manually added](<../managing-extensions/action-add.md>) actions, you can skip this step. However, the extension will still have source code files associated. See [Extension Source Files](<../getting-started/extension-source-files.md>) for more information.

1. [Publish the extension module](<extension-1-cp.md>) to the Platform Server from Integration Studio by clicking ![](images/1-click-publish-icon.png) **1-Click Publish** in the **File** menu or Toolbar.

1. [Use the created extension](<extension-use.md>) in any OutSystems applications where you want to use it, adding it as a dependency in **Service Studio**. Once the extension module is a dependency of your application, the logic that the module implements becomes available in the Logic tab of Service Studio.
