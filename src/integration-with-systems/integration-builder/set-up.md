---
locale: en-us
guid: 617ec597-a128-4b2a-872f-4a3a5856628c
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=1019:2309
summary: The article provides a guide on setting up Integration Builder in OutSystems, including prerequisites, registering infrastructure, installing dependencies, and configuring on-premises environments
---
# How to set up Integration Builder

Integration Builder is a Software as a Service (SaaS) that connects to your OutSystems environment to authenticate and validate user connections. Integration Builder works with Integration Manager to keep the status of your integrations current, so it needs to be able to connect with the environments to which you deploy the integrations. In addition, Integration Builder is available in all OutSystems editions.

![Diagram illustrating the architecture setup for Integration Builder in OutSystems](images/architecture-ib-setup-diag.png "Integration Builder Architecture Diagram")

## Prerequisites { #prerequisites }

* The [IT user](../../manage-platform-app-lifecycle/manage-it-teams/intro.md) you use to log in to Integration Builder must have the **Change and Deploy Applications** permission level and the **Create Applications** specific permission for the development environment. Check [Understanding the permission model for IT users](../../manage-platform-app-lifecycle/manage-it-teams/about-permission-levels.md) for more information.

* Use the latest version of any of the following desktop browsers: Edge, Firefox, Google Chrome, or Safari.

* Your environments are associated with any available [OutSystems Edition](https://www.outsystems.com/pricing-and-editions/), including Free, Standard, or Enterprise. **You can use your Personal Environment with Integration Builder**.

* All environments, except for the LifeTime environment, must:

    * Use [Platform Server 11.7.2](https://success.outsystems.com/Support/Release_Notes/11/Platform_Server#Platform_Server_11.7.2) or later.

    * Allow inbound and outbound HTTPS communication (port 443) with `https://integrationbuilder.outsystems.com`. The Integration Builder will use the environment's public DNS hostname to communicate. Check [Integration Builder network requirements](../../setup-infra-platform/setup/network-requirements.md#integration-builder) for detailed information.

<div class="info" markdown="1">

* It's unnecessary to connect Integration Builder to all your environments,
  although a connection to the development environment is mandatory. If you
  want to block Integration Builder from connecting to other environments,
  there are a few limitations:

    * Development Connections (created automatically by Integration Builder in
      a Dev environment for testing purposes) won't work. It's necessary to
      define your own connection.

    * Sending emails through Integration Manager to administrators to
      request new connections or assistants won't work.

    * Automatic creation of connections in Integration Manager won't work. Manual creation is still possible.

</div>


<div class="info" markdown="1">

Keep in mind:

* Each integration may have additional requirements. To verify, check the specific integration documentation.

* When using Integration Builder with Multiple Database Catalogs (MDC), and publishing to a development environment, a prompt displays for you to download your solution. Currently Integration Builder is unable to publish to a development environment. You can then use Service Center to publish your integration solution

</div>

## Registering your infrastructure

Before using Integration Builder, register the infrastructure in Integration Builder by following these steps:

1. Access <https://integrationbuilder.outsystems.com>, enter the development environment address, and click **Next**. OutSystems checks the environment exists.

1. Enter your IT username and password, and then click **Log in**. OutSystems verifies the user has the correct permissions.

1. On the Welcome screen, click **Set up Integration Builder**. The Integration Builder Disclaimer page displays.

1. On the Integration Builder Disclaimer page, review the terms and conditions, and click **Accept and Continue**. OutSystems checks your infrastructure.

1. If your development environment uses **Platform Server 11.7.6 or lower**, enter your **Activation Code** and click **Register and Continue**.

    <div class="info" markdown="1">

    To get your activation code, go to `https://<dev-environment-address>/ServiceCenter`, then click **Administration** > **Licensing**, and copy your Activation Code.

    </div>

After these steps, IT users for the infrastructure can start using Integration Builder.

## Installing dependencies

Integrations created using Integration Builder need other apps to work properly.
After registering your infrastructure, a **Setup** widget at the bottom right prompts you to install some of these dependencies.

To install dependencies, follow these steps:

![Screenshot of the Setup widget prompting to install dependencies in Integration Builder](images/setup-widget-install-depend-ib.png "Setup Widget for Installing Dependencies")

1. Click the **Setup** widget to expand it.

1. Click **Install dependencies** to start installing the dependencies.

After these steps Integration Builder stars installing the dependencies listed.

![Screenshot showing the Setup widget in the process of installing dependencies in Integration Builder](images/setup-widget-installling-depend-ib.png "Setup Widget Installing Dependencies")

## Setting up on-premises environments

When using an on-premises infrastructure with Integration Builder, you need to setup the addresses of the other environments where you'll deploy the integrations after finishing development. For example, for a standard infrastructure, Integration Builder must be able to connect to the development, quality assurance, and production environments but doesn't need to connect to the LifeTime.

After you develop and publish the first integration, the **Setup** widget at the bottom right prompts you to add the environment addresses.

To set up the environments, follow these steps:

1. Click the **Setup** widget to expand it, and the click on **Setup environments**.

1. Click **Add environment**.

1. Enter a name for the environment and its URL, then click **Add environment**. The URL is the environment address.

1. Repeat step 2 and 3 until you have added all your non-LifeTime environments.
