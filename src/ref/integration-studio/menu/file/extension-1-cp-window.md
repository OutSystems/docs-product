---
locale: en-us
guid: 7ece2478-a4fe-4f05-8f53-3053d04f30e8
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# 1-Click Publish Window

The 1-Click Publish window ![](images/1-click-publish-icon.gif) is launched when you invoke the [1-Click Publish](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-1-cp.md>).

The areas and buttons available in the 1-Click Publish window are presented below.

Operation Log
: In this area you can watch the evolution of the operation you requested. You have a line for each of the involved stages in the 1-Click Publish: Verify, Save, and Publish operations. You also have a line for each error or warning that occurs during each step.

    If any [errors](<../../../errors-and-warnings/errors-is/intro.md>) occur during the verification, the process stops and you have to fix them in order to proceed. This window provides the necessary interface to continue the process, after fixing the detected error. Simply press Verify Again in the 1-Click Publish window.

    If any [warnings](<../../../errors-and-warnings/warnings-is/intro.md>) occur during the 1-Click process, they are listed in this window, one warning per line, but the process continues.

Details
:   Presents the description of the [error](<../../../errors-and-warnings/errors-is/intro.md>), [warning](<../../../errors-and-warnings/warnings-is/intro.md>), or general information.

Progress bar
:   Presents five stage markers, one for each operation involved in the 1-Click Publish, with the one that is highlighted corresponding to the operation currently being executed.

    ![](images/note.gif) The Verify includes three steps: [Verify the Extension Definition](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-verify-definition.md>), [Update the Extension Source Code](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-update-source-code.md>) and [Compile the Extension](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-compile.md>).

Verify Again
:   Verifies your extension again. This button is available when the extension has errors and,therefore, you cannot proceed with the 1-Click Publish. When you press this button, the extension is validated again. For more details, see [Verify the Extension](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-verify.md>).

Save
:   Saves the extension to a XIF (Extension and Integration Framework) file.

Upload
:   Uploads the extension to the Platform Server you are connected to.

Publish
:   Publishes the extension in the Platform Server you are connected to.

Close
:   Closes the 1-Click Publish window.

Once the extension is published it can be [used in your modules](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-use.md>).
