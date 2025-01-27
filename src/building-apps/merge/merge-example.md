---
summary: Explore conflict resolution in OutSystems 11 (O11) using the Compare and Merge feature for simultaneous module edits.
locale: en-us
guid: a0c7450d-ca61-460a-9188-881adb2f40fb
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=280:147
tags: version control, conflict resolution, source control, collaboration, development best practices
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Compare and merge example with conflicts

In this example you are trying to publish the module, but a window **Modified version detected** shows up. It seems that you and your fellow developer edited the module at the same time. You select **Merge and publish** to try the automatic merge, but there are conflicting changes in the local version of the module and the version on the server. An automatic integration of changes is not possible, and you are presented with the **Compare and Merge** window:

![Screenshot of the 'Modified version detected' window indicating conflicts in the module](images/conflicts-detected.png "Conflicts Detected Window")

After analyzing the **Compare and Merge** window, you see that:

* You both edited the CSS on the "ClientList" screen. You need to resolve the conflicting changes.
* You both edited the "Section" Assign on the "ButtonOnClick" action. You'll need to resolve the conflicts here as well.
* The other developer added the screen "Report". There are no conflicts to resolve there.

These could be the steps to resolve the conflicts.

1. Double-click the element **Style Sheet (merged with conflicts)**. The **Compare and Merge - Style Sheet** opens. The number in the tab **Merged version (1 conflict)** indicates the number of conflicts.

    ![Compare and Merge window showing conflicting CSS edits in the 'ClientList' screen](images/conflicts-text.png "Compare and Merge - Style Sheet")

1. Select which part of the CSS code goes into the resulting local module that you will publish at the end of the merge. Click the arrow icon next to the text to replace `color: yellow;` with  `color: blue;`. **Merged version (1 conflict)** changes to  **Merged version (0 conflicts)**. You can also edit the code by typing in the **Merged version** pane.

    ![Arrow icon indicating the selection of CSS code to resolve conflicts in the merged version](images/conflicts-text-orange-arrow.png "Resolving CSS Conflicts")

1. Click **Done and back** in the lower right corner to return to the **Compare and Merge** section.

    ![Compare and Merge window with the 'Style Sheet (merged with conflicts)' element highlighted](images/merge-example-compare-ss.png "Compare and Merge Section")

1. Double-click **ButtonOnClick** to open the **Compare and Merge - ButtonOnClick** window. You can see that the `Section` assign element has conflicting values.

    ![Compare and Merge window showing conflicting changes in the 'ButtonOnClick' action](images/visual-element-changes.png "Compare and Merge - ButtonOnClick")

1. Click on the value viewer to open **Compare and Merge - Value** window. The value viewer button is labeled by the three dots (`...`).

    ![Close-up of the value viewer button with three dots indicating more options for resolving conflicts](images/visual-element-value-viewer-button.png "Value Viewer Button")

1. Click the check box in the  **Merged version (1 conflict)** pane to select the value from your version of the module. **Merged version (1 conflict)** changes to **Merged version (0 conflicts)**.

    ![Checkbox selection in the 'Merged version (1 conflict)' pane to resolve a conflict in the module](images/text-changes-checkbox.png "Selecting Merged Version Value")

1. Click **Done and back** in the lower right corner to return to the **Compare and Merge - ButtonOnClick** section.

1. Finally, click **Back** in the lower right corner to return to the main **Compare and Merge** window. If there are no conflicts (no elements highlighted red), you can continue to the next step to publish the module.

1. Click **Merge and publish** to update the local version of the module and publish it. If you want to update the local module, continue working on it and publish later — at this step you should click **Merge**.

    ![Final step in the Compare and Merge process with the 'Merge and publish' button highlighted](images/merge-complete.png "Merge and Publish Completion")
