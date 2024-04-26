---
locale: en-us
guid: f5eb9f11-455a-4bfe-bd0d-2ee4968044bb
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
summary: The File menu in Integration Studio provides various options for managing extensions, including creation, opening, saving, importing, server selection, downloading, verification, publishing, and source code synchronization
---
# File Menu

The **File menu** on the [menu bar](<../../workspace.md>) contains options dealing with the management of extensions.

The File menu contains the following operations:

Menu Item | Description
:--------:|:-----------
![Icon for creating a new extension in the File menu](images/file-new.gif "New File Icon") New | Creates a [new extension](<../../../../integration-with-systems/integration-studio/extension-life-cycle/extension-create.md>).
![Icon for opening an existing extension in the File menu](images/file-open.gif "Open File Icon") Open | Opens an extension already created in Integration Studio. Simply select the XIF (Extension and Integration Framework) file and all the elements defined for the extension are available in the [Extension](<../../multi-tree-navigator.md>) and [Resources](<../../resources-tree.md>) tree.
Close | Closes the current extension. If you have not saved it, Integration Studio prompts you with the Save window.
![Icon for saving the current extension in the File menu](images/file-save.gif "Save File Icon") Save | Saves the extension in a XIF file.
Save As... | Launches the "Save As..." window, where you can specify the name of the extension.
Import | In this option you can import ![Icon for importing actions from a .NET assembly in the File menu](images/net-wizard.gif "Import .NET Assembly Icon") [actions from a .NET assembly](<../../../../integration-with-systems/integration-studio/managing-extensions/net-assembly-import-action.md>) and ![Icon for importing entities from a database in the File menu](images/database-wizard.gif "Import Database Entities Icon") [entities from a Database](<../../../../integration-with-systems/integration-studio/managing-extensions/entity-import-from-database.md>). You can also import from other technologies, based on the Plug-in's you have installed to extend Integration Studio.
![Icon for selecting a Platform Server in the File menu](images/connect-server.gif "Select Server Icon") Select Server... | Allows you to [select the Platform Server](<server-select-window.md>) you want to use.
![Icon for downloading an extension from the Platform Server in the File menu](images/download-icon.gif "Download Icon") Download... | Allows you to [download an extension](<../../../../integration-with-systems/integration-studio/managing-extensions/extension-download.md>) already published in the Platform Server you are connected to.
![Icon for verifying the current extension's validity in the File menu](images/validate.gif "Verify Icon") Verify | [Verifies if the current extension is valid](<../../../../integration-with-systems/integration-studio/extension-life-cycle/extension-verify.md>) and ready to be published in a Platform Server.
![Icon for verifying and saving the current extension in the File menu](images/verify-save-icon.gif "Verify and Save Icon") Verify and Save | [Verifies if the current extension is valid](<../../../../integration-with-systems/integration-studio/extension-life-cycle/extension-verify.md>) and ready to be published in a Platform Server. If so, the extension is saved.
![Icon for 1-Click Publish to deploy the current extension to a Platform Server in the File menu](images/1-click-publish-icon.gif "1-Click Publish Icon") 1-Click Publish | Allows you to [publish the current extension](<../../../../integration-with-systems/integration-studio/extension-life-cycle/extension-1-cp.md>) in a Platform Server.
![Icon for updating the source code of the current extension in the File menu](images/update-source-code.gif "Update Source Code Icon") Update Source Code | [Synchronizes the source code](<../../../../integration-with-systems/integration-studio/extension-life-cycle/extension-update-source-code.md>) you added in the IDE (Integrated Development Environment) with the definition of the extension elements.
![Icon for opening the extension's solution in the specified IDE for .NET extensions in the File menu](images/launch-ide-net.gif "Edit Source Code Icon") Edit Source Code | [Opens the solution of your extension](<../../../../integration-with-systems/integration-studio/extension-life-cycle/extension-code-edit.md>) in the IDE you specified for .NET extensions.
Most recent files | List with the extensions that you recently opened in Integration Studio.
Exit | Closes Integration Studio.
