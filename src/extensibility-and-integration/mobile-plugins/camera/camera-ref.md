---
summary: Camera plugin - reference page
tags: runtime-mobile
locale: en-us
guid: ce70e86c-de5e-413e-988e-d0dca05b30f0
app_type: mobile apps
platform-version: o11
---

# Camera plugin - reference page

## Plugin Elements

### Client Actions

#### CheckCameraPlugin

Verifies if the Camera Plugin is available or properly installed in the application.

Parameter|Type|Data Type|Description
-|-|-|-
IsAvailable|Output|Boolean|Indicates if the plugin is available ('True') or not ('False').
IsPWA|Output|Boolean|Indicates if the browser is available for running Progress Web Apps ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

#### CaptureMedia

Opens the device's camera and allows the user to record a video, capture a picture, or both.

Parameter|Type|Data Type|Description
-|-|-|-
CameraMode|Input|[MediaType Entity](#mediatype-static-entity)|Sets which camera mode will be available, if photo mode, video mode, or both.
SaveToGallery|Input|Boolean|Sets if the captured media will be saved automatically in the device’s gallery.
AllowEdit|Input|Boolean|Sets if the media can be edited just after being captured. If 'True', the end-user will be redirected to an edit screen.
MediaResult|Output|[MediaResult Structure](#mediaresult-data-structure)|Returns the captured media information.
Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

#### RecordVideo

Opens the device's camera and allows the user to record a video.

Parameter|Type|Data Type|Description
-|-|-|-
SaveToGallery|Input|Boolean|Sets if the recorded video will be saved automatically in the device’s gallery.
AllowEdit|Input|Boolean|Sets if the video can be edited just after being recorded. If ‘True’, the end-user will be redirected to an edit screen.
IncludeMetadata|Input|Boolean|Sets if MediaResult should include its metadata. If an error occurs when obtaining the metadata, it will return empty.
MediaResult|Output|[MediaResult Structure](#mediaresult-data-structure)|Returns the recorded video information.
Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

#### TakePicture

Opens the device's camera and allows the user to take a picture.

Parameter|Type|Data Type|Description
-|-|-|-
Quality|Input|Integer|Sets the picture quality, in percentage (100% means full device quality). By default, the quality is 60%.
Applies only to .JPEG EncodingType.
Width|Input|Integer|Sets the picture width, in pixels.
Height|Input|Integer|Sets the picture height, in pixels.
CorrectOrientation|Input|Boolean|Sets if the captured media orientation should be automatically fixed when the device is rotated.
EncodingType|Input|Structure|Sets the captured media format: JPEG or PNG. By default, the media format is JPEG.
SaveToPhotoAlbum|Input|Boolean|Sets if the media captured can be saved in the device’s gallery.
CameraDirection|Input|Structure|Select the front or back camera as default when taking a new picture.
Default value: BackCamera.
AllowEdit|Input|Boolean|Sets if the media captured must be sent to an edit screen right after the capturing.
AllowMultiplePictures|Input|Boolean|Sets if the user can select multiple pictures.
ImageCaptured|Output|Structure|Returns the captured image and its information.
Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

#### PlayVideo

Opens a native video player to play local files.

Parameter|Type|Data Type|Description
-|-|-|-
URI|Input|Text|Sets the URI of the video to be played.
Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

#### ChooseFromGallery

Allow users to choose a picture, video, or both, directly from their gallery.

Parameter|Type|Data Type|Description
-|-|-|-
MediaType|Input|[MediaType Entity](#mediatype-static-entity)|Sets which media type will be available for selection, if photo, video, or both.
AllowEdit|Input|Boolean|Sets if the media captured must be sent to an edit screen right after the capturing.
AllowMultipleSelection|Input|Boolean|Sets if the user can select multiple media.
IncludeMetadata|Input|Boolean|Sets if MediaResult should include its metadata. If an error occurs when obtaining the metadata, it will return empty
MediaResult|Output|[MediaResult Structure](#mediaresult-data-structure)|Returns the selected media and its information.
Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

#### ChooseGalleryPicture

Allow users to choose a picture directly from their gallery.

Parameter|Type|Data Type|Description
-|-|-|-
AllowEdit|Input|Boolean|Sets if the media captured must be sent to an edit screen right after the capturing.
ImageCaptured|Output|Structure|Returns the captured image and its information.
Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

#### EditVideo
Opens a screen to edit a given video.

Parameter|Type|Data Type|Description
-|-|-|-
VideoURI|Input|Text|Sets the URI of the video' to be edited.
MediaResult|Output|[MediaResult Structure](#mediaresult-data-structure)|Returns the edited video and its information.
Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

#### EditPicture

Opens a screen to edit a given picture.

Parameter|Type|Data Type|Description
-|-|-|-
InputImage|Input|Binary Data|Sets the URI of the video' to be edited.
OutputImage|Output|Binary Data|Returns the edited picture and its information.
Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

#### Open Permissions

Opens the app’s permissions screen in the device settings.

Parameter|Type|Data Type|Description
-|-|-|-
Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

### Web Blocks

#### RecordVideo

A button that triggers the action CaptureVideo, allowing users to record a video with their device's camera.

Parameter|Type|Data Type|Description
-|-|-|-
SaveToGallery|Input|Boolean|Sets if the video recorded can be saved in the device’s gallery.
AllowEdit|Input|Boolean|Sets if the video recorded must be sent to an edit screen right after the recording.
MediaResult|Output|[MediaResult Structure](#mediaresult-data-structure)|Returns the video recorded and its information.
Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

#### TakePicture

A button that triggers the action TakePicture, allowing users to take a picture with their device's camera.

Parameter|Type|Data Type|Description
-|-|-|-
Quality|Input|Integer|Sets the quality of the picture, in percentage - 100% means full device quality. Default value: 60%. Applies only when EncodingType is .JPEG.
Width|Input|Integer|Sets the width of the picture, in pixels.
Height|Input|Integer|Sets the height of the picture, in pixels.
CorrectOrientation|Input|Boolean|If True, the plugin fixes the orientation if the user takes a photo and rotates the device.
EncodingType|Input|Structure|Select the JPEG or PNG format. Default value: JPEG.
SaveToPhotoAlbum|Input|Boolean|Sets if the media captured can be saved in the device’s gallery.
CameraDirection|Input|Structure|Select the front or back camera as default when taking a new picture. Default value: BackCamera.
AllowEdit|Input|Boolean|Sets if the media captured must be sent to an edit screen right after the capturing.
AllowMultiplePictures|Input|Boolean|Sets if the user can select multiple pictures.
ImageCaptured|Output|Structure|Returns the captured image and its information.
Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

#### ChooseFromGallery

A button that triggers the action ChooseFromGallery, allowing users to select an image from their device.

Parameter|Type|Data Type|Description
-|-|-|-
MediaType|Input|[MediaType Entity](#mediatype-static-entity)|Sets which media type will be available for selection, if photo, video, or both.
AllowEdit|Input|Boolean|Sets if the media captured must be sent to an edit screen right after the capturing.
AllowMultipleSelection|Input|Boolean|Sets if the user can select multiple media.
MediaResult|Output|[MediaResult Structure](#mediaresult-data-structure)|Returns the media selected and its information.
Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

#### PlayVideo

A button that triggers the action PlayVideo, allowing users to play a video on the native video player.

Parameter|Type|Data Type|Description
-|-|-|-
URI|Input|Text|Sets the URI of the video to be played.
Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False').
Error|Output|Error|Displays detailed information of an error, if applicable.

### Data structures and Static Entities

#### MediaType Static Entity

The static entity for the CameraMode parameter.

ID|Camera Mode
-|-
0|Both
1|Photo mode
2|Video mode

#### MediaResult Data Structure

The data structure for returning media.

Parameter|Data Type|Description
-|-|-
Type|Static|Indicates if the media selected is a picture or a video.
URI|Text (If Video)|Returns the file path of the media.
Thumbnail|Binary Data (if Picture)|Returns the thumbnail of the media.
Size|Long Integer|Returns the file size of the media in bytes.
Duration (OPTIONAL)|Long Integer|If a video, returns the duration of the media.
Format|Format Static Entity|Returns the format of the media.
Resolution|Resolution Static Entity|Returns the duration of the media in seconds.
CreationDate|Date Time|Returns the creation date of the media.

### Error Codes

Code|Platform|Message
-|-|-
OS-PLUG-CAMR-0001|PWA|The selected file format isn't supported. Select a JPEG or a PNG file and try again.
OS-PLUG-CAMR-0002|PWA|Couldn’t upload the selected file.
OS-PLUG-CAMR-0003|iOS, Android, PWA|Couldn’t access camera. Check your camera permissions and try again.
OS-PLUG-CAMR-0004|PWA|Couldn’t take picture because the browser doesn’t support the MediaDevices API. Check if the version is up to date and supports the required API.
OS-PLUG-CAMR-0005|Android|No image selected.
OS-PLUG-CAMR-0006|iOS, Android|Couldn’t access your photo gallery because access wasn’t provided. Check its permissions and try again.
OS-PLUG-CAMR-0007|Android|No picture captured.
OS-PLUG-CAMR-0008|iOS, Android|No camera available.
OS-PLUG-CAMR-0009|iOS|The selected file contains data that isn’t valid.
OS-PLUG-CAMR-0010|iOS, Android|Couldn’t edit image.
OS-PLUG-CAMR-0011|iOS, Android|Couldn’t capture picture.
OS-PLUG-CAMR-0012|iOS, Android|Couldn’t get image from the gallery.
OS-PLUG-CAMR-0013|iOS, Android|Couldn’t process image.
OS-PLUG-CAMR-0014|iOS, Android, PWA|Couldn’t edit picture because the process was canceled.
OS-PLUG-CAMR-0015 (NEW)|iOS|Couldn’t decode the 'Take Picture' action parameters.
OS-PLUG-CAMR-0016 (NEW)|iOS|Couldn’t capture picture because the process was canceled.
OS-PLUG-CAMR-0017 (NEW)|iOS, Android, PWA|The plugin is not available.
OS-PLUG-CAMR-0018 (NEW)|iOS, Android|Couldn’t capture video.
OS-PLUG-CAMR-0019 (NEW)|iOS, Android|Couldn’t capture video because the process was canceled.
OS-PLUG-CAMR-0020 (NEW)|iOS|Couldn’t choose picture because the process was canceled.
OS-PLUG-CAMR-0021 (NEW)|iOS, Android|Couldn’t choose media from the gallery
OS-PLUG-CAMR-0022 (NEW)|iOS|Couldn't encode media result.
OS-PLUG-CAMR-0023 (NEW)|iOS, Android|Couldn’t choose media from the gallery because the process was canceled.
OS-PLUG-CAMR-0024 (NEW)|Android|Couldn't get media file path.
OS-PLUG-CAMR-0025 (NEW)|iOS, Android|Cordova is not available.
OS-PLUG-CAMR-0026 (NEW)|iOS, Android|Couldn’t play video.
OS-PLUG-CAMR-0027 (NEW)|Android|The selected file doesn’t exist.
OS-PLUG-CAMR-0028 (NEW)|iOS|Couldn’t get video from the gallery.
OS-PLUG-CAMR-0029 (NEW)|iOS|There's an issue with the plugin.

