---
locale: en-us
guid: fa3cf5ad-5e7b-4fdd-acc5-7b3f6c43791e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=3065-134&t=0cuQUgeosMV2m0Kw-1
summary: Explore how OutSystems 11 (O11) manages resource properties and deployment actions in its Resource Editor.
tags: resource management, extension properties, deployment configuration, platform server directories, resource properties
audience:
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Resource Editor

The Resource Editor allows you to edit the properties of a resource that belongs to your extension. This editor is displayed when a resource is selected in the [Resources tree](<../resources-tree.md>) or in the [Multi-tab Editor](<../multi-tab-editors.md>).

## Resource Storage

The value of the Deploy Action property indicates where the resource is stored when the module that added a reference to this extension is published. The next table describes the possible values, their behavior, and in what types of files they should be used.  

|Deploy Action|Description|Files extensions|
|--- |--- |--- |
|Copy to Binaries directory|The resources are copied to the Platform Server where the module is published. The files are stored in the `bin2` directory, under the module directory.<br/>![Icon indicating a note related to storing files in the Binaries directory](images/note-icon.png "Note Icon") Files stored in this directory are not accessible through the Internet browser.|dll, config, manifest, jar|
|Copy to Application directory|The resources are copied to the Platform Server where the module is published. The files are stored in the module directory.|css, js, asmx, aspx|
|Copy to Images directory|The resources are copied to the Platform Server where the module is published. The files are stored in the `img` directory under the module directory.|bmp, eps, jpg, jpeg, gif, tiff, ico and other image format files|
|Ignore|The resources are not copied to the Platform Server. They belong to the extension but are not available in the server.|source files, documentation, etc.|

![Icon indicating a warning about changing the Deploy Action property](images/warning-icon.png "Warning Icon") You can change the Deploy Action property but this operation should be done with care because if a DLL or a JAR is not copied to the Binaries directory, the module won't be able to use the actions implemented by that DLL or JAR.

## Comparing with Template

Integration Studio has the necessary mechanisms for merging the changes in Integration Studio and the IDE (Integrated Development Environment), through the [Update Source Code](<../../../integration-with-systems/integration-studio/extension-life-cycle/extension-update-source-code.md>) operation.

The [Resources tree](<../resources-tree.md>) contains the ![Icon for the Compare With Template operation in the Resources tree](images/resource-compare-icon.png "Resource Compare Icon") Compare With Template operation, which allows you to compare the differences between the resource file, stored in the file system, and the template file.

To use this operation, you have to specify the "Compare files using" parameter in the [Options Window](<../menu/edit/options.md>).

![Icon suggesting a tip about using the Compare With Template operation](images/tip-icon.png "Tip Icon") The "Compare With Template" operation is very useful if the changes made in the extension elements are more complex and it becomes impossible to merge the two definitions. For example, if you changed the name of an element, it is not possible for the merge operation to relate the two elements.

## Change a Resource's Properties

You can change the properties of a resource at any time. Simply double-click in the resource in the [Resources tree](<../resources-tree.md>) or select the resource in the [Multi-tab editor](<../multi-tab-editors.md>), if the resource editor is already opened.

Import Details
:   This button is enabled when this resource was added due to [importing actions from a .NET assembly](<../../../integration-with-systems/integration-studio/managing-extensions/net-assembly-import-action.md>) and displays a report where you can check for additional information. The following information is displayed:

* Resource: Name of the resource with the following syntax:

    `Resource <resource_name>: <additional_information>`
