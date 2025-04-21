---
summary: This article outlines steps for configuring migration assesment planner for migration to OutSystems Developer Cloud (ODC).
locale: en-us
guid: 29920fad-9efd-45ae-a4e4-212705fceb65
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2336-2236
tags: migration, outsystems, cloud migration, database configuration, infrastructure management
audience:
  - platform administrators
  - full stack developers
  - architects
  - tech leads
outsystems-tools:
  - lifetime
  - platform server
coverage-type:
  - apply
---

# Set up the Migration Assessment Tool

<div class="info" markdown="1">

This article only applies to customers with access to the Migration Kit.

</div>

The Migration Assessment Tool helps you evaluate the readiness of O11 apps for the ODC migration and guides you through the necessary code adjustments.

The first step is to design your ODC architecture blueprint. This step is crucial to ensure that your applications, once migrated, can fully benefit from ODC capabilities, mainly app-independent lifecycle and high scalability, to name a few. In this process, the goal is to design a plan without any code changes. This plan will become your ODC apps. You use the O11 apps as building blocks for those apps, where an ODC app can be composed of one or [multiple existing O11 apps](./plan/plan-map-apps.md).

After mapping, the Migration Assessment Tool assesses elements of O11 apps and shows a report with patterns. These patterns address technical challenges during migration, such as dealing with O11-specific features that may be implemented differently in ODC and adapting app architecture. Following the patterns lets you update your application and transition from the older system to ODC's modern cloud-native framework.

The Assessment Tool consists of the following components:

Console:

* The app provides the user interface of the Assessment Tool.
* Lets you configure the connection with the engine and the probes.
* Provides you with the mapping functionality to organize the O11 apps and libraries in the ODC apps.
* It interacts with the engine.

Engine:

* It is the communication entry point between your O11 infrastructure and ODC tenant.
* Resides in LifeTime. You install the engine from the Service Center in the LifeTime environment.
* Interacts with the console and with other O11 environments through the probes.
* Initiates the probes and queues the scanning of the environments where the probes are installed.
* By default, the engine queues an analysis with the probes every 15 minutes.
* Engine keeps a record of all the findings

Probe:

* Identifies the source O11 environment for migration to ODC (development, testing, production…). The source environment is the code's origin and the data you migrate to ODC.
* The first probe you install is in  the development environment.
* Analyzes the O11 apps in the environment and returns the findings to the engine.

![Diagram showing the architecture of the Migration Assessment Tool, including the Console, Engine, and Probes in different environments (DEV, Q&A, PROD) and their interactions.](images/assessment-tool-architecture-diag.png "Migration Assessment Tool Architecture Diagram")

You can start planning the migration once you sign in to the Assessment Tool app. The process looks like this:

1. If you haven't already configured the tool, go to the home screen, select **Configuration** from the dropdown menu at the top, and enter the settings for LifeTime and the probes.
1. From the home screen, select the O11 environment from the dropdown button on the top.
1. From the **Map O11 apps** screen, select **Map O11 apps** to open a new screen that lets you map the existing O11 apps to new ODC apps. After you save the mapping, the app queues the analysis.

   <div class="info" markdown="1">

   This step requires preparation. See: [Map O11 to ODC architecture for one shot migration](plan/plan-map-apps.md).

   </div>

1. From the home screen, select **Open assessment** to view the findings, or select one of the ODC assets.
1. On the Assessment page, you can navigate through the list of findings, where you can see where that finding is present in your code and also a link to documentation with detailed information on how to fix it.  

Once you address all patterns that require changes in the O11 apps, you can initiate the migration of code and data from your ODC Portal.

## Prerequisites

You need to ensure the following before setting up the Migration Assessment Planner:

* You are part of the Early Access Program, and have been granted access to the Migration Kit.

* Your O11 infrastructure uses SQL Server databases.

* Your O11 environments use Platform Server 11.18.1 or later.

* One of your non-LifeTime environments, where you publish the Migration Assessment Tool Console, has [**Single Sign-On Between App Types** enabled](../security/configure-authentication.md). Please note that to enable this setting, you must also [toggle the **Enable HTTP Strict Transport Security (HSTS)**](../security/enforce-https-security.md) and [enable secure session cookies](../security/secure-cookies-enable-secure-session.md) in that environment.

* Your IT User has the **Manage Users and Roles** permission.

## Set up the tool

The Migration Assessment Tool setup includes the following steps:

1. [Install the Engine in the LifeTime environment](#engine)

1. [Install the Console](#console)

1. [Install the Probe in the Development environment](#probe-dev)

1. [Optional - Deploy the Probe to other environments](#probe-other-env)

1. [Configure the Migration Assessment Tool](#configure)

### Install the Engine { #engine }

1. Download the [Migration Assessment Tool Engine solution pack](resources/Migration_Assessment_Engine_v1_5_3_1.osp).

2. In your **LifeTime environment**, open Service Center and [upload and publish the Migration Assessment Tool Engine solution pack](https://success.outsystems.com/support/troubleshooting/application_lifecycle/deploy_applications_through_service_center/#step-2.upload-and-publish-the-solution-in-the-target-environment).

### Install the Console { #console }

1. Download the [Migration Assessment Tool Console solution pack](resources/Migration_Assessment_Console_v1_5_3_1.osp).

2. In any of your Environments, except for the LifeTime environment, open Service Center and [upload and publish the Migration Assessment Tool Console solution pack](https://success.outsystems.com/support/troubleshooting/application_lifecycle/deploy_applications_through_service_center/#step-2.upload-and-publish-the-solution-in-the-target-environment).

    <div class="info" markdown="1">

    OutSystems recommends you install the Migration Assessment Tool Console in your Development environment.
    Don't install the Migration Assessment Tool Console in the LifeTime environment.

    </div>

3. Still in Service Center of the same Environment, ensure [**Single Sign-On Between App Types**](../security/configure-authentication.md) is enabled.

### Install the Probe in the Development environment { #probe-dev }

1. Download the [Migration Assessment Tool Probe solution pack](resources/Migration_Assessment_Probe_v1_5_3_1.osp).

2. In your **Development environment**, open Service Center and [upload and publish the Migration Assessment Tool Probe solution pack](https://success.outsystems.com/support/troubleshooting/application_lifecycle/deploy_applications_through_service_center/#step-2.upload-and-publish-the-solution-in-the-target-environment).

### Optional - Deploy the Probe to other environments { #probe-other-env }

1. In the LifeTime console, deploy the Migration Assessment Tool Probe from the Development environment to other Environments where you want to also check the ODC-readiness of apps. For example, you may want to deploy the probe to the QA environment, so you can later run the assessment on apps during the app testing phase. Installing extra probes is not only for readiness but also to be able to migrate code and data from those environments.

### Configure the Migration Assessment Tool { #configure }

1. Open Migration Assessment Tool from the environment in which you installed the Migration Assessment Tool Console. Log in using your IT User credentials.

1. Go to the LifeTime management console, and [create a service account](../ref/apis/lifetime-deployment/rest-api-authentication.md) with the [**Administrator** role](../manage-platform-app-lifecycle/manage-it-teams/about-permission-levels.md#roles). Then copy the authentication token.

1. In the Migration Assessment Tool, configure the access to LifeTime and the engine, by setting the following fields:

    * In **Engine URL (LifeTime)** set the **LifeTime address**.

    * In **Authentication token** paste the authentication token for the LifeTime Service Account.

1. Save and test the connection to LifeTime by selecting **Save**.

1. Configure the access to the Probes in the **Development** environment, by setting the **Analysis environment URL** with the Development environment address, and then selecting **Connect**.

    <div class="info" markdown="1">

    It's mandatory to configure the access to the **Development** probe.

    </div>

1. Optionally, configure the access to the Probes in the other environments where you deployed the probe.

Next step: [Map O11 to ODC architecture for one shot migration](./plan/plan-map-apps.md)
