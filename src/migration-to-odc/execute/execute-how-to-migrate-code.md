---
summary: "OutSystems 11 (O11) to ODC code conversion using the app conversion console: run conversions, publish ODC apps, and troubleshoot errors."
guid: 4748549a-2df3-4763-bcfc-73be131cf9ff
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
tags:
  - Deploy
  - Libraries
  - Troubleshooting
platform-version: o11
figma:
audience:
  - Front-end developer
  - Developer
  - Platform administrator
outsystems-tools:
  - lifetime
  - conversion assessment tool
  - odc portal
coverage-type:
  - apply
topic:
  - convert-o11-code
  - publish-converted-apps
helpids: 30791
isautopublish: true
---

# Code conversion using the tool

This article explains how to convert O11 code to ODC using the app conversion console available in the ODC Portal.

## Prerequisites

Before you convert the code of the O11 apps in a [conversion plan](https://www.outsystems.com/tk/redirect?g=ab447daa-dffc-4374-8ae6-986c8f3d63c4), ensure the following:

* Your O11 infrastructure follows the [prerequisites for app conversion](execute-intro.md#prerequisites).

* The O11 apps in the plan are [prepared for ODC](https://www.outsystems.com/tk/redirect?g=14a67d54-aa12-45bc-8262-48c9f2a2780c).

* The source environment for code conversion is correctly configured on the **Conversion Assessment Tool > Maintenance** tab.

* The [configurations for the app conversion](execute-connect-to-tool.md) are in place.

* The O11 apps to convert are [deployed and tagged](execute-about-migrate-code.md#tagging-your-apps) in the source environment.

* You have the **Organization management** > **Convert O11 code** permission in ODC.

## Code conversion

To convert O11 code to ODC, follow these steps:

1. Log in to the ODC Portal.

1. Under the **Management** menu, go to **OUTSYSTEMS 11 > App Conversion**.

1. If your ODC organization is connected to several O11 infrastructures, select the infrastructure with the apps you want to convert from the top-right dropdown.

    The page lists the [conversion plans](https://www.outsystems.com/tk/redirect?g=ab447daa-dffc-4374-8ae6-986c8f3d63c4) defined in the **Conversion Assessment Tool** of the selected O11 infrastructure.

    In a [multi-portfolio organization](https://www.outsystems.com/tk/redirect?g=f7a2c1d8-3e5b-4a9f-b812-6d8e4f2a1c3b), the target ODC portfolio for the app conversion is the one [configured for the selected O11 infrastructure](execute-connect-to-tool.md).

1. Select the plan you want to convert to navigate to its details page.

    Validate the status of the **Last assessment** to ensure that all O11 apps in the plan are [prepared for ODC](https://www.outsystems.com/tk/redirect?g=14a67d54-aa12-45bc-8262-48c9f2a2780c). You cannot convert until the status of all Assets in the plan is **Ready for ODC** or **Change in ODC**.

1. Click **Convert code** to start a new code conversion.

    A list of O11 apps is displayed. You can click each app to review its corresponding modules and their revision number.

1. To confirm the conversion, click **Convert**.

    The code conversion process begins, and the status of apps moves to **Converting**.

If the conversion is successful, the process ends with **Finished** status. The O11 apps mapped in the Assessment tool are converted to ODC apps and libraries. These ODC apps and libraries are still **Unpublished**.

Now, in ODC, you must [publish the ODC apps and libraries](#publish).

If the conversion is unsuccessful, the process ends with a **Finished with errors** status, and you cannot open the app or the library in ODC Studio. See how to [identify code conversion issues](execute-troubleshooting.md#code-issues).

### Publish ODC apps and libraries {#publish}

The tool displays a list of apps and libraries, with producers at the top and consumers at the bottom. To prevent dependency errors in ODC, you must publish the apps and libraries in the order they appear.

To publish an ODC app or a library, follow these steps:

1. Following the order in the list, select an app or library with the **Unpublished** status and click **Download**. The file is downloaded to your local machine.

1. Open the file in **ODC Studio**.

1. [Adjust the converted code](execute-adjust-converted-code.md) as needed.

1. Select **App** > **Check for dependency updates**.

    <div class="info" markdown="1" id="preview-dependency-updates">

    Before you fix the TrueChange errors in the next step, you can preview which elements changed. This helps you identify where the errors come from, especially when a producer app or library changed after the code conversion.

    To preview the impact of the dependency update, follow these steps:

    1. Select **App** > **Compare and Merge with another revision of file**, select **Choose a file**, and select the file you originally downloaded.

    1. Expand the **Dependencies** folder in the comparison to review the elements that changed. Once you're done, cancel instead of completing the merge.

    </div>

1. Fix all the TrueChange errors.

1. Publish the app or library to the target ODC stage.

1. If it's a library, [release that library](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/libraries/#release-library).

1. Repeat steps 1 to 6 to publish the converted apps and libraries in ODC.

## Next steps

* [Review the configurations of your converted apps](execute-configure-migrated-apps.md) to ensure they work correctly.
