---
summary: This article outlines steps for configuring migration assesment planner for migration to OutSystems Developer Cloud (ODC).
locale: en-us
guid: 29920fad-9efd-45ae-a4e4-212705fceb65
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Set up the Migration Assessment Tool

The Migration Assessment Tool helps you accelerate the Plan and Preparation stages of your O11 to ODC Migration, in the following ways:

* Define the O11 to ODC architecture blueprint, based on the Apps and Modules available in your O11 Development environment.

* Validate the O11 to ODC architecture blueprint.

* Understand and decide on what adjustment your team needs to do in O11, before migrating the apps to ODC.

## Prerequisites

You need to ensure the following before setting up the Migration Assessment Planner:

* You are part of the Early Access Program, and have been granted access to the Migration Kit.

* Your O11 environments use Platform Server 11.8.0 or later.

* Your IT User has the **Manage Users and Roles** permission.

## Install the Migration Assessment Tool Engine

1. Download the [Migration Assessment Tool Engine solution pack](resources/Migration_Assessment_Engine_v1_0.osp).

1. In your **LifeTime environment**, open Service Center and [upload and publish the Migration Assessment Tool Engine solution pack](https://success.outsystems.com/support/troubleshooting/application_lifecycle/deploy_applications_through_service_center/#step-2.upload-and-publish-the-solution-in-the-target-environment).

## Install the Migration Assessment Tool Console

1. Download the [Migration Assessment Tool Console solution pack](resources/Migration_Assessment_Console_v1_0.osp).

1. In any of your Environments, except for the LifeTime environment, open Service Center and [upload and publish the Migration Assessment Tool Console solution pack](https://success.outsystems.com/support/troubleshooting/application_lifecycle/deploy_applications_through_service_center/#step-2.upload-and-publish-the-solution-in-the-target-environment).

    <div class="info" markdown="1">

    OutSystems recommends you install the Migration Assessment Tool Console in your Development environment.
    Don't install the Migration Assessment Tool Console in the LifeTime environment.

    </div>

1. Still in the Service Center of the same Environment, [enable Single sign-on between app types (SSO)](../security/configure-authentication.md).

## Install the Probe in the Development environment

1. Download the [Migration Assessment Tool Probe solution pack](resources/Migration_Assessment_Probe_v1_0.osp).

1. In your **Development environment**, open Service Center and [upload and publish the Migration Assessment Tool Probe solution pack](https://success.outsystems.com/support/troubleshooting/application_lifecycle/deploy_applications_through_service_center/#step-2.upload-and-publish-the-solution-in-the-target-environment).

## Optional - Deploy the Probe to other environments

1. In the LifeTime console, deploy the Migration Assessment Tool Probe from the Development environment to other Environments where you want to also check the ODC-readiness of apps. For example, you may want to deploy the probe to the QA environment, so you can later run the assessment on apps during the app testing phase.

## Configure the Migration Assessment Tool

1. Open Migration Assessment Tool from the environment in which you installed the Migration Assessment Tool Console. Log in using your IT User credentials.

1. Go to the LifeTime management console, and create a service account and copy the authentication token.

1. In the Migration Assessment Tool, configure the access to LifeTime and the engine, by setting the following fields:

    * In **Engine URL (LifeTime)** set the **LifeTime address**.

    * In **Authentication token** paste the authentication token for the LifeTime Service Account.

1. Save and test the connection to LifeTime by selecting **Save**.

1. Configure the access to the Probes in the **Development** environment, by setting the **Analysis environment URL** with the Development environment address, and then selecting **Connect**.

    <div class="info" markdown="1">

    It's mandatory to configure the access to the **Development** probe.

    </div>

1. Optionally, configure the access to the Probes in the other environments where you deployed the probe.
