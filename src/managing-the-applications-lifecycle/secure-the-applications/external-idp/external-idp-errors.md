---
summary: OutSystems allows your IT users to authenticate an external IdP via OpenID Connect.
tags:
locale: en-us
guid: 6AE899A4-F0F6-4977-AE00-2DBEFD989E69
app_type: traditional web apps, mobile apps, reactive web apps
---

# Troubleshooting

The following is a list of the most common troubleshooting problems that you may encounter when configuring the OIDC feature.

## Configuration errors

### Save configuration and client secret

On the LifeTime configuration screen, the **Activate** button **only saves** Client Secret information. If you change any configuration, you must click **Save** before you enter the client secret and activate the provider. Otherwise, configurations don’t update.

### User mismatch between LifeTime user provider and external IdP

After a successful login in the IdP, Service Center displays an invalid login message. This happens when the user has no corresponding user in the Platform Server or the required claim is not set correctly.

## Return errors

When the IdP returns an error page, it might be a configuration problem. The following are some of the errors you may encounter and details on their causes.

<div class="info" markdown="1">

Errors might differ depending on the external IdP provider.

</div>

### 400 Bad Request

When starting a login flow, the IdP displays a 400 Bad Request error. This can happen for one of the following reasons:
* URL for the service is configured incorrectly
* Client Ids are incorrect
* Redirect URIs are not configured correctly on the IdP side

#### Issue with Client ID configuration

When there's an issue with the Client ID configuration, the **Application with identifier app id was not found in the directory** error can occur.

This error occurs when connecting through Service Studio and the client ID (or the Client Id for Desktop Tools) is incorrectly set.

#### Issue with the redirect URI in IdP configuration

When there are incorrect or missing redirect URIs in the IdP configuration, the following error may occur: **The redirect URI specified in the request does not match the redirect URIs configured for the application application**.

#### Issue with the URL for the IdP

If the **OpenID Connect metadata document** field is wrongly configured, an error occurs when you activate the [OIDC provider in LifeTime](external-idp-lifetime.md).

### 401 Unauthorized

This error is often associated with the Client Secret configuration issue. Either there is a mismatch in the configured secret or the secret is deprecated and is therefore no longer valid.

Also, when redirecting back to the Service Center, an internal error is displayed. This typically happens when there is an issue with the Client Secret configuration that prevents Service Center from exchanging tokens with the IdP.

