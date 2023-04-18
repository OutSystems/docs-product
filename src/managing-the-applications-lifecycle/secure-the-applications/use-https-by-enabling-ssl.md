---
summary: Allow users to access your applications over HTTPS by enabling SSL in your infrastructure.
locale: en-us
guid: 089b0bf9-4ff6-462f-b6ec-43c2d10472e1
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Use HTTPS by Enabling SSL

HTTPS allows you to establish a secure communication channel between the end user and your OutSystems environment. This way:

* The data exchanged cannot be read by an unauthorized third-party, since it's encrypted.
* The data exchanged cannot be tampered with, since the message integrity is checked.
* Man-in-the-middle attacks are prevented: when the end user accesses the application using HTTPS, the application server is required to present a certificate, that the end user's browser checks to see if that is a trusted application server, or some other application server that cannot be trusted.

To use HTTPS in your application you must configure and activate SSL (Secure Socket Layers) in the environments of your infrastructure. When SSL is active, the development environments and monitoring consoles will also use a secure connection to the environment.

After configuring SSL in your infrastructure, you can define that [some parts](<../../develop/security/secure-http-requests.md>) or your [entire application/environment](<enforce-https-security.md>) must be served over HTTPS.

Note that all requests made to the back-end of a Mobile or Reactive Web app (the server part of the OutSystems generated code for your app) are **always** made over HTTPS.

## Enabling SSL in your OutSystems Infrastructure

You can enable SSL in your infrastructure in one of the following ways, depending on your infrastructure type:

SSL in OutSystems Cloud
:   Your cloud environment is automatically rolled out with a valid SSL certificate for the `outsystemsenterprise.com` domain.  
    However, you can customize both the hostname of your environment and its SSL domain certificate by following the steps outlined in [Use your SSL domain in OutSystems Cloud](../../setup-maintain/setup/ssl-domain-cloud/ssl-domain-cloud.md).

SSL in an On-Premises Infrastructure
:   In on-premises infrastructures you need to acquire and install an SSL domain certificate to add HTTPS support to your OutSystems applications.  
    Check [How to install an SSL Certificate in self-managed environments](../../setup-maintain/setup/install-ssl-platform.md) in the Support Knowledge Base.
