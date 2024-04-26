---
summary: Use File Viewer plugin to let users of your mobile app view remote or app resource files.
tags: runtime-mobile; support-application_development; support-Mobile_Apps;
locale: en-us
guid: 8f00b7c4-754a-4afd-86ac-740c255458b1
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=1075:5150
---

# File Viewer plugin

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

Use the File Viewer plugin to create logic that lets users open remote or app resource files, or in the case of a Progressive Web App (PWA), open and view files from your device (via a file picker). In Android users select an app to open the file. iOS provides a native preview for supported file types.


<div class="info" markdown="1">

See [Adding plugins](../intro.md#adding-plugins) to learn how to install and reference a plugin in your OutSystems apps, and how to install a demo app.

</div>

File Viewer plugin can open:

* **File from the app resources**. The plugin can access the **resources** path to load the file that's part of the app's static content. See [Working with app resources](#working-with-app-resources)
* **Remote file**. The plugin downloads the file to the app sandbox and then opens the file.

![Screenshot of the File Viewer plugin interface in a mobile app](images/file-viewer-preview-ss.png "File Viewer Plugin Preview")

## Progressive Web Apps (PWA)

For now, it's impossible to access and manage a file system in a PWA or browser context. This means that using this plugin in a PWA only lets you open files via the device's file picker. You can show them in an OutSystems dialog. Your application needs to manage these limitations as necessary. The File Viewer plugin sample app has an example of this.

![Screenshot showing the File Viewer plugin's support for Progressive Web Apps](images/file-viewer-pwa-ss.png "File Viewer PWA Support")

## Viewing files in Android and iOS

To let users view files in the mobile apps, create logic with the action **OpenDocument**. You need to supply a path to a local file in the **FilePath** property or to a remote file in the **URL** property.

If you want to open a file from the app resources see [Working with app resources](#working-with-app-resources).

For an example of how to use the plugin check the demo app or refer to [the example in this document](#example-of-using-file-viewer-plugin).

<div class="info" markdown="1">

For opening media files in the iOS apps, use the action **PreviewMediaContent** from **FileViewerPlugin** > **iOSOnly**. This action lets apps handle the media files better by opening them in a media player.

</div>

## Working with app resources

Here is how to add a file as a resource and open the file with the plugin.

1. In Service Studio, go to the **Data** tab.

1. Right-click the **Resources** folder and select **Import resources**. A file dialog opens, where you can select the file you want to add as a resource.

1. Select the file you added under **Resources**, and:

    * Enter `resources` in the **Target Directory** property. Note that this value must be `resources` and you can't change it.
    * Select **Deploy to Target Directory** in the **Deploy Action** list.

    ![Screenshot of adding a file as a resource in the File Viewer plugin](images/resources-file-viewer-ss.png "Adding Resources in File Viewer Plugin")

1. In the **OpenDocument** action enter `"resources\<file name>"` in the **FilePath** property. For example, if you add **sample.pdf** to **Resources**, the value of  **FilePath** is `"resources\sample.pdf"`.


<div class="info" markdown="1">

The plugin can access only the resources you deploy in the **resources** path. This is a security limitation by design. Limiting access to the plugin prevents accidental access to the resources of the app.

</div>

## Example of using File Viewer plugin

Here is an example of how to use the File Viewer plugin.

![Screenshot of the logic flow for using the File Viewer plugin in an app](images/logic-file-viewer-ss.png "Logic for File Viewer Plugin")

A good practice is to check if the plugin is available to the app, and report an error if not. You can check the plugin availability by using the **CheckPlugin** action and checking the value of the **CheckPlugin.IsAvailable** boolean (1).

When you confirm the plugin is available, use the **OpenDocument** (2) action to ask the operating system to view the file. The action accepts either a **URL** for remote files or **FilePath** for a [file from the app resources](#working-with-app-resources) (3).

## Reference

More information about parts of the plugin.

### Actions

Here is the reference of the actions you can use from the File Viewer plugin. File Viewer plugin uses a Cordova plugin, and for more information check out [cordova-outsystems-file-viewer](https://github.com/OutSystems/cordova-outsystems-fileviewer)

| Action                  | Description                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------ |
| **CheckPlugin**         | Checks if the plugin is available in the app.                                        |
| **OpenDocument**        | Opens a remote file or a [file from the app resources](#working-with-app-resources). |
| **PreviewMediaContent** | iOS only. Action to preview media content.                                           |
