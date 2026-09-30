---
summary: "OutSystems 11 (O11) to ODC conversion configuration: connect your O11 infrastructure to ODC and configure identity providers for end-user migration."
guid: a4a2aea6-eee3-4224-8f6f-8f84da3057b2
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
tags:
  - Authentication
  - End-user Authentication
  - End-users
  - External Authentication
  - IdP
  - Infrastructure
platform-version: o11
figma:
audience:
  - Platform administrator
  - Tech lead
outsystems-tools:
  - lifetime
  - service studio
coverage-type:
  - apply
topic:
  - configure-end-user-idp
  - connect-odc-to-o11
isautopublish: true
---

# Configure the conversion

Before you start converting your O11 apps and data to ODC, make sure the configurations for app conversion are in place:

1. [Ensure connection between your ODC organization and the O11 infrastructure](#validate-connection) with the apps to convert to ODC.

1. [Configure the end-user migration settings](#end-user).

## Prerequisites

* You must have the **Organization management** > **Manage O11 infrastructures** permission in your ODC tenant.

* The [Conversion Assessment Tool has been set up](https://www.outsystems.com/tk/redirect?g=29920fad-9efd-45ae-a4e4-212705fceb65) in your O11 infrastructure.

## Ensure connection between ODC and O11 infrastructure {#validate-connection}

Follow these steps to ensure that your ODC organization is connected to the O11 infrastructure with the apps to convert:

1. Log in to the ODC Portal.

1. Under the **Management** menu, go to **OUTSYSTEMS 11 > Infrastructures**.

1. Check if there's an infrastructure already configured for the O11 infrastructure where you defined the [conversion plans](https://www.outsystems.com/tk/redirect?g=ab447daa-dffc-4374-8ae6-986c8f3d63c4) with the apps to convert to ODC:

    * Search for an infrastructure card with the LifeTime URL of your O11 infrastructure.

    <div class="info" markdown="1">

    If you don't see an infrastructure card for your O11 infrastructure, make sure an administrator [connects the ODC tenant with your O11 infrastructure](https://www.outsystems.com/tk/redirect?g=6702a29e-b589-486c-aa17-f4231a6a3f10) before proceeding.

    </div>

1. In a [multi-portfolio organization](https://www.outsystems.com/tk/redirect?g=f7a2c1d8-3e5b-4a9f-b812-6d8e4f2a1c3b), define the ODC portfolio to be the target of the app conversion:

    <div class="info" markdown="1">

    If you have a single-portfolio ODC organization, your target portfolio is automatically defined, thus this configuration isn't shown.

    </div>

    1. Click the infrastructure card to navigate to its configuration details.

    1. In the **App conversion** tab, click **Edit** and set the **Target ODC portfolio** for the ODC converted assets.

Having the connection to your O11 infrastructure configured, the [conversion plans](https://www.outsystems.com/tk/redirect?g=ab447daa-dffc-4374-8ae6-986c8f3d63c4) you've defined in the Conversion Assessment Tool are available in the ODC app conversion console. Thus, you can start [converting the apps' code](execute-about-migrate-code.md).

When you are ready to migrate your apps' data and end users, make sure you [configure the end-user migration settings](#end-user).

## Configure end-user migration settings {#end-user}

Before migrating your end users from an O11 source environment to an ODC stage, you need to configure an identity provider in ODC that links to that O11 source environment. See [About migrating end users](execute-about-migrate-data.md#end-users) for further details.

Follow these steps to configure the end-user migration from a specific **O11 source environment** to a **target ODC stage**:

1. If it hasn't been created yet, create an identity provider in ODC for the O11 environment that you'll set as source of the data migration. For example, if you want to migrate end users from your O11 QA environment, create an **O11 QA** identity provider.

    * If your O11 apps use the **Internal** built-in authentication, [follow these instructions](https://www.outsystems.com/tk/redirect?g=8ba29b7e-23fa-4120-bb0d-e77dcd9268d5) to set up an O11 identity provider for the migration source environment.

    * If your O11 apps use an external identity provider, [configure the same IdP in ODC](https://www.outsystems.com/tk/redirect?g=dd27ffcf-d159-4902-b8a7-8132a9a8fd2b).

    * Make sure the identity provider is [assigned to the target ODC stage](https://www.outsystems.com/tk/redirect?g=883c4583-27f6-4617-bcba-9cb26c4abd9e) of the data migration.

    <div class="info" markdown="1">

    Considerations for the adopted [user profile mapping](https://www.outsystems.com/tk/redirect?g=bf560c9c-82b5-4c8a-ba11-09939bcc8d87):

    * If you select **Email** for user profile mapping, ensure all active and inactive end users stored in the O11 **User** system entity of the O11 source environment have a valid and unique email set on the **Email** attribute.

    * For **O11 external authentication**, select one of the following values for user profile mapping:

        * **Email**
        * **Username**

        The value **None** disables fallback matching and **isn't compatible** with the end-user migration process for O11 external authentication.

    * If you already executed a data migration that included end-user migration before identity providers were required, set the user profile mapping to **Email**.

    </div>

1. In the ODC Portal, go to **Management > OUTSYSTEMS 11 > Infrastructures**.

1. Click the infrastructure card of your O11 infrastructure to navigate to its configuration details.

1. Go to the **App conversion** tab.

    In the **End-user migration settings** area, you have the mapping of each environment in your O11 infrastructure to the corresponding ODC identity provider. Map only the environment that you'll use as source of the data migration you'll execute.

1. Click **Edit**.

1. For the **O11 source environment** of your data migration:

    * Select the **ODC identity provider** you just created. For example, the **O11 QA** identity provider.

    * If it's a non-production environment, choose a **Username prefix** for the migrated end users in ODC. For example, `qa_`.

    <div class="info" markdown="1">

    Make sure you create unique identity providers and prefixes for each O11 environment. You can't set the same identity provider or prefix to multiple O11 environments.

    </div>

    See [About migrating end users](execute-about-migrate-data.md#idp-per-env) for further details.

1. Click **Save**.

You can now proceed with the [data migration](execute-about-migrate-data.md) from the configured O11 environment to an ODC stage.
