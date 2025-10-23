---
summary: OutSystems 11 (O11) ensures HTTPS security for Mobile, Reactive, and Traditional Web Apps with built-in SSL and configurable settings.
tags: https security, ssl configuration, secure communication, data encryption, certificate validation
locale: en-us
guid: a152ecbb-2419-489f-87c5-000918d502f0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=267:97
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Enforce HTTPS Security

## HTTPS security in Mobile Apps and Reactive Web Apps

OutSystems provides developers with HTTPS security in Mobile Apps and Reactive Web Apps.

All HTTP requests in Mobile Apps (distributed as the native builds or PWA) and Reactive Web Apps are secure because they are served via HTTPS. All requests made to the back-end of these apps (the server part of the OutSystems generated code for your app) are always made over HTTPS.

This means that you don't need to configure the security of HTTP requests in your application, or in application elements such as UI Flows and Screens. Also, SSL (Secure Socket Layer) is already configured and activated in the environments of your infrastructure.

Therefore, IT Managers or Administrators don't need to override or enforce the HTTPS security of applications that are installed and running because it's already enabled.

With HTTPS security, your Mobile Apps and Reactive Web Apps establish a secure communication channel between the end user and your OutSystems environment. This way:

* The data exchanged cannot be read by an unauthorized third-party, since it's encrypted.
* The data exchanged cannot be tampered with, since the message integrity is checked.
* Man-in-the-middle attacks are prevented: when the end user accesses the application using HTTPS, the application server is required to present a certificate. The end user's browser checks to see if that is a trusted application server or some other application server that cannot be trusted.

All the communication between the app and the Platform Server is done through [secure REST calls](https://success.outsystems.com/Support/Security/Application_security_overview/Mobile_app_to_server_communication_and_security).

## HTTPS security in Traditional Web Apps

OutSystems provides developers with the ability of deciding at design time the HTTP security used in Traditional Web Apps. They can do it by [defining which pages and integrations](<secure-http-requests.md>) are available over HTTP and HTTPS.

IT Managers or Administrators can override and enforce the HTTPS security of Traditional Web Apps that are installed and running. They can do it for a **whole environment**, which affects all applications running there, or **application by application**.

You can configure the following security settings:

Enable [HTTP Strict Transport Security (HSTS)](<https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html>)
:   This option is only available for environments. Use it to ensure that all screens are served to clients using HTTPS. When enabled, all HTTP page requests will be redirected to HTTPS. Enabling this option overrides the security definitions of all web flows, web screens and the 'Force HTTPS for screens' application setting for all applications.

Force HTTPS for screens in Web Applications
:   Use it to ensure all screens in Web Applications (or in the selected application) use HTTPS. When enabled, all HTTP page requests will be redirected to HTTPS. Enabling this option overrides the security definitions of all web flows and web screens.

Force HTTPS for exposed integrations in Web Applications
:   Use it to ensure all exposed SOAP and REST integrations in Web Applications (or in the selected application) are only served via HTTPS requests. Enabling this option overrides the security definitions of all exposed integrations for the application modules.

![Screenshot of HTTPS security configuration options in OutSystems management console](images/enforce-https-security.png "Enforce HTTPS Security Configuration Options")

**Notes:**

* Any of the above configurations will only work if a valid SSL certificate is installed in the environment.

* Make sure you access your environment (management consoles, web applications and integration endpoints) using the hostname that matches the SSL certificate's Common Name (CN) or Subject Alternative Name (SAN) when using HTTPS. If you use a different hostname or just an IP address you will have errors and security warnings.

* All HTTP requests in Mobile Apps (distributed as the native builds or PWA) and Reactive Web Apps are served via HTTPS regardless of the settings above.

## Configure secure connections for an Environment

Do the following in the infrastructure management console (LifeTime):

1. Select the "Environments" section to see all environments.
1. Select the environment that you want to configure by clicking on it.
1. Click the "More Security Settings" link on the bottom section of the page.
1. Configure the security settings.

If you don't have LifeTime installed, configure secure connections in each environment using its management console (Service Center):

1. In the "Administration" section, select the "Security" option.
1. Configure the security settings.

## Configure secure connections for a single Traditional Web App

Take the following steps in the infrastructure management console (LifeTime):

1. Select the "Applications" section, and then the application you want to set up.
1. Select the "Security Settings" option.
1. In the drop list, select the environment to which the security settings will apply.
1. Configure the security settings.

If you don't have LifeTime installed, configure secure connections for a single application using the environment's management console (Service Center):

1. Select the "Factory" section and then the application.
1. Select the "Security" tab.
1. Configure the security settings.
