---
summary: This technical preview enables you to set application Site Properties in the target environment while performing a deployment in LifeTime.
tags: support-Application_Lifecycle-featured
---

# Technical Preview - Configure Site Properties During Deployment

<div class="info" markdown="1">

Read [how features in Technical Preview work](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Technical_Preview_features). We encourage you to try these features out and to [send us your feedback](https://www.outsystems.com/forums/discussion/48360/configure-site-properties-during-deployment/#Post177757).

</div>

This technical preview enables the configuration of Site Properties in the target environment during the deployment plan.

![](images/configure-settings-during-deploy-1.gif)

With this feature disabled, when you deploy an application with Site Properties that must have different values in the target environment, you need to use the Service Center console to [update them in the target environment after deployment](configure-application-settings-after-deployment.md).

<div class="info" markdown="1">

**To use this feature, make sure that:**

* The technical preview **Configure site properties during deployment** was [activated in LifeTime](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Technical_Preview_features).
* The **source** and **target** environments for the deployment are running Platform Server 11 Release Apr.2019 CP1 or later.
* The user executing the deployment has the "Change & Deploy Applications" permission for all applications in the deployment plan.

</div>

After activating the technical preview **Configure site properties during deployment**, the deployment plan wizard enables you to configure the Site Properties of the applications being deployed during the step **Configure application settings**.

![](images/configure-settings-during-deploy-2.png?width=800)

When deploying applications, after adding the applications to your deployment plan, the deployment plan wizard takes you to the step **Configure application settings**.

If there are application modules in the plan with new Site Properties that were never set in the target environment, you can define in this step the **Effective value** for those Site Properties in the target environment.

![](images/configure-site-settings-during-deploy-3.png?width=800)

In the deployment plan wizard, you can also see and change the existing settings of the applications to deploy. Click the button **All settings** to see the existing settings.

Select an application from the applications list to the left to see the settings for that application. If your deployment plan contains applications with no changes, you will not be able to change the settings for those applications.

There are some situations when this step is **skipped** or **disabled**:

* The step will be **skipped** when there are no new settings to configure. However, if you need to change any existing setting, you can manually go back to **Configure application settings** by clicking the step in the wizard.

    ![](images/configure-settings-during-deploy-4.png?width=800)

* The step will be **disabled** when there aren't any settings to configure or the user executing the deployment does not have the required permissions.

The Site Properties of the applications to deploy are set in the target environment after the applications are published. Beware of Timers that run `When Published`, since the Site Properties that the Timers may use are not yet updated when the Timers run.

This feature doesn't apply to multi-tenant Site Properties.
