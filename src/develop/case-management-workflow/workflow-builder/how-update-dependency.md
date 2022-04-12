---
tags: Workflow Builder; Case Management; update dependencies;
summary: Learn how to instal or update Workflow Builder dependencies.
guid: 456764c4-6370-4363-b576-8d399be303e3
locale: en-us
---
# How to install or update dependencies

[Workflow Builder](http://workflowbuilder.outsystems.com/) has one dependency, the Case Management framework.
To publish Workflow Builder apps, the environment must have the latest version of the Case Management framework.

To install or update this dependency, you must be a [Workflow Builder admin](how-works.md#workflow-builder-administrator), and follow these steps:

1. Select your user name, and then select **Settings**.

1. In the **Dependencies** tab, select **Install CM framework manually**.

1. In the **Install Case Management Framework** dialog, select **Download Case Management Framework** and save the **.osp** file in your computer.

1. Select **Service Center console > Factory > Solutions**.

1. In Service Center, select **Upload & Publish a Solution**.

1. Select **Choose File** and select the **.osp** file that you downloaded in step 3.

1. Select **1-Click Publish**.

1. Validate if the Solution is successfully published by checking for a **Done: The solution was successfully published** message.

1. In Workflow Builder, select the checkbox to confirm you completed all the steps, and then click on the **Installation complete**.

After completing these steps, Workflow Builder re-checks and updates the status of your dependencies.
