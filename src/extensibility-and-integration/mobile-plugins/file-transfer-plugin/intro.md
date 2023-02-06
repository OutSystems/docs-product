---
summary: Upload and download files in background.
tags: runtime-mobile; support-application_development; support-Mobile_Apps;
locale: en-us
guid: 0bb071a1-f602-4d6b-9b4e-ca0c9c044c06
app_type: mobile apps
---

# File Transfer Plugin

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only.

</div>

File Transfer Plugin lets you download and upload files in your mobile app or, in the case of a Progressive Web App (PWA), download and upload files from your device. The plugin provides advanced file transfer that runs in the background, and, in the case of a mobile app, continues even when the user closes or suspends the app.

File Transfer Plugin also has a progress update for transfers that take longer, for example, video, music, and large images. For the upload progress to work in a PWA, further configuration is needed (see more [here](#pwa-upload))

<div class="info" markdown="1">

See [Adding plugins](../intro.md#adding-plugins) to learn how to install and reference a plugin in your OutSystems apps, and how to install a demo app.

</div>

The plugin's behavior differs between mobile applications and PWAs. These differences are further explained in the next section.

## Progressive Web Apps vs Mobile Apps

In a mobile app, the File Transfer Plugin uses the [File Plugin](../file-plugin/intro.md) to save and manage the downloaded files inside the app's sandboxed file system, as well as upload files from it. This means it's possible to choose where to save a downloaded file given a path, as well as upload a file from its path. As of now, the File Plugin is not PWA compatible and as so, it's not possible to access and manage a file system in a PWA or browser context.

In the following sections, it's explained how the PWA implementation of the File Transfer Plugin works around this limitation.

### Download

Instead of using a file system URL/path to save the downloaded file, in a PWA, the plugin triggers a download to the device's default saving folder. The file name is determined based on the following criteria:

1. The server sets the HTTP header `Content-Disposition` with the desired file name.
    ```
    Content-Disposition: attachment; filename="filename.jpg"
    ```

1. If `Content-Disposition` is not set, the optional input `FileName` on the **Download** and **DownloadWithHeaders** client actions is used.

1. If both are missing, use the application name as a default (e.g. `FileSampleApp.txt`).

The file type is always decided based on the HTTP header `Content-Type`, set in the server response to the download request.

### Upload  { #pwa-upload }

This plugin doesn't offer the upload features in a PWA context, since the [Upload Widget](../../../develop/ui/inputs/upload.md) offers the same capabilities.

## Demo app

Install [File Demo App](https://www.outsystems.com/forge/component-overview/10011/file-sample-app) from Forge and open the app in Service Studio. The demo app contains logic for common use cases, which you can examine and recreate in your apps.

## Reference

The File Transfer Plugin uses a Cordova plugin, and for more information check [cordova-plugin-file-transfer](https://github.com/apache/cordova-plugin-file-transfer).

### Actions

Here is the reference for the actions you can use from the File Transfer Plugin, available in **Logic** > **Client Actions** > **FileTransferPlugin**.

| Action                      | Description                                                 |
| --------------------------- | ----------------------------------------------------------- |
| **CheckFileTransferPlugin** | Checks if the device can upload and download files.         |
| **DownloadFile**            | Action to download files from the server.                   |
| **DownloadFileWithHeaders** | Action to download files from the server with HTTP headers. |
| **UploadFile**              | Action to upload files to the server.                       |
| **UploadFileWithHeaders**   | Action to upload files to the server with HTTP headers.     |

### Events

Here is the reference for the events you can use from the File Transfer Plugin, available in **UI Flows** > **FileTransferPlugin** > **FileTransfer**.

| Event                  | Block              |
| ---------------------- | ------------------ |
| **OnDownloadComplete** | **HandleDownload** |
| **OnDownloadError**    | **HandleDownload** |
| **OnDownloadProgress** | **HandleDownload** |
| **OnUploadComplete**   | **HandleUpload**   |
| **OnUploadError**      | **HandleUpload**   |
| **OnUploadProgress**   | **HandleUpload**   |

## Known Issues and Limitations

### Multiple Downloads
**Applies to PWAs.**

Doing multiple downloads at the same time is not recommended since it may result in unexpected behaviors.
