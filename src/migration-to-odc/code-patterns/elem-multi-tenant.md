---
guid: ec55e3f4-fe42-4e01-b70c-964f2400813c
locale: en-us
summary: The conversion of assets with multi-tenant modules isn't supported.
figma:
coverage-type:
  - unblock
topic:
app_type: mobile apps,reactive web apps,traditional web apps
platform-version: o11
audience:
  - backend developers
  - frontend developers
  - full stack developers
  - mobile developers
  - architects
tags: multi-tenancy, outsystems developer cloud, conversion, o11 modules, non-supported patterns
outsystems-tools:
  - service studio
helpids: 30633
---

# The Asset cannot contain multi-tenant modules

[Multi-tenancy](https://www.outsystems.com/tk/redirect?g=6e1bb224-5f33-4233-adc5-57dc98793113) allows a single application server and database server to provide different customers with their own isolated set of computing resources. Currently, OutSystems Developer Cloud doesn’t support multi-tenancy.

This pattern identifies OutSystems 11 (O11) modules with elements configured as multi-tenant - entities, site properties, or timers.

## How to solve

<div class="info" markdown="1">

If you are only preparing your code for the conversion, at present, OutSystems recommends not making any changes to modules with findings for this code pattern, while ODC lacks built-in multi-tenancy support.

</div>

This pattern isn't supported yet.

You can only proceed with the conversion of ODC assets with modules that don't include multi-tenant elements.
