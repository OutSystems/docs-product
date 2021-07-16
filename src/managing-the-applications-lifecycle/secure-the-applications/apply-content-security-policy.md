---
summary: Use the Content Security Policy (CSP) against code injection attacks in applications developed with OutSystems to protect against a growing number of attacks on the Web.
tags: support-Security-overview
---

# Apply Content Security Policy


To protect against a growing number of attacks on the Web, use the Content Security Policy (CSP) against code injection attacks in applications developed with OutSystems. CSP provides a standard way of declaring approved origins of content that browsers are allowed to load.

CSP is configured using directives that are sent to browsers in [specific HTTP headers](<https://en.wikipedia.org/wiki/Content_Security_Policy#Status>). This way, when browsers run pages of your applications, they know from which location and/or which type of resources to load.

It is advisable that you configure the CSP in every environment. Start with the allowed sources in an environment, for all its applications. Then, specify the sources per application, as needed, to override the general configuration.

The CSP configuration works for both web and mobile applications developed with OutSystems.

![Content Security Policy in LifeTime](images/apply-content-security-policy.png?width=600)

## Configure CSP in LifeTime

If you have LifeTime installed, set Content Security Policy using this management console.

### For all environments

To configure the CSP in all environments use LifeTime, the management console of your infrastructure.

1. Go to the **Infrastructure** section to see all environments.
1. In an environment, select the **Environment Security** option.
1. Enable CSP.
1. Configure directives, with one value per line.

### For an app

To configure CSP for an application in LifeTime:

1. In LifeTime, select the **Applications** section, and then the application.
1. Select the **Security Settings** option.
1. In the drop list, select the environment to which the settings will apply.
1. Enable CSP.
1. Configure directives, with one value per line.

## Configure CSP in Service Center

If you don’t have LifeTime installed, configure CSP in each environment using the environment management console, Service Center.

### For an environment

To configure CSP for all apps in an environment, in Service Center:

1. In the **Administration** section, select the **Security** option.
1. Enable CSP.
1. Configure directives, with one value per line.

### For an app

To configure CSP for an application in Service Center:

1. Select the **Factory** section and then the application.
1. Select the **Security** tab.
1. Enable CSP.
1. Configure directives, with one value per line.

## Monitoring

Once you set CSP, monitor the blocked resources using the management console of the environment (Service Center):

1. Go to the **Monitoring** section and select the **Errors** option.
1. Set the eSpace filter to CSPReport to only see the resources blocked by CSP.

When configuring CSP take into account the following risks of misconfiguration:

* **Missing policies**: Make sure you configure policies that allow all sources used in your applications. Otherwise, users may stumble upon things like videos that are not shown or CSSs that are not applied.

* **Too permissive policies**: Be especially cautious when allowing resources to be loaded from everywhere (by using `*` in the domain list). Hackers may take advantage of links, scripts, or other resources in your applications to redirect users to malicious pages.

* **Duplicated configuration**: On self-managed environments, set the CSP directives only in LifeTime. Don't set them directly in IIS, for example. It will cause unexpected results, by including the CSP directives twice.

## Directives reference

The list of available directives to configure Content Security Policy in OutSystems is described in the table below.

| Directive     | Reason        | Default values  |
| :------------ |:--------------|:----------------|
| Base-uri      |The domains which can be used as base URL for applications screens.<br/>The following source expressions are allowed: `self`.|`self`|
| Child-src     |The domains which applications are allowed to embed framed.<br/>The following source expressions are allowed: `self` and `*`.|`self`<br/>`gap:`|
| Connect-src   |The domains from which applications are allowed to load resources using script interfaces.<br/>The following source expressions are allowed: `self` and `*`.|`self`|
| Default-src   |The domains from which applications are allowed to load resources, by default.<br/>Any resource type dedicated directive (like object-src or img-src) that is not defined will inherit this configuration.<br/>The following source expressions are allowed: `self`, `data:` and `*`.|`self`<br/>`gap:`|
| Font-src      |The domains from which applications are allowed to load fonts.<br/>The following source expressions are allowed: `self`, `data:` and `*`.|`self`<br/>`data:`|
| Img-src       |The domains from which applications are allowed to load images.<br/>The following source expressions are allowed: `self`, `data:` and `*`.|`self`<br/>`data:`|
| Media-src     |The domains from which applications are allowed to load media files.<br/>The following source expressions are allowed: `self`, `data:` and `*`.|-|
| Object-src    |The domains from which applications are allowed to load objects (for `<object>`, `<embed>` and `<applet>` elements).<br/>The following source expressions are allowed: `self` and `*`.|`-`|
| Plugin-types  |The valid plugins that the user browser may invoke|-|
| Script-src    |The domains from which applications are allowed to load scripts.<br/>The following source expressions are allowed: `self`, `data:` and `*`.|`self`|
| Style-src     |The domains from which applications are allowed to load styles.<br/>The following source expressions are allowed: `self`, `data:` and `*`.|`self`|
| Frame-ancestors|The domains which are allowed to embed applications in a frame.<br/>The following source expressions are allowed: `self` and `*`.|`self`<br/>`gap:`|
| Report-to     |URI where content security violations will be reported.|`<internal>`|
| Other directives|More directives to append to the Content Security Policy headers.|-|

## Content security policy and MABS { #mobile-apps }

<div class="info" markdown="1">

Applies to the iOS apps generated with MABS 6 and later.

</div>

The mobile apps generated with MABS 6 and higher require loading with `outsystems://` when running in iOS devices. Android apps still load content using `https://`. To ensure that images, fonts, videos, scripts, or stylesheet resources load properly in iOS apps, enter CSP configuration value so that the URL expressions are prefixed with `https://`.

Here are some examples:

| Before MABS 6           | After MABS 6                    |
| :---------------------- | :------------------------------ |
| `example.com`           | `https://example.com`           |
| `subdomain.example.com` | `https://subdomain.example.com` |
| `*.example.com`         | `https://*.example.com`         |
| `https://example.com`   | `https://example.com` (no change) |
| `http://example.com`    | `http://example.com` (no change)  |

Keep in mind that these changes **should only be applied to the mobile apps**. If CSP is configured for an entire environment in LifeTime, it is recommended to perform these changes in the mobile application CSP configuration to ensure there are no side effects for Traditional Web or Progressive Web Apps (PWAs).
