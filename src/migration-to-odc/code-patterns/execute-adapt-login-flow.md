---
summary: Learn how to adapt the login and logout flows of converted apps to authenticate end users through the identity provider configured in ODC.
tags:
  - Authentication
  - End-user Authentication
  - External Authentication
  - IdP
  - SSO
guid: 08ed0f80-3e5c-4a5d-9955-7658ea3aa344
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - service studio
coverage-type:
  - apply
isautopublish: true
---

# Adapt login and logout flow of converted apps

The built-in login and logout mechanisms are different in O11 and ODC. The converted app keeps its O11 login and logout flows, so you must manually adapt them so end users can authenticate in the converted app.

If you have access to the [O11 to ODC App Conversion Kit EAP](https://www.outsystems.com/o11-odc-migration/), the tool creates the end user's profile in ODC when migrating your O11 end users, so they can log in to the converted app using their existing O11 credentials. To support this, the converted app must authenticate end users through an external identity provider (IdP) configured in ODC. If your O11 apps use external authentication, that IdP is the same external IdP your O11 apps already use. If your O11 apps use the **internal built-in authentication**, you set your O11 environments as identity providers for your ODC organization.

## How to solve

You must solve this pattern in ODC, after proceeding with the code conversion to ODC.

### Solve in ODC

After converting your app to ODC, adapt the login and logout flows of the converted apps by following these steps:

1. Refer to [Bypass the built-in login screen and redirect to an external provider](https://www.outsystems.com/tk/redirect?g=1e9fd60c-9011-4047-bb85-d639e0ff4006) for guidance on which screens and actions to change so the converted apps redirect end users to the configured IdP. That guidance doesn't cover every custom case, so adapt it to the specificities of your apps login and logout flows.

1. If your O11 apps use external authentication, also adjust the following:

    * [Coordinate sessions between ODC and O11](https://success.outsystems.com/documentation/outsystems_developer_cloud/extending_o11_with_odc/user_interoperability/adjust_apps_for_o11_and_odc_single_sign_on/#session-coordination).
    * [Handle the ODC-to-O11 logout redirect](https://success.outsystems.com/documentation/outsystems_developer_cloud/extending_o11_with_odc/user_interoperability/adjust_apps_for_o11_and_odc_single_sign_on/#logout-redirect).
