---
locale: en-us
guid: 27ff9512-9516-45cd-9722-feb4690e5caa
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
summary: The Resources tree in Integration Studio displays and manages the files associated with an extension, including their addition, status, and physical location
---
# Resources Tree

The **Resources** tree, in the extension [workspace](<workspace.md>), presents the resources associated with the current extension and provides the necessary operations to manage them. In Integration Studio, resources are files that implement the behavior of the extension actions or any files that support other aspects of the extension, such as action icons and help files.

The resources of your extension can be added [explicitly](<../../integration-with-systems/integration-studio/managing-extensions/resource-define.md>) or automatically by Integration Studio in the following situations:

  * When the extension is [created](<../../integration-with-systems/integration-studio/extension-life-cycle/extension-create.md>), Integration Studio adds as resources the necessary [source files](<../../integration-with-systems/integration-studio/getting-started/extension-source-files.md>) for the development of the extension.

  * When you [import actions from a .NET assembly](<../../integration-with-systems/integration-studio/managing-extensions/net-assembly-import-action.md>), the assembly and its dependencies are added as resources, as well as the ![Icon representing an imported .NET action in Integration Studio](images/imported-action.gif "Imported .NET Action Icon") `DotNetAction.ico`, if it hasn't been added before.

## Resource Status

A resource has the following possible statuses:

Excluded ![Icon indicating a resource is excluded from the extension in Integration Studio](images/resource-faded.gif "Excluded Resource Icon")
:   The file exists in the File System but was not added as a resource. If you want to include this resource, see [Add a Resource](<../../integration-with-systems/integration-studio/managing-extensions/resource-define.md>).

Included ![Icon indicating a resource is included in the extension in Integration Studio](images/resource-add.gif "Included Resource Icon")
:   The file was already added as a resource and there were no changes since the last save of the extension.

Modified ![Icon indicating a resource has been modified in Integration Studio](images/resource-modified.gif "Modified Resource Icon")
:   The file was already added as a resource but there were changes since the last save of the extension. You should save the extension in order to refresh the status of the resource.

Deleted ![Icon indicating a resource has been deleted from the file system in Integration Studio](images/resource-broken.gif "Deleted Resource Icon")
:   The file was added as resource but no longer exists in the File System.

## Resources' physical location

The resources are stored in a directory, called `<extension_file_name>/<NET>`, under the directory where the XIF (Extension and Integration Framework) file was saved. The first time the extension is created, these resources are stored in a temporary directory until you save the extension.

To open the directory that contains the resources, simply right-click in the Resources folder icon and select the Open option.

![Icon used to denote a note or important information in Integration Studio documentation](images/note.gif "Note Icon") After the first save or "save as...", the resources will be moved to the `<extension_file_name>/Source/<NET>`, under the directory where the XIF file was saved.

## Extension operations

In the Resources tree, the following operations are available to handle your resources:

Operation | Description
:--------:|:-----------
![Icon for the operation to include a resource in the extension in Integration Studio](images/resource-include.gif "Include Resource Icon") Include in Extension | Adds the resource to the extension.<br/>For more information, see [Add a Resource](<../../integration-with-systems/integration-studio/managing-extensions/resource-define.md>).
![Icon for the operation to exclude a resource from the extension in Integration Studio](images/resource-exclude.gif "Exclude Resource Icon") Exclude from Extension | Removes the resource from the extension. The next time the extension is saved, this resource file is not packed in the XIF file.
Open | Opens the item you selected on the Resources tree.<br/>If a folder is selected, then Windows Explorer is launched in the corresponding folder.<br/>If a file is selected, the default program associated with that file type is launched and the file is opened.
![Icon for the operation to compare a resource with a template in Integration Studio](images/resource-compare.gif "Compare Resource Icon") Compare with Template | Allows you to compare the differences between the resource file, stored in the file systems, and the template file.<br/>For more information, see [Resources Editor](<editor/resource.md>).
