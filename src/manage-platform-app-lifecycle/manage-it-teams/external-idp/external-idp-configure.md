---
summary: Explore how to configure IT Users Authentication with External IdP via OpenId Connect in OutSystems 11 (O11).
tags: identity and access management, openid connect configuration, authentication integration, external identity providers, it user authentication
locale: en-us
guid: CC9FE733-B03A-4600-B966-0E622A638756
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - platform administrators
  - full stack developers
outsystems-tools:
  - lifetime
coverage-type:
  - apply
---

# Configuring IT Users Authentication with External IdP via OpenId Connect

To use the **IT Users Authentication with External IdP (OIDC)** feature in the OutSystems platform, you must configure the external IdP first, then configure it in Lifetime. The IdP must comply with the [OIDC Protocol](https://openid.net/connect/) and support the [Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html#IssuerDiscovery) feature that defines how clients dynamically discover information about OpenID providers.

Step 1. Configuring External IdP. 

See the following articles for configuration instructions:

* [Configuring Microsoft Azure AD authentication](external-idp-azure.md)

* [Configuring Okta authentication](external-idp-okta.md)

* [Configuring Active Directory Federation Services](external-idp-adfs.md)

* [Configuring PingFederate authentication](external-idp-pingfederate.md)

Step 2. [Configuring LifeTime authentication](external-idp-lifetime.md)
