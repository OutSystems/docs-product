---
locale: en-us
guid: e7143ce0-e179-48f5-a85c-91a174f36eba
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Define Resources

Once you have created your extension, you can define the resources that your extension requires. Integration Studio displayes the resources of your extension in the [Resources tree](<../../../ref/integration-studio/resources-tree.md>).

All these resources are packed in the XIF (Extension and Integration Framework) file when the extension is saved.

Resources can be added implicitly by Integration Studio. You can also add any file as a resource of your extension (for example, icons associated with the extension actions or help files that must be available for Service Studio developers).

When creating a new extension or updating the extension source code, Integration Studio implicitly adds the source files as resources, which are generated based on the template files. For more information, see [Extension Source Files](<../getting-started/extension-source-files.md>).  

To add a resource do the following:

1. Copy the file you want to add to the resources directory. Once the file is copied, the status of the resource, in the [Resources tree](<../../../ref/integration-studio/resources-tree.md>), is ![](images/resource-faded.gif) **Excluded**.

    **Tip:** To determine the resources directory, right-click the **Resources** icon and select **Open**.

1. Right-click this file and select ![](images/resource-include.gif) **Include in Extension**. Once the file is added as resource, the status is ![](images/resource-add.gif) **Included**.

1. Specify the following properties:

    * **Name**: Name of the resource.
    * **Last Modified**: Read-only property that indicates the date and time when the resource was last modified since the last save.
    * **Deploy Action**: Indicates where, in the Platform Server, the resource is stored when the module that added the extension is published.
    * **Description**: Description of the resource.

![](images/tip.gif) The [Resource editor](<../../../ref/integration-studio/editor/resource.md>) allows you to later change the resource properties.

<div class="info" markdown="1">

When including a DLL (Dynamic Link Library) file as a resource of your extension, beware of a possible name clash between the resource filename and the name of an application module.

For example, you may get runtime issues if you include a resource named `MyResource.dll` in your extension while also having an application module named `MyResource` in the app that uses the extension. Since OutSystems generates a `MyResource.dll` file for this module, the extension resource file might get overwritten, depending on the publishing method you use (1-Click Publish operation or solution publish).

To prevent this, you should rename the application module so that there's no clash between the extension resource filename and the module name.

</div>
