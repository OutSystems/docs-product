---
summary: 'File Plugin 4.0.0 migration in OutSystems 11 (O11): map deprecated v3 actions to new ones, handle PathDirectory, and ensure OTA-safe upgrades.'
tags:
  - Mobile app
  - Native App
  - Plugins
locale: en-us
guid: c49995b1-cff9-48fb-ad82-c4d02e3dce66
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/design/jSgZ0l0unYdVymLxKZasno/Integration-with-external-systems?node-id=3944-26
audience:
  - Developer
outsystems-tools:
  - service studio
coverage-type:
  - remember
  - apply
isautopublish: true
---

# File plugin migration guide from version 3 to version 4

This guide is intended for developers transitioning from the older version of the OutSystems File Plugin, [v3.X.X](file-plugin-version-3.md), to [version 4.0.0](intro.md). After updating the plugin, you can choose between the following paths:

* [Continute using the same actions from 3.X.X, that have since been marked as deprecated](#deprecated-client-actions).
* [Migrate from the deprecated actions to the new client actions](#migrating-client-actions).
* [Check at runtime which actions are safe to use, so your logic keeps working even on apps that haven't been rebuilt with the new native plugin yet](#check-native-plugin).

Choose the path that fits your app's situation:

* If you don't need the new plugin's capabilities yet, or don't want to invest in migrating right now, [staying on the deprecated actions](#deprecated-client-actions) requires the least effort. The deprecated actions keep working indefinitely.
* If you want to use new plugin functionality and can guarantee that every installed copy of your app will be rebuilt with the new native plugin, for instance because you fully control app distribution and can force an update, [migrating the client actions](#migrating-client-actions) is the most direct path.
* If you want to use new plugin functionality but your app can receive over-the-air (OTA) updates that reach users before a new native build does, [checking at runtime](#check-native-plugin) is the safest way to migrate your logic to new actions without breaking apps that haven't been rebuilt yet.

## Deprecated client actions {#deprecated-client-actions}

All client actions from version 3.X.X and below have been marked as deprecated, and it's recommended to use the new actions added in plugin version 4.0.0.

If however, you are updating the plugin in an existent app, and don't want to go through the effort of migrating client actions, you can keep using the deprecated actions for the time being, whose input/output remain the same.

<div class="info" markdown="1">

When you update to version 4.0.0 on Service Studio, you will keep using the client actions from the previous version, but they'll prefixed with **DEPRECATED_**. For instance, the **DeleteFile** of version 3.X.X is now **DEPRECATED_DeleteFile** in version 4.0.0.

</div>

## Migrating client actions {#migrating-client-actions}

The new client actions have a different structure - some have different names, others different inputs and outputs. There are also client actions that provide new functionality that wasn't available before in the plugin (for example, **Copy**).

<div class="warning" markdown="1">

If you migrate to the new client actions when updating to version 4.0.0, they work only after you generate a new mobile package for both Android and iOS. If your app can't guarantee that every installed copy has been rebuilt, for instance because it can receive over-the-air (OTA) updates, refer to [Check the native plugin version before using new actions](#check-native-plugin) for how to migrate your logic without breaking those installs.

</div>

This section will further detail which client actions replace the deprecated ones, and any additional changes that may be required to migrate to the new client actions.

### Client action mapping {#client-action-mapping}

| Deprecated Action | New Action to use | Migration notes |
| ----------------------------- | ------------------- | ----------------------------- |
| DEPRECATED_CheckFilePlugin | **CheckFilePlugin** | The new plugin action can return either an **Error** or a **Warning**. See [Check the native plugin version before using new actions](#check-native-plugin) below for what a **Warning** means and how to handle it. |
| DEPRECATED_CreateDirectory | **CreateDirectory** | For migrating from the deprecated **StorageType** and **StoragePersistency** to the new **PathDirectory**, [see the section below](#storage-persistence-pathdirectory). |
| DEPRECATED_DeleteDirectory | **DeleteDirectory** | For migrating from the deprecated **StorageType** and **StoragePersistency** to the new **PathDirectory**, [see the section below](#storage-persistence-pathdirectory). |
| DEPRECATED_DeleteFile | **DeleteFile** | For migrating from the deprecated **StorageType** and **StoragePersistency** to the new **PathDirectory**, [see the section below](#storage-persistence-pathdirectory). |
| DEPRECATED_DeleteFileFromUri | **DeleteFile** | Provide the Uri in the **Path** input parameter, and leave **Directory** empty. |
| DEPRECATED_GetFileData | **ReadFile** | For migrating from the deprecated **StorageType** and **StoragePersistency** to the new **PathDirectory**, [see the section below](#storage-persistence-pathdirectory). |
| DEPRECATED_GetFileDataFromUri | **ReadFile** | Provide the Uri in the **Path** input parameter, and leave **Directory** empty. |
| DEPRECATED_GetFileUri | **GetFileUri** | For migrating from the deprecated **StorageType** and **StoragePersistency** to the new **PathDirectory**, [see the section below](#storage-persistence-pathdirectory). |
| DEPRECATED_GetFileUrl | **ReadFile** | The new **ReadFile** does not return blob URL's. You may keep using the deprecated action for the time being, or refer to [Create a blob URL](#create-blob-url) to accomplish the same behavior in your app. |
| DEPRECATED_GetFileUrlFromUri | **ReadFile** | The new **ReadFile** does not return blob URL's. You may keep using the deprecated action for the time being, or refer to [Create a blob URL](#create-blob-url) to accomplish the same behavior in your app. |
| DEPRECATED_ListDirectory | **ListDirectory** | For migrating from the deprecated **StorageType** and **StoragePersistency** to the new **PathDirectory**, [see the section below](#storage-persistence-pathdirectory). |
| DEPRECATED_SaveFile | **WriteFile** | You may instead use **AppendFile** if you're saving to the end of an existing file and you don't want to overwrite it. For migrating from the deprecated **StorageType** and **StoragePersistency** to the new **PathDirectory**, [see the section below](#storage-persistence-pathdirectory). |
| DEPRECATED_SaveTemporaryFile | **WriteFile** | You may instead use **AppendFile** if you're saving to the end of an existing file and you don't want to overwrite it. For migrating from the deprecated **StorageType** and **StoragePersistency** to the new **PathDirectory**, [see the section below](#storage-persistence-pathdirectory). |

### Storage persistence and type to path directory {#storage-persistence-pathdirectory}

In the deprecated client actions, the way you specify the full path to a file was via a combination of four parameters:

* **Name**: The file name.
* **Path**: Relative path to the directory that contains the file.
* **StorageTypeId**: Android only - Identifies the type of storage system - Internal or External.
* **StoragePersistenceId**: Either Persistent or Temporary storage system.

The combination of **StorageType** and **StoragePersistence** map to a specific location in the device's filesystem.

In the new client actions introduced in version 4.0.0, you now use a **Path** and a **Directory** parameter. The new **Path** is a combination of **Name** + **Path** in the deprecated actions - for instance, **Name**="file.txt" and **Path**="directory" should now translate to **Path**="directory/file.txt". The new **Directory** is of type **PathDirectory**, and it encompasses all combinations of **StorageType** and **StoragePersistence**, while also providing additional locations in the storage system that weren't previously available in the OutSystems Plugin. The [reference page](file-plugin-ref.md) describes each type of **PathDirectory**.

If you have been using File Plugin actions apart from the **(...)FromUri** ones, you'll need to use the appropriate **PathDirectory** value in the new actions to achieve the same behavior, that is, accessing the files at the same locations in previous plugin versions in both Android and iOS. Here's how you can migrate to the new **PathDirectory** parameter from the deprecated **StorageType** and **StoragePersistence**:

1. For **StorageType.Internal** and **StoragePersistence.Persistent** (default for **DEPRECATED_SaveFile**) - use **PathDirectory.LIBRARY_NO_CLOUD**.
1. For **StorageType.Internal** and **StoragePersistence.Temporary** (default for **DEPRECATED_SaveTemporaryFile**) - use **PathDirectory.TEMPORARY**.
1. For **StorageType.External** and **StoragePersistence.Persistent** - there is no direct equivalent **Directory** parameter to achieve the same behavior in both Android and iOS. Android uses **Directory.External**, while iOS uses **PathDirectory.LIBRARY_NO_CLOUD**. If your app targets both platforms, you'll need logic to detect which platform you are on, and pass the appropriate **Directory** value on each case. You can accomplish this with the [Common Plugin](https://www.outsystems.com/forge/component-overview/1417/common-plugin-o11). The screenshot below illustrates how to do it in Service Studio.
    * Use **GetOperatingSystem** client action (1) and check **OperatingSystemsId** output parameter (2), using **PathDirectory.EXTERNAL** if it's **OperatingSystemsId.Android**, and use **PathDirectory.LIBRARY_NO_CLOUD** otherwise (3); you may assign it to a local variable to then use it in a File Plugin action. For example, **WriteFile** (4).

    ![Example for migrating from StorageType.External and StoragePersistence.Persistent to the new PathDirectory parameter, using the Common Plugin and GetOperatingSystem action](images/migration-use-common-plugin-ss.png "Common Plugin GetOperatingSystem in Service Studio")

1. For **StorageType.External** and **StoragePersistence.Temporary** - Android uses **PathDirectory.EXTERNAL_CACHE**, while iOS uses **PathDirectory.TEMPORARY**. If you're targetting both platforms, you'll need logic to distinguish between the two, as mentioned above.

### Create a blob URL {#create-blob-url}

The new **ReadFile** method returns file data as **BinaryData**, similarly to the **DEPRECATED_GetFileData**. If you want to obtain a Blob URL from **ReadFile**, (to replace **DEPRECATED_GetFileUrl**), you'll have to add some logic in your app. The screenshot below illustrates what is necessary to create a Blob URL.

After calling **ReadFile** (1), you should convert the **BinaryData** to a Base64 **Text**, which you can do for instance via [BinaryData extension's](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/BinaryData_API) **BinaryToBase64** (2). Then, add a JavaScript Block (3) that receives **BinaryToBase64.Base64**. Inside the JavaScript block - named **ConvertToBlobURL** in this example - is where you convert the data to a blob URL (4). Then you can assign the output of **ConvertToBlobURL** to a variable (5).

![Example for migrating from DEPRECATED_GetFileUrl to ReadFile, and converting the BinaryData to a Blob URL](images/migration-get-blob-url-ss.png "Use ReadFile action and get a Blob URL")

Below is the code used in the JavaScript block:

```javascript
// Decode the Base64 data
let binaryString = atob($parameters.FileData);
// create an array of binary data
let binaryArray = new Uint8Array(
    Array.from(binaryString, char => char.charCodeAt(0))
);
// Create a Blob object from the binary data
let blob = new Blob([binaryArray], { type: 'application/octet-stream' });

// Generate and return the Blob URL
$parameters.BlobURL = URL.createObjectURL(blob);
```

### Error handling {#error-handling}

For brevity, the examples above obtained the result directly from the client action. However, it's recommended to check that the action was successful before trying to retrieve the result.

In the deprecated actions, you do this by checking if the **Error.ErrorCode** returned by the action is **0**.

In the new client actions, a separate **Success** Boolean is added, which you should check if it's **true** before proceeding; if it's **false**, then you may look at the **Error** structure for information on what went wrong. For the list of error codes made available since version 4.0.0, see the plugin's [reference page](./file-plugin-ref.md).

## Check the native plugin version before using new actions {#check-native-plugin}

If you update your logic to use the new client actions, but the mobile app installed on a user's device hasn't been rebuilt since you updated the plugin, the new client actions won't work on that device. This happens, for example, when the app only received an over-the-air (OTA) update to its web layer. The native side of that app still has the pre-4.0.0 plugin, which doesn't implement them.

Call **CheckFilePlugin** before relying on the new actions, and check its output:

* If **IsAvailable** is **True**, the new client actions are available and safe to use.
* If **IsAvailable** is **False**, check **Warning.WarningCode**. **OS-PLUG-FILE-0002** means the installed native plugin is still the pre-4.0.0 version. In this situation, use the **DEPRECATED_** client actions instead. They keep talking to the plugin version already installed on the device, and keep working for as long as apps built with that older native plugin are still in use.

This runtime check combines the two paths described above into a single piece of logic: your app uses the new client actions when they're available, and automatically falls back to the deprecated ones when they aren't.

<div class="info" markdown="1">

Before version 4.1.3 of the File plugin, this check wasn't reliable. In this exact scenario, **CheckFilePlugin** incorrectly returned an **Error** with code [OS-PLUG-FILE-0003](https://www.outsystems.com/tk/redirect?g=dea144e5-b34a-4cb1-8dcb-beab6ac5f3e0) instead of a **Warning** with code [OS-PLUG-FILE-0002](https://www.outsystems.com/tk/redirect?g=9928cd76-530f-4368-8bc7-2825a9e5a9a3). This was fixed in version 4.1.3. Update to this version, especially if you can't have your users all update to the new native build.

</div>

<div class="info" markdown="1">

This check doesn't need to be permanent. Once you can confirm that your entire installed base has been rebuilt with the new native plugin, for instance after enough time has passed for old app versions to phase out, you can remove the check and call the new client actions directly, the same as if you'd migrated outright.

If your entire installed base already has the new native plugin, you don't need to add this check at all. You can update your logic to use the new client actions whenever you're ready.

</div>

## Related resources {#related-resources}

* [File Plugin version 4](intro.md)
* [File Plugin version 4 reference page](file-plugin-ref.md)
* [File Plugin version 3](file-plugin-version-3.md)
