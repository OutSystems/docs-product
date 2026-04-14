---
summary: Understand the changes in Camera Plugin 8.0.0 in OutSystems 11 (O11), and how to migrate to it from older versions.
tags: mobile app development, plugin integration, error handling, camera, migration, breaking changes
locale: en-us
guid: d64d2ff0-e554-4bdc-8769-a038f4eb7c35
app_type: mobile apps
platform-version: o11
figma:
audience:
  - mobile developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
isautopublish: true
---

# Migrating Camera Plugin from version 7 to version 8

If you are currently using version 7.X.X of the OutSystems Camera Plugin and planning to upgrade to version 8.0.0, this article walks you through the key changes and steps needed for a smooth migration. You will learn which actions and blocks have been updated or removed, understand new error handling requirements, and discover best practices to quickly adapt your mobile app to the latest Camera Plugin release.

## What changed in version 8

<div class="info" markdown="1">

For the full release notes, including new features, bug fixes and other improvements please check the [Forge page](https://www.outsystems.com/forge/component-overview/1390/camera-plugin-o11).

In case you have any questions or run into issues, please contact OutSystems support so that you may get the proper assistance.

</div>

Camera Plugin version 8.0.0 introduces changes that may require action when migrating from version 7.X. The changes include:

### Removed client actions

* **DEPRECATED_ChooseGalleryPicture** - Migrate to **ChooseFromGallery**. For more information refer to [this section](#migrating-from-deprecated_choosegallerypicture-client-action).
* **DEPRECATED_TakePicture** - Migrate to **TakePhoto**. For more information refer to [this section](#migrating-from-deprecated_takepicture-client-action).

### Removed UI blocks

* **DEPRECATED_ChooseImage** - Migrate to **ChooseFromGallery** block. For more information refer to [this section](#migrating-from-deprecated_chooseimage-block).
* **DEPRECATED_TakePicture** - Migrate to **TakePhoto** block. For more information refer to [this section](#migrating-from-deprecated_takepicture-client-action).

### Changes in parameters

* **TakePhoto** block now requires an **OnError** event to be implemented. More information on [this section](#handling-errors-in-takephoto-block).
* **AllowMultiplePictures** parameter removed from **TakePhoto** block, as it had no effect (still available in **TakePhoto** client action as **AllowMultiplePhotos**).

### Error code changes

* Error codes have been restructured and renumbered. Refer to [Updating error code handling](#updating-error-code-handling).

### Minor changes

Besides these changes, you may notice when upgrading that some client action and parameters have different names. The name change is to better separate from the deprecated client actions that were removed. This does not require any changes on your side, it is merely informative:

* **TakePicture** is now **TakePhoto**
* **EditPicture** is now **EditPhoto**
* **EditURIPicture** is now **EditURIPhoto**
* **SaveToPhotoAlbum** parameter is now **SaveToGallery**
* **AllowMultiplePictures** is now **AllowMultiplePhotos**

## Migrating from removed client actions and blocks

### Migrating from DEPRECATED_TakePicture client action

If you're using the **DEPRECATED_TakePicture** client action, replace it with **TakePhoto** (previously **TakePicture** in versions older than 8).

#### Key differences

* Parameter **SaveToPhotoAlbum** is now **SaveToGallery**.
* Parameter **AllowMultiplePictures** is now **AllowMultiplePhotos**.
* Output parameter **ImageCaptured** structure is now **MediaResult** structure.
* The other parameters should exist as in the removed client action.

To update your logic from **DEPRECATED_TakePicture** to **TakePhoto**, follow these migration steps:

1. Replace **DEPRECATED_TakePicture** with **TakePhoto** in your logic flow.

1. Update parameter names, if you are using them:
    * Replace **SaveToPhotoAlbum** with **SaveToGallery**.
    * Replace **AllowMultiplePictures** with **AllowMultiplePhotos**.

1. Update output handling:
    * Replace references to **ImageCaptured** with **MediaResult**.
    * Access the photo data using **MediaResult.Thumbnail** (instead of **ImageCaptured** binary data).
    * The **MediaResult** structure has other attributes that may be relevant, refer to the [reference article](camera-ref.md#mediaresult-data-structure) for more information.

### Migrating from DEPRECATED_ChooseGalleryPicture client action

If you're using the **DEPRECATED_ChooseGalleryPicture** client action, replace it with **ChooseFromGallery**.

#### Key differences

* Output parameter **ImageCaptured** structure is now a list of **MediaResult** structures.
* New input parameters available: **MediaType**, **AllowMultipleSelection**, **Limit**, and **IncludeMetadata**.
* The new client action works in PWAs, albeit with limitations.

To migrate from the deprecated client action, follow these steps:

1. Replace **DEPRECATED_ChooseGalleryPicture** with **ChooseFromGallery** in your logic flow.

1. Update the **MediaType** parameter:
    * Set **MediaType** to **Entities.MediaType.Photo** to maintain the same behavior as the deprecated action.

1. Update output handling:
    * **ChooseFromGallery.MediaResult** is a list. Access the first item's photo with **ChooseFromGallery.MediaResult.Current.Thumbnail**
    * The **MediaResult** structure has other attributes that may be relevant, refer to the [reference article](camera-ref.md#mediaresult-data-structure) for more information.

1. If you want to allow multiple item selection, set **AllowMultipleSelection** to **True** and iterate through the **MediaResult** list (not currently available in PWAs).

1. If you want to also select videos you can use **Entities.MediaType.Both** in the new client action (not currently available in PWAs).

### Migrating from DEPRECATED_TakePicture block

If you're using the **DEPRECATED_TakePicture** block, replace it with the **TakePhoto** block (previously **TakePicture** in versions older than 8).

#### Key differences

* Parameter **SaveToPhotoAlbum** is now **SaveToGallery**.
* **AllowMultiplePictures** parameter is not available in the block (use the **TakePhoto** client action  **AllowMultiplePhotos** if you need to capture photos inside a cycle block in PWAs).
* The block no longer displays error messages automatically - you must implement the **OnError** event.

To update your implementation, follow these migration steps:

1. Replace the **DEPRECATED_TakePicture** block reference with **TakePhoto**.

1. Update parameter names if you are using them:
    * Replace **SaveToPhotoAlbum** with **SaveToGallery**.

1. If you were using **AllowMultiplePictures**, you must switch to using the **TakePhoto** client action instead of the block

1. Update the **OnClick** event handler to use **MediaResult** instead of **ImageCaptured**.
    * Access the photo data using **MediaResult.Thumbnail** (instead of **ImageCaptured** binary data).
    * The **MediaResult** structure has other attributes that may be relevant, refer to the [reference article](camera-ref.md#mediaresult-data-structure) for more information.

1. Implement the mandatory **OnError** event. Refer to [Handling errors in TakePhoto block](#handling-errors-in-takephoto-block).

### Migrating from DEPRECATED_ChooseImage block

If you're using the **DEPRECATED_ChooseImage** block, replace it with the **ChooseFromGallery** block.

#### Key differences

* Output parameter **ImageCaptured** structure is now a list of **MediaResult** structures.
* New input parameters available: **MediaType**, **AllowMultipleSelection**, **Limit**, and **IncludeMetadata**.
* The new client action works in PWAs, albeit with limitations.
* The block no longer displays error messages automatically - you must implement the **OnError** event.

To update your implementation and ensure compatibility with the latest plugin version, follow these migration steps:

1. Replace the **DEPRECATED_ChooseImage** block reference with **ChooseFromGallery**.

1. Set the **MediaType** parameter to **Entities.MediaType.Photo** to maintain the same behavior.

1. Update the **OnClick** event handler:
    * **ChooseFromGallery.MediaResult** is a list. Access the first item's photo with **ChooseFromGallery.MediaResult.Current.Thumbnail**
    * The **MediaResult** structure has other attributes that may be relevant, refer to the [reference article](camera-ref.md#mediaresult-data-structure) for more information.

1. If you want to allow multiple photo selection, set **AllowMultipleSelection** to **True** and iterate through the **MediaResult** list.

1. Implement the mandatory **OnError** event. The information in [Handling errors in TakePhoto block](#handling-errors-in-takephoto-block) section can also be applied to this block.

## Handling errors in TakePhoto block

In version 8.0.0, the **TakePhoto** (previously **TakePicture** in versions older than 8) block requires you to implement the **OnError** event. Previously, the plugin displayed error messages automatically. This change gives you control over error handling and allows you to provide custom error messages.

To migrate your error handling with the new TakePhoto block, follow these steps:

1. Select the **TakePhoto** block on your screen.

1. Scroll down until you find the **OnError** event.

1. Create a new client action for the **OnError** event.

1. In the event handler, add logic to handle the error. The **Error** parameter contains:
    * **ErrorCode** - The error code (for example, **OS-PLUG-CAMR-0003**)
    * **ErrorMessage** - A message describing the error.

### Example error handling

For instance, you can display the error message to the user using a Feedback Message:

1. In the **OnError** event handler, add a **Message** element.

1. Set the **Message** to **Error.ErrorMessage**.

1. Set the **Message Type** to **Error**.

Alternatively, you can implement custom error handling based on the error code:

1. Add an **If** element to check **Error.ErrorCode**.

1. For specific error codes, provide custom messages, log the error or run specific actions.

1. For other errors, display the default **Error.ErrorMessage**.

## Updating error code handling

Error codes have been restructured in version 8.0.0. If your app handles specific error codes, you need to update your error handling logic.

### Key error code changes

The following table maps error codes from version 7 to version 8 based on matching error messages. If you handle a specific error code in version 7, use this table to find the corresponding version 8 error code:

| Version 7 Code | Version 7 Message | Version 8 Code | Version 8 Message | Notes |
| - | - | - | - | - |
| OS-PLUG-CAMR-0004 | Couldn't take picture because the browser doesn't support the MediaDevices API. | OS-PLUG-CAMR-0004 | Couldn't take photo because the browser doesn't support the MediaDevices API. | Message updated from "picture" to "photo" |
| OS-PLUG-CAMR-0006 | Couldn't access your photo gallery because access wasn't provided. | OS-PLUG-CAMR-0005 | Couldn't access your photo gallery because access wasn't provided. | Error code changed to 0005 |
| OS-PLUG-CAMR-0016 | Couldn't capture picture because the process was canceled. | OS-PLUG-CAMR-0006 | Couldn't take photo because the process was canceled. | Error code changed to 0006 |
| OS-PLUG-CAMR-0008 | No camera available. | OS-PLUG-CAMR-0007 | No camera available. | Error code changed to 0007 |
| OS-PLUG-CAMR-0009 | The selected file contains data that isn't valid. | OS-PLUG-CAMR-0008 | The selected file contains data that isn't valid. | Error code changed to 0008 |
| OS-PLUG-CAMR-0010 | Couldn't edit image. | OS-PLUG-CAMR-0009 | Couldn't edit image. | Error code changed to 0009 |
| OS-PLUG-CAMR-0011 | Couldn't capture picture. | OS-PLUG-CAMR-0010 | Couldn't take photo. | Error code changed to 0010, message updated |
| OS-PLUG-CAMR-0012 | Couldn't get image from the gallery. | OS-PLUG-CAMR-0011 | Couldn't get image from the gallery. | Error code changed to 0011 |
| OS-PLUG-CAMR-0013 | Couldn't process image. | OS-PLUG-CAMR-0012 | Couldn't process image. | Error code changed to 0012 |
| OS-PLUG-CAMR-0014 | Couldn't edit picture because the process was canceled. | OS-PLUG-CAMR-0013 | Couldn't edit photo because the process was canceled. | Error code changed to 0013, message updated |
| OS-PLUG-CAMR-0015 | Couldn't decode the 'Take Picture' action parameters. | OS-PLUG-CAMR-0014 | Couldn't decode the 'Take Photo' action parameters. | Error code changed to 0014, message updated |
| OS-PLUG-CAMR-0017 | The plugin is not available. | OS-PLUG-CAMR-0015 | The plugin is not available. | Error code changed to 0015 |
| OS-PLUG-CAMR-0018 | Couldn't capture video. | OS-PLUG-CAMR-0016 | Couldn't record video. | Error code changed to 0016, message updated |
| OS-PLUG-CAMR-0019 | Couldn't capture video because the process was canceled. | OS-PLUG-CAMR-0017 | Couldn't record video because the process was canceled. | Error code changed to 0017, message updated |
| OS-PLUG-CAMR-0021 | Couldn't choose media from the gallery. | OS-PLUG-CAMR-0018 | Couldn't choose media from the gallery. | Error code changed to 0018 |
| OS-PLUG-CAMR-0022 | Couldn't encode media result. | OS-PLUG-CAMR-0019 | Couldn't encode the media result. | Error code changed to 0019 |
| OS-PLUG-CAMR-0023 | Couldn't choose media from the gallery because the process was canceled. | OS-PLUG-CAMR-0020 | Couldn't choose media from the gallery because the process was canceled. | Error code changed to 0020 |
| OS-PLUG-CAMR-0024 | Couldn't get media file path. | OS-PLUG-CAMR-0021 | Couldn't get media file path. | Error code changed to 0021 |
| OS-PLUG-CAMR-0025 | Cordova is not available. | OS-PLUG-CAMR-0022 | Cordova is not available. | Error code changed to 0022 |
| OS-PLUG-CAMR-0026 | Couldn't play video. | OS-PLUG-CAMR-0023 | Couldn't play video. | Error code changed to 0023 |
| OS-PLUG-CAMR-0027 | URI parameter cannot be empty. | OS-PLUG-CAMR-0024 | URI parameter cannot be empty. | Error code changed to 0024 |
| OS-PLUG-CAMR-0028 | Couldn't get video from the gallery. | OS-PLUG-CAMR-0025 | Couldn't get video from the gallery. | Error code changed to 0025 |
| OS-PLUG-CAMR-0029 | There's an issue with the plugin. | OS-PLUG-CAMR-0026 | There's an issue with the plugin. | Error code changed to 0026 |
| OS-PLUG-CAMR-0030 | The selected file doesn't exist. | OS-PLUG-CAMR-0027 | The selected file doesn't exist. | Error code changed to 0027 |
| OS-PLUG-CAMR-0031 | Couldn't retrieve image from the URI. | OS-PLUG-CAMR-0028 | Couldn't retrieve image from the URI. | Error code changed to 0028 |
| OS-PLUG-CAMR-0032 | EditURIPicture is only available for Android and iOS. | OS-PLUG-CAMR-0029 | The client action is only available for Android and iOS. | Error code changed to 0029, message generalized |
| OS-PLUG-CAMR-0033 | Height and width values need to be greater than zero. | OS-PLUG-CAMR-0030 | Height and width values need to be greater than zero. | Error code changed to 0030 |

**Removed error codes in version 8:**

* **OS-PLUG-CAMR-0005** - "No image selected" - This error no longer exists in version 8. The closest equivalent is now OS-PLUG-CAMR-0020.
* **OS-PLUG-CAMR-0007** - "No picture captured" - This error no longer exists in version 8. The closest equivalent is now OS-PLUG-CAMR-0006.
* **OS-PLUG-CAMR-0020** - "Couldn't choose picture because the process was canceled" - Consolidated into OS-PLUG-CAMR-0020.

### Example error handling

A typical error handling can involve checking for errors related to user cancelation, and considering them a non-error, and handling other errors differently. You can accomplish that with the following if block, that can be applied to all client actions / blocks in Camera Plugin version 8:

```
Error.ErrorCode = "OS-PLUG-CAMR-0006" or Error.ErrorCode = "OS-PLUG-CAMR-0013" or Error.ErrorCode = "OS-PLUG-CAMR-0017" or Error.ErrorCode = "OS-PLUG-CAMR-0020"
```

## Notable new features and enhancements

### ChooseFromGallery now works in PWAs

Version 8.0.0 adds support for **ChooseFromGallery** in PWAs. However, PWA support has limitations:

* Only photos can be selected (no video support).
* Only single selection is supported (**AllowMultipleSelection** is not available).
* **AllowEdit** is not available.
* **MediaResult** only includes **Type** and **Thumbnail** (no **URI** or **Metadata**).

To use **ChooseFromGallery** in a PWA:

1. Set **MediaType** to **Entities.MediaType.Photo**.

1. Access the photo using **MediaResult.Current.Thumbnail**.

### Limit parameter for multiple selection

The **ChooseFromGallery** action now includes a **Limit** parameter that sets the maximum number of media files users can select when **AllowMultipleSelection** is **True**.

* Any non-positive number (0 or negative) is treated as unlimited.
* Not available in PWAs.
* For Android, only guaranteed to work on Android 13 and higher.

Here's an example:

To allow users to select up to 5 photos:

1. Set **MediaType** to **Photo**.

1. Set **AllowMultipleSelection** to **True**.

1. Set **Limit** to **5**.

### Saved parameter in MediaResult

The **MediaResult** structure now includes a **Saved** parameter that indicates whether media was successfully saved to the device gallery.

* Only applies when **SaveToGallery** is set to **True**.
* Returns **True** if media was saved successfully, **False** otherwise.
* Not available in PWAs.

Here's an example:
After taking a photo with **SaveToGallery** set to **True**, check if it was saved:

1. Check **TakePhoto.MediaResult.Saved**.

1. If **False**, you can, for instance display a message to the user that the photo wasn't saved to the gallery, and ask to try again.

### Warning output in CheckCameraPlugin

The **CheckCameraPlugin** action now returns a **Warning** structure in addition to the **Error** structure. A warning indicates that the plugin is available but action may be required.

* Check for warnings when **IsAvailable** is **True** and **Error** is empty.
* Relevant warning code: **OS-PLUG-CAMR-0032** - The app is running with an old version of the plugin.

Here's an example:

1. After calling **CheckCameraPlugin**, check if **Warning.ErrorCode** is not empty.

1. Upon receiving **OS-PLUG-CAMR-0032** warning code, you may log it, prompt the user to update their app, or perform a custom action that fits your needs.

## Testing your migration

After migrating to version 8.0.0, we recommend testing all your integrations with the Camera Plugin, with special attention to the following scenarios:

1. **Take a photo** - Verify that **TakePhoto** works correctly and error handling is implemented.

1. **Choose from gallery** - Verify that **ChooseFromGallery** works for both single and multiple selection.

1. **Error handling** - Test error scenarios (for example, deny camera permissions) to ensure custom error handling still works.

1. **PWA functionality** - If your app supports PWAs and you want to use **ChooseFromGallery**, make sure to test, keeping in mind that [functionality is limited](#choosefromgallery-now-works-in-pwas).
