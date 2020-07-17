---
tags: runtime-traditionalweb; support-devOps; support-Security; support-Security-featured
---

# Secure HTTP Requests

You can increase the security of your Web application by increasing the security level of the HTTP requests. You can configure the security level of the HTTP requests in the following elements:

* UI Flows (the value specified is used as default for all Web Screens in the flow) 
* Web Screens
* Exposed SOAP Web Services
* Exposed REST APIs

HTTP requests are always secure in reactive and mobile apps, therefore this configuration does not apply to mobile scenarios.

To configure the HTTP security level for these elements, set its **HTTP Security** property to the desired value. The following types of HTTP security are available:

* `None`
* `SSL/TLS`: The HTTPS protocol is used in the requests and client certificates can be accepted but are not required.
* `SSL/TLS with client certificates`: The HTTPS protocol is used in requests and client certificates are required. This option is not applicable to REST APIs and is not supported for OutSystems Cloud. 

If you access an application using an explicit secure request (starting with `https://`), OutSystems will maintain the secure protocol while navigating over non-secure elements.

The security level that you define in your application at design time can be overridden by IT Managers or Administrators, as they can [enforce the HTTPS security of applications](<../../managing-the-applications-lifecycle/secure-the-applications/enforce-https-security.md>) that are installed and running in an environment.

## Client Certificate Actions

If you have OutSystems installed **on-premises**, you can use the following System Actions when you are using client certificates:

* [ClientCertificateGetDetails](<../../ref/apis/auto/system-actions.final.md#ClientCertificateGetDetails>): Returns information about the current client certificate.
* [ClientCertificateValue](<../../ref/apis/auto/system-actions.final.md#ClientCertificateValue>): Returns the value of a specific property of the current client certificate.
