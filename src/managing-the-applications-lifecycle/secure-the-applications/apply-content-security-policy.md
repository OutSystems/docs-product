---
summary: Use the Content Security Policy (CSP) against code injection attacks in applications developed with OutSystems to protect against a growing number of attacks on the Web.
tags: support-Security-overview
---

# Apply Content Security Policy


Content Security Policy (CSP) lets you define rules that help protect your users and apps from web attacks. CSP provides a standard way of declaring approved origins of content that browsers are allowed to load.

CSP is configured using directives that are sent to browsers in [specific HTTP headers](<https://en.wikipedia.org/wiki/Content_Security_Policy#Status>). This way, when browsers run pages of your applications, they know from which location and/or which type of resources to load.

It is advisable that you configure the CSP in every environment. Start with the allowed sources in an environment, for all its applications. Then, specify the sources per application, as needed, to override the general configuration.

The CSP configuration works for both web and mobile applications developed with OutSystems.



## Configure CSP in LifeTime

If you have **LifeTime** installed, set the **Content Security Policy** using this management console.

![Content Security Policy in LifeTime](images/apply-content-security-policy-lt.png)

### For all environments

To configure the CSP in all environments in **LifeTime**:

1. Go to the **Infrastructure** section to see all environments.
1. In an environment, select the **Environment Security** option.
1. Enable CSP.
1. Configure directives, with one value per line.
1. Click **Save**.
1. Republish all applications using an ["All Components" solution](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Creating_and_using_an_%22All_Components%22_solution).

### For an app

To configure CSP for an application in **LifeTime**:

1. Select the **Applications** section, and then the application.
1. Select the **Security Settings** option.
1. In the dropdown list, select the environment to which the settings will apply.
1. Enable CSP.
1. Configure directives, with one value per line.
1. Click **Save**.
1. Republish the application in Service Center.

<div class="info" markdown="1">

By design, the Content Security Policy on the app level overrides the same policy on the environment level. 

</div>

## Configure CSP in Service Center

If you don’t have **LifeTime** installed, configure CSP in each environment using the environment management console, **Service Center**.

![Environment Security in Service Center](images/environment-security-sc.png)

### For an environment

To configure CSP for all apps in an environment in Service Center:

1. In the **Administration** section, select the **Security** option.
1. Enable CSP.
1. Configure directives, with one value per line.

### For an app

To configure CSP for an application in **Service Center**:

1. Select the **Factory** section and then the application.
1. Select the **Security** tab.
1. Enable CSP.
1. Configure directives, with one value per line.

<div class="info" markdown="1">

By design, the Content Security Policy on the app level overrides the same policy on the environment level.

</div>

## Monitoring  { #monitoring }

Once you set CSP, monitor the blocked resources using the management console of the environment in **Service Center**:

1. Go to the **Monitoring** section and select the **Errors** option.
1. Set the eSpace filter to SecurityUtils to only see the resources blocked by CSP.

When configuring CSP take the following risks of misconfiguration into account:

* **Missing policies**: Make sure that you configure policies that allow all sources used in your applications. Otherwise, users may stumble upon things like videos that are not shown, or CSS that is not applied.

* **Too permissive policies**: Be especially cautious when allowing resources to be loaded from everywhere (by using `*` in the domain list). Hackers may take advantage of links, scripts, or other resources in your applications to redirect users to malicious pages.

* **Duplicated configuration**: On self-managed environments, set the CSP directives only in **LifeTime**. Don't set them directly in IIS, for example. It will cause unexpected results, by including the CSP directives twice.

## Directives reference

The table below describes the list of available directives to configure Content Security Policy in **OutSystems**. The **Required values** column indicates the values that **LifeTime** automatically applies to the directive for the applications to work correctly. Those values cannot be removed.

| Directive     | Reason        | Required values  |
| :------------ |:--------------|:----------------|
| Base-uri      |The domains which can be used as base URL for applications screens.<br/>The following source expressions are allowed: `self`.|`self`|
| Child-src     |The domains which applications are allowed to embed framed.<br/>The following source expressions are allowed: `self` and `*`.|`self`<br/>`gap:`|
| Connect-src   |The domains from which applications are allowed to load resources using script interfaces.<br/>The following source expressions are allowed: `self` and `*`.|`self`|
| Default-src   |The domains from which applications are allowed to load resources, by default.<br/>Any resource type dedicated directive (like object-src or img-src) that is not defined will inherit this configuration.<br/>The following source expressions are allowed: `self`, `data:` and `*`.|`self`<br/>`gap:`<br/><br/>Values added at runtime:<br/>`'unsafe-inline'`<br/>`'unsafe-eval'`|
| Font-src      |The domains from which applications are allowed to load fonts.<br/>The following source expressions are allowed: `self`, `data:` and `*`.|`self`<br/>`data:`|
| Img-src       |The domains from which applications are allowed to load images.<br/>The following source expressions are allowed: `self`, `data:` and `*`.|`self`<br/>`data:`<br/><br/>Values added at runtime:<br/>`blob:`|
| Media-src     |The domains from which applications are allowed to load media files.<br/>The following source expressions are allowed: `self`, `data:` and `*`.|-|
| Object-src    |The domains from which applications are allowed to load objects (for `<object>`, `<embed>` and `<applet>` elements).<br/>The following source expressions are allowed: `self` and `*`.|`-`|
| Plugin-types  |The valid plugins that the user browser may invoke|-|
| Script-src    |The domains from which applications are allowed to load scripts.<br/>The following source expressions are allowed: `self`, `data:` and `*`.|`self`<br/><br/>Values added at runtime:<br/>`'unsafe-inline'`<br/>`'unsafe-eval'`|
| Style-src     |The domains from which applications are allowed to load styles.<br/>The following source expressions are allowed: `self`, `data:` and `*`.|`self`<br/><br/>Values added at runtime:<br/>`'unsafe-eval'`|
| Frame-ancestors|The domains which are allowed to embed applications in a frame.<br/>The following source expressions are allowed: `self` and `*`.|`self`<br/>`gap:`|
| Frame-src | There's no dedicated field, but you can use the `Child-src` field to enter the values for the platform to generate the `Frame-src` directive. | `self` |
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

**Applies to mobile apps only**. If you configure CSP on the environment level in LifeTime, change the schema to `outsystems://` in the mobile apps CSP configuration only. This prevents side effects for Traditional Web Apps or Progressive Web Apps (PWAs).

## Using iframes in iOS apps

If you want to use both CSP directives and iframes in your iOS apps, add the following to the **frame-ancestors** directive field:

```
outsystems://YOUR_APP_URL
https://YOUR_APP_URL
```

Failure to do so prevents content from rendering. You can identify the issue by searching for the **Interrupting main resource load due to CSP frame-ancestors or X-Frame-Options** error log.

### Embedding an app in an OutSystems Native Mobile app iframe

Since the release of [MABS version 6.0](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service/MABS_Version_6.0), **OutSystems** mobile apps require a custom scheme in iOS in order to

* Enable offline support with WKWebView
* Navigate to other **OutSystems** mobile applications
* Access other **OutSystems** mobile applications with InAppBrowser 

For Android and InAppBrowser windows, **OutSystems** native mobile apps run under the `https://` scheme. On iOS the `outsystems://` scheme is used.

Since `outsystems://` is a custom scheme, it must be specifically added to the authorization list. To embed an app in an iframe on an **OutSystems** native mobile app, add the following to the **frame-ancestors** directive field:

```
outsystems://YOUR_APP_URL
https://YOUR_APP_URL
```

## Common problems with embedded iframes in iOS apps

### iframe content not rendered

If iframe content displays as expected on Android on a browser but not on iOS, the most probable cause is that the `outsystems://` scheme is missing.

Add the following to the **frame-ancestors** directive field:

```
outsystems://YOUR_APP_URL
https://YOUR_APP_URL
```

You can get more information if you notice this behavior from the **Service Center**  [monitoring page](#monitoring). You can identify the issue by searching the **Interrupting main resource load due to CSP frame-ancestors or X-Frame-Options** error log.


### iframe content is displayed but does not behave as expected

With the [version 2.3](https://webkit.org/blog/9521/intelligent-tracking-prevention-2-3/) release of Apple’s Webkit Intelligent Tracking Prevention (ITP) in 2017, the Safari browser blocks all cookies for cross-site resources by default. This means that users of Safari on iOS 13 and iPadOS beta, and Safari 13 on macOS, cannot access a reactive **OutSystems** app  that is hosted on a different domain which is embedded in an iframe element.

An example of this behavior is shown below:

1. An end-user logs into a portal page ([https://portal.example.com](https://portal.example.com)) which has authentication mechanisms to create first-party cookies.
1. An **OutSystems** app in an HTML iframe ([https://app.example.net](https://app.example.net)), which is on a different domain, attempts to create third-party cookies. The Safari browser blocks all access to the domain/application that is consuming the first party cookies. The content in the iframe is not rendered.

![Safari blocks iframe from 3rd party app](images/safari-blocks-iframe.png)

<div class="info" markdown="1">

You can read more about this issue in the [Safari Blocks Third-Party Cookies by Default](https://www.infoq.com/news/2020/04/safari-third-party-cookies-block/) InfoQ newsletter.

</div>

In March 2020, Apple published a blog post ([Full Third-Party Cookie Blocking](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/)) that suggested two workarounds to address developer concerns about legitimate third-party cookies, such as those used by **OutSystems** to store login and session information. 


#### OAuth 2.0 Authorization

One method requires the end-user to authenticate third-party apps (such as [https://app.example.net](https://app.example.net) in an iframe) to forward an authorization token to a hosting website which can then establish a first-party login session.

For more information about implementing this solution see the following documents:

* [OAuth 2.0 Authorization](https://tools.ietf.org/html/rfc6749) 
* [Secure and HttpOnly cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies#Secure_and_HttpOnly_cookies)
* [Manage cookies and website data in Safari on Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/mac)


#### Storage Access API

A second method relies on Apple’s Webkit [Storage Access API](https://webkit.org/blog/11545/updates-to-the-storage-access-api/) that protects end-user privacy and prevents cross-site request forgeries by asking users to consent to giving access to their cookies from one domain to another.

The following workflow uses Storage Access API as follows:

1. A navigation/redirect moves users from a portal page ([https://portal.example.com](https://portal.example.com)) to the **OutSystems** app ([https://app.example.net](https://app.example.net)) in the iframe.
1. The user interacts with the **OutSystems** app as the first party. The example shown in the illustration prompts the user to log in and then accept the use of cookies. Once this is done, the browser knows that the user has seen and used the site. 
1. A first-party cookie is created by the third-party app. This establishes the website in the iframe as visited for the purposes of the underlying Storage Access API cookie policy.

![Safari allows iframe from 3rd party app](images/safari-allows-iframe.png)


Designers may use the following guidelines as a basis for designing a natural end-user workflow that presents minimal friction using Storage Access API.

<div class="info" markdown="1">

Change URLs in the code snippets to reflect the actual project addresses. 

</div>


##### Portal page

Include the following elements on the portal page ([https://portal.example.com](https://portal.example.com)):


* A sandbox within the iframe element. Sample text is shown below: 

```HTML
    <iframe
      frameborder="0"
      style="border:0"
      class="responsive-iframe"
      src="https://app.example.net"
      sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin">
    </iframe>
```
* A script that checks if the browser supports Storage Access API, sets cookie properties, and then navigates to the hosted **OutSystems** app in the iframe.

```javascript
<script>
     // Check if the browser (i.e. Safari) supports the Storage Access API by checking if the document.requestStorageAccess method is defined.
     if (document.requestStorageAccess) {
         // See if cookie exists (https://stackoverflow.com/a/25617724/1502448)
         if (!document.cookie.match(/^(.*;)?\s*fixed\s*=\s*[^;]+(.*)?$/)) {
             // Set cookie to maximum (https://stackoverflow.com/a/33106316/1502448)
             document.cookie = 'fixed=fixed; expires=Tue, 19 Jan 2038 03:14:07 UTC; path=/';
             // Navigate to interaction screen at the first party. In our case, the screen with the button that created the cookie
             window.location.replace("https://portal.example.com");
        }
    }
 <script>
```

##### iframe app

The hosted **OutSystems** app in the iframe element ([https://app.example.net](https://app.example.net)) should begin with a mechanism for the user to authorize the use of cookies.


##### Workflow using Storage Access API

When the user goes to the portal page ([https://portal.example.com](https://portal.example.com)) the following happens:

1. The script checks that the browser supports Storage Access API, meaning that the user is on the Safari browser. Cookie properties are set. The user is then sent to the login screen in the **OutSystems** app ([https://app.example.net](https://app.example.net)) hosted in an iframe of the portal.
2. If no cookies have been previously created for the app in the iframe the user is asked to give consent. 

    <div class="info" markdown="1">

    If consent had been given on a previous visit, only a **Continue** button appears.. 

    </div>

3. Once consent is given, the consent button is hidden and the **Log in** button is shown.
4. The user logs in and is directed to the portal application. The iframe app is now functional.

See [Introducing Storage Access API](https://webkit.org/blog/8124/introducing-storage-access-api/) for a detailed explanation about implementing this solution.


### Web application not recognizing authentication from mobile app

When the user authenticates using the mobile app and accesses an **OutSystems** web application, it may not be automatically authenticated. To do so, follow the steps described on [How to Reuse Web Screens in Mobile Apps](https://success.outsystems.com/Documentation/How-to_Guides/Front-End/How_to_Reuse_Web_Screens_in_Mobile_Apps#Use_an_iframe_in_the_Mobile_App)
