---
summary: Explore the Camera Plugin functionalities in OutSystems 11 (O11), including client actions, web blocks, and error handling.
tags: mobile app development, plugin integration, camera functionality, error handling, pwa compatibility
locale: en-us
guid: ce70e86c-de5e-413e-988e-d0dca05b30f0
app_type: mobile apps
platform-version: o11
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - service studio
coverage-type:
  - remember
isautopublish: true
---

# Camera plugin version 8 reference

<div class="info" markdown="1">

This reference article applies to Camera Plugin version 8. If you are using Camera Plugin version 7.x, refer to the [Camera Plugin version 7 reference article](camera-ref-version-7.md).

</div>

## Plugin elements

### Client actions

#### CheckCameraPlugin

Verifies if the Camera Plugin is available or properly installed in the application.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| IsAvailable | Output | Boolean | Indicates if the plugin is available ('True') or not ('False'). |
| IsPWA | Output | Boolean | Indicates if the app is running as PWA in the browser ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |
| Warning | Output | Warning | Warning for the Camera Plugin check. If you get a Warning but not an Error, it means the plugin should still work but action may be required. |

#### RecordVideo

Opens the device's camera and allows the user to record a video. Not available on PWAs.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| SaveToGallery | Input | Boolean | Sets if the recorded video will be saved automatically in the device’s gallery. |
| IncludeMetadata | Input | Boolean | Sets if MediaResult should include its metadata. If an error occurs when obtaining the metadata, it will return empty. |
| IsPersistent | Input | Boolean | Indicates whether or not to save the video in the app's persistent storage. If you plan to open videos after recording them, set it to True or leave it empty, as it is True by default. |
| MediaResult | Output | [MediaResult Structure](#mediaresult-data-structure) | Returns the recorded video information. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### TakePhoto

Opens the device's camera and allows the user to take a photo.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Quality | Input | Integer | Sets the photo quality, in percentage (100% means full device quality). By default, the quality is 60%. Applies only to .JPEG EncodingType. |
| Width | Input | Integer | Sets the photo width, in pixels. |
| Height | Input | Integer | Sets the photo height, in pixels. |
| CorrectOrientation | Input | Boolean | Sets if the captured media orientation should be automatically fixed when the device is rotated. Not available on PWAs. |
| EncodingType | Input | Structure | Sets the captured media format: JPEG or PNG. By default, the media format is JPEG. |
| SaveToGallery | Input | Boolean | Sets if the media captured can be saved in the device’s gallery. Not available on PWAs. |
| CameraDirection | Input | Structure | Select the front or back camera as default when taking a new photo. Default value: BackCamera.  Not available on Android. |
| AllowEdit | Input | Boolean | Sets if the media captured must be sent to an edit screen right after the capturing. |
| AllowMultiplePhotos | Input | Boolean | In a PWA context, if set to True, the user will be able to take photos in bulk when this action is used in a cycle. Using this functionality might affect the photo quality. |
| IncludeMetadata | Input | Boolean | Sets if MediaResult should include its metadata. If an error occurs when obtaining the metadata, it will return empty. Not available on PWAs. |
| MediaResult | Output | [MediaResult Structure](#mediaresult-data-structure) | Returns the captured photo and its information. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### PlayVideo

Opens a native video player to play local files. Not available on PWAs.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| URI | Input | Text | Sets the URI of the video to be played. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### EditPhoto

Opens a screen to edit a given photo.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| InputImage | Input | Binary Data | Sets the binary image to edit. |
| OutputImage | Output | Binary Data | Returns the edited photo and its information. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### EditURIPhoto

Opens a screen to edit a given photo. The photo is provided as a URI. Not available on PWAs.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| URI | Input | Binary Data | Sets the URI that contains the photo to edit. |
| SaveToGallery | Input | Boolean | Sets if the edited photo can be saved in the device’s gallery. |
| IncludeMetadata | Input | Boolean | Sets if MediaResult should include its metadata. If an error occurs when obtaining the metadata, it will return empty. |
| MediaResult | Output | [MediaResult Structure](#mediaresult-data-structure) | Returns the edited photo and its information. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

#### ChooseFromGallery

Allow users to choose a photo, video, or both, directly from their gallery. Limited functionality on PWAs.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| MediaType | Input | [MediaType Entity](#mediatype-static-entity) | Sets which media type will be available for selection: photo, video, or both. Not currently available on PWAs. Only Photos are allowed on PWAs. |
| AllowEdit | Input | Boolean | Sets if the media captured must be sent to an edit screen right after the capturing. Only applicable when selecting a single photo. |
| AllowMultipleSelection | Input | Boolean | Sets if the user can select multiple media. Not available on PWAs. |
| Limit (NEW in 8.0.0) | Input | Boolean | The maximum number of media files that the user can choose. Only applicable if AllowMultipleSelection is True. Any non-positive number will be treated as unlimited. Not available on PWAs. For Android, it is only guaranteed to be applied on Android 13 and higher. |
| IncludeMetadata | Input | Boolean | Sets if MediaResult should include its metadata. If an error occurs when obtaining the metadata, it will return empty. Not available on PWAs. |
| MediaResult | Output | List of [MediaResult Structure](#mediaresult-data-structure) | Returns the selected media items and their information. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

### Web Blocks

#### RecordVideo

A button that triggers the action CaptureVideo, allowing users to record a video with their device's camera. Not available on PWA.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| SaveToGallery | Input | Boolean | Sets if the video recorded can be saved in the device’s gallery. |
| IsPersistent | Input | Boolean | Indicates whether or not to save the video in the app's persistent storage. If you plan to open videos after recording them, set it to True or leave it empty, as it is True by default. |
| IncludeMetadata | Input | Boolean | Sets if MediaResult should include its metadata. If an error occurs when obtaining the metadata, it will return empty. |
| OnClick | Event | [MediaResult Structure](#mediaresult-data-structure) | Triggers an event when the user records a video with their device's camera. |
| OnError | Event | Error | Triggered when an error occurs. |

#### TakePhoto

A button that triggers the action TakePhoto, allowing users to take a photo with their device's camera.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Quality | Input | Integer | Sets the quality of the photo, in percentage - 100% means full device quality. Default value: 60%. Applies only when EncodingType is .JPEG. |
| Width | Input | Integer | Sets the width of the photo, in pixels. |
| Height | Input | Integer | Sets the height of the photo, in pixels. |
| CorrectOrientation | Input | Boolean | If True, the plugin fixes the orientation if the user takes a photo and rotates the device. Not available on PWAs. |
| EncodingType | Input | Structure | Select the JPEG or PNG format. Default value: JPEG. |
| SaveToGallery | Input | Boolean | Sets if the media captured can be saved in the device’s gallery. Not available on PWAs. |
| CameraDirection | Input | Structure | Select the front or back camera as default when taking a new photo. Default value: BackCamera. Not available on Android. |
| AllowEdit | Input | Boolean | Sets if the media captured must be sent to an edit screen right after the capturing. |
| IncludeMetadata | Input | Boolean | Sets if MediaResult should include its metadata. If an error occurs when obtaining the metadata, it will return empty. Not available on PWAs. |
| OnClick | Event | [MediaResult Structure](#mediaresult-data-structure) | Triggers an event when the user takes a photo from their device. |
| OnError | Event | Error | Triggered when an error occurs. |

#### EditPhoto

A button that triggers the action EditPhoto, allowing users to edit a given photo.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Image | Input | Binary Data | Sets the binary image to edit. |
| OnSuccess | Event | Binary Data | Triggers an event when the user has edited the photo. |
| OnError | Event | Error | Triggered when an error occurs. |

#### EditURIPhoto

A button that triggers the action EditURIPhoto, allowing users to edit a given photo. Not available on PWAs.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| URI | Input | Binary Data | Sets the URI that contains the photo to edit. |
| SaveToGallery | Input | Boolean | Sets if the edited photo can be saved in the device’s gallery. |
| IncludeMetadata | Input | Boolean | Sets if MediaResult should include its metadata. If an error occurs when obtaining the metadata, it will return empty. |
| OnSuccess | Event | [MediaResult Structure](#mediaresult-data-structure) | Triggers an event when the user has edited the photo. |
| OnError | Event | Error | Triggered when an error occurs. |

#### ChooseFromGallery

A button that triggers the action ChooseFromGallery, allowing users to select images and/or videos from their device. Limited functionality on PWAs.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| MediaType | Input | [MediaType Entity](#mediatype-static-entity) | Sets which media type will be available for selection: photo, video, or both. Not currently available on PWAs. Only Photos are allowed on PWAs. |
| AllowEdit | Input | Boolean | Sets if the media captured must be sent to an edit screen right after the capturing. Not currently available on PWAs - always False. |
| AllowMultipleSelection | Input | Boolean | Sets if the user can select multiple media. Not available on PWAs. |
| Limit (NEW in 8.0.0) | Input | Boolean | The maximum number of media files that the user can choose. Only applicable if AllowMultipleSelection is True. Any non-positive number will be treated as unlimited. Not available on PWAs. For Android, it is only guaranteed to be applied on Android 13 and higher. |
| IncludeMetadata | Input | Boolean | Sets if MediaResult should include its metadata. If an error occurs when obtaining the metadata, it will return empty. Not available on PWAs. |
| OnClick | Event | List of [MediaResult Structure](#mediaresult-data-structure) | Triggers an event when the user selects media from their device. |
| OnError | Event | Error | Triggered when an error occurs. |

#### PlayVideo

A button that triggers the action PlayVideo, allowing users to play a video on the native video player. Not available on PWA.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| URI | Input | Text | Sets the URI of the video to be played. |
| Error | Event | Error | Triggered when an error occurs. |

### Data structures and Static Entities

#### MediaType static entity

The static entity to use in ChooseFromGallery. Also used to indicate the type of media returned by the client actions in [MediaResult](#mediaresult-data-structure).

| ID | Type |
| - | - |
| 0 | Photo |
| 1 | Video |
| 2 | Both (Photos and Videos) |

#### MediaMetadata data structure

The data structure for returning media's metadata.

| Parameter | Data Type | Description |
| - | - | - |
| Size | Long Integer | Returns the file size of the media in bytes. |
| Duration | Long Integer | If a video, returns the duration of the media, in seconds. |
| Format | Text | Returns the format of the media. |
| Resolution | Text | Returns the resolution of the media in pixels, in `<width>x<height>` format. |
| CreationDate | Date Time | Returns the creation date of the media. |

#### MediaResult data structure

The data structure for returning media.

| Parameter | Data Type | Description |
| - | - | - |
| Type | [Static Entity](#mediatype-static-entity) | Indicates if the media selected is a photo or a video. |
| URI | Text | Returns the file path of the media. Not available on PWA. |
| Thumbnail | Binary Data | Returns the thumbnail of the media. |
| Metadata | [MediaMetadata](#mediametadata-data-structure) | Returns the metadata of the media. Not available on PWA. |
| Saved (NEW in 8.0.0) | Boolean | True if media was saved to device successfully, false otherwise. Only applies if SaveToGallery input option was sent as True. Not available on PWA. |

### Error Codes

| Code | Platform | Message |
| - | - | - |
| OS-PLUG-CAMR-0001 | PWA | The selected file format isn’t supported. Select a JPEG or a PNG file and try again. |
| OS-PLUG-CAMR-0002 | PWA | Couldn’t upload the selected file. |
| OS-PLUG-CAMR-0003 | iOS, Android, PWA | Couldn’t access camera. Check your camera permissions and try again. |
| OS-PLUG-CAMR-0004 | PWA | Couldn’t take photo because the browser doesn’t support the MediaDevices API. |
| OS-PLUG-CAMR-0005 | iOS, Android | Couldn’t access your photo gallery because access wasn’t provided. |
| OS-PLUG-CAMR-0006 | Android, iOS | Couldn’t take photo because the process was canceled. |
| OS-PLUG-CAMR-0007 | iOS, Android | No camera available. |
| OS-PLUG-CAMR-0008 | iOS | The selected file contains data that isn’t valid. |
| OS-PLUG-CAMR-0009 | iOS, Android | Couldn’t edit image. |
| OS-PLUG-CAMR-0010 | iOS, Android | Couldn’t take photo. |
| OS-PLUG-CAMR-0011 | iOS | Couldn’t get image from the gallery. |
| OS-PLUG-CAMR-0012 | iOS, Android | Couldn’t process image. |
| OS-PLUG-CAMR-0013 | iOS, Android, PWA | Couldn’t edit photo because the process was canceled. |
| OS-PLUG-CAMR-0014 | iOS | Couldn’t decode the ‘Take Photo’ action parameters. |
| OS-PLUG-CAMR-0015 | iOS, Android | The plugin is not available. |
| OS-PLUG-CAMR-0016 | iOS, Android | Couldn’t record video. |
| OS-PLUG-CAMR-0017 | iOS, Android | Couldn’t record video because the process was canceled. |
| OS-PLUG-CAMR-0018 | iOS, Android | Couldn’t choose media from the gallery. |
| OS-PLUG-CAMR-0019 | iOS | Couldn’t encode the media result. |
| OS-PLUG-CAMR-0020 | iOS, Android | Couldn’t choose media from the gallery because the process was canceled. |
| OS-PLUG-CAMR-0021 | Android | Couldn’t get media file path. |
| OS-PLUG-CAMR-0022 | iOS, Android | Cordova is not available. |
| OS-PLUG-CAMR-0023 | iOS, Android | Couldn’t play video. |
| OS-PLUG-CAMR-0024 | Android | URI parameter cannot be empty. |
| OS-PLUG-CAMR-0025 | iOS | Couldn’t get video from the gallery. |
| OS-PLUG-CAMR-0026 | iOS | There’s an issue with the plugin. |
| OS-PLUG-CAMR-0027 | Android | The selected file doesn’t exist. |
| OS-PLUG-CAMR-0028 | iOS, Android | Couldn’t retrieve image from the URI. |
| OS-PLUG-CAMR-0029 | PWA | The client action is only available for Android and iOS. |
| OS-PLUG-CAMR-0030 | iOS, Android, PWA | Height and width values need to be greater than zero. |
| OS-PLUG-CAMR-0031 (NEW in 8.0.0) | Android | Invalid argument provided to plugin method. |
| OS-PLUG-CAMR-0032 (NEW in 8.0.0) | iOS, Android | (This may be returned as a warning instead of an error for CheckCameraPlugin client action) The app is running with an old version of the plugin. Please create a new mobile package. |
| OS-PLUG-CAMR-0033 (NEW in 8.0.0) | Android | Unable to get the context. |

## Related resources

* [Camera Plugin version 8](intro.md)
* [Migrating camera plugin from version 7 to version 8](camera-plugin-migration-guide-7-to-8.md)
