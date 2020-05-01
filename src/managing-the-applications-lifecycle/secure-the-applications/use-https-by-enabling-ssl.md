---
summary: Allow users to access your applications over HTTPS by enabling SSL in your infrastructure.
---

# Use HTTPS by Enabling SSL

HTTPS allows you to establish a secure communication channel between the end user and your OutSystems environment. This way:

* The data exchanged cannot be read by an unauthorized third-party, since it's encrypted.
* The data exchanged cannot be tampered with, since the message integrity is checked.
* Man-in-the-middle attacks are prevented: when the end user accesses the application using HTTPS, the application server is required to present a certificate, that the end user's browser checks to see if that is a trusted application server, or some other application server that cannot be trusted.

To use HTTPS in your application you must configure and activate SSL (Secure Socket Layers) in the environments of your infrastructure. When SSL is active, the development environments and monitoring consoles will also use a secure connection to the environment.

After configuring SSL in your infrastructure, you can define that [some parts](<../../develop/security/secure-http-requests.md>) or your [entire application/environment](<enforce-https-security.md>) must be served over HTTPS.

Note that all requests made to the back-end of a mobile app (the server part of the OutSystems generated code for your mobile app), Progressive Web App (PWA) or a Rective Web app are **always** made over HTTPS.

## Enabling SSL in your OutSystems Infrastructure

You can enable SSL in your infrastructure in one of the following ways, depending on your infrastructure type:

SSL in OutSystems PaaS
:   Your cloud environment is automatically rolled out with a valid SSL certificate for the `outsystemsenterprise.com` domain.  
    However, you can customize both the hostname of your environment and its SSL domain certificate by following the steps outlined in [Enable a Custom SSL Domain in OutSystems PaaS](<https://success.outsystems.com/Support/Enterprise_Customers/Installation/Enable_Custom_SSL_Domain_In_OutSystems_PaaS>).

SSL in an On-Premises Infrastructure
:   In on-premises infrastructures you need to acquire and install an SSL domain certificate to add HTTPS support to your OutSystems applications.  
    Check [How to install an SSL certificate for the OutSystems platform](<https://success.outsystems.com/Support/Enterprise_Customers/Installation/How_to_install_an_SSL_Certificate_for_the_OutSystems_platform>) in the Support Knowledge Base.
