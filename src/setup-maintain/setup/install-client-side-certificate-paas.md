---
summary: For OutSystems cloud, when you need to consume webservices that require authentication using client-side certificates, request OutSystems Support to install the certificates on the front-end servers.
tags: support-Cloud_Platform
locale: en-us
guid: 7c93c0ac-8de4-412f-8c80-37179170f1d8
app_type: traditional web apps, mobile apps, reactive web apps
---

# Requesting to install client-side certificates on OutSystems cloud

When consuming webservices external to the OutSystems servers and considering the [Client-server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model), the OutSystems servers are, in this scenario, the **client-side**, and the servers that host the webservice, the **server-side**.

## Applicable use case

When the server-side requires authentication via a certificate, the client-side needs to be configured so that it bears the certificate to be able to send it on it’s requests to the server.

 All the front-ends of the environment need to have the certificate configured.
For OutSystems cloud environments, this operation is performed by OutSystems support. 

This option is available depending on your subscription, check here for more details about [Cloud service delivery requiring direct assistance from OutSystems Support](https://www.outsystems.com/legal/success/cloud-services-catalog/).

## Requesting the service

You’ll need to [open a support case](https://success.outsystems.com/Support/OutSystems_community/Opening_a_support_case_with_OutSystems) and:

* Provide the client-side certificate:
    * in .PFX format, with password
    * any other required root certificates, in .CER format, if not yet included in the .PFX

* Make sure to be clear about what environments should the certificate be installed in.

## What will OutSystems deliver 

OutSystems staff installs the certificate in all the front-ends and notifies you once the operation is complete. 
The path to the certificate is provided so that you can use it in your integrations. 


## Using the certificate on integrations
For instructions on how to secure your integrations with client side certificates authentication check:

[Secure Rest APIs with client side authentication](https://success.outsystems.com/Support/Security/Secure_Rest_APIs_with_client_side_authentication)

[SOAP: Authenticate using a client certificate](../../extensibility-and-integration/soap/consume/extensibility-use-cases/certificate.md)


