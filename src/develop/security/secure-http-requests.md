---
tags: runtime-traditionalweb; support-devOps; support-Security; support-Security-featured
summary: Increase the security of your Traditional Web app by increasing the security level of HTTP requests.
---

# Secure HTTP Requests

You can increase the security of your Traditional Web app by increasing the security level of HTTP requests. You can configure the security level of HTTP requests in the following elements:

* UI Flows (OutSystems uses the value specified for the flow as the default for all the flow Web Screens)
* Web Screens
* Exposed SOAP Web Services
* Exposed REST APIs

HTTP requests are always secure in Reactive and Mobile apps, therefore this configuration doesn't apply to mobile scenarios.

To configure the HTTP security level for these elements, set its **HTTP Security** property to the desired value. The following types of HTTP security are available:

* `None`
* `SSL/TLS`: Uses the HTTPS protocol in requests. Client certificates can be accepted but aren't required.
* `SSL/TLS with client certificates`: Uses the HTTPS protocol in requests and client certificates are required. This option isn't available for REST APIs. Additionally, this option isn't supported in OutSystems Cloud.

If you access an application using an explicit secure request (starting with `https://`), OutSystems maintains the secure protocol while navigating over non-secure elements.

The security level that you define in your application at design time can be overridden by IT Managers or Administrators, as they can [enforce the HTTPS security of applications](<../../managing-the-applications-lifecycle/secure-the-applications/enforce-https-security.md>) installed and running in an environment.

## Client certificate actions

If you have OutSystems installed **on-premises**, you can use the following System Actions when you are using client certificates:

* [ClientCertificateGetDetails](<../../ref/apis/auto/system-actions.final.md#ClientCertificateGetDetails>): Returns information about the current client certificate.
* [ClientCertificateValue](<../../ref/apis/auto/system-actions.final.md#ClientCertificateValue>): Returns the value of a specific property of the current client certificate.
