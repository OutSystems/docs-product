---
summary: mTLS client certificate authentication for REST APIs in OutSystems 11 (O11) Cloud validates callers via a certificate header in OnAuthentication.
tags: rest apis, mtls, tls client certificates, authentication, security, outsystems cloud
locale: en-us
guid: 84bc79ee-929e-4488-9c4b-f134287ad649
app_type: traditional web apps,mobile apps,reactive web apps
platform-version: o11
figma:
audience:
  - Developer
  - Architect
  - Platform administrator
coverage-type:
  - understand
  - apply
  - unblock
topic:
  - authentication-mechanisms
  - rest-webservice-data
outsystems-tools:
  - service studio
helpids:
isautopublish: true
---

# Authenticate REST API callers with mTLS

<div class="info" markdown="1">

This article applies only to OutSystems Cloud.

</div>

OutSystems 11 Cloud supports mTLS passthrough for REST API endpoints. This lets your applications authenticate REST API clients using certificates, in addition to or instead of traditional credentials.

In a mutual TLS (mTLS) handshake, both parties present a certificate to prove their identity:

* The server proves its identity to the client (normal HTTPS).
* The client proves its identity to the server.

This approach is common for secure machine-to-machine integrations and partner APIs that require stronger authentication than API keys or bearer tokens alone.

## Prerequisites

You need a CA certificate in `.CER` format.

## Set up mTLS authentication

Setting up mTLS authentication for your exposed REST API involves two steps:

1. [Get your CA trusted](#get-your-ca-trusted)

    Chain your CA certificate up to a Certificate Authority that your OutSystems front-end servers trust.

1. [Validate the certificate](#validate-the-certificate)

    Read the certificate header that the load balancer forwards, and validate it in `OnAuthentication` on every request.

### Get your CA trusted {#get-your-ca-trusted}

To verify a client certificate, the application chains it up to a trusted Certificate Authority (CA). Install these CA certificates on your OutSystems front-end servers; otherwise, valid client certificates are rejected as untrusted.

To configure this trust:

* [Open a support case](https://success.outsystems.com/support/outsystems_community/opening_a_support_case_with_outsystems/) if your environment doesn't already trust your CA. In the support case:
    * Provide the root, and any intermediate, CA certificate in `.CER` format.
    * Identify the environments that need this certificate.

OutSystems installs the certificate on all front ends and provides the path to it for use in your integrations.

### Validate the certificate {#validate-the-certificate}

With mTLS passthrough, the Application Load Balancer (ALB) forwards the caller's certificate to your backend as a URL-encoded request header. Your OutSystems app is then responsible for reading this header and validating the certificate.

The following diagram shows the request flow, from the client presenting its certificate to the ALB, through header forwarding, to validation in `OnAuthentication`:

![Sequence diagram showing the client sending an HTTPS request with its client certificate to the Application Load Balancer, which forwards it to the exposed REST API as an X-Amzn-Mtls-Clientcert header. OnAuthentication validates the header against the installed CA certificate and returns a 200 response if the certificate is valid, or a 401 response if it's missing or invalid.](images/mtls-diag.png "mTLS passthrough flow for exposed REST APIs")

The client and load balancer steps happen automatically. Implement the following pattern in your REST API's `OnAuthentication` callback to read and validate the header, corresponding to the validation step in the diagram:

1. **Read the header** ([GetRequestHeader](../../../ref/apis/auto/httprequesthandler-api.final.md#GetRequestHeader)).

    The header AWS uses to forward the certificate is `X-Amzn-Mtls-Clientcert`. It returns the client certificate in URL-encoded PEM format, or empty if no certificate was presented.

1. **Verify the header** (`ValidateClientCert`).

    Implement the logic to validate the forwarded header. Your implementation should do the following:

    * Correctly URL-decode the header.
    * Parse the PEM certificate.
    * Verify it chains up to the CA from [Get your CA trusted](#get-your-ca-trusted).

    Furthermore, ensure your implementation verifies the certificate's expiration, checks the chain of trust against your configured CA, and validates the Certificate Revocation List (CRL).

1. **Enforce authentication** (`OnAuthentication`).

    Wire your validation logic into the REST API's callback. This gates every request automatically, returning a 401 status code if the certificate is missing or invalid, before any method logic executes.

## Troubleshooting hints {#troubleshoot}

If the integration doesn't behave as expected, a diagnostic endpoint helps you inspect the forwarded header and understand why a certificate is accepted or rejected. This endpoint reads the `X-Amzn-Mtls-Clientcert` header and returns its raw value alongside the validation result.

<div class="warning" markdown="1">

This endpoint exposes certificate details that aren't normally accessible to the caller. A malicious actor could use it to harvest information about the certificates used in your TLS communication. Enable this endpoint only in non-production environments, and disable or remove it before going live.

If you need it in production for incident troubleshooting, protect it behind a site property toggle and restrict access to trusted IPs at the network level.

</div>

## Important considerations

* Enabling integration logging causes header values to be logged. Header values contain sensitive identifying material, so exercise caution with production logs.
* **Identity versus authorization**: successful mTLS authentication proves the client holds a trusted certificate, but it doesn't inherently authorize access to specific resources. For caller-specific access control, inspect the certificate subject and match it against an allow-list in your application logic.
