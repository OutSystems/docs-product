---
locale: en-us
guid: 2bb10995-f2e7-48a6-a6d5-2fbb248f09e6
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Download an Extension

You can download to your work area any extension previously published in a Platform Server. When this operation is executed, the XIF (Extension and Integration Framework) file that corresponds to this extension will be stored where you specify. Afterwards, you can make the necessary changes in the extension and [publish](<../extension-life-cycle/extension-1-cp.md>) it again when it is ready.

## Downloading an Extension version

The ![](images/download-icon.gif) **Download** operation is available in the **File** menu or in the toolbar.

If you're not connected to a Platform Server, Integration Studio automatically prompts you to select a server and a user name to establish the connection. [See how to Select Server window](<../../../ref/integration-studio/menu/file/server-select-window.md>).

When the [Download from Server window](<../../../ref/integration-studio/menu/file/extension-download-window.md>) is launched, you can select the extension you want to download.

To download the latest extension version uploaded to the server, which may or many not be the one currently published, click **Download**.

If you want to download another extension version, click **Older versions**, select the version, and click **Download**. See how to [download a specific extension version](<../../../ref/integration-studio/menu/file/extension-download-version-window.md>).

## Download access rights

To download an extension from the server, you must have, at least, a "Download" security level for that extension.

![](images/note.gif) To check your permissions, you must login to the Service Center. In the **My Settings** screen, available by clicking on your user name in the top right corner of the Service Center interface, you can check your effective permissions in the **Security Settings**, **Applications Granted**, **Modules Granted**, **Extensions Granted**, and **Solutions Granted** areas. If necessary, contact the Service Center administrator and ask to be granted the suitable permissions.

![](images/tip.gif) You can also download an extension version in Service Center, in **Factory** > **Extensions** > **(extension detail)** screen.
