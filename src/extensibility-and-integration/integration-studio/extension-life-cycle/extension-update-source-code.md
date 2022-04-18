---
locale: en-us
guid: 985d898a-a78b-4cb3-8628-8f9027631d7c
app_type: traditional web apps, mobile apps, reactive web apps
---

# Update the Extension Source Code

The Update Source Code operation synchronizes the source code you added in the .NET IDE with the definition of the extension elements. This operation involves the following steps:

1. **Generate the template files** according to the definition of your [actions](<../managing-extensions/action-define.md>), [structures](<../managing-extensions/structure-define.md>), and [entities](<../managing-extensions/entity-define.md>).

    If one of these files does not exist as an extension resource, then this operation implicitly adds the file as a resource, except when the extension does not contain any [source files](<../getting-started/extension-source-files.md>) at all.

1. **Update** the [extension implementation files](<../getting-started/extension-source-files.md>), according to the extension definition in Integration Studio.

    <div class="info" markdown="1">

    Any changes you have made directly in these files are overridden in this step.
    
    </div>

1. **Merge** the `<extension_name>.cs` file. This operation updates the signatures of the methods with the action definition, but it is applied only to the signatures: the body of the methods remains as is.

    <div class="info" markdown="1">

    Any changes you have made in the signatures of the methods directly in the IDE are overridden in this step.  
    
    </div>
  
## How to update the extension source code

In the **File** menu or in the toolbar, click ![](images/update-source-code.png) **Update Source Code** or ![](images/1-click-publish-icon.png) [**1-Click Publish**](<extension-1-cp.md>).

<div class="info" markdown="1">

The Update Source Code operation is also executed when you [edit source code](<extension-code-edit.md>) or [verify](<extension-verify.md>) the extension.

</div>

## Merge Algorithm

The merge algorithm is responsible for updating the source code with the changes made in the extension definition. The next steps describe the merge algorithm:

* Scan the source files that contain the signatures of the actions and, by name, verifies whether the signatures in these files are according to the action definition in Integration Studio.

    To perform this verification, Integration Studio compares the content of the actions template, generated previously, and `<extension_name>.cs`:

    1. If the signature in the template is the same as in the source file, then proceed to next action.

    1. If the signature in the template is different from the source file, then update `<extension_name>.cs` with the new definition as defined in the template.

    1. If the signature in the template does not exist in the source file, then add the new definition as defined in the template to `<extension_name>.cs`.

In some situations, the Merge algorithm might not be able to establish the correspondence between an element in the template file and in the source files, for example if you change an action name. In this situation, you should use the [Compare with Template](<../../../ref/integration-studio/editor/resource.md#comparing-with-template>) operation.
