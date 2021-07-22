---
summary: Check how IT Managers or Administrators can be assured by the HTTPS security of OutSystems Reactive Web Apps and Mobile Apps that are installed and running.
tags: support-Security-overview
---

# HTTPS Security in Mobile Apps and Reactive Web Apps

OutSystems provides developers with HTTPS security in Mobile Apps and Reactive Web Apps.

All HTTP requests in Mobile Apps (distributed as the native builds or PWA) and Reactive Web Apps are secure because they are served via HTTPS. All requests made to the back-end of these apps (the server part of the OutSystems generated code for your app) are always made over HTTPS. 

This means that you don't need to configure the security of HTTP requests in your application, or in application elements such as UI Flows and Screens. Also, SSL (Secure Socket Layer) is already configured and activated in the environments of your infrastructure.

Therefore, IT Managers or Administrators don't need to override or enforce the HTTPS security of applications that are installed and running because it's already enabled. 

With HTTPS security, your Mobile Apps and Reactive Web Apps establish a secure communication channel between the end user and your OutSystems environment. This way:

* The data exchanged cannot be read by an unauthorized third-party, since it's encrypted.
* The data exchanged cannot be tampered with, since the message integrity is checked.
* Man-in-the-middle attacks are prevented: when the end user accesses the application using HTTPS, the application server is required to present a certificate. The end user's browser checks to see if that is a trusted application server or some other application server that cannot be trusted.

All the communication between the app and the Platform Server is done through [secure REST calls](<../../security/app-security/mobile-app-server.md>).

