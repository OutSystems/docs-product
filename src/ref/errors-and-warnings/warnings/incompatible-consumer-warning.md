---
summary: OutSystems 11 (O11) addresses incompatible consumer module dependencies by recommending a refresh and republish of affected modules.
locale: en-us
guid: ca2b9a26-9427-4ceb-877e-709b284b7b17
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, dependency management, runtime errors, module compatibility, service studio tutorials
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Incompatible Consumer Warning

<a id="helpid-30183"></a>

Message
:   `Consumer module '<module>' has incompatible dependencies. To avoid runtime errors, refresh dependencies in '<module>' and republish it.`

Cause
:   You changed a module that exposes functionality used by other module (consumer). You performed changes in the signature of exposed elements that are incompatible with the consumer module and will probably cause runtime errors.

Recommendation
:   The consumer module needs to [refresh the dependency](../../../building-apps/reuse-and-refactor/handle-changes.md#refresh-dependencies) to your producer module in Service Studio, adapt the logic to your changes, and be republished.
