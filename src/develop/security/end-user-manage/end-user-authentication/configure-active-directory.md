---
summary: How to configure Active Directory end user authentication for your applications.
---

# Configure Active Directory Authentication

<div class="info" markdown="1">

Only available in OutSystems on-premises installations.

</div>

The Active Directory authentication method for authenticating end users requires the front-end server to be part of the Active Directory domain.

To use Active Directory domain authentication:

1. In the [Users application](<../accessing-users.md>), click "Configure Authentication" in the sidebar.

    ![](<images/users-auth-active-directory.png>)

1. Choose `Active Directory` in the **Authentication** drop-down list.

1. Add the authentication domain in the **Default Domain** text field.

1. To enable Integrated Windows Authentication for all applications, select **Windows Integrated Authentication** (only available in Traditional Web applications).

    Alternatively, you can enable Integrated Windows Authentication for a just [a selected number of elements](integrated-authentication.md) in Service Studio (for example, just for some web screens, web flows or web services).
