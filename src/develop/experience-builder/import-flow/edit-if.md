---
summary: Edit previously imported Flows in Experience Builder.
locale: en-us
guid: bfe493f7-3801-4266-a435-e2d7b64e395f
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=4454:2894
---

# Editing Flow Templates

After importing flows into Experience Builder, you can edit them. The way you edit the flows depends on the type of data you want to edit:

* To modify metadata you defined in Experience Builder during the importing process (for example, screens display name, screen preview image) use the [Flow edition process](#edit-the-flow-metadata).

* To apply changes made in Service Studio to the flows template module, use the [Flow reimport process](#reimporting-a-flow).

## Edit the flow metadata

1. Log into Experience Builder and click the **Flows** tab.

    ![Screenshot of the Flows tab in Experience Builder interface](images/flows-tab-eb.png "Flows Tab in Experience Builder")

1. Locate the imported flow you want to edit and from the contextual menu, select **Edit flow**.

    ![Contextual menu in Experience Builder showing the 'Edit flow' option](images/edit-flow-eb.png "Edit Flow Option")

1. Edit the flow display name,  flow category, and tags and then click the **Next: edit screens** button.

    ![Editing flow metadata such as display name, category, and tags in Experience Builder](images/edit-wizard-flow-metadata-eb.png "Edit Flow Metadata Wizard")

1. Edit the screen's display name, **Has menu?** property, screen image, and reposition the exit points and then, click the **Next: review flows** button.

    ![Interface for setting additional data for screens including display name, menu property, and image](images/set-additional-data-eb.png "Set Additional Data for Screens")

1. Check your changes and click the **Next: manage update** button.

    ![Reviewing edited flow details in Experience Builder before managing updates](images/edit-wizard-review-eb.png "Review Edited Flow")

1. Review which apps will be affected by this change and then click the **Save** button. 

    All apps that use any re-imported flows are moved to Draft. This allows you to review them again before re-publishing them.

    ![Managing update process in Experience Builder showing affected apps](images/edit-wizard-manage-update-eb.png "Manage Update Wizard")

## Reimporting a flow

To reimport a flow, you must reimport the entire template module that contains it. Keep in mind that all flows contained in that template module will also be updated by this process.

1. Log into Experience Builder and click the **Flows** tab.

    ![Screenshot of the Flows tab in Experience Builder interface](images/flows-tab-eb.png "Flows Tab in Experience Builder")

1. Click the **Import Flow** button.

    ![Import Flow button in Experience Builder to start the flow import process](images/import-flows-button-eb.png "Import Flows Button")

1. Select the **I have already created my Experience Builder template** checkbox and then click the **Next: select template** button.

      ![Checkbox for confirming the creation of an Experience Builder template module](images/module-template-created-eb.png "Module Template Created Checkbox")

1. From the list of modules, select the one that contains the flow template you want to update and click the **Next: validate template** button.

    ![Selecting an application module from a list in Experience Builder](images/select-application-eb.png "Select Application Module")

1. Analyze the validation process feedback messages. Your module needs to be re-validated to check if it still complies with Experience Builder guidelines.

    If there are no blocking errors, click the **Next: define flows** button to continue the importing process.

    ![Validation feedback messages during the module reimport process in Experience Builder](images/check-validation-eb.png "Check Module Validation")

1. Edit flow data according to the [metadata reference](metadata-if.md) document. Then, click the **Next: define screens** button.

    ![Editing flow data during the reimport process in Experience Builder](images/eb-reimport-flow.png "Reimport Flow Data Editing")

1. Edit the screen data according to the [metadata reference](metadata-if.md) document and then click the **Next: review flow** button..

    ![Editing screen data during the flow reimport process in Experience Builder](images/reimport-screen-eb.png "Reimport Screen Data Editing")

 1. Review all of the flows and screens. Ensure that all of the names and images are in place and that the screens inside each flow are in the correct order. Then click the **Next: Manage update** button.

    ![Reviewing reimported flows and screens in Experience Builder](images/reimport-review-eb.png "Review Reimported Flow")

1. Review which apps will be affected by this change and then click the **Save** button. All apps that use any re-imported flows are moved to Draft. This allows you to review them again before re-publishing them.

    ![Managing update process in Experience Builder showing affected apps](images/edit-wizard-manage-update-eb.png "Manage Update Wizard")
