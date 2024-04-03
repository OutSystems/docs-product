---
locale: en-us
guid: e3eef60b-0694-4c49-9666-5f4749d6cf32
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
summary: The article explains how to edit .NET extension source code in Integration Studio and synchronize it with the extension definition
---
# Edit Extension Source Code

You can open the .NET IDE directly from Integration Studio, with the advantage of synchronizing the elements definition with the extension source code. In fact, before launching the IDE, Integration Studio updates the source code. Learn more about [Update Source Code](<extension-update-source-code.md>).  

## How to edit the extension source code

1. In the **File** menu or in the toolbar, click ![Animated GIF showing the Edit Source Code button in Integration Studio](images/launch-ide-net.gif "Edit Source Code Button") **Edit Source Code**.

    When developing an extension you must edit the source code in the .NET IDE. In this situation you are responsible of ensuring the synchronization of the written code, since Integration Studio only guarantees the synchronization of the extension definition.

1. The IDE you specified in the [Options Window](<../../../ref/integration-studio/menu/edit/options.md>) is launched with the .NET solution.
