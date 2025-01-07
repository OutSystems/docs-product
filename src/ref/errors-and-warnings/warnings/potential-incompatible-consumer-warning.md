---
summary: Explore how OutSystems 11 (O11) handles potential incompatible consumer module dependencies and the necessary steps to ensure compatibility.
locale: en-us
guid: 0e28cb64-765b-4e99-816b-54dca99e4c01
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: dependency management, module compatibility, runtime errors, system maintenance, version control
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - service center
coverage-type:
  - unblock
---

# Potential Incompatible Consumer Warning

<a id="helpid-30182"></a>

Message
:   `Consumer module '<module>' may have incompatible dependencies. Republish module to validate compatibility and avoid runtime errors.`

Cause
:   You changed a module that exposes functionality used by other module (consumer). You performed changes in the signature of exposed elements that may be incompatible with the consumer module and cause runtime errors.

Recommendation
:   The consumer module must be republished in Service Studio or Service Center in order to validate the compatibility of your changes. If your changes are compatible, the consumer has no need to refresh the dependency to your producer module. On the other hand, if your changes are incompatible, the consumer module needs to [refresh the dependency](../../../building-apps/reuse-and-refactor/handle-changes.md#refresh-dependencies) to your producer module in Service Studio, adapt the logic to your changes, and be republished.

