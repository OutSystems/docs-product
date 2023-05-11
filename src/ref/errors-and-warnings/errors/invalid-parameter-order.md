---
summary: Invalid parameter order in a page name when working with SEO. 
tags:
locale: en-us
guid: b7f0d19c-a092-4b06-9cf1-56d3fd23ab88
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Invalid Parameter Order

Service Studio shows the **Invalid Parameter Order** error:

* Invalid Parameter Order | Mandatory parameters must come before optional ones when parameters are set to Path. Reorder mandatory input parameters by placing them above optional parameters.

When you have a Screen with custom URLs, put the mandatory Input Parameters first. You can place optional Input Parameters only after the mandatory ones. You can fix the error by:

* Reordering the Input Parameters. Drag the Input Parameters under the Screen where the error shows, and reorder them by putting the mandatory parameters on the top of the parameter list.
* Changing the **Is Mandatory** property of Input Parameters. Check the properties of the Input Parameters under the Screen that reports the error. If there's a Parameter that should be mandatory instead of optional, set **Is Mandatory** to **Yes**.   

<div class="info" markdown="1">

This error is part of [SEO-friendly URLs for Reactive Web Apps](../../../develop/seo/intro.md).

</div>