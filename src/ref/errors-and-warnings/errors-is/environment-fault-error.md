---
locale: en-us
guid: 0da9d6af-49d3-4ddf-a728-5984516ccf04
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Environment Fault Error

Message
:   `An error occurred while preparing the templates generation: <error detail>.`

Cause
:   It was not possible to complete the generation of the extension templates. These templates will be stored in a folder under the extension folder and are generated during the [creation of an extension](<../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-create.md>), when [updating the source code](<../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-update-source-code.md>) or when using the [Compare With Template operation](<../../integration-studio/editor/resource.md#comparing-with-template>).

Recommendation
:   This error is related to a file system error and you should check whether your environment is working properly: If Integration Studio has the permissions necessary to write these template files in the extension folder; if your disk has space available; if the folder where the extension is being stored exists. If the problem persists, contact your System Administrator to ask for help.

---

Message
:   `Unable to open the Integrated Development Environment.`

Cause
:   You are trying to launch the Integrated Development Environment you specified and it was not possible to open it.

Recommendation
:   You should check whether the IDE (Integrated Development Environment) path is correctly defined in [Options Window](<../../integration-studio/menu/edit/options.md>). Try to launch the IDE independently from Integration Studio. If the problem persists, contact your System Administrator.

---

Message
:   `A time-out has occurred. Compiler appears to be blocked.`

Cause
:   You are trying to [compile](<../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-compile.md>) your extension but the Compiler is not responding.

Recommendation
:   Check whether there are Compiler processes running that might prevent the compilation from continuing. Try to compile the extension again and if the problem persists, contact your System Administrator.

---

Message
:   `Unable to save the Extension.`

Cause
:   To save an extension it is necessary that none of its source files are being used in the IDE. In this situation, Integration Studio pops-up a message notifying you that you should close these files in your IDE (Integrated Development Environment). If you ignore this suggestion, this error message is presented and the extension could not be saved.

Recommendation
:   Close your IDE and try to save the extension again.

---

Message
:   `An error occurred while saving the Extension: <error detail>.`

Cause
:   You are trying to save your extension and a general error was found.

Recommendation
:   This error is related to a file system error and you should check whether your environment is working properly: If your disk has space available; if the folder where the extension is being saved exists. If the problem persists, contact your System Administrator to ask for help.

---

Message
:   `An error occurred while accessing the file system: <error detail>.`

Cause
:   Integration Studio needs to access the file system but a general error was detected.

Recommendation
:   This error is related to a file system error and you should check whether your environment is working properly: If Integration Studio has the permissions necessary to access the extension files in the extension folder; if your disk has space available; if the folder where the extension is being stored exists. If the problem persists, contact your System Administrator to ask for help.

---

Message
:   `'OutSystems Integration Plug-in for Eclipse' cannot be copied to the folder plugins, under the Eclipse installation folder.`

Cause
:   It was not possible to copy the "OutSystems' Integration Plug-in for Eclipse" into the folder plugins.

Recommendation
:   This error is related to a file system error and you should check whether your environment is working properly: If Integration Studio has the permissions necessary to copy the Plug-in to the folder plugins; if your disk has space available; if the folder to where the Plug-in is to be copied exists. If the problem persists, contact your System Administrator to ask for help.

---

Message
:   `Folder plugins, under the Eclipse installation folder, does not exist.`

Cause
:   The folder plugins, where the "OutSystems' Integration Plug-in for Eclipse" is to be copied, does not exist.

Recommendation
:   This error is related to a file system error and you should check whether your environment is working properly. Either you need to install Eclipse again, or simply restore the Eclipse installation. If the problem persists, contact your System Administrator to ask for help.

---

Message
:   `'OutSystems Integration Plug-in for Eclipse' is missing.`

Cause
:   It was not possible to copy OutSystems' Integration Plug-in for Eclipse to the folder plugins, under the Eclipse installation folder.

Recommendation
:   For some unexpected reason, "OutSystems' Integration Plug-in for Eclipse" does not exist in your desktop. Either install Integration Studio again, or check with your System Administrator to determine what could have happened to the plug-in.

---

Message
:   `'OutSystems Integration Plug-in for Eclipse' cannot be copied since the Eclipse SDK path is invalid.`

Cause
:   The Eclipse SDK path specified in Integration Studio is not correct.

Recommendation
:   Check the Eclipse SDK path under the [Options Window](<../../integration-studio/menu/edit/options.md>), in the Edit menu.
