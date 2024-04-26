---
locale: en-us
guid: 426b3956-f51e-4d01-a743-33fcb462fce6
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
summary: The Verify window in Integration Studio provides an interface to monitor and fix errors during the extension verification process
---
# Verify Window

The Verify window ![Animated GIF showing the Verify window process in action](images/validate.gif "Verify Window Animation") is launched when you are [verifying](<../../../../integration-with-systems/integration-studio/extension-life-cycle/extension-verify.md>) your extension.

The areas and buttons available in the Verify window are presented below.

Verify log
:   In this area you can watch the evolution of the verify operation. You have a line for each step involved in the verify: [Verify the extension definition](<../../../../integration-with-systems/integration-studio/extension-life-cycle/extension-verify-definition.md>), [Update Source Code](<../../../../integration-with-systems/integration-studio/extension-life-cycle/extension-update-source-code.md>), and [Compile](<../../../../integration-with-systems/integration-studio/extension-life-cycle/extension-compile.md>).

    If any errors occurred during the Verify, for example the extension has an error, the process stops and you have to fix them in order to proceed. The Verify window provides you with the necessary interface to continue the process, after fixing the detected error. If any warnings occur during the Verify, they are listed in the Verify window, with each warning on a different line, but the process continues.

    Each error, warning, or piece of information is displayed on a separate line. On each line you have the category (error, warning or information), a small description and the details of the message. If the details are too long, you can check it in the Details area. The last line indicates the number of errors and warnings found.

    To determine exactly where this error or warning occurs, simply select the corresponding line, double-click the message or click on the ellipsis button at the end.

Detail
:   Presents a complete description of the error, warning, or information.

Progress Bar
:   Displays the progress of the operation.

Verify Again
:   Performs a new verification considering the fixes that have already been made. This operation is available when the extension has errors that you have to fix.

Save
:   This operation belongs to the [1-Click Publish operation](<../../../../integration-with-systems/integration-studio/extension-life-cycle/extension-1-cp.md>).

Upload
:   This operation belongs to the [1-Click Publish operation](<../../../../integration-with-systems/integration-studio/extension-life-cycle/extension-1-cp.md>).

Publish
:   This operation belongs to the [1-Click Publish operation](<../../../../integration-with-systems/integration-studio/extension-life-cycle/extension-1-cp.md>).

Close
:   Closes the Verify window with no further action.
