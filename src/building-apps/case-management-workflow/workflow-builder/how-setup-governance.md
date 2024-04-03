---
tags: Workflow Builder; Case Management; OutSystems; Business Users; Citizen Developers; Citizen Dev; Workflow; Governance Model; Business developers
summary: Learn how to set up the users governance model in Workflow Builder.
guid: b0e9d928-403a-4d65-b5bc-c945f78b8436
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=4376:912
---

# How to set up the users governance model

The goal of this document is to guide [IT users](../../../manage-platform-app-lifecycle/manage-it-teams/about-permission-levels.md) through the setup the end users governance model in [Workflow Builder](http://workflowbuilder.outsystems.com/).

<div class="info" markdown="1">

You need LifeTime version 11.5.0 (released March 2020) or later to set up the users governance model.

</div>

Setting up the users governance model, allows you to define what users can do in Workflow Builder and what shared services or components they can use.

To set up the user governance, perform the following steps:

1. Create teams, roles, and IT users in LifeTime. Refer to [Manage IT users](../../../manage-platform-app-lifecycle/manage-it-teams/about-permission-levels.md) and to [End user management](../../../user-management/end-user-manage/accessing-users.md) for more information.

1. On the **LifeTime environment address** field, enter your LifeTime environment address.

1. [Get your LifeTime service account token](../../../ref/apis/lifetime-deployment/rest-api-authentication.md#creating-a-service-account) and enter it on the **LifeTime service account token** field.

    ![Initial setup screen for user governance in Workflow Builder showing fields for environment address and service account token](images/wfb-setup-govern-init.png "Workflow Builder Governance Setup Initialization")

1. Click on the **Save** button to save the changes.
