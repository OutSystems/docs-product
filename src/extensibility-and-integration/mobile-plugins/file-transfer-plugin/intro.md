---
summary: Upload and download files in background.
tags: runtime-mobile; support-application_development; support-Mobile_Apps;
---

# File Transfer Plugin

File Transfer Plugin lets you download and upload files in your mobile app. The plugin provides advanced file transfer that runs in the background, and continues even when the user closes or suspends the app.

File Transfer Plugin also has a progress update for transfers that take longer, for example video, music, and large images.

<div class="info" markdown="1">

See [Adding plugins](../intro.md#adding-plugins) to learn how to install and reference a plugin in your OutSystems apps, and how to install a demo app.

</div>

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
