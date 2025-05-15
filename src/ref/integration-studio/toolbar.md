---
locale: en-us
guid: 5395d30e-5e9a-4605-9d92-717fedcfeefb
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=3042-298&t=ndVLjp7PlMY2g9Hg-1
summary: Explore the toolbar functionalities in OutSystems 11 (O11) for managing extensions in Integration Studio.
tags: ide usage, reactive web apps, tutorials for beginners, extension development, integration studio
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - integration studio
coverage-type:
  - remember
---

# Toolbar

The Toolbar is the area of your [workspace](<workspace.md>) where you can execute the following operations:

Button | Description
:-----:|:-----------
![Icon for creating a new extension in Integration Studio](images/file-new-icon.png "New Button") New | Creates a [new extension](<../../integration-with-systems/integration-studio/extension-life-cycle/extension-create.md>).
![Icon for opening an existing extension in Integration Studio](images/file-open-icon.png "Open Button") Open | Opens an extension already created in Integration Studio. Simply select the XIF (Extension and Integration Framework) file and all the elements defined for the extension are available in the [Extension](<multi-tree-navigator.md>) and [Resources](<resources-tree.md>) tree.
![Icon for saving the current extension in Integration Studio](images/file-save-icon.png "Save Button") Save | Saves the extension in a XIF file.
![Icon for undoing the last operation in Integration Studio](images/file-undo-icon.png "Undo Button") Undo | Reverse the last operation you executed in the current screen contents. Each click reverses one more operation.
![Icon for redoing the last undone operation in Integration Studio](images/file-redo-icon.png "Redo Button") Redo | Reverse the action of the Undo. Each click reverse one more Undo operation.
![Icon for cutting selected elements or text in Integration Studio](images/file-cut-icon.png "Cut Button") Cut | Removes the selected element(s) or text and stores it in the Clipboard.
![Icon for copying selected elements or text in Integration Studio](images/file-copy-icon.png "Copy Button") Copy | Stores the selected element(s) or text in the Clipboard.
![Icon for pasting elements or text from the Clipboard in Integration Studio](images/file-paste-icon.png "Paste Button") Paste | Insert the element(s) or text in the Clipboard at the insertion point.
![Icon for displaying the Start Screen of Integration Studio](images/home-icon.png "Start Screen Button") Start Screen | Displays the Start Screen of Integration Studio where you can manage your extensions, take a tour of Integration Studio and get some help.
![Icon for selecting the Platform Server in Integration Studio](images/connect-server-icon.png "Select Server Button") Select Server... | Allows you to [select the Platform Server](<menu/file/server-select-window.md>) you want to use.
![Icon for downloading an extension from the Platform Server in Integration Studio](images/download-icon.png "Download Button") Download... | Allows you to [download an extension](<../../integration-with-systems/integration-studio/managing-extensions/extension-download.md>) already published in the Platform Server you are connected to.
![Icon for verifying the current extension's validity in Integration Studio](images/validate-icon.png "Verify Button") Verify | [Verifies if the current extension is valid](<../../integration-with-systems/integration-studio/extension-life-cycle/extension-verify.md>) and ready to be published in a Platform Server.
![Icon for verifying and saving the current extension in Integration Studio](images/verify-save-icon.png "Verify and Save Button") Verify and Save | [Verifies if the current extension is valid](<../../integration-with-systems/integration-studio/extension-life-cycle/extension-verify.md>) and ready to be published in a Platform Server. If so, the extension is saved.
![Icon for publishing the current extension with one click in Integration Studio](images/1-click-publish-icon.png "1-Click Publish Button") 1-Click Publish | Allows you to [publish the current extension](<../../integration-with-systems/integration-studio/extension-life-cycle/extension-1-cp.md>) in a Platform Server.
![Icon for updating the source code of the extension in Integration Studio](images/update-source-code-icon.png "Update Source Code Button") Update Source Code | [Synchronizes the source code](<../../integration-with-systems/integration-studio/extension-life-cycle/extension-update-source-code.md>) you added in the IDE with the definition of the extension elements.
![Icon for editing the source code of the .NET extension in the specified IDE](images/launch-ide-net-icon.png "Edit Source Code Button") Edit Source Code | [Opens the solution of your extension](<../../integration-with-systems/integration-studio/extension-life-cycle/extension-code-edit.md>) in the IDE you specified for the .NET extensions.
