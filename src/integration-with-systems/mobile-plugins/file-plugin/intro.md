---
summary: OutSystems 11 (O11) File Plugin enables file and folder management within mobile app sandboxes.
tags: file management, plugin integration, mobile app development, binary data handling, outsystems forge
locale: en-us
guid: 77c53fcc-d787-4377-895f-90390ee33f3f
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/design/jSgZ0l0unYdVymLxKZasno/Integration-with-external-systems?node-id=611-0
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - forge
coverage-type:
  - understand
  - apply
  - remember
topic:
  - using-cordova-plugins
---

# File Plugin version 4

<div class="info" markdown="1">

If you are looking for information about version 3.X of the File Plugin, refer to the [Version 3 documentation](file-plugin-version-3.md).

</div>

<div class="info" markdown="1">

The File Plugin version 4.0.0 is a major revamp of the Plugin, and includes many changes in the plugin's logic. If you are using an older version and are looking to update to 4.0.0, refer to [the migration guide](file-plugin-migration-guide.md) for more information.

</div>

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

<div class="info" markdown="1">

See [Adding plugins](../intro.md#adding-plugins) to learn how to install and reference a plugin in your OutSystems apps, and how to install a demo app.

</div>

File Plugin lets you manage files and folders on a mobile device within the app sandbox.

## Sample app

Install [File Sample App](https://www.outsystems.com/forge/component-overview/10011/file-sample-app) from Forge and open the app in Service Studio. The sample app contains logic for common use cases, which you can examine and recreate in your apps. For example, the sample app shows how to:

* Handle files - Read, Write, Delete, Copy.
* List directories.
* Create and delete directories.
* Integration with other OutSystems Plugins like Camera, File Viewer, and File Transfer.
* Test deprecated actions (deprecated since File Plugin version 4.0.0)

![Screenshot of the File Sample App interface showing file management features](images/sample-v4-app.png "File Sample App Interface")

## Working with binary content

File Plugin in some actions requires parameters of the binary data type. To convert data to binary you have two choices:

* [BinaryData extension](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/BinaryData_API) is an official and supported extension. The BinaryData extension exposes server Actions and **requires a connection to the server** when it runs one of the actions from the BinaryData extension. This extension doesn't work offline.
* [BinaryData Client Side](https://www.outsystems.com/forge/component-overview/3242/binarydata-client-side) is a Forge plugin contributed by the OutSystems community and it's not officially supported. Actions in this plugin run in the client, and your app can **use them while offline**.

## Examples

Here are some examples of how to use File Plugin.

### Store some text in a file

The **WriteFile** requires a binary input, so you need to convert the text to binary first. Use the **TextToBinaryData** (1) action from the **BinaryData** extension (you need to reference the **BinaryData** extension first).

You can then use the **WriteFile** action from **Logic** > **Client Actions** > **FilePlugin** to create a file and save text (2). Set the **PathDirectory** and relative path to the file, along with the **Binary Data** (3).

Finally, check the result of **WriteFile**. If **Success** is true, it means the file was saved successfully. Otherwise, you can show the returned **Error** (4).

![Step-by-step illustration of saving text in a file using the WriteFile action in OutSystems](images/save-text-in-file-mobile-v4-ss.png "Save Text in File Process")

<div class="info" markdown="1">

Refer to [Working with binary content](#working-with-binary-content) for more information on using **BinaryData**.

</div>

### Copy a file

Imagine that you want to copy the file [you stored previously](#store-some-text-in-a-file) - You can use the **Copy** action from **Logic** > **Client Actions** > **FilePlugin** (1). Pass the relative path and **PathDirectory** of the file you want to copy in **FromPath** and **FromDirectory**, respectively (2). In this example, the copied file will be in the same **PathDirectory**, so only **ToPath** is specified. You can provide a different **ToDirectory** if you'd like to copy a file to an entirely different location.

Finally, check the result of **Copy**. If Success is true, it means the file was copied successfully. Otherwise, you can show the returned Error (3).

![Example of copying the previously saved file to another location using the Copy action in OutSystems](images/copy-file-mobile-v4-ss.png "Copy File Process")

### Get the list of files

Use the **ListDirectory** action from **Logic** > **Client Actions** > **FilePlugin** to get the list of the files (1). In this example, we want to list all the contents of in the **TEMPORARY** directory - passing an empty path to indicate we want the contents at the root of the temporary directory (2).

You can check if **ListDirectory** has **Success** equal to true. If so, proceed to the next step. Otherwise, you can show the returned Error (3).

The **ListDirectory** returns both files and sub-directories inside that directory. To get only the files, we can use the **ListFilter** action on the **Result** from **ListDirectory** and filter for **Type = Entities.PathType.File** (4).

Then, assign the **FilteredList** to a variable to use in your UI (5).

![Example of listing files in a directory using the ListDirectory action in OutSystems](images/list-files-mobile-v4-ss.png "List Files in Directory")

## References

For more information on the plugin elements, refer to the [File Plugin version 4 reference page](./file-plugin-ref.md).
