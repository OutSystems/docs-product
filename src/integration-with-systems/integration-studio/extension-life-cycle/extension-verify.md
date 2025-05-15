---
locale: en-us
guid: 1b37d2df-87ea-4a65-a8c1-82b41ede7e07
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility-and-Integration?type=design&node-id=3387%3A2064&mode=design&t=187UAgmZTPxcY0ZG-1
summary: OutSystems 11 (O11) includes a Verify operation to ensure extensions are valid and ready for publication on a Platform Server.
tags: extensions, platform server, dynamic link library (dll), verification process, integration studio
audience:
  - full stack developers
  - backend developers
  - frontend developers
  - platform administrators
outsystems-tools:
  - integration studio
coverage-type:
  - apply
---

# Verify the Extension

The Verify operation checks whether the extension is valid and ready to be published in a Platform Server. This operation involves the following steps:

1. **Verify the extension definition.** Only valid extensions can be published and, therefore, used in a module. For more information, see [Verify the extension](<extension-verify-definition.md>).

1. **Update the source code with the extension definition.** For more information, see [Update the Extension Source Code](<extension-update-source-code.md>).

1. **Compile the extension.** This step will generate the main DLL (Dynamic Link Library). For more information, see [Compile the extension](<extension-compile.md>).


## Verifying an Extension

To verify your extension do the following:
  
1. In the **File** menu or in the toolbar, click ![Icon for validating an extension in the File menu or toolbar](images/validate.png "Validate Extension") **Verify**, ![Icon for the Verify and Save option for an extension](images/verify-save-icon.png "Verify and Save Extension") **Verify and Save**, or ![Icon for the 1-Click Publish option for an extension](images/1-click-publish-icon.png "1-Click Publish Extension") [**1-Click Publish**](<extension-1-cp.md>).
1. Check the [Verify window](<../../../ref/integration-studio/menu/file/extension-verify-window.md>) for any errors and warnings for your extension.
