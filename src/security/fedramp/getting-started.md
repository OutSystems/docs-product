---
summary: Set up your OutSystems FedRAMP environment, configure IT user authentication through an external IdP, and prepare Service Studio for FIPS compliance.
tags:
  - Authentication
  - End-user Authentication
  - External Authentication
  - IdP
  - IT Users
  - OIDC
  - Security
  - SAML
locale: en-us
guid: 4b1b0fcf-5012-476d-8631-eccb7e5da9ab
app_type: traditional web apps, reactive web apps
platform-version: o11
figma:
audience:
  - Platform administrator
  - Developer
outsystems-tools:
  - service center
  - service studio
coverage-type:
  - apply
isautopublish: true
---

# Getting started with OutSystems FedRAMP

This article describes the initial setup and configuration steps for a newly provisioned [OutSystems FedRAMP](fedramp-overview.md) environment.

## Prerequisites

Before starting, confirm the following:

* Your organization has a signed agreement with OutSystems for the FedRAMP offering.
* Your organization has an external Identity Provider (IdP) that supports OpenID Connect (OIDC) and enforces multi-factor authentication (MFA).
* Your organization has an external IdP that supports SAML and enforces multi-factor authentication (MFA).
* You have identified the IT users who need access to OutSystems management consoles.
* Your external OIDC IdP is configured for IT user authentication as part of the onboarding process, before your environment is provisioned. OutSystems contacts you during onboarding to collect the required IdP details.
* You have received the environment provisioning confirmation from OutSystems, including your LifeTime URL.

## Log in for the first time

OutSystems provisions your environment with the domain `osgov-cloud.com` by default. IT user authentication through your external IdP is configured before provisioning, so IT users sign in through it from the first login.

To log in for the first time:

1. Open a browser and navigate to the LifeTime URL provided in your provisioning confirmation.
1. Sign in with your external IdP credentials.

## IT user authentication

In OutSystems FedRAMP, IT users authenticate through an external IdP using the OIDC protocol, with MFA enforced by your IdP. Neither SAML nor the built-in IdP is available for IT users. IT users sign in to LifeTime, Service Center, and Service Studio through the external IdP.

The initial IdP configuration is done before provisioning. After provisioning, you manage the IdP configuration for IT users in LifeTime.

<div class="warning" markdown="1">

If an administrator loses access to LifeTime, for example because of an IdP misconfiguration, open a [support case](https://www.outsystems.com/legal/success/support-terms-and-service-level-agreements-sla-of-the-outsystems-software/) to regain access.

</div>

For how the integration works, refer to [IT Users Integration with External IdP via OpenId Connect](../../manage-platform-app-lifecycle/manage-it-teams/external-idp/intro.md).

## End-user authentication

End users of your applications authenticate through an external IdP using SAML, with MFA enforced by your IdP. To set up end-user authentication, refer to [End users authentication](../../user-management/end-user-manage/end-user-authentication/intro.md).

## Configure Service Studio for FIPS compliance {#configure-service-studio-for-fips-compliance}

To use Service Studio in an OutSystems FedRAMP environment, update the `Settings.xml` file on each developer's workstation to disable the features that aren't compliant with the Federal Information Processing Standards (FIPS). These features are active by default.

<div class="warning" markdown="1">

You're responsible for applying this configuration. It applies to each Service Studio installation separately, so repeat these steps on every developer's workstation.

</div>

To configure Service Studio for FIPS compliance:

1. Close Service Studio if it's running.
1. Navigate to the folder where Service Studio stores `Settings.xml`. The location depends on the operating system:
    * Windows: `%USERPROFILE%\AppData\Local\OutSystems\ServiceStudio 11 XPlatform Stable`
    * macOS: `~/Library/Application Support/OutSystems/ServiceStudio 11 XPlatform`
1. Open `Settings.xml` in a text editor.
1. Add or update the following settings:

    ```xml
    <BreakdownConnections>true</BreakdownConnections>
    <DisableFeedback>true</DisableFeedback>
    ```

1. Save the file and restart Service Studio.

## Next steps

After completing the initial setup, you're ready to start building applications in OutSystems FedRAMP. The following resources help you continue:

* [Unavailable features in OutSystems FedRAMP](unavailable-features.md): review platform limitations before designing your applications.
* [IT Users Integration with External IdP via OpenId Connect](../../manage-platform-app-lifecycle/manage-it-teams/external-idp/intro.md): detailed IdP configuration reference.
