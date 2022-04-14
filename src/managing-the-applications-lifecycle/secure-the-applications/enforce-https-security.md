---
summary: Check how IT Managers or Administrators can override and enforce the HTTP security of OutSystems applications that are installed and running.
tags: runtime-traditionalweb; support-Security-overview
locale: en-us
guid: a152ecbb-2419-489f-87c5-000918d502f0
---

# Enforce HTTPS Security

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

OutSystems provides developers with the ability of deciding at design time the HTTP security used in applications. They can do it by [defining which pages and integrations](<../../develop/security/secure-http-requests.md>) are available over HTTP and HTTPS.

IT Managers or Administrators can override and enforce the HTTPS security of applications that are installed and running. They can do it for a **whole environment**, which affects all applications running there, or **application by application**.

You can configure the following security settings:

Enable [HTTP Strict Transport Security (HSTS)](<https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html>)
:   This option is only available for environments. Use it to ensure that all screens are served to clients using HTTPS. When enabled, all HTTP page requests will be redirected to HTTPS. Enabling this option overrides the security definitions of all web flows, web screens and the 'Force HTTPS for screens' application setting for all applications.

Force HTTPS for screens in Web Applications
:   Use it to ensure all screens in Web Applications (or in the selected application) use HTTPS. When enabled, all HTTP page requests will be redirected to HTTPS. Enabling this option overrides the security definitions of all web flows and web screens.

Force HTTPS for exposed integrations in Web Applications
:   Use it to ensure all exposed SOAP and REST integrations in Web Applications (or in the selected application) are only served via HTTPS requests. Enabling this option overrides the security definitions of all exposed integrations for the application modules.

![](images/enforce-https-security.png)

**Notes:**

* Any of the above configurations will only work if a valid SSL certificate is installed in the environment.

* Make sure you access your environment (management consoles, web applications and integration endpoints) using the hostname that matches the SSL certificate's Common Name (CN) or Subject Alternative Name (SAN) when using HTTPS. If you use a different hostname or just an IP address you will have errors and security warnings.

* All HTTP requests in Mobile Apps (distributed as the native builds or PWA) and Reactive Web Apps are served via HTTPS regardless of the settings above.

## Configure Secure Connections for an Environment

Do the following in the infrastructure management console (LifeTime):

1. Select the "Environments" section to see all environments.
1. Select the environment that you want to configure by clicking on it.
1. Click the "More Security Settings" link on the bottom section of the page.
1. Configure the security settings.

If you don't have LifeTime installed, configure secure connections in each environment using its management console (Service Center):

1. In the "Administration" section, select the "Security" option.
1. Configure the security settings.

## Configure Secure Connections for a Single Application

Take the following steps in the infrastructure management console (LifeTime):

1. Select the "Applications" section, and then the application you want to set up.
1. Select the "Security Settings" option.
1. In the drop list, select the environment to which the security settings will apply.
1. Configure the security settings.

If you don't have LifeTime installed, configure secure connections for a single application using the environment's management console (Service Center):

1. Select the "Factory" section and then the application.
1. Select the "Security" tab.
1. Configure the security settings.
