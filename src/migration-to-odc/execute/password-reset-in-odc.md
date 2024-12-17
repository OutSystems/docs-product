---
summary: Learn about password reset in ODC.
guid: ec56a386-83fb-44d9-8bf6-2210eaefa7f4
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma:
tags: password management, user authentication, security, email verification, account recovery
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Password reset in ODC

ODC provides pre-built screens that allow end users to request a new password (RecoverPasswordRequest) and set a new password (RecoverPasswordReset) for their app.  For detailed information, refer to [Custom authentication flows](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/user_interface/custom_authentication_flows/).

The password reset in ODC is authenticated via a verification code received in an email. 

Here’s the high-level overview of the password reset mechanism in ODC:

1. To receive the verification code, the end-user enters the email address in **RecoverPasswordRequest** screen.

1. The **RecoverPasswordRequest** screen invokes the system server action **StartResetPassword,** which sends the verification code to the end user's email address.

1. The user receives the verification code and a link to the **RecoverPasswordReset** page in the email. 

1. The user opens the  **RecoverPasswordReset** page and enters the new secure password. 

1. The **RecoverPasswordReset** page invokes the system client action **FinishResetPassword**, and sets the email, verification code, and new password for the end user in the Identity server. 
