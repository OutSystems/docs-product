---
summary: Duplicated page name when working with SEO. 
tags:
---

# Duplicated Page Name

Service Studio shows the **Duplicated Page Name** error:

* Duplicated Page Name | (screen name) has name Page Name clashing with (element name). Use unique values.

To fix the error, change the Page Names so it's different from the names of the following **elements in the module**:

* Screens, including the name of the Screen where you set Page Name
* Blocks
* UI Flows
* The module itself

## Avoiding duplicated redirects

Avoid duplicate page names in your modules when adding custom Screen URLs and Site Rules. When choosing a page name for a Screen, consider the following:

* Does the module have Screens with Page Names?
* Have you set Page Names to an app name or module name in the environment? 
* Is there a Site Rule in the environment that redirects to that module?

If yes, there's a risk of creating duplicate redirects pointing to different places.

Consider the following example.

* In the module **MyApp**, there's a Screen **Screen1** with the Page Name set to `Users`.
* In the environment, there's the **Users** system app to manage users at `/Users`.
* In the environment, the Site Rule redirects `www.example.com` to the module **MyApp**.

When users navigate to the `www.example.com/Users` URL, there are two possibilities for the platform to route the URL:

* Navigate to `Screen1` of the **MyApp** module.
* Navigate to the **Users** system app.

Depending on **where the platform registers the request** to access `www.example.com/Users`, the routing is as follows:

* If the request comes from **within** the browser running MyApp, **Screen1** of the module **MyApp** loads.
* If the request comes **outside** the browser running MyApp, the system app **Users** loads.

<div class="info" markdown="1">

This error is part of [SEO-friendly URLs for Reactive Web Apps](../../../develop/seo/intro.md).

</div>