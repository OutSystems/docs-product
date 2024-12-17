---
tags: workflow conversion, workflow builder, workflow management, outsystems platform, app development
summary: Explore how to convert a Workflow Builder app to Service Studio in OutSystems 11 (O11).
guid: d1b8c5b6-6844-42f6-91cb-0dd183c2eda4
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=4376:907
audience:
  - business analysts
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
  - workflow builder
coverage-type:
  - apply
---

# Converting a Workflow Builder app to Service Studio

If you want to evolve your app by adding features unavailable in Workflow Builder, you need to convert the app to Service Studio. 
Once you convert your app to Service Studio, you can no longer use Workflow Builder to edit it.
 
To convert your app you must be a [**Workflow Builder administrator**](how-works.md#workflow-builder-administrator) and follow these steps:

1. On the **My Apps** screen, click the three dots (**...**) in your app.

1. From the dropdown menu, click **Convert to edit in Service Studio**.

    ![Dropdown menu with the option to Convert to edit in Service Studio highlighted](images/wfb-convert-ss.png "Convert to edit in Service Studio option")

1. Read the disclaimer carefully, and click the **I understand and want to convert my app** checkbox.

    ![Conversion disclaimer screen with the checkbox for understanding and wanting to convert the app](images/wfb-convert-ss-disclaimer.png "Conversion Disclaimer")

1. To start the conversion, click **Convert app**. The conversion process can take several minutes to complete.

    ![Screen showing the app conversion process with a progress indicator](images/wfb-convert-ss-converting.png "App Conversion Process")

1. Once the conversion ends, the app shows the status **Converted to Service Studio**. From this point on, you can now edit the app in Service Studio and you can't edit the app in Workflow Builder.

    ![App status updated to 'Converted to Service Studio' after the conversion process](images/wfb-convert-ss-converted.png "Converted to Service Studio Status")

1. If you want to remove the converted app from the **My Apps** screen of Workflow Builder, click the three dots (**...**) in your app and click **Remove from Workflow Builder**.

    ![Option to remove the app from Workflow Builder displayed in a dropdown menu](images/wfb-convert-ss-remove-wb.png "Remove from Workflow Builder Option")
