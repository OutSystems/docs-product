---
summary: Redirect URLs and create site and Screen URLs to to improve user experience and search page ranking.  
tags: article-page,
---

# Technical Preview - SEO in Reactive Web Apps

Use **SEO-friendly URLs for Reactive Web Apps** to create the SEO-friendly versions of the uniform resource locators (URLs). Service Center lets you manage Site Rules and Redirects. You can edit custom URLs in Service Studio, in the properties of each Screen. 

## Prerequisites

**SEO-friendly URLs for Reactive Web Apps** is a technical preview feature. To use it you need to meet the following requirements:

* You're using Platform Server 11.12.0 or later.
* Your Service Studio is up to date.
* The [technical preview](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Technical_Preview_features) **SEO-friendly URLs for Reactive Web Apps** is active in LifeTime for all environments.
* You're using an OutSystems enterprise cloud offer or a properly configured on-premises installation.
* For on-premises installations only: make sure that [ISAPI Filters](<https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Customize_or_redirect_the_application_URL#Installing_ISAPI_Filters_and_Logging>) are active in your environment.

<div class="warning" markdown="1">

**About activating or deactivating the feature**

* To deactivate **SEO-friendly URLs for Reactive Web Apps** you first need to remove all Site Rules from Service Center.
* After you **activate or deactivate** the feature, publish your apps to apply the changes.

</div>

## Site Rules

A Site Rule maps the URL to a module in the environment. If the user enters `www.example.com` in the browser, the platform loads the home screen of the **MyMainModule**.

The following table shows examples of Site Rules:

| URL                             | To the module         |
| ------------------------------- | --------------------- |
| `www.example.com`               | MyMainModule          |
| `www.example.com/myapp`         | MyAppHomeModule       |
| `subdomain1.example.com`        | MyAppSubdomainModule  |
| `subdomain1.example.com/myapp1` | MyAppSubdomainModule2 |


See [Managing site rules](#managing-site-rules) for instructions.

## Custom Screen URLs

A custom Screen URL works on the module level, letting you change how the URL of one screen shows in the browser. The Screen **ProductListSection** from your module can load from the URL /`Products` instead of `/ProductListSection`. Custom Screen URLs support having the parameters on the path instead of using the query string, so you can redirect users to the URL `/Products/1` that would without the custom URL load as `/Products?Id=1`.

The following table shows examples of custom Screen URLs:

| Original URL              | With **Path** | With **Query string**   |
| ------------------------- | ------------- | ----------------------- |
| `/ProductListSection`     | `/Products`   |                         |
| `/Products?Id=1`          | `/Item/1`     | `/Item?Id=1`            |
| `/Order?Id=1`             | `/Buy/1`      | `/Buy?Id=1`             |
| `/Order?Id=1&Quantity=10` | `/Buy/1/10`   | `/Buy?Id=1&Quantity=10` |

<div class="info" markdown="1">

Make sure all Page Names are unique in the environment. Otherwise, some URLs may not work. See also: [Avoiding duplicated redirects](#avoiding-duplicated-redirects).

</div>


See [Managing custom Screen URLs](#managing-custom-screen-urls) for instructions.

## Redirects

Redirect rules let you redirect browser requests from the old domain or subdomain to the new URLs. OutSystems uses the **301 HTTP status code** for the domain-level redirects.

The following table shows examples of redirects:

| Old URL               | New URL                 |
| --------------------- | ----------------------- |
| `example.com`         | `www.example.com`       |
| `about.example.com`   | `www.example.com/about` |
| `oldname.example.com` | `newname.example.com`   |

See [Managing redirects](#managing-redirects) for instructions.

## Managing URL rules and redirects

The following sections cover more technical details related to managing Redirects, Site Rules, and custom Screen URLs.

### Managing Site Rules

To manage Site Rules you need:

* **Base URL**. The string to match the rule, for example `www.example.com/myapp`.
* **Root Application**. The module to which the platform redirects the requests, for example `MyMainModule`. 

Go to **Service Center** > **Administration** > **SEO URLs** > **Site Rules List** to:

* Add a Rite Rule
* Update a Site Rule
* Disable or delete a Site Rule

When working with Site Rules, keep in mind the following:

* You can have only one Site Rule per root application for domains with subpaths.
* Creating or editing a Site Rule may temporarily slow down the app because the platform needs to reload the setting files.

![Site rules list in Service Center](images/site-rules-sc.png?width=910)

### Managing custom Screen URLs

You can add custom Screen URLs in Service Studio. Go to the properties of the Screen to which you want to set the name. Then, set **Custom URL** to **Yes** in the **Advanced** section and edit the URL structure.

![Screen URLs settings and properties](images/page-redirects-properties-ss.png?width=350)

If an app passes an empty string as a value for a required parameter, the users see an error message. See [Empty string in a required parameter causes an error](troubleshooting.md#empty-string-in-a-required-parameter-causes-an-error) for more information.

Here are more details about the properties.

| Property          | Description                                                                                                                                                                                                             |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Custom URL**    | If you set **Custom URL** to **Yes**, Service Studio activates custom Screen URLs and lets you edit the redirect settings.                                                                                                  |
| **Page Name**     | The name of the page to show in the URL. Use only alphabetical characters and numbers. You can use the following  special characters, but not at the beginning or at the end of the page name: "_", "-", "/" , and "~". |
| **URL Structure** | Set to **Path** to pass the parameters separated by `/` in the URL (example: `/Product/1`). Set to **Query string** to pass the parameters as a string (example: `Products?Id=1`).                                      |
| **URL Pattern**   | Preview only. Shows the URL preview as you edit the settings.                                                                                                                                                           |

When working with custom URLs, keep in mind that:

* You can add custom URLs to all Screens **except** the Default Screen.
* When copying Screens with custom URLs from Reactive Web App module to Mobile App module, Service Studio removes the URL rules in the Mobile App module.

### Managing Redirect Rules

To manage Redirect Rules you need to know the following:

* **Base URL**. The string to match the rule, for `old.example.com`
* **Replace With**. The replacement string for the URL, for example `new.example.com` 

Go to **Service Center** > **Administration** > **SEO URLs** > **Redirect Rules List** to:

* Add a Redirect Rule
* Update a Redirect Rule
* Disable or delete a Redirect Rule

![Redirects in Service Center](images/redirects-sc.png?width=910)
