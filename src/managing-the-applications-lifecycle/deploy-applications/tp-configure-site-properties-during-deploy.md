---
summary: Learn how to set application Site Properties in the target environment while performing a deployment in LifeTime.
tags: 
locale: en-us
guid: 4acf3283-61b0-4409-a357-cb2ef63f1a5e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing-the-Applications-Lifecycle?type=design&node-id=257%3A33&mode=design&t=98kL4vRdGIKpuwQm-1
---

# Configure site properties during deployment

You can configure your applications' site properties in the target environment during the deployment plan.

<div class="info" markdown="1">

Ensure the user executing the deployment has the **Change & Deploy Applications** permission for all apps in the deployment plan.

</div>

The deployment plan wizard allows you to configure the site properties of the apps being deployed during the **Configure application settings** step.

![Screenshot of the deployment plan wizard highlighting the 'Configure application settings' step.](images/configure-settings-during-deploy-2.png "Configure Application Settings During Deployment")

When deploying apps, after you add the apps to your deployment plan, the deployment plan wizard takes you to the **Configure application settings** step.

If there are application modules in the plan with new site properties that were never set in the target environment, you can define the **Effective value** for those site properties in the target environment in this step.

Additionally, if you make any changes to the **IsSecret** property of the site property, you must define the effective value for the site property.

![Screenshot of the deployment plan wizard where the user defines the Effective value for new Site Properties.](images/cfg-site-prop-stg-lt.png "Effective Value for Site Properties")

In the deployment plan wizard, you can also change the existing settings of the applications to deploy. Because secret site properties don't have default values, the **Default Value** field will not display any information. To display the existing settings, click the **All settings** button.

Select an app from the app list to display the settings for that application. If your deployment plan contains applications with no changes, you can't change the settings for those apps.

The following are some examples of when this step is **skipped** or **disabled**:

* The step is **skipped** when there are no new settings to configure. However, if you need to change any existing settings, you can manually go back to **Configure application settings** by clicking the step in the wizard.

    ![Illustration of the deployment plan wizard with the 'Configure application settings' step skipped or disabled.](images/configure-settings-during-deploy-4.png "Skipping or Disabling Configuration Steps")

* The step is **disabled** when there aren't any settings to configure or the user executing the deployment doesn't have the required permissions.

The site properties of the applications to deploy are set in the target environment after the apps are published. Beware of Timers that run `When Published`, since the site properties that the Timers may use are not yet updated when the Timers run.

To update the site properties value in the target environment after the deployment, [use the Service Center console](configure-application-settings-after-deployment.md).

<div class="info" markdown="1">

This feature doesn't apply to multi-tenant site properties.

</div>


