---
summary: Learn how to configure secure endpoints to prevent host header injection in OutSystems Cloud.
locale: en-us
guid: 6c1dcebe-0c55-4fb3-b94b-21d162a23053
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing-the-Applications-Lifecycle?type=design&node-id=3492-399&mode=design&t=POXL6zLzKO5sOwUF-0
---
# Protecting against host header injection with secure endpoints


Host header injection is a vulnerability in which an attacker manipulates the host header of a HTTP request to deceive a server into handling the request as if it were intended for a different domain. Malicious actors can intercept a user's request and change the host header.
The following diagram shows an example of such an attack.

![Diagram illustrating a host header injection attack where an attacker manipulates the host header to redirect a user's request to a malicious server.](images/hh-injection-attack-diag.png "Host Header Injection Attack Diagram")


To safeguard against unauthorized access to sensitive data, manipulation of user sessions, and exposure to malicious content, it's crucial to mitigate this vulnerability. Implementing this configuration is essential for achieving [PCI compliance](https://www.outsystems.com/tk/redirect?g=1fcf38a0-15c1-486a-b022-a9d21dea89b6).

In the OutSystems Cloud, LifeTime provides functionality to set up secure endpoints. This feature safeguards against host header injection attacks by verifying incoming requests against your defined list of endpoints. Any request with an unauthorized host header is declined, enforcing access exclusively through the designated endpoints to enhance security.

![Diagram showing the functionality of secure endpoints in OutSystems Cloud to safeguard against host header injection attacks.](images/secured-endpoints-diag.png "Secured Endpoints Diagram")



Therefore, configuring the endpoint list according to your organization’s specific infrastructure is important to ensure your endpoints aren’t rejected.

The following are important notes regarding secure endpoints:

* Both enabling and disabling the feature require a support ticket.
* When host header injection protection is enabled, the environment's hostname is always allowed by default.
* Once enabled, you can customize the list of allowed endpoints in self-service.
* Wildcards (*.example.com) aren’t supported as secure endpoints.
* If you remove all allowlisted endpoints, your environment only allows access with its own hostname.
* [Managing the list of secure endpoints](#manage-secure-endpoints) is available for all environments except LifeTime. To manage secure endpoints for the LifeTime environment, open a support case.
* When requests are blocked, users will see an error in the browser. See [Troubleshooting error 503 - Host header does not match](https://www.outsystems.com/tk/redirect?g=c9a42528-9c9c-471c-aded-e5c2a0aef08e) for more details.


## Prerequisites { #prerequisites }

To configure additional secure endpoints for host header injection protection, you first need to ensure the following conditions:

* Your infrastructure is in the OutSystems Cloud.
* The LifeTime version is 11.17.4.0 or higher.
* To manage secure endpoints, you need to have Admin built-in role in LifeTime.


## Enabling and managing secure endpoints { #enable-secure-endpoints }

Before configuring additional secure endpoints it’s important to gather all the valid hostnames to ensure a correct configuration.

The following diagram shows an overview of the process.

![Process overview diagram for enabling and managing secure endpoints, with steps including checking endpoint configurations, checking redirect rules, enabling secure endpoints, and managing secure endpoints.](images/hh-protect-process-diag.png "Host Header Protection Process Overview")


### Check your endpoint configurations { #check-endpoint-configurations }

<div class="warning" markdown="1">

Before enabling secure endpoints you must list all the hostnames used to access your environment. You'll need this list to configure the allowed hosts. Otherwise, you'll start losing access, impacting your app’s normal operation. 

</div>


* **Check your DNS configuration:**

    You may have configured different hostnames internally that would have their address resolved to the environment’s public name. In this case, you should also allow them.

    For example, you may have `endpoint 1` and `endpoint 2` pointing to `endpoint 3` that then points to your `outsystemsenterprise.com` environment address.

    ![Diagram depicting DNS configuration with multiple endpoints pointing to an OutSystems environment address, illustrating the need to add all endpoints as secure in LifeTime.](images/dns-config-diag.png "DNS Configuration Diagram")

    In this scenario, you must add all endpoints that can eventually lead to your `outsystemsenterprise.com` environment address as secure endpoints in LifeTime. In this example, you would need to add `endpoint 1`, `endpoint 2`, and `endpoint 3`.

    <div class="info" markdown="1">

    Note all the valid endpoints in your DNS configuration. You'll need them to compile the list of secure endpoints to configure in LifeTime.

    </div>

* **Check if you have more than one FQDN (fully qualified domain name)for your domain:**

    If you have more than one FQDN or multi-domain (SAN) certificate, you must allow all corresponding domains on the list of secure endpoints for your environment.

    <div class="info" markdown="1">

    Note all your valid domains. You'll need them to compile the list of secure endpoints to configure in LifeTime.


    </div>

### Check redirect rules in Service Center { #check-redirect-rules }

With [redirect rules](../../develop/seo/seo-friendly-url-traditional.md#redirect-rules), your environment might redirect requests to an endpoint not gathered in the section above. Make sure to verify the **Redirect Rules List**  in Service Center and allow all the destination endpoints present in the **New URL**.

<div class="info" markdown="1">

Note all your redirect rules destination domains. You'll need them to compile the list of secure endpoints to configure in LifeTime.


</div>


After you’ve checked the endpoint configurations and the redirect rules, you should have a compiled list.


## Enabling secure endpoints { #enable-secure-endpoints }

To protect against host header injection, you can enable secure endpoints in any environment. OutSystems Support must perform the first configuration. Follow these steps:

1. [Open a support case](https://www.outsystems.com/support/portal/open-support-case)
1. In the support case, provide the environments to enable the feature and the compiled list of endpoints per environment. This is a fundamental step, if no list is provided, only the environment address will be allowed in the host header.
1. Wait for a confirmation in the support case.


Once OutSystems support confirms secure endpoints have been enabled for the first time, you’ll be able to manage them as needed.

<div class="warning" markdown="1">

When you change the endpoint configurations or redirect rules, especially when adding new values, you must accordingly manage the secure endpoints in LifeTime. Failing to do so may impact your apps.

</div>

## Managing the list of secure endpoints { #manage-secure-endpoints } 

When you enable host header injection protection, LifeTime displays **Additional Secure Endpoints**. These endpoints form the allow list for validating host headers. Any request with a host header that differs from those in the allow list will be blocked.

To manage secure endpoints follow these steps:

1. Go to **LifeTime** > **Environments** and select the environment you want to manage.
1. Under **Additional secure endpoints**, click **Change**.
1. Add or remove endpoints.
1. Confirm by clicking **Update Additional Secure Endpoints**. Your changes will be applied automatically.


![Screenshot of the LifeTime interface for managing additional secure endpoints, showing where to add or remove endpoints and update settings.](images/manage-endpoints-lt.png "Managing Secure Endpoints in LifeTime")

