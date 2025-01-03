---
summary: Explore REST API integration and exposure capabilities in OutSystems 11 (O11) for enhanced application interoperability.
tags: rest api, api integration, api exposure, application interoperability, service actions
locale: en-us
guid: e66f1a19-83df-4bb1-ad39-a61cfaaa6bbb
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - understand
---

# REST

You can integrate your OutSystems applications with REST APIs provided by other systems, or even by other OutSystems applications. Use this functionality either to obtain data from those systems or to request them to perform some action.

You can also expose REST APIs in your OutSystems applications. In this case, other systems can consume the API methods you create under a REST API.

<div class="info" markdown="1">

If you're creating a REST API to expose functionality that is going to be consumed only by other modules or applications inside the same OutSystems environment, consider using **Service Actions** instead.

A Service Action is a REST-based remote call to another process, but its usage is very similar to public Server Actions. For more information check [Use Services to Expose Functionality](../../building-apps/reuse-and-refactor/services.md).

</div>
