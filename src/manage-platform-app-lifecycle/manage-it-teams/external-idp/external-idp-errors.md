---
summary: OutSystems allows your IT users to authenticate an external IdP via OpenID Connect.
tags:
locale: en-us
guid: 6AE899A4-F0F6-4977-AE00-2DBEFD989E69
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Troubleshooting

The following is a list of the most common troubleshooting problems that you may encounter when configuring the OIDC feature.

## Configuration errors

### 1. Save configuration and client secret

On the LifeTime configuration screen, the **Activate** button **only saves** Client Secret information. If you change any configuration, you must click **Save** before you enter the client secret and activate the provider. Otherwise, configurations don’t update.

### 2. User mismatch between LifeTime user provider and external IdP

After a successful login in the IdP, Service Center displays an invalid login message. This happens when the user has no corresponding user in the Platform Server or the required claim is not set correctly.

### 3. Invalid login SSO Error

In the case of an Invalid login SSO error, one possible reason could be a mismatch between the **username claim value** and **username** entered in the user profile. For example, if **preferred_username** is entered as a **username claim value** which contains an email, then the **username** field must also contain an email in the user profile.

### 4. External IdP is not activated for all the environments configured in Lifetime 

When proxy settings exist for some, but not all environments in the infrastructure, OIDC activation might fail for the environments that don't have proxy setting. You must maintain the same proxy settings throughout all enviornments configured in Lifetime.

You must ensure SS proxy configurations are up to date in the machine.config file. For instructions on how to (confiure the SS proxy configurations?? or to update them??), refer to the [this article.](https:https://learn.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/network/defaultproxy-element-network-settings)


## Both username/password and SSO login options are available

When you activate OIDC, and both username/password and SSO login options are available, this can be due to one of the following: 
* The factory configurations are not up to date.
* All environments in the infrastructure are not up to date.
* OIDC was activated before Lifetime upgrade v11.16.1. In this case, the user must deactivate and activate OIDC again.

## Return errors

When the IdP returns an error page, it might be a configuration problem. The following are some of the errors you may encounter and details on their causes.

<div class="info" markdown="1">

Errors might differ depending on the external IdP provider.

</div>

### 1. 400 Bad Request

When starting a login flow, the IdP displays a 400 Bad Request error. This can happen for one of the following reasons:

* Client Ids are incorrect
* Redirect URIs are not configured correctly on the IdP side
* URL for the service is configured incorrectly

#### i. Issue with Client ID configuration

When there's an issue with the Client ID configuration, the **Application with identifier app id was not found in the directory** error can occur.

This error occurs when connecting through Service Studio and the client ID (or the Client Id for Desktop Tools) is incorrectly set.

#### ii. Issue with the redirect URI in IdP configuration

When there are incorrect or missing redirect URIs in the IdP configuration, the following error may occur: **The redirect URI specified in the request does not match the redirect URIs configured for the application application**.

#### iii. Issue with the URL for the IdP

If the **OpenID Connect metadata document** field is wrongly configured, an error occurs when you activate the [OIDC provider in LifeTime](external-idp-lifetime.md).

### 2. 401 Unauthorized

This error is often associated with the Client Secret configuration issue. Either there is a mismatch in the configured secret or the secret is deprecated and is therefore no longer valid.

Also, when redirecting back to the Service Center, an internal error is displayed. This typically happens when there is an issue with the Client Secret configuration that prevents Service Center from exchanging tokens with the IdP.

