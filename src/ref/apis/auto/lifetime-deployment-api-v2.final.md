---
summary: OutSystems 11 (O11) LifeTime API v2 enables management of applications, environments, deployments, and user roles.
tags: api management, deployment automation, environment management, user management, swagger integration
locale: en-us
guid: 8ebd5215-2960-4071-8a9c-83fe39674ee0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=609:507
audience:
  - platform administrators
  - full stack developers
  - backend developers
  - tech leads
  - architects
outsystems-tools:
  - lifetime
  - service center
coverage-type:
  - remember
topic:
  - deployments-api-automation
api-render: true
---

# LifeTime API v2

The LifeTime API allows you to manage applications, modules, environments, deployments, users, teams, roles and deployment zones of your OutSystems infrastructure. Please bear in mind that what while the LifeTime UI and API deal with the same concepts, there are scenarios that are supported only via UI. All API operations are limited to the permissions associated with the Service Account used to call it, as defined in LifeTime. For operations on DB connections, the permissions are defined at the environment level. For more information about DB connection permissions, please refer to the following link: [Allow Integrations With External Databases](https://success.outsystems.com/documentation/11/managing_outsystems_platform_and_application_lifecycle/manage_it_users/allow_integrations_with_external_databases/).

## Version: v2

The LifeTime API allows you to manage applications, modules, environments, and deployments of your OutSystems infrastructure. Version 2 of the API adds support for deployment zones, users, teams, and roles.

Follow the guidelines presented in [REST API Authentication](<../lifetime-deployment/rest-api-authentication.md>) to authenticate your API requests.

<div class="info" markdown="1">

Check [LifeTime API Examples](<../lifetime-deployment/api-use-cases.md>) to learn how to perform common tasks using the LifeTime API.

</div> 

You can download the Swagger file for the LifeTime API v2 in the download page of LifeTime Management Console binaries (available from LifeTime version 11.5.0). Go to the [Downloads area](https://www.outsystems.com/Downloads/search/LifeTime/11/), and select your LifeTime version:

![Screenshot of the LifeTime API v2 downloads page with links to download Swagger file](images/lifetime-api-downloads.png "LifeTime API Downloads")

## Summary {#swagger--summary-tags}

The LifeTime API is available through your LifeTime environment, with the API base URL determined by your LifeTime environment's domain. For instance, if your LifeTime address is `example-lt.example.com/lifetime`, then the LifeTime API base URL is `example-lt.example.com/lifetimeapi/rest/v2`.

You can also find and test [LifeTime API v2 in Postman](https://www.postman.com/outsystems-official). 

Base URL
:    `<lifetime-domain>/lifetimeapi/rest/v2`

Version
:    v2

Scheme
:   https

<style>
#b3-b4-b1-InjectHTMLWrapper {height: auto!important}
.image-zoom div div{height: auto!important}
</style>

<rapi-doc spec-url = 'resources/lifetime-api.json'  theme = 'light' nav-bg-color = '#fff' show-header = 'false'  show-info = 'false'  allow-authentication ='false'  allow-server-selection = 'false'  allow-api-list-style-selection ='false' render-style = 'view' layout = 'column' show-method-in-nav-bar = 'as-plain-text' use-path-in-nav-bar = 'true' allow-spec-file-download = 'true' show-side-nav = 'true' allow-try='false' regular-font = 'NotoSans' primary-color = '#242320' bg-color = '#fff' text-color = '#4D4D49' mono-font = 'monospace' allow-schema-description-expand-toggle = 'false' schema-style = 'tree' schema-description-expanded = 'true' default-schema-tab = 'schema'>
</rapi-doc>
