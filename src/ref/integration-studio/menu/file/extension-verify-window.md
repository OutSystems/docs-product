# Verify Window

The Verify window ![](images/validate.gif) is launched when you are [verifying](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-verify.md>) your extension.

The areas and buttons available in the Verify window are presented below.

Verify log
:   In this area you can watch the evolution of the verify operation. You have a line for each step involved in the verify: [Verify the extension definition](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-verify-definition.md>), [Update Source Code](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-update-source-code.md>), and [Compile](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-compile.md>).

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
:   This operation belongs to the [1-Click Publish operation](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-1-cp.md>).

Upload
:   This operation belongs to the [1-Click Publish operation](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-1-cp.md>).

Publish
:   This operation belongs to the [1-Click Publish operation](<../../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-1-cp.md>).

Close
:   Closes the Verify window with no further action.
