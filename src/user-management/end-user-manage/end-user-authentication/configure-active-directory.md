---
summary: This article provides a guide on configuring Active Directory authentication in OutSystems 11 (O11) for self-managed installations.
locale: en-us
guid: b4a590a6-d9e2-4f0a-80c4-d3ac9f3bd14b
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=280:62
---

# Configure Active Directory authentication

<div class="info" markdown="1">

Only available in OutSystems self-managed installations. In the OutSystems Cloud you can use [LDAP](configure-ldap.md), [Azure AD](configure-azuread.md), [Okta](configure-okta.md), or [SAML 2.0](configure-saml.md).

</div>

This article describes how to configure Active Directory authentication for end users.  

## Prerequisites

Before configuring Active Directory authentication, make sure you meet the following requirements.

* The front-end server needs to be part of the Active Directory domain.  

* You need to have a domain (to be set as **Default Domain**) that ensures all traversed paths between domains are bidirectional in terms of trust.

    <div class="info" markdown="1">

    The Active Directory APIs used by the Platform require all traversed paths between domains during the search process to be bidirectional in terms of trust between said domains. If this is not possible, all the synchronization and access to users' details from the external system are unavailable. Some of the issues of using a default domain with restricted access are:

    * Users deactivated in the external system will still be active on the Platform.
    * Metadata changed in the external system will not be synced to the Platform.

    </div>

## Configure Active Directory authentication

To use Active Directory domain authentication:

1. In the [Users application](<../accessing-users.md>), click "Configure Authentication" in the sidebar.

    ![Screenshot of the Users application with the 'Configure Authentication' option highlighted](images/users-auth-active-directory.png "Active Directory Authentication Configuration")

1. Choose `Active Directory` in the **Authentication** drop-down list.

1. Add the authentication domain in the **Default Domain** text field.

    <div class="warning" markdown="1">

    The **Default Domain** needs to ensure all traversed paths between domains are bidirectional in terms of trust. Don't use a domain with restricted access.

    </div>

    <div class="info" markdown="1">

    Security best practices strongly advise against using the Windows Integrated Authentication when a workstation is shared between several users.

    </div>
