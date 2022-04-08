---
locale: en-us
guid: ae415dc5-20df-4cc4-9726-f02f47645ce8
---

# Add an Action

Once you have created your extension you may manually add the actions that you want to expose in the extension.

Once you define the actions and publish the extension, add a reference to these actions in Service Studio to [use them in the module](<../extension-life-cycle/extension-use.md>).

Do the following:

1. Right-click on the **Actions** folder in the Multi-tree Navigator and select ![](images/action.gif) **Add Action**.

1. Specify the following properties:

    * **Name**: Name of the action.
    * **Icon**: Icon associated with the action used in Service Studio to graphically identify this action.
    * **Description**: Description of the action.
    * **Function**: When set to `Yes`, allows you to use the action as a user function in Service Studio.

    For more details about these properties, see [Action Properties](<../../../ref/integration-studio/element-property/action.md>).

1. Specify the parameters of the action by editing them in the [Action Parameters](<action-parameter.md>) editor.

You can later change any of the action properties, in the [Action editor](<../../../ref/integration-studio/editor/action.md#import-details>).

Integration Studio also provides the [Import Actions from .NET Assembly](<net-assembly-import-action.md>) wizard that allows you to add several actions with less effort by using introspection.

## Web Services

When creating custom extensions to consume Web Services you can use the Import Actions from a .NET Assembly wizard, which supports Web Service proxies. Learn how to [Import Web Services from a .NET Assembly](<net-assembly-import-web-service.md>).
