---
summary: Learn the best way to handle immediate corrective development situations, also known as Hotfix.
tags: support-Application_Lifecycle-featured
locale: en-us
guid: e79dfbfc-4c0b-4239-ae8d-824f5da95d2d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=257:90
---

# Apply a Hotfix

This topic describes how to implement an immediate corrective development, also known as **Hotfix**.

We highly recommend publishing hotfixes to a Pre-Production environment fully synchronized with a Production environment, and not to the Production environment directly. Both environments should have the same application version as well as its data replicated. This way you can test and debug the hotfix and then deploy it to Production, with no downtime. Finally the hotfix is propagated backwards to previous environments (Quality Assurance and Development).

In the following example, it is described how a hotfix is applied to fix a severe bug found in the eCommerce application.

## Fix the Defect

A severe defect was discovered in the eCommerce application in Production and has to be immediately fixed. Proceed as follows:

1. Open Service Studio.
1. Connect it to the Pre-Production environment (or one synchronized with Production).
1. Download the module with the defect.
1. Fix the defect, deploy the module back to Pre-Production, and test it.

The version number in Pre-Production has changed: it is suffixed with a '+' (for new changes) and is in red because it is a hotfix.

![Screenshot showing the version number in Pre-Production environment suffixed with a '+' indicating a hotfix, highlighted in red.](images/apply-a-hotfix-1.png "Pre-Production Environment with Hotfix Version")

## Deploy the Hotfix to Production

To apply the hotfix to Production, simply [deploy the application](<deploy-an-application.md>) from Pre-Production to Production. LifeTime automatically suggests you to choose 'Tag &amp; Deploy 1.7.1'. The hotfix is tagged with a third number in Pre-Production and the application is deployed to Production.

Both Pre-Production and Production have now the 1.7.1 version, and the Pre-Production version is still in red: the hotfix needs to be propagated backwards.

![Screenshot of the deployment process with 'Tag & Deploy 1.7.1' highlighted, indicating the deployment of a hotfix to Production.](images/apply-a-hotfix-2.png "Deploying Hotfix to Production")

## Propagate the Hotfix

To solve an hotfix, all changes made to the application have to be propagated backwards to all of the previous environments; in this case first to Quality Assurance, and then to Development. Proceed as follows:

1. Click on the eCommerce application: the modules are listed and the ones with the hotfix are marked with a red '+'.

    ![Screenshot of the eCommerce application modules list with hotfix changes marked by a red '+' sign.](images/apply-a-hotfix-3.png "eCommerce Application Modules with Hotfix")   

1. Merge all the modules with the hotfix changes in Pre-Production to Quality Assurance: click on the compare button (the difference sign) between the environments and select the specific changes you have done to implement the hotfix.

1. In Service Studio select the hotfix changes and click **Merge**.

1. In Service Studio publish the new versions of the modules to Quality Assurance.

1. Repeat steps 2, 3 and 4 from Quality Assurance to Development.

1. When the fix is propagated through all environments, click the **Mark Hotfix as Solved** button on the application details screen, to signal that the fix is now implemented across all infrastructure.

The hotfix is solved and there are no more application versions marked in red.

![Screenshot showing the application versions with no red highlights, indicating that the hotfix has been successfully propagated and marked as solved.](images/apply-a-hotfix-5.png "Hotfix Marked as Solved")
