---
summary: OutSystems 11 (O11) File Plugin enables file and folder management within mobile app sandboxes.
tags: file management, plugin integration, mobile app development, binary data handling, outsystems forge
locale: en-us
guid: 86ebad43-0937-4450-bfe9-8b06655edfd7
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/design/jSgZ0l0unYdVymLxKZasno/Integration-with-external-systems?node-id=3980-79
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

# File Plugin version 3

<div class="info" markdown="1">

[Version 4.0.0 of the File Plugin](intro.md) introduces significant updates to its core logic and functionality. If you are currently using version 3.x or below and plan to upgrade to 4.0.0, be sure to review [the migration guide](file-plugin-migration-guide.md) for detailed instructions and changes.

</div>

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

<div class="info" markdown="1">

See [Adding plugins](../intro.md#adding-plugins) to learn how to install and reference a plugin in your OutSystems apps, and how to install a demo app.

</div>

File Plugin lets you manage files and folders on a mobile device within the app sandbox.

## Demo app

Install [File Demo App](https://www.outsystems.com/forge/component-overview/10011/file-sample-app) from Forge and open the app in Service Studio. The demo app contains logic for common use cases, which you can examine and recreate in your apps. For example, the demo app shows how to:

* Read a file
* List files
* List folders
* Save text in temporary file

![Screenshot of the File Demo App interface showing file management features](images/sample-v3-app.png "File Demo App Interface")

## Working with binary content

File Plugin in some actions requires parameters of the binary data type. To convert data to binary you have two choices:

* [BinaryData extension](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/BinaryData_API) is an official and supported extension. The BinaryData extension exposes server Actions and **requires a connection to the server** when it runs one of the actions from the BinaryData extension. This extension doesn't work offline.
* [BinaryData Client Side](https://www.outsystems.com/forge/component-overview/3242/binarydata-client-side) is a Forge plugin contributed by the OutSystems community and it's not officially supported. Actions in this plugin run in the client, and your app can **use them while offline**.

## Examples

Here are some examples of how to use File Plugin.

#### Store some text in a file

The **SaveFile** requires a binary input, so you need to convert the text to binary first. Use the **TextToBinaryData** (1) action from the **BinaryData** extension (you need to reference the **BinaryData** extension first). You can then use the **SaveFile** action from **Logic** > **Client Actions** > **FilePlugin** to create a file and save text (2). Set the file name and the path in the properties (3).

![Step-by-step illustration of saving text in a file using the SaveFile action in OutSystems](images/save-text-in-file-mobile-v3-ss.png "Save Text in File Process")

<div class="info" markdown="1">

Refer to [Working with binary content](#working-with-binary-content) for more information.

</div>

#### Get the list of files

Use the **ListDirectory** action from **Logic** > **Client Actions** > **ListDirectory** to get the list of the files (1). The file names are in the list **ListDirectory.FileList** (2).

![Example of listing files in a directory using the ListDirectory action in OutSystems](images/list-files-mobile-v3-ss.png "List Files in Directory")

## Reference

More information about parts of the plugin.

### Actions

Here is the reference of the actions you can use from the File Plugin. File Plugin uses a Cordova plugin, and for more information check [cordova-plugin-file](https://github.com/OutSystems/cordova-plugin-file).

| Action                 | Description                                                       |
| ---------------------- | ----------------------------------------------------------------- |
| **CheckFilePlugin**    | Enables to check if the plugin was loaded.                        |
| **CreateDirectory**    | Recursively creates a directory in the file system.               |
| **DeleteDirectory**    | Deletes a directory and all its content in the file system.       |
| **DeleteFile**         | Deletes a single file.                                            |
| **DeleteFileFromUri**  | Deletes a single file from a URI address.                         |
| **GetFileData**        | Returns the binary file encoded in Base64.                        |
| **GetFileDataFromUri** | Returns the binary file encoded in Base64 from a file's URI path. |
| **GetFileUri**         | Returns the file's URI path.                                      |
| **GetFileUrl**         | Returns the file's blob URL path (blob://).                       |
| **GetFileUrlFromUri**  | Returns the file's blob URL path from a file's URI path.          |
| **ListDirectory**      | Lists the directory's content.                                    |
| **SaveFile**           | Saves a file in a specific directory.                             |
| **SaveTemporaryFile**  | Saves a file in a temporary directory.                            |

## Storage type

Information about the **StorageTypeId** property, which tells the app where to store the files. This property is available in some of the actions of the plugin. 

| StorageTypeId                     | Description                                                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Entities.StorageType.Internal** | Sandboxed app data in the internal memory. Corresponds to Cordova's **cordova.file.dataDirectory**.             |
| **Entities.StorageType.External** | App data on an external storage. Corresponds to Cordova's **cordova.file.externalDataDirectory**. Android only. |

For more information check out the document [Where to Store Files](https://github.com/OutSystems/cordova-plugin-file#where-to-store-files) from Cordova.
